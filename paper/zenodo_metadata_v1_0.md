# Zenodo metadata — v1.0

## DOI

10.5281/zenodo.23171698

https://doi.org/10.5281/zenodo.23171698

## Title

Failure-Preserving AI-Assisted Research: A Nested Research Architecture for Individual Computational Science

## Subtitle / description line

A Longitudinal Case Study from Boundary Information Geometry

## Creator

**Name:** Jun Lucis  
**Affiliation:** Independent researcher

## Publication date

2026-10-06

## Resource type

Publication -> Preprint

## Version

1.0

## Publication status

Published on Zenodo

## Language

English

A Japanese reference translation is included as a companion file in the same release package.

## Access right

Open Access

## License

**Confirmed:** Creative Commons Attribution 4.0 International (CC BY 4.0)

Executable helper code under `tools/` is licensed separately under the MIT License; the scholarly release remains CC BY 4.0.

## Author context note

The author conducts this work as an independent researcher outside the scope of his primary employment. His primary professional role is non-technical and unrelated to the research described here. The research used only personally controlled computing resources and accounts together with publicly available data; no employer-controlled computing resources, proprietary data, confidential information, or employer-provided research facilities were used. Human research activity was performed primarily during personal time, while some long-running computations continued unattended during periods when the author was sleeping or otherwise away from active research.

## Description

This methodological paper proposes a failure-preserving architecture for AI-assisted individual computational research. The framework distinguishes three nested cycles: (1) a micro cycle alternating AI-assisted reasoning with externally executed numerical computation; (2) a meso cycle of predeclaration, frozen testing, retained PASS/FAIL/INCONCLUSIVE/INVALID verdicts, and separately named redesign; and (3) a macro cycle in which archived failures and diagnostics become a research-memory state that can later support constraint reuse, model redesign, or representational change. A fourth component, experimental handoff, marks the point at which public data and simulation are insufficient and new physical measurements require laboratories, organizations, equipment, calibration, and domain expertise.

Boundary Information Geometry (BIG) is used as a longitudinal case study of the process rather than as a premise of the methodology. In the standardized B19-B40 lineage audit v0.3, 25 negative or limiting source stages were identified and 22 had an explicit downstream backward link, giving a descriptive fraction of 88.0%. A stricter FAIL/NOT_SUPPORTED-style sensitivity gives 14/16 = 87.5%. These values are descriptive properties of the coded BIG interval and are not presented as universal estimates of the value of scientific failure.

The archive also permits an exploratory temporal audit. Explicit backward linkage is observed in 10/13 source stages in the B19-B26 epoch and 12/12 in B27-B40, but the difference is not statistically persuasive and later documentation is more complete. Fourteen retained-artifact source-to-successor transitions have a median result-to-successor-freeze interval of about 1.20 hours (IQR 0.49-2.03 h), with no evidence of monotonic shortening over time (Spearman rho approximately 0.051, p approximately 0.864).

Documented examples include a failed boundary-functional reduction whose archived profiles motivated a replacement predictor later tested on fresh held-out cases; protocol and readiness failures that blocked claim-bearing experiments until redesigned criteria were met; interpretation correction in earlier reduced observation models; and a later shift from fragile absolute timing observables toward relative and relational timing followed by newly frozen prospective tests.

The paper does not claim that AI eliminates scientific error, that every failure has future value, that failure preservation itself is a novel concept, or that computational research replaces experimental validation. Closely related 2026 AI-research systems already preserve persistent research memory, failed trials, exploration graphs, or trial-to-behavior relations. The narrower contribution is an auditable, human-led longitudinal implementation combining non-retroactive verdict preservation, separation of retrospective discovery from fresh claim-bearing evaluation, nested micro/meso/macro research cycles, quantitative lineage and latency audits, and an explicit experimental-handoff boundary.

The release includes the frozen English v1.0 manuscript, a Japanese reference translation, vector figures, coding protocols, audit tables, lineage ledgers, provenance notes, reference verification, and source/action authority checks.

## Keywords

- AI-assisted research
- computational science
- individual research
- human-AI collaboration
- negative results
- failure preservation
- failure salvage
- research memory
- prospective testing
- preregistration
- research provenance
- scientific workflow
- reproducible research
- experimental handoff
- research methodology
- Boundary Information Geometry

## Related identifiers

### Methodology repository

https://github.com/Jun-Lucis/failure-preserving-research

Suggested relation: **Is supplemented by / Software / URL** (depending on the Zenodo relation selector available in the deposit form).

### Primary case-study repository

https://github.com/Jun-Lucis/BIG-theory

Suggested relation: **References / URL**.

## Files intended for the Zenodo v1.0 package

Primary manuscripts:

- `Failure_Preserving_AI_Assisted_Research_v1_0.pdf`
- `Failure_Preserving_AI_Assisted_Research_Japanese_Reference_v1_0.pdf`
- `paper/manuscript_v1_0.md`
- `paper/manuscript_v1_0_Japanese_reference.md`

Core audit / reproducibility materials:

- `protocols/lineage_coding_protocol_v0_1.md`
- `docs/quantitative_lineage_audit_v0_3.md`
- `docs/temporal_lineage_audit_v0_2.md`
- `docs/early_lineage_audit_B3_B18_v0_2.md`
- `docs/claim_boundary_table_v0_3.md`
- `docs/reference_verification_v0_1.md`
- `docs/source_action_authority_recheck_v1_0.md`
- `evidence/stage_lineage_B19_B40_v0_3.csv`
- `evidence/failure_salvage_ledger_v0_3.csv`
- `evidence/source_action_edges_v0_3.csv`
- `evidence/failure_reuse_latency_v0_1.csv`
- `evidence/early_verified_lineage_candidates_v0_2.csv`
- `evidence/early_provenance_manifest_v0_2.csv`
- `case_studies/BIG/failure_salvage_audit_v0_3.md`
- `case_studies/BIG/B34_B35_calibration_gating.md`
- `figures/figure_manifest_v1_0.md`
- vector SVG figures
- SHA-256 release manifest

## Notes for the Zenodo form

- Keep BIG as a **case study**, not as a validated premise of the methodology.
- Keep 88.0% explicitly labeled as a **descriptive statistic of the standardized B19-B40 coded interval**.
- Do not claim a statistically established temporal increase in failure reuse.
- Do not claim shortening of reuse latency.
- Do not claim invention of persistent research memory or failure preservation.
- State that the Japanese manuscript is a **reference translation**, with the English manuscript controlling in case of discrepancy.
