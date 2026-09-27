#!/usr/bin/env python3
"""W09 #2 panel-expansion origins accounting (amendment lock 8e27195).
Per-cluster independent-origin support over {Deinococcota, Actinomycetota (14:20 arm),
Archaea, Tardigrada, Rotifera}; cross-origin core = clusters supported in >=3 distinct origins.
Report-only; expansion layer kept separate from the saturated 11-species panel statistics."""
import json, glob

ORIGINS = {
    'Deinococcota': ['results/h_panel_expansion_GCF_000092425.1.json'],
    'Actinomycetota': ['results/h_kineococcus_radiotolerans_confirmation.json',
                       'results/h_rubrobacter_radiotolerans_confirmation.json'],
    'Archaea': ['results/h_panel_expansion_GCF_057318935.1.json',
                'results/h_panel_expansion_GCF_037482175.1.json'],
    'Tardigrada': ['results/h_panel_expansion_GCA_001949185.1.json',
                   'results/h_panel_expansion_GCA_002082055.1.json'],
    'Rotifera': ['results/h_panel_expansion_GCA_021613535.1.json',
                 'results/h_panel_expansion_GCA_905332065.1.json'],
}
support = {}   # cluster -> origin -> bool
provenance = {}
for origin, files in ORIGINS.items():
    for f in files:
        d = json.load(open(f))
        provenance[f] = {'proteome': d['proteome'], 'n_proteins': d['n_proteins'],
                         'n_supported': d['n_supported'], 'sha256_gz': d['sha256_gz'],
                         'amendment': d.get('amendment') or d.get('amendment_commit')}
        for cl, ok in d['support'].items():
            support.setdefault(cl, {})
            support[cl][origin] = support[cl].get(origin, False) or bool(ok)

rows = []
for cl, o in support.items():
    n = sum(1 for v in o.values() if v)
    rows.append({'cluster': cl, 'per_origin': o, 'n_origins': n, 'cross_origin_core': n >= 3})
core = [r['cluster'] for r in rows if r['cross_origin_core']]
out = {'amendment_commit': '8e27195', 'origin_scheme': list(ORIGINS),
       'archaeal_provenance': 'verdict-asserted (round-4 archived verdict), flagged per amendment',
       'n_clusters': len(rows), 'cross_origin_core_n': len(core), 'cross_origin_core': core,
       'rows': sorted(rows, key=lambda r: -r['n_origins']), 'provenance': provenance}
json.dump(out, open('results/h2_panel_expansion_origins.json', 'w'), indent=1)
print('core', len(core), '/', len(rows))
for r in out['rows'][:11]:
    print(r['n_origins'], r['cluster'])
