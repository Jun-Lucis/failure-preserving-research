# BIG as a longitudinal case study

Boundary Information Geometry (BIG) is used in this repository as a longitudinal case study of AI-assisted individual computational research.

Primary research repository:

https://github.com/Jun-Lucis/BIG-theory

The methodological analysis here is intentionally separate from the scientific validity of BIG. A research process can be documented and audited even if some scientific claims later fail, narrow, or change interpretation.

## Why BIG is useful as a process case study

The B-series contains many retained outcomes of different kinds:

- PASS
- FAIL
- INCONCLUSIVE
- IMPLEMENTATION_INVALID / protocol-invalid outcomes
- retrospective diagnostics
- prospective replacement tests
- later localization of earlier failures

This makes the programme unusually suitable for studying what happens when failures are retained instead of removed from the narrative.

## Representative salvage chains

### B25: failed reduction -> archived-profile diagnosis -> fresh replacement PASS

```text
B25.1
AB_CONSTANT_DENSITY_FAIL
  -> B25.1R retrospective coarea decomposition
  -> replacement relation frozen
  -> B25.1b
AB_LEVEL_RESOLVED_BRIDGE_PASS
```

The B25.1 FAIL remained unchanged. Archived profiles were used only for diagnosis/model construction. The replacement relation was then evaluated on nine new held-out shape/resolution cases.

Source:
https://github.com/Jun-Lucis/BIG-theory/tree/main/papers/B24_B25_predictive_boundary_functional_transfer

### B27-B29: increasingly rich state descriptions

```text
B27.2 RECONFIGURATION_COVARIANCE_FAIL
  -> B28 geometry-only transport hypothesis
  -> B28.1 GEOMETRY_CONDITIONED_LINEAGE_TRANSPORT_FAIL
  -> B29 asks whether retained history/path adds predictive information
  -> training-domain readability boundary closes held-out test
```

This chain did not end in a PASS. Its methodological value is different: each failure constrained what a viable state description would need to contain.

Source:
https://github.com/Jun-Lucis/BIG-theory/blob/main/docs/research_status_update_B27_B36.md

### B32-B33: failed dynamic suppression -> node-lifting description

```text
B32.1 DYNAMIC_COMPLEX_PARITY_MODE_FAIL
  -> response pattern retained
  -> B33 reframes the question
  -> FREQUENCY_DEPENDENT_TRANSVERSE_NODE_LIFTING_PASS
  -> PERIOD_DEPENDENT_TRANSVERSE_NODE_LIFTING_PASS
```

This is an example of changing the explanatory variable instead of repeatedly weakening one failed qualitative claim.

### B35-B36: failed common timing law -> additive decomposition

```text
B35.1 / B35.2 linear timing FAILs
  -> B36.1 geometry-conditioned ordering FAIL
  -> B36.2 additive geometry/readout decomposition
  -> ADDITIVE_GEOMETRY_SAMPLING_DECOMPOSITION_PASS
```

The surviving statement is weaker and more structured than the failed universal timing claim.

### B37-B38: change of observable

```text
B37.1 intrinsic contour reparameterization FAIL
B37.2 fixed-arc-support timing collapse FAIL
  -> diagnostics expose grid-phase sensitivity of absolute peak timing
  -> relative lag becomes the new prospective observable
  -> B38.1 RELATIVE_BOUNDARY_LAG_GEOMETRY_PASS
  -> B38 develops relational source/receiver/readout structure
```

This sequence is treated as a key example of representational salvage.

Source:
https://github.com/Jun-Lucis/BIG-theory/blob/main/docs/research_status_update_B37_B38.md

### B39: parent FAIL retained while a fresh protocol succeeds

```text
B39.3-P1
INTEGRATION_LEVEL_REPARAMETERIZATION_COVARIANCE_FAIL
  -> P1A failure localization
  -> P1B response-independent clock-map calibration
  -> new P2 protocol frozen before fresh trajectories
  -> B39.3-P2
INTRINSIC_CLOCK_MAP_INTEGRATION_COVARIANCE_PASS
```

The P2 PASS does not regrade P1.

Source:
https://github.com/Jun-Lucis/BIG-theory/blob/main/docs/research_status_update_B39.md

### B40: failure localization rather than rescue

B40 retains both:

- `CLOCK_MAP_FAMILY_TRANSFER_FAIL`
- `TARGET_EXCLUDED_RELATIONAL_RECONSTRUCTION_FAIL`

Successor tests localize those failures and identify narrower finite-grid structures, including lag-grid quantization localization and an orientation-reversing covariance of reconstruction success/failure.

Source:
https://github.com/Jun-Lucis/BIG-theory/blob/main/docs/research_status_update_B40.md

## Case-study rule

A later interpretation never changes the historical verdict.

The case study distinguishes:

```text
historical verdict
!=
later scientific usefulness
```

A failed result can later be useful for diagnosis, model construction, or limiting a claim while remaining a failed test of its original hypothesis.
