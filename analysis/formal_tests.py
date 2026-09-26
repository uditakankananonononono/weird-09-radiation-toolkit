import json
import numpy as np
from scipy.stats import hypergeom, norm

RES_DEINO=["Deinococcus_radiodurans","Deinococcus_geothermalis","Deinococcus_deserti"]
ORIGIN_IDX=[(0,1,2),(3,),(4,)]  # Deinococcaceae, Tardigrada, Bdelloidea
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

def fisher_p(pm,ps): return hypergeom.sf(pm-1,11,pm+ps,5)
def mwu_p(A,B):
    U=(A[:,:,None]>B[:,None,:]).sum(axis=(1,2))+0.5*(A[:,:,None]==B[:,None,:]).sum(axis=(1,2))
    return norm.sf((U-15.0-0.5)/np.sqrt(30.0))

pm=(X[:,:5]>0).sum(1); ps=(X[:,5:]>0).sum(1)
keep=(pm+ps)>0
pf_obs=fisher_p(pm,ps); pw_obs=mwu_p(X[:,:5],X[:,5:])

rng=np.random.default_rng(11)
NPERM=1000
cnt_f=np.zeros(n,dtype=np.int32); cnt_w=np.zeros(n,dtype=np.int32)
for it in range(NPERM):
    order=rng.permutation(11)
    Xm=X[:,order][:,:5]; Xs=X[:,order][:,5:]
    pmp=(Xm>0).sum(1); psp=(Xs>0).sum(1)
    cnt_f+=(fisher_p(pmp,psp)<=pf_obs)
    cnt_w+=(mwu_p(Xm,Xs)<=pw_obs)
emp_f=(cnt_f+1.0)/(NPERM+1.0); emp_w=(cnt_w+1.0)/(NPERM+1.0)

def origins(i):
    c=X[i]; det=[]
    for idxs in ORIGIN_IDX:
        po=int((c[list(idxs)]>0).sum()); p_=int((c[5:]>0).sum())
        det.append(po>0 and po>p_)
    return det

hits=[]
for i in range(n):
    if not keep[i]: continue
    if emp_f[i]<0.05 and pm[i]>ps[i]:
        det=origins(i)
        if sum(det)>=2:
            hits.append({"rep":reps[i],"res_copies":int(X[i,:5].sum()),"sen_copies":int(X[i,5:].sum()),"origins":det,"emp_p":float(emp_f[i])})
hits_mwu=[{"rep":reps[i],"emp_p":float(emp_w[i]),"res_copies":int(X[i,:5].sum()),"sen_copies":int(X[i,5:].sum())} for i in range(n) if keep[i] and emp_w[i]<0.05 and X[i,:5].sum()>X[i,5:].sum()]

out={"n_orthogroups_tested":int(keep.sum()),"n_permutations":NPERM,
"fisher_empirical_hits_2of3_origins":len(hits),"mwu_empirical_hits":len(hits_mwu),
"hits":hits[:30],
"gate_met":len(hits)>0,"correction":"2026-09-27 00:54 IST amendment: true 5v6 panel mapping (prior run had Thermus_aquaticus in resistant arm + phantom 12th column + 6v6 constants); gates/seed/NPERM unchanged","method":"sensitive mmseqs cluster; Fisher one-sided presence/absence; MWU one-sided copy number (normal approx, cc, no tie correction); 1000 label permutations, per-orthogroup empirical p; gate: empirical p<0.05 + resistant-direction + >=2 of 3 independent origins (Deinococcaceae/Tardigrada/Bdelloidea). Milnesium missing (no assembly): Tardigrada origin = R. varieornatus only."}
json.dump(out,open("results/h1_formal_tests.json","w"),indent=1)
print(json.dumps({k:v for k,v in out.items() if k!="hits"},indent=1))
for h in hits[:10]: print(h)
