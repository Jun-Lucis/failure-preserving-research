# Case study: B6 archived dense scan -> crossing-only salvage

**Provenance status:** archive-verified, public raw-data link pending.

This case is included as an early, nonstandard-verdict example under the frozen lineage-coding protocol. The numerical values below were recovered from an archived BIG project output dated 7 June 2026. The corresponding raw archive has not yet been linked from the public BIG GitHub repository, so this case should remain supplementary until that public provenance is completed.

## 1. Retained dense scan

The archived scan contains the following mean fitted boundary exponents:

| m | mean nu |
| ---: | ---: |
| 0.50 | 2.263516 |
| 0.52 | 2.241559 |
| 0.54 | 2.209627 |
| 0.56 | 2.183180 |
| 0.58 | 2.160224 |
| 0.60 | 2.111463 |
| 0.62 | 2.055275 |
| 0.64 | 2.028777 |
| 0.66 | 1.972842 |

The retained data therefore cross `nu=2` between `m=0.64` and `m=0.66`.

## 2. Crossing-only reanalysis

A later archived output is explicitly labeled:

`2026-06-07_B6_4_crossing_only_analysis`

It did not rerun the full dense PDE scan. Instead, it analyzed the retained scan numerically as a crossing problem.

Reported estimates were:

```text
linear interpolation:  m_c = 0.6502895
local linear fit:      m_c = 0.6490295
bootstrap mean:        m_c = 0.6491058
bootstrap std:               0.001859
95% interval:          0.6456584 - 0.6529818
local slope:          -2.2118
local intercept:       3.435523
local fit range:       0.60 <= m <= 0.66
```

## 3. Methodological interpretation

The relevant process structure is:

```text
expensive dense numerical scan
-> retain summary-level numerical state
-> later question changes
-> no need to rerun the full PDE
-> crossing-only analysis of the retained data
```

This is a strong early example of **COMPUTATIONAL_REUSE** plus **QUESTION_REFORMULATION**.

The important scientific distinction is that the crossing-only analysis is retrospective. It does not turn the same archived data into a fresh prospective validation set.

## 4. What this case does and does not show

It supports the methodological statement that retained numerical summaries can preserve future analytical options after the expensive simulation stage has ended.

It does **not** by itself establish:

- why the dense scan was originally generated;
- that a previous plateau hypothesis was formally frozen and failed;
- that the crossing estimate received an independent fresh-data validation.

Those stronger historical claims require additional source recovery and are therefore not asserted here.

## 5. Audit status

Coding tags:

- `EARLY_NONSTANDARD_VERDICT`
- `COMPUTATIONAL_REUSE`
- `QUESTION_REFORMULATION`
- `RETROSPECTIVE_ONLY`

Before formal Zenodo release of the methodology paper, the corresponding raw B6 archive should be either deposited publicly or referenced by an immutable archive identifier.
