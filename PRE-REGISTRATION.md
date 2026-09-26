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
