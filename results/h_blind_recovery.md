# Blind known-gene recovery (queue #6, amendment 2026-09-27 14:12 IST)
Data: results/h_blind_recovery.json. Observed screen statistic recomputed for all 52,786 orthogroups (kernel identical to committed formal_tests.py, no permutations); 17-entry B1 list collapses to 12 unique S+ orthogroups, all mapped in clusters_sensitive.tsv; family labels held out during ranking.
## Result: 0/12 recovered at the gate - honest negative, with structure
- NONE of the 12 S+ orthogroups passes the screen gate (p<0.05 + resistant-direction + >=2/3 origins); none ranks in the top 100.
- BUT the ranking is not noise: the four Deinococcus-specific repair genes (PprI, DdrB, PprA, Dps1) rank 290/341/373/429 of 52,786 - median 357, the top ~0.7% - while the full S+ median is 14,394.5.
- Why they fail the gate: known stress machinery is SHARED (DdrA's best B1 hit is literally a Thermus - sensitive control - protein; Dsup/CAHS/Dps2 sit at ranks 13,729-19,073 because sensitive species carry homologs). The gate selects resistant-SPECIFIC retention, so universal stress biology is rejected by design.
## Reading
The validation answers queue #6 precisely: blind ranking enriches known stress biology ~75-fold at the top (0.7% vs 52,786-uniform expectation), so the statistic carries real signal; the strict gate then trades known-gene recovery for novelty - a locked design choice, now quantified. Recorded verbatim; no re-tuning.
