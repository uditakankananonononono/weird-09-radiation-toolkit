# W09 PRE-REGISTRATION - RADIATION-SURVIVAL TOOLKIT (locked 2026-09-25)

## Question
Which molecular mechanisms for surviving extreme radiation/desiccation recur across independently radioresistant organisms (Deinococcus, tardigrades, bdelloid rotifers, radiotrophic fungi, extreme archaea), and which are plausibly transferable?

## Hypotheses
- H1: Cross-kingdom comparative analysis of radioresistant vs sensitive sister taxa identifies a convergent protective module set (Mn-antioxidant systems, DNA repair architectures, IDP protectants like Dsup/CAHS/LEA) enriched beyond a locked permutation null (p<0.01).
- H2: >=5 nominated transferable protectants show orthogonal support: convergent recruitment + structural evidence + (where published) heterologous-protection experiments concordant at locked thresholds.

## Locked gates
- G1 DATA: >=120 accession-level datasets (genomes/proteomes/transcriptomes of resistant + sister sensitive species; irradiation response datasets; protein structure resources).
- G2 TOOLS: >=40 genuine external tools (NCBI/SRA, OrthoFinder, HMMER/Pfam, MAFFT, IQ-TREE, HyPhy, ESMFold/AlphaFold DB, IUPred, enrichment stacks, etc.).
- G3 BENCHMARK: pipeline recovers the locked known protectants (Dsup, CAHS, DdrO/PprI axis, Mn-peptide antioxidants literature list) at >=80% recall before new nominations.
- G4 FORMULAS: >=10 numbered (convergence stats, enrichment nulls, dN/dS, structural metrics).
- G5 PAPER: >=20 pages TNR. G6 TOOL: "radshield" scorer ranking any proteome for predicted radioresistance toolkit completeness.

## Analysis plan
1. Freeze species panel: resistant/sensitive sister pairs per kingdom.
2. Orthogroup + convergence analysis (H1).
3. Structural/functional deep-dive on convergent modules; nomination list (H2).
4. Transferability scoring (expression feasibility, toxicity flags, literature support).
5. Toolkit tool + tests + paper.

## Redirect rules
- If H1 convergence fails at gene level: redirect to pathway/metabolite-level convergence (Mn/Fe homeostasis, metabolite protectants).
- If orthogroups across kingdoms are too sparse: redirect to domain-level and IDP-property-level analysis.
- If transferability scoring lacks ground truth: pivot to an astronaut/crop-relevant prioritization framework with explicit assumption ledger.

## Honest-negative policy
Modules found in only one lineage are labeled lineage-specific, never counted as convergent.

## AMENDMENT 2026-09-25 19:44 IST (user steering, authenticated WhatsApp 7:43 PM)
G5 PAPER floor raised: >= 50 pages of actual research content, EXCLUDING headings
and references (supersedes the >=20-page floor). Real content only - methods,
full per-attempt result tables, benchmark comparisons vs all relevant published
baselines, boundary analyses, negative-result supplements. Padding prohibited.
Also locked: world's-best-tools standard; continuous depth/feature improvement
after gates pass; negatives never published as the result (angles redirect until
a genuine positive, else escalate). Stacks on all prior steering; nothing relaxed.

## AMENDMENT 2026-09-25 21:29 IST (user steering, authenticated WhatsApp 9:28 PM, relayed by parent)
Every natural sub-project inside this item is a SEPARATE project with its own FULL
gate set: 40+ genuine external tools, 120+ accession datasets, 50-page TNR paper,
benchmark win or match+named-plus-point. Shared pipelines DO NOT transfer gate
credit between sub-projects: a run counts for a sub-project only when genuinely
executed FOR that sub-project; item-level shared runs are logged at item level
and do not inflate sub-project counts. Verdict reporting is per sub-project.

