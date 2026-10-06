# Methodology preprint release checklist

**Target:** first formal Zenodo preprint release  
**Current manuscript:** `paper/manuscript_v1_0.md`

## Scientific / methodological freeze

- [x] Define the three nested cycles.
- [x] Separate discovery data from claim-bearing validation.
- [x] State the non-retroactivity rule.
- [x] Define experimental handoff.
- [x] Complete initial external literature positioning.
- [x] Freeze lineage-coding protocol before full early-history expansion.
- [x] Complete standardized B19-B40 stage-level audit.
- [x] Add separate early B3-B18 audit with nonstandard-verdict labeling; provenance-corrected v0.2 now current.
- [x] Add explicit claim-boundary table.
- [x] Recover practical early provenance: exact B6 source/reuse artifacts and timestamps recovered; E02 downgraded when exact numerical source could not be traced.
- [x] Main-text policy fixed: E01/E03/E04/E05 retained; partial-provenance E02 moved to supplement.
- [x] Freeze current numerical/statistical summary after sensitivity analysis; any later changes require a new audit version.

## Quantitative audit

- [x] B19-B40 broad source-stage coding.
- [x] Broad negative/limiting source count: 25.
- [x] Explicit downstream backward-link count: 22 (audit v0.3; v0.2 preserved 21).
- [x] Descriptive broad reuse fraction: 88.0% (audit v0.3; v0.2 preserved 84%).
- [x] Preserve caveat that this is not a causal productivity estimate.
- [x] Expanded failure-salvage event ledger.
- [x] Normalize source-to-action edge table.
- [x] Provenance-corrected failure-salvage ledger and source-action edge tables to v0.3 after E02/FS17 downgrade.
- [x] Run strict FAIL/NOT_SUPPORTED-only sensitivity analysis — 14/16 = 87.5%.
- [x] Run opportunity-adjusted terminal-stage sensitivity analysis — 22/23 = 95.65%; retained as secondary only.
- [x] Test B-number-level aggregation versus named-stage aggregation — 93.75% any-source / 81.25% all-sources per group.
- [x] Add exploratory temporal-development audit — 76.9% earlier epoch vs 100% later epoch; increase not established (Fisher two-sided p≈0.220).
- [x] Recover exact retained-artifact timestamps for a comparable 14-transition latency subset.
- [x] Test reuse-latency trend — median 1.20 h, IQR 0.49-2.03 h; no monotonic shortening (Spearman rho≈0.051, p≈0.864).
- [x] Preserve privacy boundary — publish artifact names/timestamps/provenance class, not private Drive URLs or IDs.
- [x] Recheck source/action links against authoritative public/archival records; see `docs/source_action_authority_recheck_v1_0.md`.

## Figures

- [x] Nested-cycle diagram source.
- [x] Failure-salvage spiral source.
- [x] Relational-time pivot diagram source.
- [x] Export publication-ready vector versions — SVG v0.1 for core architecture, salvage spiral, relational pivot, and audit sensitivity.
- [x] Add one quantitative audit figure — `figures/lineage_sensitivity_v0_1.svg`.
- [x] Add one compact BIG lineage example figure — `figures/big_salvage_lineage_v0_1.svg`.
- [x] Add supplementary reuse-latency audit figure — `figures/reuse_latency_v0_1.svg`.
- [x] Freeze captions and source-data references; see `figures/figure_manifest_v1_0.md`.

## Manuscript

- [x] Introduction and core claim.
- [x] Prior-work positioning.
- [x] Three-scale architecture.
- [x] Preliminary quantitative lineage audit.
- [x] Early pre-standardization examples.
- [x] B19/B19E non-rescue example.
- [x] B23/B23A protocol repair and terminal narrowing.
- [x] B25 predictor redesign.
- [x] B27-B29 state enrichment.
- [x] B32-B36 failure/decomposition examples.
- [x] B37-B40 relational-time pivot.
- [x] Preclaim gating section.
- [x] Experimental-handoff boundary.
- [x] Claim limitations.
- [x] Add figure references in Markdown and build final English/Japanese v1.0 PDFs.
- [x] Terminology/claim-boundary consistency pass updated through manuscript v0.12; recheck once more at v1.0 freeze.
- [x] External citation verification completed in `docs/reference_verification_v0_1.md`; corrected Henderson & Chambers attribution and narrowed adjacent-work novelty claim.
- [x] Create manuscript v1.0 release candidate 1.
- [x] Create manuscript v1.0 release candidate 2 after final provenance copyedit.
- [x] Create Japanese reference translation aligned to v1.0 RC2.
- [x] Freeze English manuscript v1.0 and aligned Japanese reference translation. License decision remains a repository/release metadata item.

## Post-publication clarification

- [x] Concise author-independence clarification added to the English v1.0 manuscript and Japanese reference translation.
- [x] Clarification states that the work is outside the scope of primary employment, uses personally controlled computing resources and public data, and does not use employer-controlled resources, proprietary data, confidential information, employer-provided research infrastructure, or employer research funding.
- [x] Clarification avoids wording about primary-employment hours; unattended computation is described only as occurring during sleep or other periods away from active research.
- [x] Scientific claims, numerical results, verdicts, and audit statistics are unchanged.
- [x] Replacement PDFs rebuilt successfully through the reproducible PDF workflow after shortening the author note.

## PDF production

- [x] Reproducible GitHub Actions PDF workflow completed successfully.
- [x] English v1.0 PDF: 28 A4 pages after the post-publication author-note clarification.
- [x] Japanese reference v1.0 PDF: 28 A4 pages after the post-publication author-note clarification.
- [x] Visual QA of both PDFs completed from rendered page images; no clipping, broken glyphs, or figure overflow observed.

## Repository and reproducibility

- [x] Separate methodology repository.
- [x] Cross-link from BIG repository.
- [x] Versioned manuscript snapshots.
- [x] Public audit tables.
- [x] Public coding protocol.
- [x] Public case-study notes.
- [x] License confirmed: CC BY 4.0 for scholarly content; MIT for executable tools.
- [ ] Tag the exact Git release used for Zenodo.
- [x] Release-package builder prepared (`tools/build_release_package.py`).
- [x] Create SHA-256 manifest for the English/Japanese PDF pair; full audit-package manifest remains for tagged release.
- [x] Create compact PDF archive for delivery; full audit-package archive remains for tagged release.

## Zenodo

- [x] Zenodo publication reported complete by the author on 6 October 2026.

- [x] Metadata draft.
- [x] Zenodo-ready metadata v1.0 prepared in `paper/zenodo_metadata_v1_0.md`.
- [x] Final v1.0 title/subtitle: *Failure-Preserving AI-Assisted Research: A Nested Research Architecture for Individual Computational Science* / *A Longitudinal Case Study from Boundary Information Geometry*.
- [x] Zenodo license confirmed: CC BY 4.0.
- [x] Zenodo DOI assigned: `10.5281/zenodo.23171698`.
- [ ] Verify the published Zenodo file inventory includes the intended frozen English/Japanese PDFs and supplementary audit materials.
- [ ] Verify the published Zenodo metadata lists the methodology GitHub and BIG GitHub as related resources.
- [x] Publish on Zenodo under DOI `10.5281/zenodo.23171698`.
- [x] Insert DOI into `CITATION.cff`.
- [x] Insert DOI into methodology README.
- [x] Insert DOI into BIG methodology bridge.
