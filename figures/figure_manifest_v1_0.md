# Figure manifest and frozen captions — v1.0

**Date:** 6 October 2026  
**Target:** methodology preprint release candidate

This file freezes the figure identities, captions, and source-data references for the first formal preprint package. Any substantive figure change after this point should increment the figure version and the manuscript release candidate.

## Main-text figures

### Figure 1 — Nested architecture

**File:** `figures/nested_cycles_v0_1.svg`  
**Source:** `figures/nested_cycles.md`

**Frozen caption**

> **Figure 1. Nested architecture of failure-preserving AI-assisted research.** At the micro scale, AI-assisted reasoning is repeatedly exposed to externally executed numerical computation. At the meso scale, hypotheses are prospectively frozen and assigned persistent verdicts before redesign. At the macro scale, the retained archive becomes a research-memory state from which earlier negative or limiting outcomes can be retrieved as discovery data. Experimental handoff marks the boundary at which decisive evidence requires new physical measurements.

**Source-data status:** conceptual diagram; no numerical source table.

---

### Figure 2 — Failure-salvage spiral

**File:** `figures/failure_salvage_spiral_v0_1.svg`  
**Source:** `figures/failure_salvage_spiral.md`

**Frozen caption**

> **Figure 2. Failure-salvage spiral.** Historical failures are not reclassified as successes. They remain fixed outcomes while retained data and diagnostics may later influence a new hypothesis. If old data participate in redesign, they are discovery data; claim-bearing support for the replacement hypothesis requires a separately identified fresh or held-out evaluation.

**Source-data status:** conceptual diagram; no numerical source table.

---

### Figure 3 — Lineage-audit sensitivity

**File:** `figures/lineage_sensitivity_v0_1.svg`  
**Source:** `figures/lineage_sensitivity.md`

**Frozen caption**

> **Figure 3. Lineage-audit sensitivity.** The broad named-stage 88.0% value is the primary descriptive statistic. The strict, B-family, and opportunity-adjusted bars use different denominators and are shown only to assess sensitivity of the qualitative conclusion; they are not interchangeable estimands or estimates of a universal failure-reuse rate.

**Source data**

- `docs/quantitative_lineage_audit_v0_3.md`
- `evidence/stage_lineage_B19_B40_v0_3.csv`

**Frozen values**

```text
broad named-stage:            22 / 25 = 88.0%
strict FAIL/NOT_SUPPORTED:    14 / 16 = 87.5%
B-family all-sources reused:  13 / 16 = 81.25%
opportunity-adjusted broad:   22 / 23 = 95.65%
```

---

### Figure 4 — Selected BIG failure-salvage lineages

**File:** `figures/big_salvage_lineage_v0_1.svg`  
**Source:** `figures/big_salvage_lineage.md`

**Frozen caption**

> **Figure 4. Selected audited BIG failure-salvage lineages.** Arrows indicate downstream influence or succession, not retrospective upgrading of the parent verdict. The examples show multiple roles for retained negative or limiting outcomes: external transfer, predictor redesign, state enrichment, explanatory-variable change, representational salvage, protocol repair, and limit localization.

**Source data / audit tables**

- `evidence/stage_lineage_B19_B40_v0_3.csv`
- `evidence/failure_salvage_ledger_v0_3.csv`
- `evidence/source_action_edges_v0_3.csv`
- `case_studies/BIG/failure_salvage_audit_v0_3.md`
- `docs/source_action_authority_recheck_v1_0.md`

---

### Figure 5 — Relational-time pivot

**File:** `figures/relational_time_pivot_v0_1.svg`  
**Source:** `figures/relational_time_pivot.md`

**Frozen caption**

> **Figure 5. Representational salvage in the later BIG timing programme.** Repeated negative or fragile absolute-timing results were retained rather than erased. Their diagnostics contributed to a change of observable toward relative and relational timing. The old results served as discovery material, while later relational claims were evaluated in newly frozen prospective tests.

**Source records**

- `docs/research_status_update_B27_B36.md` in the BIG repository
- `docs/research_status_update_B37_B38.md` in the BIG repository
- `docs/research_status_update_B39.md` in the BIG repository
- `docs/research_status_update_B40.md` in the BIG repository

---

## Supplementary figure

### Supplementary Figure S1 — Failure-reuse latency

**File:** `figures/reuse_latency_v0_1.svg`  
**Source:** `figures/reuse_latency.md`

**Frozen caption**

> **Supplementary Figure S1. Observed source-to-successor freeze latency.** Fourteen source-to-successor transitions for which retained artifact timestamps permit a reasonably comparable interval from a source result/final status to a separately frozen successor protocol or programme architecture. The median interval is 1.20 h (IQR 0.49-2.03 h). No monotonic shortening is detected across the observed dates (Spearman rho=0.051, p=0.864). These intervals are provenance timestamps, not direct measurements of human or AI reasoning time.

**Source data**

- `evidence/failure_reuse_latency_v0_1.csv`
- `docs/temporal_lineage_audit_v0_2.md`

**Privacy rule:** private Drive URLs and file IDs are not included in the public figure source.

## Freeze status

```text
FIGURE_IDENTITIES_FROZEN = yes
MAIN_CAPTIONS_FROZEN     = yes
SOURCE_DATA_LINKS_FROZEN = yes
SUPPLEMENT_CAPTION_FROZEN= yes
```

Typography, line wrapping, and final placement may still change during PDF production without changing the scientific content of the figures.