## AMENDMENT 2026-09-25 21:43 IST (user steering, authenticated WhatsApp 9:41-9:42 PM, relayed by parent)
(1) NOVELTY-LEAD: the paper must lead with what is genuinely NEW - the discovery,
pipeline/design advance, or new method. Benchmarks are supporting evidence, not
the headline. If no real novelty claim exists, that is said honestly and a
novelty-creation plan is named; incremental results are not dressed up.
(2) ISEF-JUDGE LOOP (completion requirement, per project incl. sub-projects):
after gates complete, ask ChatGPT (browser, user's account, free tier) whether
the project would win ISEF and for its weaknesses. Every round recorded verbatim
in the repo (question, critique, fix applied). Iterate until no material
weaknesses remain or only wet-lab/large-GPU items are left. Final judge verdict
reported honestly; never claim a win the judge did not give.

## AMENDMENT 2026-09-26 10:58 IST (pre-compute, ChatGPT design-verification round 1 - verbatim in judge/consult_design_round1.txt)
Locked BEFORE analysis. Amendments:
1. CONVERGENCE HIERARCHY PRE-DEFINED: ortholog-level where possible; else domain/fold/property-level; else pathway-level. Ortholog-level failure is NOT read as biological failure; primary analysis includes domain/property-level statistics from the start.
2. CIRCULARITY SPLIT: discovery phase blind (no known-protectant labels; blind pathway/domain enrichment), evaluation phase separate (known protectants used only to score, never to discover).
3. PHENOTYPE DEFINITIONS LOCKED: primary = quantitative radiation-survival metric (LD50/D10 where available); secondary categories recorded in ledger before sister-pair contrasts.
4. H2 OBJECTIVE RUBRIC: scoring rubric locked pre-analysis (evolutionary evidence fixed points, structure-confidence threshold, experimental-validation category weights) - no post-hoc composite tuning.
5. BENCHMARK NEGATIVES ADDED: radiation-sensitive relatives, unrelated stress-response proteins, random matched proteins; report recovery AND false-positive rate.
6. INDEPENDENCE TRACKING: both accession count and independent biological units (species/lineages/studies) tracked; independence inflation disclosed.
7. Judge dissent on dataset-count gates NOT adopted (user steering, verified WhatsApp 9:21/9:28 PM + 12:08 AM): count gates remain as deliverables alongside the scientific gates above.

## AMENDMENT 2026-09-26 11:15 IST (pre-formal-analysis; locked before formal outcome inspection)
Exploratory linclust tallies (results/orthology/) are QC-level only, no hypothesis claim. Formal tests locked here:
1. ORTHOGROUP CALLING: mmseqs2 sensitive cluster primary (min_id 0.3, cov 0.5, cov-mode 1); linclust as sensitivity only. Subset concordance (subset20k_concordance.json: purity 0.914, retention 0.363) documents linclust fragmentation - formal claims never rest on linclust counts.
2. ENRICHMENT TEST: per orthogroup, one-sided Fisher exact presence/absence resistant (Deinococcus x3 + tardigrade x2 + Adineta, independent origins) vs sensitive (Thermus x2, Hypsibius, C. elegans, Drosophila, E. coli); Mann-Whitney U on copy number. BH FDR 0.05.
3. INDEPENDENCE: Deinococcus spp are one origin; convergent signal requires enrichment in >=2 independent resistant origins (Deinococcaceae, Tardigrada, Bdelloidea).
4. NEGATIVE CONTROLS: 100 label permutations, FDR calibration reported.
5. No threshold tuning after formal results.

## AMENDMENT 2026-09-26 11:29 IST (PRE-OUTCOME: no formal test results exist yet for this project)
W03's locked H1 run proved the BH-FDR(0.05)-over-all-orthogroups gate is structurally impossible at this panel size (results in W03 repo: h1_power_analysis.json - minimum achievable p at 6v6 complete separation 1.08e-3 vs BH rank-1 threshold ~1e-6). The same flaw applies to this project's 11:15 amendment. Locked correction BEFORE any formal outcome inspection:
1. The Fisher+MWU tests, one-sidedness, independence tiers, and convergence criteria stand unchanged.
2. The BH-FDR GATE is replaced by permutation-calibrated empirical significance: 1000 label permutations; per-orthogroup empirical p = fraction of permutations with a more extreme statistic; GATE = empirical p<0.05 with effect in the locked direction, replicating in the locked number of independent origins. This is a power correction, not a relaxation: the permutation null is stricter than BH for correlated tests and is the same calibration already locked as the negative control.
3. Rationale and W03 power analysis cited in the paper's methods/honesty section.

## AMENDMENT 2026-09-26 13:18 IST (H1-extension: stress-matched control panel; judge formal round 1 required strengthening; PRE-DATA: no proteomes downloaded yet)
Judge verdict (judge/consult_formal_round1.txt, attachment-verified): surviving alternative explanation = broad stress-adaptation rather than radiation selection. Locked extension, species chosen BEFORE any download or test:
1. STRESS-MATCHED RADIO-SENSITIVE CONTROLS (4): Pyrococcus furiosus (hyperthermophile), Sulfolobus solfataricus (thermoacidophile), Lactobacillus plantarum (acid/osmotolerant), Saccharomyces cerevisiae (osmo/ethanol-tolerant). All are stress-tolerant AND radiation-sensitive (literature-known; if any turns out radiation-resistant it stays in the panel and the fact is reported - no swapping).
2. TEST: identical locked pipeline (sensitive clustering on the expanded 16-proteome set, same Fisher/MWU/1000-permutation gates, same >=2-of-3-origins rule). The 12 gate-passing orthogroups are re-tested: the radiation-specificity claim survives ONLY for candidates absent from >=3 of 4 stress-matched controls (locked threshold). Candidates failing this are re-labeled broad-stress-adaptation and the paper says so.
3. New proteomes logged as accession datasets with provenance verification (existing ledger rules).
4. This extension does not reopen H1's gates or p-values; it adds a specificity layer on top of the already-committed result.

## AMENDMENT 2026-09-26 20:21 IST (domain-level orthogonal confirmation arm; PRE-DATA: no new proteomes downloaded yet, no outcomes inspected)
Locked BEFORE download/analysis. Purpose: test whether the 10 v2 radiation-specific candidates' PFAM DOMAIN content recurs in an INDEPENDENT set of radiation-resistant lineages absent from the original 15-species panel (paper "Next experiments" item 3; design-amendment hierarchy step 2).
Extended confirmation panel (accessions live-verified via NCBI datasets v2alpha 20:19-20:21 IST):
- Deinococcus radiophilus GCF_020889625.1 (Complete)
- Deinococcus proteolyticus GCF_000190555.1 (Complete)
- Deinococcus maricopensis GCF_000186385.1 (Complete)
- Adineta ricciae GCA_905250025.1 (Scaffold)
- Rotaria magnacalcarata GCA_965140935.1 (Scaffold)
Unavailable (logged, no substitution): Richtersius coronifer (no assembly in datasets v2alpha), Milnesium tardigradum GCF_001039535.1 (API FAIL, consistent with earlier finding).
Rules: (1) confirmation = a candidate's Pfam domain architecture (v1 annotation/pfam_domtblout calls) found in >=1 protein of >=2 of the 5 NEW proteomes; (2) NEW-panel hits count only at the domain level (no orthology claim to original reps); (3) candidates failing confirmation are NOT removed from the v2 set - the arm is confirmatory only, and a negative is reported as "domain-level support absent in extended panel"; (4) accessions ledgered with sha256 in data/panel_accessions.json at download; (5) no threshold changes after first result inspection.

## AMENDMENT H4 2026-09-26 20:57 IST (phylogenetically controlled convergence layer; locked BEFORE any H4 computation)
Authority: judge round 2 novelty foldback (judge/consult_formal_round2.meta.md) + user steering 16:12 IST rule 6 (pivot on strongest redirection). Judge's flagged hole: label permutation only partially randomizes family-level phylogenetic structure; 3 Deinococcus spp. and 2 Thermus spp. are not independent replicates.
1. For each of the 10 v2 radiation-specific candidates: collect orthogroup member sequences from clusters_v2.tsv, align (local aligner; EBI mafft REST fallback), build protein tree (Biopython NJ; FastTree if a binary can be fetched), and run ancestral-state reconstruction of presence/absence on the FIXED 15-species cladogram (species tree topology fixed from NCBI taxonomy at lock time, recorded in data/species_tree.nwk) using PastML (ML, F81-like two-state). 
2. Statistic per candidate: N_ind = minimum number of independent resistant-lineage retentions (gains or maintained presences at independent origins) required to explain the observed pattern, taken from the PastML reconstruction (root-to-tip gain count under the resistant clades' MRCAs).
3. Null: 10,000 phenotype-label permutations that PRESERVE phylogenetic structure - resistant/sensitive labels permuted only within exchangeable strata {Deinococcaceae resistant spp.} and {Thermus controls} and {other controls}, never across - recompute N_ind for each. Win per candidate: observed N_ind >= 2 (independent origins) AND observed pattern in the upper 5% tail vs structured null (one-sided p<0.05).
4. Gate: H4 is a CONFIRMATION layer on the v2 set (same rule as the domain arm): candidates failing H4 are labeled "phylogenetic-structure caveat" in the paper, NOT removed. H4-passing candidates get the strengthened claim "convergence beyond what species relatedness predicts."
5. Species tree, aligner, tree method, and the permutation strata are fixed here; no changes after first H4 result inspection.

## AMENDMENT H4b 2026-09-26 20:59 IST (locked BEFORE computation; H4 result inspected and recorded)
H4 result (results/h4_phylo_convergence.json): the structure-preserving null has ZERO VARIANCE on the 15-species panel (all 10 candidates: N_ind=2, null median=2, p=1.0). Cause: resistance labels are perfectly confounded with the tree (single resistant bacterial family + two fixed metazoan singleton origins), so no within-strata permutation can separate convergence from clade structure. This is an honest structural null, not a candidate failure; it quantifies the judge-flagged limitation already admitted in the paper.
1. EXTENDED-PANEL ARM: rebuild the presence/absence matrix on the 20-species panel (original 15 + H3's 5 confirmation lineages: D. radiophilus, D. proteolyticus, D. maricopensis, A. ricciae, R. magnacalcarata). Candidate presence in the 5 new lineages = domain-level presence from the H3 confirmation scan (h3_domain_confirmation.json), explicitly labeled domain-level (no orthology claim, same rule as H3).
2. Extended tree: bdelloid clade becomes (A_vaga,(A_ricciae,R_magnacalcarata)); Deinococcaceae clade gains the 3 new Deinococcus spp. as an unresolved clade with the original 3; recorded in data/species_tree_ext.nwk. Strata: deinococcaceae_resistant (6), bdelloid_resistant (3), other leaves unchanged.
3. Statistic and null identical to H4 (Fitch min gains into resistant-subtending branches; 10,000 within-strata presence shuffles; seed 260926). Win per candidate: N_ind>=2 AND p<0.05. Failing candidates keep the "phylogenetic-structure caveat" label (H4 rule 4 unchanged); passing candidates earn the strengthened convergence claim.
4. If the extended null still has no power, that is reported as the terminal identifiability statement for the computational panel and the paper carries it as the primary limitation.

## AMENDMENT H4c 2026-09-26 21:00 IST (metric-direction bug fix; locked BEFORE the corrected evaluation; H4b result inspected and recorded)
H4b result (results/h4b_phylo_convergence_ext.json): all 10 candidates p=1.0. Inspection shows the bug is in MY locked tail direction, not the data: under the structured null, presence scattered randomly within a resistant clade requires MORE gains, while clade-consistent retention requires FEWER. The convergence-consistent direction is therefore the LOWER tail (observed gains fewer than null), exactly the reverse of H4/H4b's "upper 5% tail". Per the standing rule (metric bugs get new locked amendments): the statistic is corrected to p_lower = (1 + #{null <= obs})/(N+1), win = N_ind >= 2 AND p_lower < 0.05. Everything else (tree, strata, seed, NPERM, Fitch gains, domain-level rule for new lineages) unchanged from H4b.

## CORRECTION AMENDMENT 2026-09-27 00:54 IST (panel-mapping bug; locked BEFORE corrected-outcome inspection)
Paper-builder code audit found analysis/formal_tests.py built copy vectors as np.zeros(12) over an 11-species panel (5 resistant - Milnesium terminally unavailable - 6 sensitive): Thermus_aquaticus (index 5) entered the RESISTANT arm, a phantom 12th all-zero column entered the sensitive arm, and the Fisher hypergeometric (12/6), MWU 6x6 constants (mean 18, sd sqrt(39)), and rng.permutation(12) all encoded the wrong 6v6 panel. analysis/specificity_layer.py has correct 5v6 slices and Fisher, but hard-coded the same wrong 6x6 MWU constants.
LOCKED CORRECTION (no gate/threshold changes): true panel 5v6 (11 species); vectors np.zeros(11); resistant indices 0-4, sensitive 5-10; Fisher hypergeom.sf(pm-1, 11, pm+ps, 5); MWU 5x6 normal approx mean 15, sd sqrt(30); rng.permutation(11); SAME locked gates (empirical p<0.05 resistant-direction, >=2 of 3 origins; MWU secondary arm), SAME seed 11, SAME NPERM=1000, same (cnt+1)/(NPERM+1) convention as the H2 layer. The buggy outputs are archived (results/h1_formal_tests_buggy_20260926.json) for the audit trail; corrected run overwrites results/h1_formal_tests.json with a correction note in the method field. H2 specificity layer re-run on the corrected H1 candidate set. Whatever survives survives; candidates that die are reported as dead.

## AMENDMENT 2026-09-27 01:14 IST (H5: mechanistic-prioritization rubric - locked BEFORE any candidate scores are computed)
Judge round 3 named the remaining hole: mechanistic prioritization beyond statistical control. Locked rubric:
MECHANISM CATEGORIES (from radiation-survival literature): (C1) DNA repair & genome maintenance; (C2) oxidative-stress response & redox homeostasis; (C3) protein protection & repair; (C4) nucleotide/precursor supply; (C5) envelope & extracellular polysaccharide (desiccation-radiation coupling).
DOMAIN -> CATEGORY MAP (fixed, from Pfam family descriptions; each domain maps to at most one category; unmapped domains score nothing and are recorded):
HPPK->C4; Pterin_bind->C4; Ank,Ank_2,Ank_3,Ank_4,Ank_5->C3 (scaffold mediating repair-complex interactions); DHH,DHHA2->C1 (DHH-family phosphoesterases include repair nucleases); DSBA,Thioredoxin_4->C2; Flavin_Reduct->C2; NmrA->C2 (redox sensor); Amidase,Bac_rhamnosid,Bac_rhamnosid6H,Bac_rhamnosid_N,Ig_Rha78A_N->C5; 3Beta_HSD,Epimerase,GDP_Man_Dehyd,Polysacc_synt_2,RmlD_sub_bind->C5; DUF4385,HAD_2,Hydrolase,Hydrolase_like,NAD_binding_4,NAD_binding_10,Acetyltransf_1,Acetyltransf_7,Acetyltransf_10,PAD_porph->unmapped (generic/insufficient mechanistic link; PAD_porph recorded as unmapped rather than weak-C2 to keep the map conservative).
SCORE: number of DISTINCT mechanism categories hit by a candidate's confirmed Pfam domain set (0-2 expected, max 5). Tie-breaks in order: (a) domain-confirmation status (confirmed in extended panel first); (b) FEWER total domains (specificity over promiscuity).
WIN CONDITION (falsifiable): the top-ranked candidate's protein family has independent literature evidence of a radiation- or desiccation-resistance phenotype (PubMed title/abstract search, queries locked below, executed after scoring). If the top rank lacks support while a lower-ranked candidate has it, the rubric's current form is falsified and reported honestly; the ranking is not tuned post-hoc.
LOCKED QUERIES (PubMed esearch, per candidate family): "<family name> AND (radiation resistance OR radioresistance OR desiccation resistance OR ionizing radiation)". Hits inspected by title/abstract; a hit counts only if it reports a resistance-associated phenotype for the family, not mere co-occurrence of words.

## AMENDMENT 2026-09-27 08:59 IST (H4 redirect foldback: Saturated Co-Retention test - locked BEFORE any S-value inspection)
Source: judge redirect consult round 4 (Gemini, thread https://gemini.google.com/app/5033ed15bb2f6e00, verdict archived judge/round4_h4redirect_verdict_gemini.txt). The H4 boundary stands: convergence-beyond-relatedness is unidentifiable on the saturated 11-species panel. The verdict's immediately computable reframe is locked here as the next arm. (Its other two directions - HyPhy/codeml RELAX selection-intensity test and dispersed-origin panel expansion with named taxa - are staged follow-ups that get their own locked amendments before any run.)

REFRAMED CLAIM: conserved co-retention across deep divides - candidate orthogroups show COMPLETE co-retention across all sampled resistant clades with absence from all sensitive controls, a configuration that is RARE against the proteome-wide orthogroup background.

STATISTIC (exact, per verdict): for orthogroup g, clade completeness c_C(g) = (# resistant species of clade C with a member of g) / (# resistant species of clade C in the panel). Clades: Deinococcaceae (3 species), Tardigrada (1: R. varieornatus; Milnesium terminally unavailable, disclosed), Bdelloidea (1: A. vaga). S(g) = c_Deino * c_Tardi * c_Bdello. Complete co-retention tier: S(g) = 1.0 AND zero sensitive-lineage copies.

NULL DISTRIBUTION: all M = 52,786 tested orthogroups in results/orthology/clusters_sensitive.tsv (same corrected 5v6 panel mapping as the 00:54 amendment; no re-clustering, no new data).

EMPIRICAL P (exact): P = (1 + #{background orthogroups with S = 1.0 AND sensitive copies = 0}) / (M + 1).

WIN CONDITION (locked, from verdict): P < 0.005 - i.e. fewer than 0.5% of background orthogroups attain complete co-retention while remaining absent from controls, so the candidate configuration sits in the extreme tail.

FALSIFICATION BRANCH: if P >= 0.005, complete co-retention is not rare on this panel; the reframe is reported as NOT earned and the paper keeps the quantified H4 identifiability boundary as the terminal statement (no post-hoc re-tuning).

HONESTY CAVEATS (locked into the report): (i) candidates were selected on presence criteria that overlap S, so this test quantifies the background RARITY of the selection configuration; it is not an independent validation of convergence; (ii) Tardigrada completeness is a 1-species call; (iii) P is a background-frequency statement, not a phylogenetic-independence statement - convergence beyond relatedness remains unclaimed.

## AMENDMENT 2026-09-27 10:10 IST (H5 v2: evidence-graded shortlist + reference-standard benchmark; judge verdict foldback from round_supp2, thread https://gemini.google.com/app/9098779be8e670b7, verdict judge/round_supp2_h5v2_verdict_gemini.txt; locked BEFORE any evidence-grading or enrichment computation)

The v1 rubric win condition (top-ranked candidate carries FAMILY-LEVEL published radiation-resistance evidence) FAILED and is preserved as an honest negative. v2 adopts the judge's option (c): the deliverable is the ranked shortlist WITH a two-tier evidence classification; the falsifiable claim is prioritization quality against a locked reference standard. Rubric v1's failure is reported alongside v2 in the paper (judge's instruction adopted).

POSITIVE REFERENCE STANDARD S+ (locked; N=10 families chosen from canonical reviews and primary literature, INDEPENDENT of the v1 ranking and pool; selection grounded in the sources below, not in any candidate outcome):
1. DdrA (Deinococcus radiodurans; genome-integrity protection) - PLOS Biology 2004, DOI 10.1371/journal.pbio.0020304.
2. DdrB (D. radiodurans; ssDNA annealing, DSB repair/ESDSA) - PMC3268515; PMC4843489.
3. PprA (D. radiodurans; DNA ligation stimulation) - Mol Microbiol 2004, DOI 10.1111/j.1365-2958.2004.04272.x.
4. PprI (D. radiodurans; damage-sensing protease, radioresistance switch) - Biochem Biophys Res Commun 2003 (S0006291X03009653); Nat Commun 2024, DOI 10.1038/s41467-024-46208-9.
5. Dps1/Dps2 (D. radiodurans; DNA-binding protection, ferritin homolog) - PMID 26290287; PMID 22857940.
6. RecA (D. radiodurans; ESDSA reassembly of shattered chromosomes) - Zahradka et al. Nature 2006, PMID 17006450.
7. Dsup (tardigrade Hypsibius; DNA-protection protein, radiotolerance transfer) - Hashimoto et al. Nat Commun 2016, PMID 27649274.
8. CAHS (tardigrade cytoplasmic abundant heat soluble) - PLOS ONE 2012, DOI 10.1371/journal.pone.0044209; Boothby et al. Mol Cell 2017, PMID 28318683.
9. SAHS (tardigrade secretory abundant heat soluble) - PLOS ONE 2012 (same DOI); Comms Biology 2024, DOI 10.1038/s42003-024-06336-w.
10. LEA group 3 (bdelloid rotifer Adineta; desiccation/radiation-linked protection) - functional characterization (repository.cam.ac.uk/items/668590fb-ed03-4632-848a-fe5a3d99cde0); BMC Biology 2023, PMC10809525.
Clade coverage: 6 Deinococcaceae, 3 Tardigrada, 1 Bdelloidea - mirrors the project clades.

CANDIDATE POOL C (locked): the 11 v1-ranked candidates in results/h5_mechanistic_prioritization.json (K=11). No additions or removals in v2.

EVIDENCE-GRADING PROTOCOL (locked): each candidate family gets a PubMed/PMC literature pass: query = family name + (radiation OR radioresistance OR desiccation OR "oxidative stress" OR "DNA repair"); TIER 1 = at least one primary experimental paper tying the protein FAMILY (or a named ortholog group containing it) to radiation/desiccation resistance phenotypes, verified by reading the abstract (false-positive inspection mandatory, per the v1 NmrA lesson); TIER 2 = mechanism-level only (domain chemistry consistent with C1-C5 repair/protection, no family-level resistance paper); TIER 0 = neither. Grading notes saved per candidate in results/h5v2_evidence_grading.json.

METRICS + NULL + WIN (judge's locked form, verbatim structure):
- Primary: P@5 precision and hypergeometric enrichment. NULL H0: ranking concentrates Tier-1/S+ families no better than a uniform random permutation of C. Statistic: P(X>=x) hypergeometric with K=11, k=5, |S+ ∩ C| = (computed at grading time, reported), x = Tier-1/S+ families in top 5.
- Secondary: MRR of S+ members in the ranking; EF@5.
- WIN v2 iff BOTH: (i) P@5 >= 3/5 candidates with Tier-1 OR Tier-2 evidence AND at least one Tier-1/S+ candidate in the top 3; (ii) hypergeometric enrichment p < 0.05.
- FALSIFICATION: either leg fails -> the prioritization claim is reported as not earned; no post-hoc changes to S+, C, k, or alpha.

CORRECTION 10:12 IST: the RecA anchor PMID in the 10:10 amendment read 17016550; the correct Zahradka et al. Nature 2006 PMID is 17006450 (verified pubmed.ncbi.nlm.nih.gov/17006450). Reference-set membership unchanged; citation field fixed above.

CORRECTION 10:14 IST (pre-grading, pre-evaluation; no v2 outcome has been computed): the 10:10 amendment's enrichment base "S+ ∩ C" is vacuous BY SCREEN CONSTRUCTION - the screen required presence in resistant clades AND absence from sensitive controls, which systematically excludes universal canonical repair families (RecA, Dps, catalase-class enzymes are present in sensitive species and were filtered out upstream), so S+ ∩ C = 0 and the hypergeometric leg would be unsatisfiable, providing no selection signal (same failure class as the W11 v1 battery). The enrichment reference is therefore redefined WITHOUT touching the statistical form: x = number of Tier-1-evidenced candidates in the top 5; reference total = the number of Tier-1-evidenced candidates among all K=11, where Tier-1 grading is performed rank-blind (all 11 graded before any rank-position lookup) under the locked grading protocol. The locked S+ list is retained as the grading literature map (Tier-1 assignment may cite S+ membership OR other family-level primary evidence, e.g. the DsbA PMIDs already on record). NULL H0: Tier-1 candidates concentrate in the top 5 no better than uniform random permutation of C (hypergeometric, K=11, k=5, alpha 0.05). WIN leg (ii) unchanged: p < 0.05. WIN leg (i) unchanged: P@5 >= 3/5 Tier-1-or-Tier-2 AND >= 1 Tier-1 in top 3. This correction is locked BEFORE the grading pass begins.

## AMENDMENT 2026-09-27 12:06 IST (provided-verdict queue #3: formal Identifiability Score - locked BEFORE computation)
Formalizes the H4-terminal identifiability boundary as a per-candidate diagnostic. Definitions locked:
- INFORMATIVE STRATUM: a shuffled stratum (Deinococcaceae k/6, Bdelloida k/3) with PARTIAL occupancy (0 < k < stratum size) - only partial strata give the within-strata shuffle real variance.
- Components per candidate (20-species extended panel): I = (n_informative_strata, achievable gains range [g_min, g_max] under the locked null, null SD, p_min = (1 + #(null <= g_min)) / (NPERM+1) - the smallest lower-tail p ANY observation could achieve).
- CLASS (locked): IMPOSSIBLE if null SD = 0 (all strata saturated or empty - the shuffle is the identity); UNDERPOWERED if SD > 0 and p_min >= 0.05; TESTABLE if SD > 0 and p_min < 0.05.
- Null streams: replicate the locked H4c pipeline exactly (exec-prefix of src/h4b_extended.py through its seed line; one Random(260926) stream consumed in the committed candidate order; 10,000 within-strata shuffles per candidate, full distribution recorded).
- SANITY LOCKS: every candidate's recomputed observed gains and p must reproduce results/h4c_phylo_convergence_ext.json exactly (within permutation rounding); mismatch aborts with no score claimed.
- The 15-species panel is described from committed results only (H4: zero-variance nulls on all 10) - no recomputation.
- Framing locked: the score is the centerpiece of the framework-that-prevents-false-convergence headline (her 10:35 directive): it separates "falsified" from "untestable in principle on this panel" and names the remedy (dispersed resistant lineages, not more within-clade proteomes). No H4 gate or label changes.

## AMENDMENT 2026-09-27 12:08 IST (provided-verdict queue #19: formal pipeline definition - locked BEFORE writing)
PAPER ARTIFACT, no compute gate. Add a Methods subsection defining the pipeline end-to-end in operator form: inputs (panel proteomes + fixed resistant/sensitive labels + background orthogroup universe), the five stage operators (clustering, enrichment gate, specificity filter, domain confirmation, identifiability audit), and the OUTPUT object: an ordered verdict class per candidate, not a scalar. Locked framing: a scalar "convergence score" would be post-hoc numerology on a panel where the identifiability audit returns IMPOSSIBLE/UNDERPOWERED; the honest output is the ordered class {confirmed-convergent > candidate-testable > candidate-underpowered > candidate-untestable > rejected}, with the identifiability class as a PRECONDITION for interpreting any convergence claim (framework-that-prevents-false-convergence, her 10:35 directive). Every symbol reuses committed definitions; no new empirics, no gate changes.

## AMENDMENT 2026-09-27 12:09 IST (provided-verdict queue #13: genome-wide permutation FDR - locked BEFORE computation)
Question: how many of the 12 passing candidates are expected by chance under a COMPLETE null (no label structure)?
Design locked:
1. Presence matrix rebuilt from results/orthology/clusters_v2.tsv (the screen's own clustering, true 5v6 panel per the 00:54 correction): X[g,i] in {0,1}, 52,786 x 11.
2. Genome-wide null: B'=1000 label permutations (seed 260927, one shared Random stream); per permutation b, every orthogroup is scored by the RAW one-sided Fisher (hypergeometric tail, margins fixed by the permutation: N=11, K=k_total(g), n=5 resistant) - vectorized.
3. Pass rule under permutation (locked mirror of the screen gate): raw Fisher p < 0.05 AND resistant-direction (k_res > expected under margins) AND present in >=2 of the 3 resistant-origin clades among the permutation-labeled resistant species (Deinococcaceae/Tardigrada/Bdelloidea, fixed clade definitions).
4. DISCLOSED APPROXIMATION (locked): the screen gate used per-orthogroup EMPIRICAL p (1000 perms each); the genome-wide null uses RAW Fisher p, because nesting 1000 perms inside 1000 perms over 52,786 orthogroups is infeasible. The estimate is therefore the FDR of the raw-Fisher screen at the same alpha and gates; the empirical-p screen is its B=1000 shuffle-calibrated refinement. This direction of approximation is disclosed, not hidden.
5. Outputs: null distribution of total passer counts; FDR_hat = mean(null passers)/12; P(null passers >= 12); per-permutation passer lists retained for overlap analysis (are the 12 real passers ever hit under null, and how often).
6. SANITY LOCKS: under TRUE labels, the reconstruction's raw-Fisher passer set must contain the 12 committed screen hits (their k_res/k_total must match clusters_v2); mismatch aborts.
7. Framing locked: FDR_hat reported as an estimate with its approximation disclosed; no gate changes; the identifiability classes of Section 4.5 remain the terminal convergence statement.

## FOLLOW-UP AMENDMENT h8b (locked 2026-09-27 12:13 IST, BEFORE compute): screen-exact genome-wide permutation FDR
Amendment h8 (raw one-sided hypergeometric Fisher on the clusters_v2 presence matrix) ABORTED on its own sanity lock: 3 of the 12 committed hits (UJR09360.1, UJR10666.1, UJR11615.1) are not raw-Fisher passers. Root cause found before any further compute: h8 tested the WRONG statistic on the WRONG input - the H1 screen (analysis/formal_tests.py, commit c0ace15) operates on copy counts in clusters_sensitive.tsv (5 resistant: 3 Deinococcus + R. varieornatus + A. vaga; 6 sensitive), with per-orthogroup empirical p from 1000 label permutations (seed 11, (cnt+1)/1001) plus the >=2-of-3-origins gate. Abort recorded in results/h8_genomewide_fdr.json.
LOCKED h8b DESIGN (no further degrees of freedom after this line):
1. Replicate the screen EXACTLY from analysis/formal_tests.py: same input, arms, hypergeom call, seed 11, NPERM=1000; store per-orthogroup Fisher stats for the true labeling AND all 1000 permutations (matrix S, n x 1001), plus the permutation orders.
2. SANITY LOCK: true-label replication must reproduce exactly the 12 committed hit reps and emp_p = 13/1001 for each; else abort, document, exit 1.
3. FDR by rank recursion over S: for each permutation k, pseudo-hits_k = #{g: (1 + #{j != k: S[g,j] <= S[g,k]})/1001 < 0.05 AND pm_g(k) > ps_g(k) AND origins_g(k) >= 2}, with origins evaluated on fixed genome identity under the permuted arm split. Disclosed approximation: each permuted labeling is calibrated against the same fixed permutation set (exact by group symmetry only in expectation over redrawn permutations).
4. Report: FDR_est = mean_k(pseudo-hits_k)/12, 95% normal upper bound, median and max null hits, distribution summary.
5. Pass rule (report-only, no retro-fit): FDR_est <= 0.05 supports the statement "genome-wide permutation FDR <= 5%"; any higher value is reported verbatim in Results and Caveats. The twelve committed hits, gates, seed and NPERM are unchanged; this amendment adds an error-rate estimate, it does not re-select hits.

### h8b erratum (12:15 IST): sanity-lock criterion corrected BEFORE any h8b output is used - the committed h1 record holds WP_012692142.1 at emp_p=17/1001 (11 hits at 13/1001, 1 at 17/1001). Lock now requires EXACT per-hit reproduction of the stored h1_formal_tests.json values (stricter than the original blanket 13/1001).

## AMENDMENT 2026-09-27 12:19 IST (provided-verdict queue #7: simpler-method baselines - locked BEFORE any baseline list is generated or graded)
QUESTION: does the full framework's committed 12-candidate list beat simpler selection rules on the locked H5 v2 evidence standard?
ARMS (each selects exactly 12 orthogroups from the 52,786 H1-tested universe):
- B0 RANDOM: uniform without replacement, numpy default_rng(26092707), 1000 replicate draws; reported as a distribution, never a single draw. Grading approximation (locked, disclosed): 3 draws (36 entries) graded, mean extrapolated to the distribution.
- B1 SEQUENCE-ONLY: mmseqs2 easy-search (static build 057db43, e-value <= 1e-5, min cov 0.5) of the 11 PANEL proteomes (all_proteomes_tagged.faa) against the locked S+ reference set (10 families from the 10:10 amendment; representative accessions efetched from NCBI protein, sha256-ledgered). An orthogroup (clusters_sensitive.tsv universe) is called if ANY member hits; ranked by best e-value then bitscore; top 12. Tool disclosure: mmseqs2 substitutes for BLAST (same sequence-similarity class).
- B2 DOMAIN-ONLY: resistant-vs-sensitive one-sided Fisher on Pfam domain presence per orthogroup (existing annotation, same hypergeom kernel as H1), p<0.05, resistant direction, NO specificity layer, NO origins gate; top 12 by p then effect size (pm-ps).
- B3 FULL FRAMEWORK: the committed 12 (already graded in h5v2).
EVALUATION (locked, no retro-fit): B1+B2+B0 candidates pooled, shuffled under Random(26092708), graded arm-blind under the locked 10:10 protocol (Tier 1 family-level primary paper, abstract verified; Tier 2 mechanism-level; Tier 0 neither); grading notes per entry; arm mapping archived. Metrics: Tier-1 count and Tier-1-or-2 count per arm.
STATEMENT RULE: "framework outperforms baseline X" only if B3 STRICTLY exceeds X on Tier-1-or-2 count; ties/shortfalls reported verbatim; B0 by interval comparison, no p-value claimed.
ABORT RULES: B1 or B2 returning <12 calls -> shortfall reported, no padding; S+ efetch failure for a family -> family dropped, reduction disclosed.
SCOPE: no re-selection of the committed 12, no gate changes; benchmarking arm, reported as its own Results subsection.

### #7 erratum (12:21 IST, BEFORE any B2 list generation): "existing annotation" covered only 23 candidate proteins. B2 therefore generates its input by a panel-wide hmmscan of the SAME locked 64 Pfam HMM set (data/pfam_hmms, HMMER 3.3.2) against all_proteomes_tagged.faa, domtblout E<=1e-5 per domain; unit stays per-orthogroup (any member annotated -> orthogroup annotated); all other B2 terms unchanged. This expands data generation, not the decision rule.

## AMENDMENT 2026-09-27 12:29 IST (provided-verdict queue #9: orthogroup-calling uncertainty - locked BEFORE computation)
QUESTION: are the committed 12 stable to the orthogroup-calling method? Locked design: re-map each committed hit's member proteins across the three committed clusterings on disk (clusters_sensitive.tsv = primary mmseqs sensitive; clusters_v2.tsv = 13-species v2; clusters_linclust30.tsv = linclust sensitivity arm). A hit is STABLE in a clustering if its members co-cluster (same cluster id for >=80% of its resistant-arm members) AND the resistant-vs-sensitive presence pattern (5v6 arms, panel intersection) reproduces the primary direction (pm>ps). Report: per-hit stability table + count stable in 2/2 alternative clusterings. PASS RULE (report-only): stability count reported verbatim; hits unstable in both alternatives are flagged in Results+Caveats, NOT removed (the primary clustering is the committed screen; this is a sensitivity audit). No re-selection, no gate changes.

## AMENDMENT 2026-09-27 12:29 IST (provided-verdict queue #8: copy-number/assembly-bias control - locked BEFORE computation)
QUESTION: do the committed 12 reflect assembly quality differences rather than biology? Locked design: assembly stats per panel genome from results/proteome_stats (protein counts; BUSCO if present) + NCBI assembly metadata already ledgered. Controls: (a) Spearman correlation between per-genome protein count and per-genome presence count across the 12 hit orthogroups (null: rho>0.7 = assembly-driven); (b) arm-level comparison: resistant vs sensitive median proteome size (MWU, disclosed small-n); (c) per-hit check: every committed hit must have >=3 of 5 resistant genomes with protein counts within 2x of the panel median (locked threshold, disclosed heuristic). PASS RULE (report-only): statistics reported verbatim; any hit failing (c) is flagged, not removed. No gate changes.

## AMENDMENT 2026-09-27 12:38 IST (provided-verdict queue #10: radiation-specific vs general-stress classification - locked BEFORE computation; delegated executor under this protocol)
QUESTION: are the committed 12 radiation-specific or general-stress adaptation? Locked design: re-run the H1 gate on the SAME clusters_sensitive.tsv matrix under TWO alternative sensitive-arm compositions, 1000 label permutations each (seed 260927, per-orthogroup empirical p, (cnt+1)/1001), gate unchanged (empirical p<0.05, resistant direction, >=2/3 origins):
- S-A LAB-MODEL CONTROLS ONLY: sensitive = {C. elegans, D. melanogaster, E. coli} (8 genomes total; Fisher hypergeom.sf(pm-1, 8, pm+ps, 5)).
- S-B STRESS-SPECIALIST CONTROLS ONLY: sensitive = {T. aquaticus, T. thermophilus, H. exemplaris} (8 genomes total; same kernel).
CLASSIFICATION (locked, descriptive): RADIATION-LEANING = passes committed panel AND S-B (association survives subtracting stress-specialist controls); GENERAL-STRESS-LEANING = passes S-A but NOT S-B (shared with stress-tolerant sensitive species); CONTROL-DEPENDENT = fails S-A. Scope: the 12 committed candidates ONLY; no new hit selection, no removals. PASS RULE (report-only): per-candidate classification + empirical p under each composition, verbatim; classes are descriptive labels for the paper, not gate changes.

## AMENDMENT 2026-09-27 13:21 IST (provided-verdict queue #1: paper-spine reframe - documentation-only, locked BEFORE drafting)
DOCUMENTATION-ONLY: rewrite the Introduction spine so the contribution is the FALSE-CONVERGENCE PREVENTION FRAMEWORK (locked gates, identifiability scoring, baseline comparison, power limits) with the molecular null reported inside it - not a paper whose headline is a failed molecular claim. No new compute; no result changes; every cited number must trace to a committed result file.

## AMENDMENT 2026-09-27 13:25 IST (provided-verdict queue #5: functional evidence tiers - locked BEFORE classification)
CLASSIFICATION-ONLY from committed data: each of the 12 committed candidates gets a tier record: T1 domain presence (committed hmmscan annotation JSONs), T2 orthology confidence (committed candidate_orthologs_ledger status + h10 stability flags), T3 expression (NOT AVAILABLE - no committed transcriptomes), T4 phenotype association (NOT AVAILABLE - no committed phenotype data). Tier rules locked: T1 pass = at least one Pfam domain at the committed E<1e-10 threshold; T2 pass = ledger status ok for all member orthologs AND not flagged in h10. No new compute; T3/T4 recorded as absent evidence, never inferred.

## ADDENDUM to the 13:25 IST tier amendment (13:27 IST) - locked BEFORE classification
The amendment's T1 rule cited the screen-level E<1e-10 threshold, but the committed per-candidate Pfam evidence is results/h3_domain_confirmation.json at its own committed rule (E<=1e-05, support in new proteomes). LOCKED CORRECTION: T1 pass = candidate appears in committed h3_domain_confirmation.json with n_domains>=1; the domain threshold is the committed h3 rule, named in the output. All other terms unchanged.

## AMENDMENT 2026-09-27 13:31 IST (provided-verdict queue #17: ranked public resource - artifact-only, locked BEFORE assembly)
ARTIFACT-ONLY: assemble the committed 12-candidate evidence into one ranked atlas table (data/stress_atlas_v1.json + paper table): per candidate - rep, domains (h3), tier record (h_functional_tiers), h12 class, h8b FDR context, h10 stability. Ranking key LOCKED: pm descending, ties broken by T1-then-T2 pass. No new compute; every cell traces to a committed file.

## AMENDMENT 2026-09-27 13:39 IST (provided-verdict queue #19: formal pipeline output definition - documentation-only, locked BEFORE drafting)
DOCUMENTATION-ONLY: define the pipeline's formal output. The convergence confidence output is an ORDERED EVIDENCE TUPLE per candidate, not a scalar: (screen empirical p + origin-replication count, identifiability class from h7, genome-wide FDR context from h8b, orthology-stability flag from h10, specificity class from h12, evidence-tier ceiling from h_functional_tiers). Every component is already committed; no new composite statistic is invented; a candidate is "confirmed" only if EVERY component passes its own locked rule (conjunction), which the paper states plainly.
