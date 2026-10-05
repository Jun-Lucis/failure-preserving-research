# Source/action authority recheck — v1.0

**Date:** 6 October 2026  
**Purpose:** final pre-release recheck of the public/archival support behind the normalized source-to-action lineage table.

## Scope

The primary objects rechecked are:

- `evidence/stage_lineage_B19_B40_v0_3.csv`
- `evidence/failure_salvage_ledger_v0_3.csv`
- `evidence/source_action_edges_v0_3.csv`
- `evidence/early_provenance_manifest_v0_2.csv`

The rule is conservative:

> An edge may remain claim-bearing only when the source verdict/limitation and the successor action are traceable to an authoritative public BIG status record or to a retained archival artifact whose provenance is explicitly labeled.

## Standardized B19-B40 public records

The following public BIG records were re-opened and checked on 6 October 2026. All links were live.

| Public record | Main content rechecked |
| --- | --- |
| `docs/research_status_map_B3_B26.md` | B19 negative scalar-collapse conclusion and early integrated status map |
| `papers/B19E_external_flow_validation/README.md` | A1 `NULL_OR_INCONCLUSIVE`; Stage-B `BUDGET_CLOSURE_PASS`; explicit no-rescue relation |
| `papers/B20_response_boundaries/README.md` | B20.6 retained `INCONCLUSIVE` verdict |
| `papers/B23_cross_branch_geometric_prediction/README.md` | original aggregate `INCONCLUSIVE`; E3R implementation-invalid history; E3R2 corrective replication |
| `papers/B23A_structural_universality_limits/README.md` | P1-P6 retained verdict map and explicit non-reclassification |
| `docs/research_status_update_B24_B25.md` | B24.2 `MULTIPLE_BOUNDARY_CLASSES_INDICATED` and question reformulation |
| `papers/B24_B25_predictive_boundary_functional_transfer/README.md` | B25.1 FAIL -> B25.1R diagnostic -> B25.1b fresh held-out PASS; B25.2 INVALID |
| `docs/research_status_update_B25_phaseII.md` | B25.1c-e PASS sequence and B25.2 `IMPLEMENTATION_INVALID` |
| `docs/research_status_update_B26.md` | topology-span failure, B26.1 bracket localization, B26.2 valid prospective FAIL |
| `docs/research_status_update_B27_B36.md` | B27-B36 retained FAIL/PASS/readiness lineages, including B29-T1 -> B30 backward link |
| `docs/research_status_update_B37_B38.md` | B37 absolute-timing FAILs -> B38 fresh relative-lag programme |
| `docs/research_status_update_B39.md` | P1 FAIL -> diagnostic/calibration -> newly frozen P2 PASS, with P1 retained |
| `docs/research_status_update_B40.md` | B40.1/B40.2 parent FAILs and successor localization/replication results |

No standardized B19-B40 source/action edge was found to require deletion or verdict reversal.

## Edge-level disposition

### E001-E018 — standardized failure/limitation lineages

**Disposition: KEEP.**

These edges are supported by the public records listed above. The recheck confirms the manuscript's central non-retroactivity distinction:

- retrospective diagnosis/calibration is not counted as a parent rescue;
- a successor PASS is separately named;
- fresh/held-out evaluation is used where the source record states that distinction;
- INVALID and INCONCLUSIVE parent states remain historically unchanged.

### E019 / FS16 — B6 computational reuse

**Disposition: KEEP as retrospective computational reuse.**

Owner-side archival provenance was recovered for:

```text
B6_3_summary_all.csv
B6_4_input_B6_3_summary.csv
B6_4_crossing_summary.csv
```

The explicit B6.4 input filename and file chronology support the statement that the dense B6.3 scan was reused for a later crossing-only analysis rather than rerun as a new claim-bearing PDE experiment.

This remains retrospective and is not presented as fresh validation.

### E020 / FS17 — early elliptic-boundary measurement redesign candidate

**Disposition: SUPPLEMENT ONLY / PARTIAL PROVENANCE.**

The earlier exact numerical pair

```text
nu ~ 2.63 -> 2.024 +/- 0.014
```

was not recovered from an immutable source. The v0.3 edge table therefore no longer treats it as a verified source-action edge.

Recovered same-day artifacts do establish an elliptic-boundary analysis sequence:

```text
B5_3
-> B5_3A local-exponent profile
-> B5_7 free-boundary normal-fit programme
```

but the differing parameter sets prevent a clean controlled before/after numerical claim.

This case is omitted from the main manuscript and retained only as an early measurement-redesign candidate.

### E021 / FS18 — B12 mechanism redesign

**Disposition: KEEP.**

The B12 public record explicitly states that B12.1c still allowed deterministic low-noise lock and that B12.1d introduced an ignition barrier. The resulting finite-noise R-lock window is reported under the redesigned model.

### E022-E023 / FS19 — B13/B13.1 interpretation correction

**Disposition: KEEP.**

The B13.1 public record and retained fit artifacts support the narrowing from a direct cos-squared-like interpretation to a logistic basin-boundary kernel plus finite-width cloud averaging.

### E024 / FS20 — B17->B18 readout enrichment

**Disposition: KEEP.**

The B18 public record explicitly describes the read-start local-load result as a useful negative result and reports the successive improvement under path and interface-core exposure. The source-to-redesign relation is direct in the manuscript.

### E025 / FS21 — B9 empirical claim-boundary retention

**Disposition: KEEP.**

The public B9 Empirical Phase II record explicitly retains mixed/negative/unresolved results:

- mixed external barrier-magnitude check;
- failed near-spinodal exponent tests;
- unresolved nonlocal quartic coefficient;
- no quantitative lambda-to-MeV calibration.

The successor synthesis deliberately retains only a structural metastability conclusion. This is claim-boundary retention, not a rescued quantitative PASS.

Public record:

https://github.com/Jun-Lucis/BIG-theory/blob/main/papers/B9_fission_like_metastability/empirical_phase_II.md

### E026-E029 / FS22-FS23 — B34/B35 preclaim gating

**Disposition: KEEP.**

The integrated B27-B36 status record supports the distinction between non-claim-bearing readiness failures and later fresh claim-bearing stages. In particular, B35.1 subsequently returned a scientific FAIL after calibration/readiness had passed, arguing against a simple tune-until-PASS interpretation.

## Cross-table consistency

After the E020 downgrade:

```text
standardized B19-B40 primary statistic: 22 / 25 = 88.0%
early main-text cases:                 4
early supplement-only partial case:    1
```

The E020 downgrade does not change the 22/25 standardized statistic because the early B3-B18 cases are analytically separate from that denominator.

## Release decision

```text
STANDARDIZED_SOURCE_ACTION_RECHECK = PASS
EARLY_MAIN_TEXT_SOURCE_RECHECK      = PASS
E020_EARLY_MEASUREMENT_CASE         = PARTIAL_PROVENANCE / SUPPLEMENT_ONLY
PARENT_VERDICT_NON_RETROACTIVITY    = PRESERVED
```

No additional source/action correction is required before manuscript v1.0 freeze, subject to normal final copyediting.
