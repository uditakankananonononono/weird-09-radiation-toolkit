import json
import numpy as np

# Locked 2026-09-27 08:59 IST amendment: Saturated Co-Retention test.
# Same corrected 5v6 panel mapping as the 00:54 amendment; no re-clustering, no new data.
RES_DEINO=["Deinococcus_radiodurans","Deinococcus_geothermalis","Deinococcus_deserti"]
RES=RES_DEINO+["Ramazzottius_varieornatus","Adineta_vaga"]
SEN=["Thermus_aquaticus","Thermus_thermophilus","Hypsibius_exemplaris","Caenorhabditis_elegans","Drosophila_melanogaster","Escherichia_coli"]
SP=RES+SEN; SPIDX={s:i for i,s in enumerate(SP)}

clu={}
for line in open("results/orthology/clusters_sensitive.tsv"):
    rep,mem=line.rstrip("\n").split("\t")
    sp=mem.split("|")[0]
    if sp in SPIDX:
        clu.setdefault(rep,np.zeros(11,dtype=np.int32))[SPIDX[sp]]+=1
reps=list(clu.keys()); X=np.stack([clu[r] for r in reps]); n=len(reps)

# S(g) = product of within-clade presence completeness over the 3 resistant clades
deino = (X[:,0:3]>0).mean(1)          # Deinococcaceae completeness (3 species)
tardi = (X[:,3]>0).astype(float)      # Tardigrada: R. varieornatus only (1)
bdell = (X[:,4]>0).astype(float)      # Bdelloidea: A. vaga (1)
S = deino*tardi*bdell
sen0 = (X[:,5:].sum(1)==0)
complete = (S==1.0)&sen0
M = int((((X[:,:5]>0).sum(1)+(X[:,5:]>0).sum(1))>0).sum())  # tested orthogroups (same keep rule as H1)
cnt = int(complete.sum())
P = (cnt+1.0)/(M+1.0)
win = P < 0.005

# which of the 12 corrected H1 candidates are in the complete tier (identity check only)
h1 = json.load(open("results/h1_formal_tests.json"))
cand_reps = {h["rep"].split("|")[-1] for h in h1["hits"]}
rep2i = {r:i for i,r in enumerate(reps)}
cand_complete = []
for h in h1["hits"]:
    i = rep2i[h["rep"]]
    cand_complete.append({"rep": h["rep"], "S": float(S[i]), "sen0": bool(sen0[i]),
                          "complete_tier": bool(complete[i])})

out = {"amendment":"2026-09-27 08:59 IST (Saturated Co-Retention, locked pre-inspection)",
 "M_tested_orthogroups": M,
 "background_complete_coretention_control_absent": cnt,
 "background_fraction": cnt/M,
 "empirical_P": P, "win_threshold": 0.005, "win": bool(win),
 "falsification_branch":"if P>=0.005: reframe not earned; H4 identifiability boundary stays terminal",
 "candidates_in_complete_tier": cand_complete,
 "caveats":["candidates were selected on presence criteria overlapping S - background-rarity quantification, not independent validation",
            "Tardigrada completeness is a 1-species call (Milnesium unavailable)",
            "P is background frequency, not phylogenetic independence - convergence beyond relatedness remains unclaimed"]}
json.dump(out, open("results/h6_co_retention.json","w"), indent=1)
print(json.dumps({k:v for k,v in out.items() if k!="candidates_in_complete_tier"}, indent=1))
print("candidates complete tier:", sum(1 for c in cand_complete if c["complete_tier"]), "of", len(cand_complete))
for c in cand_complete: print(" ", c["rep"], "S=%.2f" % c["S"], "sen0=%s" % c["sen0"], "TIER" if c["complete_tier"] else "")
