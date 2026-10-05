# Failure-salvage map

This page summarizes the current auditable salvage chains selected from the BIG programme.

The map is intentionally conservative: only chains with a clear retained parent outcome and a documented later use are included.

## Map

```text
B25.1 FAIL
  |
  +-- archived profiles
  |      |
  |      v
  |   B25.1R retrospective obstruction analysis
  |      |
  |      v
  +--> B25.1b fresh held-out PASS

B27.2 FAIL
  |
  v
B28 geometry-only redesign
  |
  v
B28.1 FAIL
  |
  v
B29 richer-information question
  |
  v
training readability boundary / no held-out verdict

B32.1 FAIL
  |
  v
reframe dynamic suppression
  |
  v
B33 frequency/period-dependent node lifting PASS

B35.1 FAIL
B35.2 FAIL
  |
  v
B36.1 FAIL
  |
  v
decompose geometry and sampling
  |
  v
B36.2 PASS

B37.1 FAIL
B37.2 FAIL
  |
  +-- phase-sensitivity diagnostics
  +-- waveform alignment analysis
  |
  v
change observable: absolute peak time -> relative lag
  |
  v
B38.1 PASS
  |
  v
B38.2-B38.6 relational/operator/readout tests

B39.3-P1 FAIL
  |
  +-- P1A localization
  +-- P1B response-independent clock calibration
  |
  v
fresh P2 freeze
  |
  v
B39.3-P2 PASS

B40.1 FAIL
  |
  v
fine-grid lag localization PASS
(parent FAIL retained)

B40.2 FAIL
  |
  v
P1B-P1F localization / transformation tests
  |
  v
restricted covariance PASSes
(parent FAIL retained)
```

## Salvage classes represented

| Chain | Primary salvage type |
| --- | --- |
| B25 | MODEL_REDESIGN |
| B27-B29 | CONSTRAINT_REUSE / STATE_ENRICHMENT |
| B32-B33 | EXPLANATORY_VARIABLE_CHANGE |
| B35-B36 | DECOMPOSITION |
| B37-B38 | REPRESENTATIONAL_SALVAGE |
| B39 | PROTOCOL_REPAIR + FRESH_RETEST |
| B40 | LIMIT_LOCALIZATION |

## Important distinction

The arrows above do not mean that the earlier result statistically validates the later result.

They mean that the earlier result influenced the later research question.

When archived data participate in redesign, they are treated as discovery data. Prospective status is assigned only to the later frozen evaluation.
