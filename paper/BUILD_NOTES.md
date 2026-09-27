# Manuscript build note

- Build: `cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice. A4, 12-point.
- Source base: `99295384480b47c129732abb51dbf6d141fb6716`. Working branch `paper-build` is not merged into main.
- Font: `mathptmx` is Times-compatible, not genuine licensed Times New Roman, which is absent here.
- Implementation audit: main includes the corrected 5-versus-6 H1 rerun, archived buggy outputs, and a dated correction amendment. The paper's Caveats retains the audit, and the appendix expands it.
- Current compiled PDF: 21 pages. This draft is incomplete and does not reach the 50-page submission floor. The cross-clade phylogenetic inference remains negative.

- H3 architecture table transcribes committed `results/h3_domain_confirmation.json`; it includes 11 domain-tested representatives, of which HPPK fails the v2 enrichment gate and amidase fails H3.

- Rebuilt from science main 9929538 on September 27; the main-branch manuscript is authoritative and the appendix does not reverse later negative gates.
- H5 strict family-level rubric v1 failed despite general mechanism support for the top rank; the new H5 appendix uses the committed strict verdict.

- H6 background rarity passes its arithmetic test, but zero actual candidates reach the complete tier. The proposed reframe is not earned; H4 identifiability remains terminal.

- Per-candidate H4/H4b/H4c ledger transcribes committed result JSONs, labels superseded tail and domain-level extension; phylogenetic inference remains negative.

- No author byline or PDF Author metadata is present in this manuscript.
