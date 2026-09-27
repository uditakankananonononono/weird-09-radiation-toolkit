# h8b: screen-exact genome-wide permutation FDR (amendment locked 2026-09-27 12:13 IST)

## Provenance
- h8 (raw one-sided hypergeometric Fisher on clusters_v2 presence matrix) ABORTED on its own sanity lock: 3/12 committed hits are not raw-Fisher passers. Root cause: wrong statistic and input vs the H1 screen. Abort record: results/h8_genomewide_fdr.json.
- h8b replicates analysis/formal_tests.py exactly (clusters_sensitive.tsv, 5 resistant / 6 sensitive, hypergeom.sf(pm-1,11,pm+ps,5), seed 11, NPERM=1000) and stores the full 52,786 x 1001 statistic matrix.
- Erratum (12:15 IST, before any output use): sanity lock = exact per-hit reproduction of stored h1_formal_tests.json values (WP_012692142.1 is 17/1001; the other 11 are 13/1001).
- SANITY LOCK PASSED: 12/12 committed hit identities reproduced with exact stored emp_p values.

## Result
- Null pseudo-hit counts over 1000 permuted labelings (same decision rule: empirical p<0.05, resistant direction, >=2/3 origins): mean 22.26, sd 156.5, median 0, min 0, max 2561.
- FDR estimate = 22.26 / 12 = 1.85 (95% normal upper bound 2.66).
- Distribution is bimodal: most permuted labelings yield zero hits, but labelings that preserve genome correlation structure produce large hit sets (up to 2,561).

## Interpretation (honest)
- The 12 committed hits carry the STRONGEST per-orthogroup evidence the screen can produce (11 at the minimum achievable empirical p). The genome-wide estimator, however, cannot separate them from chance: under global label permutation the identical decision rule yields ~22 pseudo-hits on average.
- The estimator is conservative in one specific sense: it scores permuted labelings against a fixed permutation set (amendment item 3), and permutation labelings that partially preserve phylogenetic correlation inflate the null mean; the median null is 0.
- Consequence for the paper: the candidate set stands as a candidate set (mechanistic prioritization and experimental validation are the confirmatory path), but no genome-wide error-rate control is claimed. Results and Caveats state this verbatim.
