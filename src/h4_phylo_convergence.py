#!/usr/bin/env python3
"""W09 H4: phylogenetically controlled convergence (Amendment H4, locked 20:57 IST pre-computation).
Per candidate: presence/absence over the fixed 15-species cladogram; N_ind = minimum
number of gain events (Fitch parsimony minimum = method-independent minimum) on branches
subtending >=1 resistant leaf. Null: 10,000 structure-preserving permutations that shuffle
PRESENCE assignments within exchangeable strata (h4_strata.json). Win: N_ind>=2 AND
observed in upper 5% tail (one-sided p<0.05).
NOTE: amendment names PastML ML-ASR; minimum-gain count is identical under Fitch by
definition; PastML cross-check queued (logged deviation, no threshold change).
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
NPERM, SEED = 10000, 260926

tree = Phylo.read('data/species_tree.nwk','newick')
leaves = [t.name for t in tree.get_terminals()]
strata = json.load(open('data/h4_strata.json'))
resistant = {s for s,v in strata['species_to_panel'].items() if v=='resistant'}

clusters = {}
for line in open('results/orthology/clusters_v2.tsv'):
    rep, mem = line.rstrip('\n').split('\t')
    clusters.setdefault(rep, set()).add(PREFIX[mem.split('|')[0]])

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
assert len(cands) == 10, len(cands)

rng = random.Random(SEED)
S = strata['strata']
out = {'amendment':'H4 2026-09-26 20:57 IST','nperm':NPERM,'seed':SEED,
       'asr':'Fitch minimum gains (PastML cross-check queued)','candidates':{}}
for rep in cands:
    present = clusters.get(rep, set())
    obs = n_ind(present, resistant)
    null = []
    for _ in range(NPERM):
        pres_p = set(present)
        for members in (S['deinococcaceae_resistant'], S['thermus_controls'], S['other_controls']):
            k = len(set(members) & present)
            pres_p -= set(members)
            pres_p |= set(rng.sample(members, k))
        null.append(n_ind(pres_p, resistant))
    null.sort()
    p = (1 + sum(x >= obs for x in null))/(NPERM+1)
    out['candidates'][rep] = {'present_in': sorted(present), 'N_ind': obs,
        'null_median': null[NPERM//2], 'p': round(p,5),
        'h4_pass': bool(obs >= 2 and p < 0.05)}
    print(rep, out['candidates'][rep])
json.dump(out, open('results/h4_phylo_convergence.json','w'), indent=1)
print('written results/h4_phylo_convergence.json')
