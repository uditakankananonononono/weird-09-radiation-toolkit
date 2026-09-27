#!/usr/bin/env python3
"""W09 queue #10 (12:38 IST amendment): radiation-specific vs general-stress classification.
Mirrors analysis/formal_tests.py kernel exactly (hypergeom.sf(pm-1,N,pm+ps,5), (cnt+1)/1001,
1000 label perms, origins gate) under two 8-genome sensitive-arm compositions, seed 260927.
Targets: the 12 committed h1 reps only. Report-only; no new hits, no removals."""
import json, numpy as np
from scipy.stats import hypergeom

RES=["Deinococcus_radiodurans","Deinococcus_geothermalis","Deinococcus_deserti","Ramazzottius_varieornatus","Adineta_vaga"]
ORIGIN_IDX=[(0,1,2),(3,),(4,)]  # Deinococcaceae, Tardigrada, Bdelloidea (committed code)
COMP={
 "S-A_lab_model_controls":{"sensitive":["Caenorhabditis_elegans","Drosophila_melanogaster","Escherichia_coli"]},
 "S-B_stress_specialist_controls":{"sensitive":["Thermus_aquaticus","Thermus_thermophilus","Hypsibius_exemplaris"]},
}
SEED=260927; NPERM=1000
HITS=[h["rep"] for h in json.load(open("results/h1_formal_tests.json"))["hits"]]

# build rows for the 12 committed reps across all 11 species
ALLSP=RES+["Thermus_aquaticus","Thermus_thermophilus","Hypsibius_exemplaris","Caenorhabditis_elegans","Drosophila_melanogaster","Escherichia_coli"]
SPIDX={s:i for i,s in enumerate(ALLSP)}
clu={}
for line in open("results/orthology/clusters_sensitive.tsv"):
    rep,mem=line.rstrip("\n").split("\t")
    if rep in HITS:
        sp=mem.split("|")[0]
        if sp in SPIDX:
            clu.setdefault(rep,np.zeros(11,dtype=np.int32))[SPIDX[sp]]+=1
missing=[r for r in HITS if r not in clu]
assert not missing, f"committed reps absent from clusters_sensitive.tsv: {missing}"

def fisher_p(pm,ps,N): return hypergeom.sf(pm-1,N,pm+ps,5)

def run_comp(sen):
    sp=RES+sen; N=len(sp)
    idx=[ALLSP.index(s) for s in sp]
    X=np.stack([clu[r][idx] for r in HITS]); n=len(HITS)
    pm=(X[:,:5]>0).sum(1); ps=(X[:,5:]>0).sum(1)
    pf_obs=fisher_p(pm,ps,N)
    rng=np.random.default_rng(SEED)
    cnt=np.zeros(n,dtype=np.int32)
    for it in range(NPERM):
        order=rng.permutation(N)
        Xm=X[:,order][:,:5]; Xs=X[:,order][:,5:]
        pmp=(Xm>0).sum(1); psp=(Xs>0).sum(1)
        cnt+=(fisher_p(pmp,psp,N)<=pf_obs)
    emp=(cnt+1.0)/(NPERM+1.0)
    def origins(i):
        c=X[i]; det=[]
        for idxs in ORIGIN_IDX:
            po=int((c[list(idxs)]>0).sum()); p_=int((c[5:]>0).sum())
            det.append(bool(po>0 and po>p_))
        return det
    res=[]
    for i in range(n):
        det=origins(i)
        gate = bool(emp[i]<0.05 and pm[i]>ps[i] and sum(det)>=2)
        res.append({"rep":HITS[i],"pm":int(pm[i]),"ps":int(ps[i]),
          "res_copies":int(X[i,:5].sum()),"sen_copies":int(X[i,5:].sum()),
          "origins":det,"fisher_p_obs":float(pf_obs[i]),"emp_p":float(emp[i]),"pass":gate})
    return res

comps={k:run_comp(v["sensitive"]) for k,v in COMP.items()}
out_rows=[]
for i,rep in enumerate(HITS):
    a=comps["S-A_lab_model_controls"][i]; b=comps["S-B_stress_specialist_controls"][i]
    if not a["pass"]: cls="CONTROL-DEPENDENT"
    elif not b["pass"]: cls="GENERAL-STRESS-LEANING"
    else: cls="RADIATION-LEANING"
    out_rows.append({"rep":rep,"pm":a["pm"],"ps_S-A":a["ps"],"ps_S-B":b["ps"],"emp_p_S-A":a["emp_p"],"pass_S-A":a["pass"],
      "emp_p_S-B":b["emp_p"],"pass_S-B":b["pass"],"class":cls,
      "res_copies":a["res_copies"],"sen_copies_S-A":a["sen_copies"],"sen_copies_S-B":b["sen_copies"],
      "origins_S-A":a["origins"],"origins_S-B":b["origins"]})
counts={}
for r in out_rows: counts[r["class"]]=counts.get(r["class"],0)+1
out={"amendment":"2026-09-27 12:38 IST queue #10 (delegated executor, report-only)",
 "executor_note":"computed by delegated executor at ref c72b429; uncommitted, returned to lane-29 for review",
 "kernel":"mirrors analysis/formal_tests.py: hypergeom.sf(pm-1, N, pm+ps, 5), (cnt+1)/1001, 1000 label perms, ORIGIN_IDX [(0,1,2),(3,),(4,)], gate emp_p<0.05 + resistant direction (pm>ps) + >=2/3 origins",
 "compositions":{k:{"sensitive":v["sensitive"],"N":8,"resistant":RES} for k,v in COMP.items()},
 "seed":SEED,"n_permutations":NPERM,"targets":"12 committed h1 reps only (results/h1_formal_tests.json hits)",
 "classification_rule":"RADIATION-LEANING = passes committed panel AND S-B; GENERAL-STRESS-LEANING = passes S-A but NOT S-B; CONTROL-DEPENDENT = fails S-A (decision tree: fails S-A -> CONTROL-DEPENDENT; else fails S-B -> GENERAL-STRESS-LEANING; else RADIATION-LEANING)",
 "class_counts":counts,"per_candidate":out_rows,
 "interpretation_lock":"REPORT-ONLY. Classes are descriptive labels for the paper, not gate changes. No new hits, no removals."}
json.dump(out, open("results/h12_stress_specificity.json","w"), indent=1)
print(json.dumps(counts,indent=1))
for r in out_rows: print(r["class"], r["emp_p_S-A"], r["emp_p_S-B"], r["rep"])
