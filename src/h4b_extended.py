#!/usr/bin/env python3
"""W09 H4b: phylogenetically controlled convergence on the EXTENDED 20-species panel
(Amendment H4b, locked 20:59 IST pre-computation). Presence in the 5 H3 lineages =
domain-level presence from h3_domain_confirmation.json (labeled domain-level, no
orthology claim). Statistic/null identical to H4: Fitch min gains into
resistant-subtending branches; 10,000 within-strata presence shuffles; seed 260926.
Strata: deinococcaceae_resistant(6), bdelloid_resistant(3); all else fixed.
"""
import json, random
from Bio import Phylo

PREFIX = {'Adineta_vaga':'A_vaga','Caenorhabditis_elegans':'C_elegans',
 'Deinococcus_deserti':'D_deserti','Deinococcus_geothermalis':'D_geothermalis',
 'Deinococcus_radiodurans':'D_radiodurans','Drosophila_melanogaster':'D_melanogaster',
 'Escherichia_coli':'E_coli','Hypsibius_exemplaris':'H_exemplaris',
 'Lactobacillus_plantarum':'L_plantarum','Pyrococcus_furiosus':'P_furiosus',
 'Ramazzottius_varieornatus':'R_varieornatus','Saccharomyces_cerevisiae':'S_cerevisiae',
 'Sulfolobus_solfataricus':'S_solfataricus','Thermus_aquaticus':'T_aquaticus',
 'Thermus_thermophilus':'T_thermophilus'}
NEW = {'Deinococcus_radiophilus':'D_radiophilus','Deinococcus_proteolyticus':'D_proteolyticus',
 'Deinococcus_maricopensis':'D_maricopensis','Adineta_ricciae':'A_ricciae',
 'Rotaria_magnacalcarata':'R_magnacalcarata'}
NPERM, SEED = 10000, 260926
DEINO = ['D_radiodurans','D_geothermalis','D_deserti','D_radiophilus','D_proteolyticus','D_maricopensis']
BDELL = ['A_vaga','A_ricciae','R_magnacalcarata']
RES = set(DEINO) | set(BDELL) | {'R_varieornatus'}

tree = Phylo.read('data/species_tree_ext.nwk','newick')
leaves = [t.name for t in tree.get_terminals()]
assert len(leaves) == 20, leaves

clusters = {}
for line in open('results/orthology/clusters_v2.tsv'):
    rep, mem = line.rstrip('\n').split('\t')
    clusters.setdefault(rep, set()).add(PREFIX[mem.split('|')[0]])
h3 = {c['rep']: set(NEW[p] for p in c['support_proteomes']) for c in
      json.load(open('results/h3_domain_confirmation.json'))['candidates']}

def n_ind(present, res):
    down = {}
    for clade in tree.find_clades(order='postorder'):
        if clade.is_terminal(): down[id(clade)] = {1 if clade.name in present else 0}
        else:
            ch = [down[id(c)] for c in clade.clades]
            inter = set.intersection(*ch)
            down[id(clade)] = inter if inter else set.union(*ch)
    gains = 0
    def walk(node, pstate):
        nonlocal gains
        s = pstate if pstate in down[id(node)] else min(down[id(node)])
        if s == 1 and pstate == 0 and any(l.name in res for l in node.get_terminals()):
            gains += 1
        for c in node.clades: walk(c, s)
    walk(tree.root, 0)
    return gains

h2 = json.load(open('results/h2_specificity_layer.json'))
cands = [c['v2_rep'] for c in h2['v1_candidates']
         if c['specificity']=='radiation_specific' and c['v2_emp_p_fisher'] < 0.05]
assert len(cands) == 10

rng = random.Random(SEED)
out = {'amendment':'H4c 2026-09-26 21:00 IST (tail-direction bug fix)','nperm':NPERM,'seed':SEED,
 'panel':'20 species (15 + H3 confirmation lineages); new-lineage presence is DOMAIN-LEVEL',
 'asr':'Fitch minimum gains (PastML cross-check queued)','candidates':{}}
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
    null.sort()
    p = (1 + sum(x <= obs for x in null))/(NPERM+1)  # H4c: LOWER tail (fewer gains = clade-consistent)
    out['candidates'][rep] = {'present_in': sorted(present), 'N_ind': obs,
        'null_median': null[NPERM//2], 'p': round(p,5),
        'h4b_pass': bool(obs >= 2 and p < 0.05)}
    print(rep, out['candidates'][rep])
json.dump(out, open('results/h4c_phylo_convergence_ext.json','w'), indent=1)
print('written results/h4c_phylo_convergence_ext.json')
