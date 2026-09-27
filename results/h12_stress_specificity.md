# Queue #10: radiation-specific vs general-stress classification (h12) - REPORT ONLY

Amendment 2026-09-27 12:38 IST. Delegated-executor computation at ref c72b429, uncommitted.

## Headline
All 12 committed candidates classify **CONTROL-DEPENDENT**: every candidate fails the gate under S-A (and identically under S-B), with empirical p = 0.0749-0.0809 vs the 0.05 threshold.

## Why (design observation, descriptive)
All 12 hits have zero sensitive-species copies under both compositions (sen_copies = 0 everywhere), so S-A and S-B give identical statistics. At N = 8 genomes with ps = 0, the Fisher label-permutation minimum attainable empirical p is C(5,pm)/C(8,pm): 0.0714 for pm = 4, 0.1786 for pm = 3; only pm = 5 (copies in all five resistant species) can reach 0.0179 < 0.05. None of the 12 has pm = 5. Under the committed N = 11 panel the same pm = 4 profile yields 0.0152, which is how these candidates passed H1. The 8-genome compositions therefore make the locked gate unreachable for every committed candidate - the CONTROL-DEPENDENT sweep is a power property of the reduced compositions, not new biological evidence of control dependence.

## Numbers (verbatim, locked kernel)
Kernel mirrored from analysis/formal_tests.py: hypergeom.sf(pm-1, N, pm+ps, 5), (cnt+1)/1001, 1000 label permutations per composition, seed 260927, ORIGIN_IDX [(0,1,2),(3,),(4,)], gate = emp_p<0.05 + resistant direction (pm>ps) + >=2/3 origins. Per-candidate emp_p, pm/ps, origins and pass flags: results/h12_stress_specificity.json.

## Locked framing
Report-only: classes are descriptive labels, not gate changes; no new hits, no removals.
