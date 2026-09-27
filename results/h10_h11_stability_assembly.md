# h10/h11: orthology stability + assembly-bias control (#9, #8; amendments locked 12:29 IST)

## #9 Orthogroup-calling uncertainty (h10)
Rule (locked): >=80% of resistant-arm members co-cluster in the alternative clustering.
- vs clusters_v2 (13-species mmseqs v2): 11/12 stable. UJR10666.1 splits - FLAGGED in Results+Caveats, not removed (locked rule).
- vs clusters_linclust30: 3/12 co-cluster, consistent with linclust's DOCUMENTED fragmentation (subset20k concordance: purity 0.914, retention 0.363; PRE-REG line 73: formal claims never rest on linclust counts). Low linclust co-clustering reads as a property of the clustering, not of the hits.

## #8 Copy-number/assembly-bias control (h11)
- Spearman rho(proteome size, hit-presence count) = -0.095 (p=0.781): no assembly-size gradient in hit presence.
- Arm sizes: resistant median 3,479 vs sensitive median 12,974 proteins; MWU p=0.931 (small-n, disclosed): no significant arm imbalance.
- Check (c) (>=3 of 5 resistant genomes within 2x panel-median size, per hit): 0/12 fail.
- Verbatim verdict: the committed 12 are not explained by assembly quality differences.
