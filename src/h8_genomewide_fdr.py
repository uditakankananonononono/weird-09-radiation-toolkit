#!/usr/bin/env python3
"""W09 queue #13: genome-wide permutation FDR (amendment 2026-09-27 12:09 IST, locked pre-computation)."""
import json, random
import numpy as np
from scipy.stats import hypergeom

SEED, NPERM = 260927, 1000
PREFIX = {'Adineta_vaga':'A_vaga','Caenorhabditis_elegans':'C_elegans',
 'Deinococcus_deserti':'D_deserti','Deinococcus_geothermalis':'D_geothermalis',
 'Deinococcus_radiodurans':'D_radiodurans','Drosophila_melanogaster':'D_melanogaster',
 'Escherichia_coli':'E_coli','Hypsibius_exemplaris':'H_exemplaris',
 'Lactobacillus_plantarum':'L_plantarum','Pyrococcus_furiosus':'P_furiosus',
 'Ramazzottius_varieornatus':'R_varieornatus','Saccharomyces_cerevisiae':'S_cerevisiae',
 'Sulfolobus_solfataricus':'S_solfataricus','Thermus_aquaticus':'T_aquaticus',
 'Thermus_thermophilus':'T_thermophilus'}
SPECIES = ['D_radiodurans','D_geothermalis','D_deserti','R_varieornatus','A_vaga',
           'C_elegans','D_melanogaster','E_coli','H_exemplaris','L_plantarum','P_furiosus']
# true 5v6 panel (00:54 correction): 5 resistant = 3 Deinococcus + R_varieornatus + A_vaga
RES = set(SPECIES[:5]); SEN = set(SPECIES[5:])
CLADE = {'D_radiodurans':'deino','D_geothermalis':'deino','D_deserti':'deino',
         'R_varieornatus':'tardi','A_vaga':'bdello'}
idx = {s: i for i, s in enumerate(SPECIES)}

clusters = {}
for line in open('results/orthology/clusters_v2.tsv'):
    rep, mem = line.rstrip('\n').split('\t')
    sp = PREFIX.get(mem.split('|')[0])
    if sp in idx:
        clusters.setdefault(rep, set()).add(sp)
reps = sorted(clusters)
X = np.zeros((len(reps), 11), dtype=bool)
for gi, rep in enumerate(reps):
    for sp in clusters[rep]:
        X[gi, idx[sp]] = True
k_total = X.sum(axis=1)
print('orthogroups:', len(reps), flush=True)

def passers(y_bool):
    k_res = X[:, :11] @ y_bool.astype(int)
    n_res = int(y_bool.sum())
    K = k_total
    p = hypergeom.sf(k_res - 1, 11, K, n_res)
    expected = K * n_res / 11.0
    direction = k_res > expected
    cand = np.where((p < 0.05) & direction & (K > 0))[0]
    out = []
    for gi in cand:
        pres = {SPECIES[i] for i in np.where(X[gi])[0]}
        res_species = {SPECIES[i] for i in np.where(y_bool)[0]}
        origins = {CLADE[s] for s in pres & res_species if s in CLADE}
        if len(origins) >= 2:
            out.append(reps[gi])
    return out

y_true = np.array([s in RES for s in SPECIES])
true_pass = passers(y_true)
h1 = json.load(open('results/h1_formal_tests.json'))
hits = h1['hits'] if isinstance(h1['hits'], list) else []
hit_reps = {h['rep'] if isinstance(h, dict) and 'rep' in h else h for h in hits}
missing = hit_reps - set(true_pass)
print('true-label raw-Fisher passers:', len(true_pass), '; committed hits:', len(hit_reps), '; missing from reconstruction:', len(missing), flush=True)
if missing:
    print('MISSING:', missing, flush=True)
    json.dump({'abort': 'sanity lock failed', 'missing': sorted(missing)}, open('results/h8_genomewide_fdr.json', 'w'))
    raise SystemExit(1)

rng = random.Random(SEED)
counts, hit_freq = [], {}
for b in range(NPERM):
    yb = np.array(rng.sample([True]*5 + [False]*6, 11))
    ps = passers(yb)
    counts.append(len(ps))
    for r in ps:
        hit_freq[r] = hit_freq.get(r, 0) + 1
    if (b + 1) % 200 == 0:
        print('perm', b + 1, 'running mean', round(float(np.mean(counts)), 3), flush=True)
counts = np.array(counts)
real_hits_under_null = {r: f for r, f in hit_freq.items() if r in hit_reps}
out = {'amendment': '2026-09-27 12:09 IST queue #13 genome-wide FDR', 'seed': SEED, 'nperm': NPERM,
       'approximation': 'raw one-sided Fisher p<0.05 under permutation (screen used per-orthogroup empirical p; nested permutation infeasible) - disclosed in amendment',
       'true_label_raw_passers': len(true_pass), 'committed_empirical_hits': len(hit_reps),
       'null_passer_counts': {'mean': float(counts.mean()), 'median': float(np.median(counts)),
                              'max': int(counts.max()), 'p_ge_12': float((counts >= 12).mean())},
       'FDR_hat': float(counts.mean()) / len(hit_reps),
       'real_candidates_ever_hit_under_null': real_hits_under_null,
       'sanity': 'all 12 committed hits reproduced in true-label raw-Fisher reconstruction'}
json.dump(out, open('results/h8_genomewide_fdr.json', 'w'), indent=1)
print('FDR_hat:', out['FDR_hat'], 'null mean:', out['null_passer_counts'], flush=True)
