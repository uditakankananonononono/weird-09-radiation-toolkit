# LOCKED PRE-DATA (amendment 2026-09-26 13:18 IST): specificity layer for the
# 12 v1 gate-passing orthogroups against the 4-species stress-matched
# radiation-sensitive control panel. Written before v2 clustering completes.
# Logic fixed by amendment: candidate survives as radiation-specific ONLY if
# absent from >=3 of 4 controls; otherwise re-labeled broad-stress-adaptation.
import json
import numpy as np
from scipy.stats import hypergeom, norm

RES_DEINO=["Deinococcus_radiodurans","Deinococcus_geothermalis","Deinococcus_deserti"]
RES=RES_DEINO+["Ramazzottius_varieornatus","Adineta_vaga"]
SEN=["Thermus_aquaticus","Thermus_thermophilus","Hypsibius_exemplaris",
     "Caenorhabditis_elegans","Drosophila_melanogaster","Escherichia_coli"]
CTRL=["Pyrococcus_furiosus","Sulfolobus_solfataricus","Lactobacillus_plantarum","Saccharomyces_cerevisiae"]
SP=RES+SEN+CTRL; SPIDX={s:i for i,s in enumerate(SP)}
NCTRL=len(CTRL)

# v1 candidates (from results/h1_formal_tests.json)
v1=json.load(open("results/h1_formal_tests.json"))["hits"]
v1_reps={h["rep"] for h in v1}

# v2 clustering (createtsv output on CLU_V2_SENS)
clu={}
for line in open("results/orthology/clusters_v2.tsv"):
    rep,mem=line.rstrip("\n").split("\t")
    sp=mem.split("|")[0]
    if sp in SPIDX:
        clu.setdefault(rep,np.zeros(len(SP),dtype=np.int32))[SPIDX[sp]]+=1

# Map each v1 candidate rep to its v2 counterpart cluster:
# the v2 cluster containing the v1 rep's own protein id (rep ids are member ids).
v2_of_v1={}
for rep in v1_reps:
    for v2rep,X in clu.items():
        pass  # membership-by-rep mapping handled below via member scan
# membership scan: build protein->v2rep map only for v1 rep ids
prot2v2={}
for line in open("results/orthology/clusters_v2.tsv"):
    rep,mem=line.rstrip("\n").split("\t")
    if mem in v1_reps:
        prot2v2[mem]=rep
mapped={r:prot2v2.get(r) for r in v1_reps}

reps=list(clu.keys()); X=np.stack([clu[r] for r in reps]); n=len(reps)
def fisher_p(pm,ps): return hypergeom.sf(pm-1,len(SP)-NCTRL,pm+ps,len(RES))
def mwu_p(A,B):
    U=(A[:,:,None]>B[:,None,:]).sum(axis=(1,2))+0.5*(A[:,:,None]==B[:,None,:]).sum(axis=(1,2))
    return norm.sf((U-18.0-0.5)/np.sqrt(39.0))

# gates re-run on v2 (resistant vs sensitive only; controls NOT in the Fisher/MWU partition)
pm=(X[:,:len(RES)]>0).sum(1); ps=(X[:,len(RES):len(RES)+len(SEN)]>0).sum(1)
pf_obs=fisher_p(pm,ps); pw_obs=mwu_p(X[:,:len(RES)],X[:,len(RES):len(RES)+len(SEN)])

rng=np.random.default_rng(11)
NPERM=1000
cnt_f=np.zeros(n,dtype=np.int32); cnt_w=np.zeros(n,dtype=np.int32)
for it in range(NPERM):
    P=rng.permutation(len(RES)+len(SEN))
    Y=X[:,:len(RES)+len(SEN)][:,P]
    pmp=(Y[:,:len(RES)]>0).sum(1); psp=(Y[:,len(RES):]>0).sum(1)
    cnt_f+=(fisher_p(pmp,psp)<=pf_obs)
    cnt_w+=(mwu_p(Y[:,:len(RES)],Y[:,len(RES):])<=pw_obs)
emp_f=(cnt_f+1.0)/(NPERM+1.0); emp_w=(cnt_w+1.0)/(NPERM+1.0)

ORIGIN_IDX=[(0,1,2),(3,),(4,)]
results=[]
for i,rep in enumerate(reps):
    origins=[bool((X[i,list(ix)]>0).any()) for ix in ORIGIN_IDX]
    results.append({"rep":rep,"emp_p_fisher":float(emp_f[i]),"emp_p_mwu":float(emp_w[i]),
                    "origins":origins,"ctrl_present":int((X[i,len(RES)+len(SEN):]>0).sum())})

out={"n_v2_clusters":n,"n_permutations":NPERM,
     "v1_candidates":[],
     "method":"v2 re-cluster incl. 4 stress controls; gates re-run identically; specificity: absent in >=3/4 controls"}
for h in v1:
    v2rep=mapped[h["rep"]]
    rec={"v1_rep":h["rep"],"v2_rep":v2rep,"v1_emp_p":h["emp_p"]}
    if v2rep is None:
        rec.update({"status":"v1_candidate_dissolved_in_v2","specificity":"not_evaluable"})
    else:
        row=results[reps.index(v2rep)]
        absent=NCTRL-row["ctrl_present"]
        rec.update({"v2_emp_p_fisher":row["emp_p_fisher"],"origins":row["origins"],
                    "controls_present_in":row["ctrl_present"],
                    "specificity":"radiation_specific" if absent>=3 else "broad_stress_adaptation"})
    out["v1_candidates"].append(rec)
json.dump(out,open("results/h2_specificity_layer.json","w"),indent=1)
print(json.dumps({"mapped":sum(1 for v in mapped.values() if v),"dissolved":sum(1 for v in mapped.values() if not v),
                  "radiation_specific":sum(1 for c in out['v1_candidates'] if c.get('specificity')=='radiation_specific')},indent=1))
