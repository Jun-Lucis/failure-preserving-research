# Methodology preprint release checklist

**Target:** first formal Zenodo preprint release  
**Current manuscript:** `paper/manuscript_v0_8.md`

## Scientific / methodological freeze

- [x] Define the three nested cycles.
- [x] Separate discovery data from claim-bearing validation.
- [x] State the non-retroactivity rule.
- [x] Define experimental handoff.
- [x] Complete initial external literature positioning.
- [x] Freeze lineage-coding protocol before full early-history expansion.
- [x] Complete standardized B19-B40 stage-level audit.
- [x] Add separate early B3-B18 audit with nonstandard-verdict labeling.
- [x] Add explicit claim-boundary table.
- [ ] Recover remaining early immutable provenance where practical.
- [ ] Decide whether the main paper reports early cases in the main text or moves some to supplement.
- [ ] Freeze final numerical/statistical summary after sensitivity analysis.

## Quantitative audit

- [x] B19-B40 broad source-stage coding.
- [x] Broad negative/limiting source count: 25.
- [x] Explicit downstream backward-link count: 21.
- [x] Descriptive broad reuse fraction: 84%.
- [x] Preserve caveat that this is not a causal productivity estimate.
- [x] Expanded failure-salvage event ledger.
- [x] Normalize source-to-action edge table.
- [x] Run strict FAIL/NOT_SUPPORTED-only sensitivity analysis — 14/16 = 87.5%.
- [x] Run opportunity-adjusted terminal-stage sensitivity analysis — 22/23 = 95.65%; retained as secondary only.
- [x] Test B-number-level aggregation versus named-stage aggregation — 93.75% any-source / 81.25% all-sources per group.
- [x] Add exploratory temporal-development audit — 76.9% earlier epoch vs 100% later epoch; increase not established (Fisher two-sided p≈0.220).
- [ ] Recheck every source/action link against authoritative public record before release.

## Figures

- [x] Nested-cycle diagram source.
- [x] Failure-salvage spiral source.
- [x] Relational-time pivot diagram source.
- [x] Export publication-ready vector versions — SVG v0.1 for core architecture, salvage spiral, relational pivot, and audit sensitivity.
- [x] Add one quantitative audit figure — `figures/lineage_sensitivity_v0_1.svg`.
- [x] Add one compact BIG lineage example figure — `figures/big_salvage_lineage_v0_1.svg`.
- [ ] Freeze captions and source-data references.

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
- [x] Add figure references in current Markdown manuscript layout; final PDF layout remains pending.
- [ ] Final terminology consistency pass — use audit v0.3 / 88.0% consistently.
- [ ] Final citation verification.
- [ ] Freeze manuscript v1.0.

## Repository and reproducibility

- [x] Separate methodology repository.
- [x] Cross-link from BIG repository.
- [x] Versioned manuscript snapshots.
- [x] Public audit tables.
- [x] Public coding protocol.
- [x] Public case-study notes.
- [ ] Decide LICENSE.
- [ ] Tag the exact Git release used for Zenodo.
- [ ] Create SHA-256 manifest for release files.
- [ ] Create compact release archive if useful.

## Zenodo

- [x] Metadata draft.
- [ ] Decide final title/subtitle.
- [ ] Decide license.
- [ ] Create reserved DOI only after manuscript v1.0 is frozen.
- [ ] Upload manuscript, audit supplement, tables, and release manifest.
- [ ] Add methodology GitHub and BIG GitHub as related resources.
- [ ] Publish.
- [ ] Insert DOI into `CITATION.cff`.
- [ ] Insert DOI into methodology README.
- [ ] Insert DOI into BIG methodology bridge.
