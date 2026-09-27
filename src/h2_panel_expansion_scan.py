#!/usr/bin/env python3
"""W09 queue #18 control-calibration (amendment commit c59ee4e, locked pre-scan).
Scan 5 committed control proteomes under the h3 rule: full v1 domain set in >=1
protein, E<=1e-05, committed 64-HMM set. Threshold = max control support count.
Applies verbatim to the 6 committed confirmation proteomes' committed counts."""
import json, glob, gzip, hashlib, sys
import pyhmmer
from Bio import SeqIO

abc = pyhmmer.easel.Alphabet.amino()
def nm(x): return x.decode() if isinstance(x, bytes) else x
hmms = []
for f in sorted(glob.glob('data/pfam_hmms/*.hmm')):
    with pyhmmer.plan7.HMMFile(f) as hf: hmms.append(hf.read())
h3 = {c['rep']: set(c['domains']) for c in json.load(open('results/h3_domain_confirmation.json'))['candidates']}

def scan(path, label):
    with open(path, 'rb') as fh: sha = hashlib.sha256(fh.read()).hexdigest()
    recs = []
    with gzip.open(path, 'rt') as fh:
        for r in SeqIO.parse(fh, 'fasta'):
            recs.append(pyhmmer.easel.TextSequence(name=r.id.encode(), sequence=str(r.seq)).digitize(abc))
    prot_domains = {}
    for th in pyhmmer.hmmsearch(hmms, recs, E=1e-05):
        for h in th:
            if h.included: prot_domains.setdefault(nm(h.name), set()).add(nm(th.query.name))
    support = {}
    for rep, dset in h3.items():
        support[rep] = any(dset <= pd for pd in prot_domains.values())
    return {'amendment_commit': '8e27195 (16:18 IST panel-expansion lock)', 'proteome': label, 'n_proteins': len(recs),
            'sha256_gz': sha, 'rule': 'h3 identical, E<=1e-05', 'support': support,
            'n_supported': sum(support.values())}

if __name__ == '__main__':
    path, label = sys.argv[1], sys.argv[2]
    out = scan(path, label)
    fn = f'results/h_panel_expansion_{label}.json'
    json.dump(out, open(fn, 'w'), indent=1)
    print(label, out['n_supported'], '/', len(h3), '->', fn, flush=True)
