# h9: simpler-method baselines (amendment locked 2026-09-27 12:19 IST + 12:21 erratum; #7)

## Arms (12 orthogroups each, from the 52,786-universe)
- B0 RANDOM: 1000 draws (seed 26092707); 3 draws (36 entries) graded.
- B1 SEQUENCE-ONLY: mmseqs2 easy-search (e<=1e-5, cov 0.5) of panel proteomes vs the locked S+ reference (9/10 families; LEA3 dropped per abort rule - no verifiable bdelloid group-3 LEA accession). 17 orthogroups hit; top 12 by e-value.
- B2 DOMAIN-ONLY: panel-wide hmmscan of the locked 64 Pfam HMM set (erratum: prior annotation was candidate-only), per-orthogroup one-sided Fisher, p<0.05 resistant direction, no specificity/origins layers; exactly 12 pass.
- B3 FULL FRAMEWORK: the committed 12.

## Results (arm-blind grading, pool shuffled Random(26092708), locked 10:10 protocol)
| arm | Tier-1 | Tier-2 | Tier-0 | T1or2 |
|-----|--------|--------|--------|-------|
| B0 random (per 12) | 0 | 0 | 12 | 0 |
| B1 sequence-only | 12 | 0 | 0 | 12 |
| B2 domain-only | 1 | 7 | 4 | 8 |
| B3 framework | 1 | 7 | 4 | 8 |

## Statement-rule outcomes (locked)
- B3 vs B1: 8 < 12 -> framework does NOT outperform sequence-only on Tier-1-or-2. Reported verbatim. Structural disclosure (a priori property of the rule): B1 selects BY known-family sequence, so Tier-1 is tautological for it; B1's top-12 contains zero novel candidates (all are the canonical S+ families themselves, including copies in SENSITIVE species - Thermus DdrA, Hypsibius CAHS/SAHS - which the enrichment screen is designed to look past).
- B3 vs B2: 8 = 8 -> tie; the lists are IDENTICAL. On the annotatable universe (913 orthogroups carrying the 64 candidate-relevant Pfam families), domain-only selection returns the same 12: the specificity and origins layers confirmed rather than filtered. Disclosure: the 64-HMM set was assembled for candidate analysis, so B2 does not test a genome-wide domain screen.
- B3 vs B0: 8 > 0 -> framework outperforms random selection.

## Files
results/h9_b1_sequence_only.json, h9_b0_random_meta.json + h9_b0_draws.json, h9_b2_domain_only.json, h9_grading_pool.json, h9_evidence_grading.json, h9_baseline_metrics.json; reference ledger data/splus_reference/splus_ledger.json (sha256 per accession).
