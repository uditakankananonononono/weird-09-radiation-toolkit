# Judge round 2 (formal) — W09 radiation-toolkit

- Route: TEXT-PASTE (browser slot, whole paper text, fresh conversation for this round)
- Conversation URL: https://chatgpt.com/c/6ab7e163-e3fc-83ee-8249-cc9284f93250
- Source text: /tmp/w09_paper_paste.txt, sha256 prefix 0d39127d98876aff
- Sent: 2026-09-26 ~20:45 IST, two ~4k parts (part 2 click-Send; Enter unreliable)
- Verdict-validity quotes present: "AhpC-TSA peroxiredoxin ... is re-labeled broad-stress adaptation", "DUF4385 protein --- the last representing genuinely novel candidate space", "locked gates", "Two honest negatives" — review is verifiably of THIS version.

## Verdict (judge, advisory)
1. v1->v2 specificity layer = MAJOR STRENGTH ("the strongest part of the project"); demoting AhpC-TSA to broad-stress adaptation increases credibility.
2. Biggest hole: PHYLOGENETIC NON-INDEPENDENCE. 3 Deinococcus spp. and 2 Thermus spp. are not independent replicates; label permutation only partially randomizes family structure (paper already admits this). Judge: "How do you know this is convergent retention caused by radiation resistance rather than ancestral retention in a stress-tolerant clade?"
3. One highest-value addition (laptop-feasible): phylogenetically aware convergence test — per surviving candidate, protein tree (FastTree/IQ-TREE), map presence/absence on species tree, infer min gains/losses (PastML/Count/Notung), compare vs structure-preserving randomized phenotype labels. Upgrades claim from "shared by resistant lineages" to "evolutionary convergence beyond what species relatedness predicts".
4. Verdict: strong ISEF finalist / possible category award contender NOW; with phylogenetic convergence modeling, substantially closer to grand-award competitive. Score-style: question importance very high, controls excellent, honesty excellent, biological mechanism moderate, validation absent.

## Critique + novelty change folded back (round counts only with this)
- Critique accepted: surviving candidates are candidate lists, not mechanistic discoveries; phylogenetic structure not fully controlled.
- NOVELTY CHANGE (to fold back): lock Amendment H4 — phylogenetically controlled convergence layer. For each of the 10 radiation-specific candidates: build orthogroup protein tree, run ancestral gain/loss reconstruction (PastML or Count) on the 15-species tree, and compare the number of independent resistant-lineage retentions against label permutations that PRESERVE phylogenetic structure (restricted permutations within clades). Locked before outcome inspection; results amend Section 3 and the limitations. Implementation: FastTree + PastML (pure-python), laptop-feasible, no new downloads beyond existing proteomes.
- Folded back in: data/PREREG amendment h4 (to be committed) + results/h4_phylo_convergence.json when run.
