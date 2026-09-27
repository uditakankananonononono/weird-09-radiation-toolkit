#!/usr/bin/env python3
"""W09 queue #3: formal Identifiability Score (amendment 2026-09-27 12:06 IST, locked pre-computation)."""
import json, random
src = open('src/h4b_extended.py').read()
ns = {}
exec(src.split('rng = random.Random(SEED)')[0], ns)
n_ind, clusters, h3, cands = ns['n_ind'], ns['clusters'], ns['h3'], ns['cands']
DEINO, BDELL, RES, NPERM, SEED = ns['DEINO'], ns['BDELL'], ns['RES'], ns['NPERM'], ns['SEED']
committed = json.load(open('results/h4c_phylo_convergence_ext.json'))['candidates']

rng = random.Random(SEED)
out = {'amendment': '2026-09-27 12:06 IST queue #3 Identifiability Score', 'nperm': NPERM, 'seed': SEED,
       'panel': '20-species extended (H4c)', 'candidates': {}, 'sanity': []}
for rep in cands:
    present = clusters.get(rep, set()) | h3.get(rep, set())
    obs = n_ind(present, RES)
    null = []
    for _ in range(NPERM):
        pres_p = set(present)
        for members in (DEINO, BDELL):
            k = len(set(members) & present)
            pres_p -= set(members)
            pres_p |= set(rng.sample(members, k))
        null.append(n_ind(pres_p, RES))
    null_s = sorted(null)
    p = (1 + sum(x <= obs for x in null_s)) / (NPERM + 1)
    c = committed[rep]
    assert obs == c['N_ind'] and abs(p - c['p']) <= 1.5 / (NPERM + 1), (rep, obs, p, c)
    out['sanity'].append(rep + ' reproduces committed N_ind and p')
    kd = len(set(DEINO) & present); kb = len(set(BDELL) & present)
    n_info = (0 < kd < 6) + (0 < kb < 3)
    import statistics
    sd = statistics.pstdev(null)
    p_min = (1 + sum(x <= null_s[0] for x in null_s)) / (NPERM + 1)
    cls = 'IMPOSSIBLE' if sd == 0 else ('TESTABLE' if p_min < 0.05 else 'UNDERPOWERED')
    out['candidates'][rep] = {
        'occupancy': {'deinococcaceae': f'{kd}/6', 'bdelloida': f'{kb}/3'},
        'n_informative_strata': int(n_info), 'obs_gains': obs,
        'gains_range': [null_s[0], null_s[-1]], 'null_sd': round(sd, 4),
        'null_median': null_s[NPERM // 2], 'p_obs': round(p, 5), 'p_min_achievable': round(p_min, 5),
        'class': cls}
    print(rep, out['candidates'][rep]['class'], out['candidates'][rep]['occupancy'],
          'sd', round(sd, 4), 'p_min', round(p_min, 5), flush=True)
from collections import Counter
out['panel_summary'] = dict(Counter(v['class'] for v in out['candidates'].values()))
out['panel_15_note'] = 'Committed H4 (15-species): zero-variance nulls on all 10 candidates - all IMPOSSIBLE (no recomputation, per amendment)'
out['framing'] = 'Separates falsified from untestable-in-principle; remedy = dispersed resistant lineages, not more within-clade proteomes. No H4 gate or label changes.'
json.dump(out, open('results/h7_identifiability_score.json', 'w'), indent=1)
print('PANEL:', out['panel_summary'], flush=True)
