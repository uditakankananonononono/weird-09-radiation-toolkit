#!/usr/bin/env python3
"""W09 queue #14 expression integration (amendment commit 4ba2dce, locked pre-download).
GSE176207 WT arm (3 unirr + 3 x 10kGy, 2h recovery). Candidate -> D. radiodurans member
(committed KDR proteome) -> phmmer vs ASM856v1 proteome (E<=1e-50) -> protein_id ->
old_locus_tag DR_ (GFF bridge) -> HTSeq CPM -> induction (log2FC>=1 AND CPM_IR>=1) ->
one-sided Fisher vs background. Report-only."""
import json, gzip, re, math
from collections import defaultdict
import pyhmmer
from Bio import SeqIO

abc = pyhmmer.easel.Alphabet.amino()
def nm(x): return x.decode() if isinstance(x, bytes) else x
D = 'data/expression_gse176207'

# 1. candidate -> KDR WP_ members
clusters = {}
for line in open('results/orthology/clusters_v2.tsv'):
    rep, mem = line.rstrip('\n').split('\t')
    clusters.setdefault(rep, set()).add(mem)
h3 = json.load(open('results/h3_domain_confirmation.json'))['candidates']
cand_wp = {}
for c in h3:
    rep = c['rep']
    cand_wp[rep] = [m.split('|')[1] for m in clusters.get(rep, set()) if 'radiodurans' in m]

# 2. extract member sequences from committed KDR proteome
kdr = {}
with gzip.open('data/proteomes/Deinococcus_radiodurans.faa.gz', 'rt') as fh:
    for r in SeqIO.parse(fh, 'fasta'):
        kdr[r.id] = str(r.seq)

# 3. ASM856v1 proteome + GFF bridge
ref_seqs = []
with gzip.open(f'{D}/GCF_000008565.1_ASM856v1_protein.faa.gz', 'rt') as fh:
    for r in SeqIO.parse(fh, 'fasta'):
        ref_seqs.append(pyhmmer.easel.TextSequence(name=r.id.encode(), sequence=str(r.seq)).digitize(abc))
prot2gene, gene2dr = {}, {}
cur = {}
with gzip.open(f'{D}/GCF_000008565.1_ASM856v1_genomic.gff.gz', 'rt') as fh:
    for line in fh:
        if line.startswith('#'): continue
        f = line.rstrip('\n').split('\t')
        if len(f) < 9: continue
        attr = f[8]
        if f[2] == 'gene':
            m = re.search(r'ID=(gene-[^;]+)', attr); o = re.search(r'old_locus_tag=(DR_\d+)', attr)
            if m and o: gene2dr[m.group(1)] = o.group(1)
        elif f[2] == 'CDS':
            p = re.search(r'protein_id=([A-Z0-9_.]+)', attr); g = re.search(r'Parent=(gene-[^;]+)', attr)
            if p and g: prot2gene[p.group(1)] = g.group(1)

# 4. phmmer mapping
mapping = {}
for rep, accs in cand_wp.items():
    for acc in accs:
        if acc not in kdr: mapping[acc] = {'dr': None, 'why': 'not in committed KDR proteome'}; continue
        q = pyhmmer.easel.TextSequence(name=acc.encode(), sequence=kdr[acc]).digitize(abc)
        hits = list(pyhmmer.phmmer([q], ref_seqs, E=1e-50))
        best = None
        for th in hits:
            for h in th:
                if h.included: best = (nm(h.name), h.evalue); break
            if best: break
        if best:
            prot, ev = best
            gene = prot2gene.get(prot); dr = gene2dr.get(gene)
            mapping[acc] = {'ref_protein': prot, 'evalue': ev, 'dr': dr}
        else:
            mapping[acc] = {'dr': None, 'why': 'no phmmer hit E<=1e-50'}

# 5. counts -> CPM
samples = {'unirr': ['GSM5360107_WTA0', 'GSM5360109_WTB0', 'GSM5360111_WTC0'],
           'ir':    ['GSM5360108_WTA10', 'GSM5360110_WTB10', 'GSM5360112_WTC10']}
counts = {}
for cond, fs in samples.items():
    for s in fs:
        lib = 0; c = {}
        with gzip.open(f'{D}/{s}.bowtie.removerrna.htseq.gff.gz', 'rt') as fh:
            for line in fh:
                g, n = line.rstrip('\n').split('\t')
                n = int(n); c[g] = n; lib += n
        for g, n in c.items():
            counts.setdefault(g, {}).setdefault(cond, []).append(n / lib * 1e6)

all_genes = list(counts)
def induced(g):
    d = counts[g]
    mu, mi = sum(d.get('unirr', [0]))/3, sum(d.get('ir', [0]))/3
    if mu == 0 and mi == 0: return None, None  # unexpressed
    lfc = math.log2((mi + 0.01) / (mu + 0.01))
    return lfc, (lfc >= 1 and mi >= 1)

bg_ind = bg_not = 0
lfc_all = {}
for g in all_genes:
    lfc, ind = induced(g)
    if lfc is None: continue
    lfc_all[g] = lfc
    if ind: bg_ind += 1
    else: bg_not += 1

cand_rows = []
c_ind = c_not = c_unmapped = c_unexpr = 0
for rep, accs in cand_wp.items():
    for acc in accs:
        m = mapping[acc]
        dr = m.get('dr')
        if not dr: c_unmapped += 1; cand_rows.append({'candidate': rep, 'kdr_wp': acc, 'dr': None, 'note': m.get('why', 'no DR bridge')}); continue
        if dr not in counts: c_unmapped += 1; cand_rows.append({'candidate': rep, 'kdr_wp': acc, 'dr': dr, 'note': 'no counts'}); continue
        lfc, ind = induced(dr)
        if lfc is None: c_unexpr += 1; cand_rows.append({'candidate': rep, 'kdr_wp': acc, 'dr': dr, 'note': 'unexpressed'}); continue
        if ind: c_ind += 1
        else: c_not += 1
        cand_rows.append({'candidate': rep, 'kdr_wp': acc, 'dr': dr, 'log2FC': round(lfc, 3), 'induced': ind})

from scipy.stats import fisher_exact
try:
    tab = [[c_ind, c_not], [bg_ind - c_ind, bg_not - c_not]]
    odds, p = fisher_exact(tab, alternative='greater')
except Exception:
    odds, p = None, None
out = {'amendment_commit': '4ba2dce', 'dataset': 'GSE176207 WT arm (3 unirr + 3 x 10kGy, 2h recovery)',
       'mapping_rule': 'phmmer E<=1e-50 KDR member -> ASM856v1 protein -> old_locus_tag',
       'background': {'induced': bg_ind, 'not_induced': bg_not, 'n_genes': len(lfc_all)},
       'candidates': {'induced': c_ind, 'not_induced': c_not, 'unmapped': c_unmapped, 'unexpressed': c_unexpr},
       'fisher_one_sided_p': p, 'odds_ratio': odds, 'rows': cand_rows}
json.dump(out, open('results/h14_expression_integration.json', 'w'), indent=1)
print('bg', bg_ind, '/', bg_ind + bg_not, 'cand', c_ind, '/', c_ind + c_not, 'unmapped', c_unmapped, 'unexpr', c_unexpr)
print('fisher p', p, 'odds', odds)
for r in cand_rows: print(r)
