# Domain-level orthogonal confirmation (amendment 2026-09-26 20:21 IST).
# Rule: candidate's v1 Pfam domain SET found complete in >=1 protein of >=2 of 5
# NEW proteomes. Domain-call threshold for new-proteome scans: full-sequence
# E-value <= 1e-5 (standard hmmsearch stringency, fixed HERE pre-result).
# Confirmatory only; negatives reported, never remove v2 candidates.
import json
ECAP = 1e-5
NEW = ["Deinococcus_radiophilus","Deinococcus_proteolyticus","Deinococcus_maricopensis",
       "Adineta_ricciae","Rotaria_magnacalcarata"]

# v1 candidate domain sets (query protein -> {pfam families})
cand = {}
for line in open('results/annotation/pfam_domtblout.txt'):
    if line.startswith('#'): continue
    f = line.split()
    if len(f) < 19: continue
    fam, query, eval_ = f[0], f[3], float(f[6])
    if eval_ > ECAP: continue
    cand.setdefault(query, set()).add(fam)

# v2 radiation-specific 10 (from h2)
h2 = json.load(open('results/h2_specificity_layer.json'))
reps10 = [c['v1_rep'] for c in h2['v1_candidates'] if c['specificity']=='radiation_specific']

# new-proteome protein -> family set
prot_fams = {sp:{} for sp in NEW}
for sp in NEW:
    for line in open(f'/tmp/hs_{sp}.tbl'):
        if line.startswith('#'): continue
        f = line.split()
        target, fam, eval_ = f[0], f[2], float(f[4])  # this build's hmmsearch tblout: no tlen/qlen cols
        if eval_ > ECAP: continue
        prot_fams[sp].setdefault(target, set()).add(fam)

out = {"rule": f"full v1 domain set in >=1 protein of >=2/5 new proteomes; E<={ECAP}",
       "candidates": []}
for rep in reps10:
    doms = cand.get(rep, set())
    support = [sp for sp in NEW if any(doms <= pf for pf in prot_fams[sp].values())]
    out['candidates'].append({"rep": rep, "n_domains": len(doms),
        "domains": sorted(doms), "support_proteomes": support,
        "confirmed": len(support) >= 2})
out['summary'] = {"confirmed": sum(c['confirmed'] for c in out['candidates']),
                  "of": len(out['candidates'])}
json.dump(out, open('results/h3_domain_confirmation.json','w'), indent=1)
print(json.dumps(out['summary']))
for c in out['candidates']:
    print(f"{'OK ' if c['confirmed'] else 'no '} {c['rep']:38s} doms={c['n_domains']} support={len(c['support_proteomes'])}/5")
