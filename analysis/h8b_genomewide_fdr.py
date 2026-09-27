import json, time
import numpy as np
from scipy.stats import hypergeom
from scipy.stats import rankdata

# h8b: screen-exact genome-wide permutation FDR (amendment locked 2026-09-27 12:13 IST)
# Replicates analysis/formal_tests.py exactly (input, arms, hypergeom, seed 11, NPERM=1000),
# stores the full n x 1001 Fisher-stat matrix, then estimates FDR by rank recursion.

RES=["Deinococcus_radiodurans","Deinococcus_geothermalis","Deinococcus_deserti","Ramazzottius_varieornatus","Adineta_vaga"]
SEN=["Thermus_aquaticus","Thermus_thermophilus","Hypsibius_exemplaris","Caenorhabditis_elegans","Drosophila_melanogaster","Escherichia_coli"]
SP=RES+SEN; SPIDX={s:i for i,s in enumerate(SP)}
ORIGIN_IDX=[(0,1,2),(3,),(4,)]
COMMITTED=["Adineta_vaga|UJR10666.1","Deinococcus_deserti|WP_012692117.1","Adineta_vaga|UJR36058.1","Adineta_vaga|UJR11615.1","Adineta_vaga|UJR17759.1","Deinococcus_geothermalis|WP_272975990.1","Adineta_vaga|UJR28130.1","Adineta_vaga|UJR26281.1","Adineta_vaga|UJR09360.1","Deinococcus_deserti|WP_012692142.1","Deinococcus_geothermalis|WP_414646549.1","Deinococcus_geothermalis|WP_272975981.1"]

clu={}
for line in open("results/orthology/clusters_sensitive.tsv"):
    rep,mem=line.rstrip("\n").split("\t")
    sp=mem.split("|")[0]
    if sp in SPIDX:
        clu.setdefault(rep,np.zeros(11,dtype=np.int32))[SPIDX[sp]]+=1
reps=list(clu.keys()); X=np.stack([clu[r] for r in reps]); n=len(reps)
def fisher_p(pm,ps): return hypergeom.sf(pm-1,11,pm+ps,5)
pm=(X[:,:5]>0).sum(1); ps=(X[:,5:]>0).sum(1); keep=(pm+ps)>0
pf_obs=fisher_p(pm,ps)

NPERM=1000
S=np.empty((n,NPERM+1),dtype=np.float32); S[:,0]=pf_obs
orders=np.empty((NPERM,11),dtype=np.int8)
rng=np.random.default_rng(11)
cnt_f=np.zeros(n,dtype=np.int32)
t0=time.time()
for it in range(NPERM):
    order=rng.permutation(11); orders[it]=order
    Xm=X[:,order][:,:5]; Xs=X[:,order][:,5:]
    pmp=(Xm>0).sum(1); psp=(Xs>0).sum(1)
    Sp=fisher_p(pmp,psp); S[:,it+1]=Sp
    cnt_f+=(Sp<=pf_obs)
emp_f=(cnt_f+1.0)/(NPERM+1.0)
print(f"screen replication done in {time.time()-t0:.0f}s; n={n}, keep={int(keep.sum())}",flush=True)

# SANITY LOCK (amendment item 2)
def origins_from(c_res_presence, p_):
    return [int(po>0 and po>p_) for po in c_res_presence]
hits={}
for i in range(n):
    if not keep[i]: continue
    if emp_f[i]<0.05 and pm[i]>ps[i]:
        c=X[i]; p_=int((c[5:]>0).sum())
        det=origins_from([int((c[list(idxs)]>0).sum()) for idxs in ORIGIN_IDX], p_)
        if sum(det)>=2: hits[reps[i]]=float(emp_f[i])
STORED={h["rep"]:h["emp_p"] for h in json.load(open("results/h1_formal_tests.json"))["hits"]}
if set(hits)!=set(COMMITTED) or any(abs(hits[r]-STORED[r])>1e-12 for r in COMMITTED):
    json.dump({"abort":"h8b sanity lock failed","got":sorted(hits),"expected":sorted(COMMITTED)},open("results/h8b_genomewide_fdr.json","w"))
    print("ABORT: sanity lock failed",sorted(hits)); raise SystemExit(1)
print("sanity lock PASSED: 12/12 committed hits reproduced, emp_p=13/1001 each",flush=True)

# rank recursion (amendment item 3): rank_max via sort, chunked
cnt_all=np.empty((n,NPERM+1),dtype=np.int32)
CH=4096
for s in range(0,n,CH):
    e=min(n,s+CH)
    r=rankdata(S[s:e],axis=1,method='max')  # #{j: S_j <= S_k}
    cnt_all[s:e]=r-1  # exclude self
print("ranks done",flush=True)

origin_presence=[(X[:,list(idxs)]>0).sum(1) for idxs in ORIGIN_IDX]
null_hits=np.zeros(NPERM,dtype=np.int32)
for k in range(NPERM):
    order=orders[k]
    pmk=(X[:,order][:,:5]>0).sum(1); psk=(X[:,order][:,5:]>0).sum(1)
    p_k=(X[:,order][:,5:]>0).sum(1)  # sensitive-arm presence under permuted split
    emp_k=(cnt_all[:,k+1]+1.0)/(NPERM+1.0)
    ok=keep & (emp_k<0.05) & (pmk>psk)
    det=np.stack([(op>0)&(op>p_k) for op in origin_presence]).sum(0)
    null_hits[k]=int((ok & (det>=2)).sum())
m=null_hits.mean(); sd=null_hits.std(ddof=1)
out={"amendment":"h8b locked 2026-09-27 12:13 IST","statistic":"screen-exact Fisher presence, seed 11, NPERM=1000, clusters_sensitive.tsv",
"n_orthogroups":int(n),"n_tested":int(keep.sum()),"true_hits":12,
"null_hit_counts_summary":{"mean":float(m),"sd":float(sd),"median":float(np.median(null_hits)),"max":int(null_hits.max()),"min":int(null_hits.min())},
"FDR_est":float(m/12),"FDR_upper95_normal":float((m+1.96*sd/np.sqrt(NPERM))/12),
"approximation":"each permuted labeling calibrated against the same fixed permutation set (exact in expectation by group symmetry)",
"runtime_s":round(time.time()-t0,1)}
json.dump(out,open("results/h8b_genomewide_fdr.json","w"),indent=1)
np.save("/tmp/h8b_null_hits.npy",null_hits)
print(json.dumps(out,indent=1))
