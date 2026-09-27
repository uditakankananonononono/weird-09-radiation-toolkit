import json, numpy as np
from scipy.stats import hypergeom
SP=["Deinococcus_radiodurans","Deinococcus_geothermalis","Deinococcus_deserti","Ramazzottius_varieornatus","Adineta_vaga","Thermus_aquaticus","Thermus_thermophilus","Hypsibius_exemplaris","Caenorhabditis_elegans","Drosophila_melanogaster","Escherichia_coli"]
SPIDX={s:i for i,s in enumerate(SP)}
mem2rep={}; clu={}
for line in open('results/orthology/clusters_sensitive.tsv'):
    rep,mem=line.rstrip('\n').split('\t')
    mem2rep[mem]=rep
    sp=mem.split('|')[0]
    if sp in SPIDX: clu.setdefault(rep,np.zeros(11,dtype=np.int32))[SPIDX[sp]]+=1
keep={r for r,c in clu.items() if ((c[:5]>0).sum()+(c[5:]>0).sum())>0}
annotated=set(); prot2doms={}
for line in open('/tmp/b2_domtblout.txt'):
    if line.startswith('#'): continue
    p=line.split()
    dom,prot=p[0],p[3]
    rep=mem2rep.get(prot)
    if rep in keep:
        annotated.add(rep); prot2doms.setdefault(rep,set()).add(dom)
rows=[]
for r in annotated:
    c=clu[r]; pm=int((c[:5]>0).sum()); ps=int((c[5:]>0).sum())
    p=hypergeom.sf(pm-1,11,pm+ps,5)
    if p<0.05 and pm>ps: rows.append((r,p,pm-ps,pm,ps,sorted(prot2doms[r])))
rows.sort(key=lambda x:(x[1],-x[2]))
b2=[{"rep":r,"fisher_p":p,"effect":eff,"pm":pm,"ps":ps,"domains":d} for r,p,eff,pm,ps,d in rows[:12]]
json.dump({"n_annotated_in_universe":len(annotated),"n_passing":len(rows),"list":b2},open('results/h9_b2_domain_only.json','w'),indent=1)
print(f"annotated: {len(annotated)}, passing: {len(rows)}, listed: {len(b2)}")
for e in b2: print(" ",e["rep"],f"p={e['fisher_p']:.4f}",e["pm"],"v",e["ps"],e["domains"][:3])
