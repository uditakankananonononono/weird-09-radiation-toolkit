#!/usr/bin/env python3
"""H5 mechanistic prioritization - deterministic scoring under the 01:14 IST locked rubric."""
import json
MAP = {
 'HPPK':'C4','Pterin_bind':'C4',
 'Ank':'C3','Ank_2':'C3','Ank_3':'C3','Ank_4':'C3','Ank_5':'C3',
 'DHH':'C1','DHHA2':'C1',
 'DSBA':'C2','Thioredoxin_4':'C2','Flavin_Reduct':'C2','NmrA':'C2',
 'Amidase':'C5','Bac_rhamnosid':'C5','Bac_rhamnosid6H':'C5','Bac_rhamnosid_N':'C5','Ig_Rha78A_N':'C5',
 '3Beta_HSD':'C5','Epimerase':'C5','GDP_Man_Dehyd':'C5','Polysacc_synt_2':'C5','RmlD_sub_bind':'C5',
}
d = json.load(open('results/h3_domain_confirmation.json'))
rows = []
for c in d['candidates']:
    cats = sorted({MAP[x] for x in c['domains'] if x in MAP})
    unmapped = [x for x in c['domains'] if x not in MAP]
    rows.append({'rep': c['rep'], 'score': len(cats), 'categories': cats,
                 'confirmed': c['confirmed'], 'n_domains': c['n_domains'], 'unmapped': unmapped})
rows.sort(key=lambda r: (-r['score'], not r['confirmed'], r['n_domains']))
for i, r in enumerate(rows, 1): r['rank'] = i
json.dump({'amendment': '2026-09-27 01:14 IST (locked pre-scoring)', 'ranking': rows},
          open('results/h5_mechanistic_prioritization.json', 'w'), indent=1)
for r in rows: print(r['rank'], r['rep'], r['score'], r['categories'], 'confirmed' if r['confirmed'] else 'UNCONFIRMED')
