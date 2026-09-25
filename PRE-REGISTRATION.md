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
