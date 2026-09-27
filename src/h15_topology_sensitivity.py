#!/usr/bin/env python3
"""W09 queue #15 alt-topology arm (amendment commit 823696a, locked pre-computation).
100 trees x k=3 random NNI on the committed 15-species cladogram; per tree per h4
candidate: observed Fitch N_ind + 2,000 within-strata null shuffles (h4 rule).
Stability table: N_ind/p min-median-max, pass-label flips, >10% => TOPOLOGY-SENSITIVE."""
import json, random, copy
from Bio import Phylo

SEED, NTREES, K_NNI, NPERM = 260927, 100, 3, 2000
PREFIX = {'Adineta_vaga':'A_vaga','Caenorhabditis_elegans':'C_elegans',
 'Deinococcus_deserti':'D_deserti','Deinococcus_geothermalis':'D_geothermalis',
 'Deinococcus_radiodurans':'D_radiodurans','Drosophila_melanogaster':'D_melanogaster',
 'Escherichia_coli':'E_coli','Hypsibius_exemplaris':'H_exemplaris',
 'Lactobacillus_plantarum':'L_plantarum','Pyrococcus_furiosus':'P_furiosus',
 'Ramazzottius_varieornatus':'R_varieornatus','Saccharomyces_cerevisiae':'S_cerevisiae',
 'Sulfolobus_solfataricus':'S_solfataricus','Thermus_aquaticus':'T_aquaticus',
 'Thermus_thermophilus':'T_thermophilus'}
base_tree = Phylo.read('data/species_tree.nwk','newick')
clusters = {}
for line in open('results/orthology/clusters_v2.tsv'):
    rep, mem = line.rstrip('\n').split('\t')
    clusters.setdefault(rep, set()).add(PREFIX[mem.split('|')[0]])
strata = json.load(open('data/h4_strata.json'))
resistant = {s for s,v in strata['species_to_panel'].items() if v=='resistant'}
S = strata['strata']
h4 = json.load(open('results/h4_phylo_convergence.json'))
cands = list(h4['candidates'].keys())

def n_ind(tree, present, res):
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

def random_nni(tree, rng):
    # pick a random internal edge (parent->child, child internal), swap one of
    # child's subtrees with one of parent's other subtrees
    internal = [c for c in tree.find_clades() if not c.is_terminal() and c is not tree.root]
    child = rng.choice(internal)
    parent = tree.get_path(child)[-2] if len(tree.get_path(child)) >= 2 else None
    # find parent via traversal (biopython lacks parent pointers)
    parent = None
    for c in tree.find_clades():
        if child in c.clades: parent = c; break
    if parent is None or len(child.clades) < 2 or len(parent.clades) < 2: return
    a = rng.choice(child.clades)           # subtree of child to move up
    b_choices = [c for c in parent.clades if c is not child]
    if not b_choices: return
    b = rng.choice(b_choices)              # subtree of parent to move down
    child.clades.remove(a); parent.clades.remove(b)
    child.clades.append(b); parent.clades.append(a)

rng = random.Random(SEED)
out = {'amendment_commit':'823696a','seed':SEED,'n_trees':NTREES,'k_nni':K_NNI,'nperm':NPERM,
       'scope':'NNI-perturbed alternative topologies; bootstrap/Bayesian arms deferred (no aligner/MSA) - recorded',
       'candidates':{}}
for rep in cands:
    present = clusters.get(rep, set())
    base = h4['candidates'][rep]
    rec = {'committed_tree': {'N_ind': base['N_ind'], 'p': base['p'], 'h4_pass': base['h4_pass']},
           'N_ind_dist': [], 'p_dist': [], 'pass_flips': 0}
    for t in range(NTREES):
        tr = copy.deepcopy(base_tree)
        for _ in range(K_NNI): random_nni(tr, rng)
        obs = n_ind(tr, present, resistant)
        null = []
        for _ in range(NPERM):
            pres_p = set(present)
            for members in (S['deinococcaceae_resistant'], S['thermus_controls'], S['other_controls']):
                k = len(set(members) & present)
                pres_p -= set(members)
                pres_p |= set(rng.sample(members, k))
            null.append(n_ind(tr, pres_p, resistant))
        p = (1 + sum(x >= obs for x in null))/(NPERM+1)
        passed = bool(obs >= 2 and p < 0.05)
        rec['N_ind_dist'].append(obs); rec['p_dist'].append(round(p,5))
        if passed != base['h4_pass']: rec['pass_flips'] += 1
    nd = sorted(rec.pop('N_ind_dist')); pd = sorted(rec.pop('p_dist'))
    rec['N_ind_min_med_max'] = [nd[0], nd[NTREES//2], nd[-1]]
    rec['p_min_med_max'] = [pd[0], pd[NTREES//2], pd[-1]]
    rec['topology_sensitive'] = rec['pass_flips'] > NTREES//10
    out['candidates'][rep] = rec
    print(rep, rec['N_ind_min_med_max'], rec['p_min_med_max'], 'flips', rec['pass_flips'], 'SENSITIVE' if rec['topology_sensitive'] else '', flush=True)
json.dump(out, open('results/h15_topology_sensitivity.json','w'), indent=1)
print('written results/h15_topology_sensitivity.json')
