# Early BIG lineage audit — B3 to B18, v0.2

**Date:** 6 October 2026  
**Protocol:** `protocols/lineage_coding_protocol_v0_1.md`  
**Provenance manifest:** `evidence/early_provenance_manifest_v0_2.csv`

## Purpose

The later B19-B40 programme contains standardized prospective verdicts and explicit freeze records. Earlier BIG work does not consistently use the same vocabulary.

This audit therefore asks a narrower question:

> Can earlier archived records be identified in which a limitation, apparent contradiction, or unsuccessful transfer explicitly changed a later research action?

The answer remains yes, but the early evidence must stay analytically separate from the B19-B40 quantitative lineage statistic.

Version 0.2 adds retained-artifact timestamps, distinguishes public from owner-side provenance, and corrects one early numerical claim whose exact source could not be recovered.

## E01 — Dense B6 scan reused as a crossing-only analysis

The owner archive contains a dense B6.3 scan over `m=0.50...0.66`. The retained summary and transition-fit artifacts were created on 7 June 2026.

A later folder is explicitly named:

```text
2026-06-07_B6_4_crossing_only_analysis
```

and contains:

```text
B6_4_input_B6_3_summary.csv
B6_4_crossing_summary.csv
```

This is direct file-level evidence that the B6.4 analysis reused the B6.3 numerical summary rather than rerunning the full PDE.

The crossing summary reports:

```text
mc_linear_interpolation = 0.6502895077
mc_local_linear_fit     = 0.6490294859
mc_bootstrap_mean       = 0.6491057863
95% CI                  = 0.6456583509 - 0.6529817664
```

The B6.3 transition fit itself had a much larger uncertainty and should not be conflated with the later crossing-only estimate.

Classification:

- `EARLY_NONSTANDARD_VERDICT`
- `COMPUTATIONAL_REUSE`
- `QUESTION_REFORMULATION`
- `RETROSPECTIVE_ONLY`

Provenance status:

- exact source/reuse artifacts recovered;
- exact owner-side timestamps recovered;
- public immutable raw-data link not yet available.

This remains the clearest early example of expensive numerical work retaining later computational value.

## E02 — Elliptic boundary measurement redesign: provenance correction

Version 0.1 quoted a numerical pair:

```text
apparent radial nu ~ 2.63
local inward-normal nu = 2.024 +/- 0.014
```

The present provenance recovery did **not** locate an immutable artifact supporting that exact pair. It should therefore not remain in the main manuscript as a source-backed numerical example.

What is directly recovered is a same-day sequence of elliptic-boundary artifacts:

```text
B5_3 elliptic compact-support outputs
-> B5_3A local-exponent profile
-> B5_7 elliptical free-boundary normal-fit programme
```

Representative retained summaries are:

```text
B5_3_summary.json:
    mean_nu_good = 0.800773

B5_3A_summary.json:
    mean_window_nu = 0.848595

B5_7_summary_all.csv:
    gamma=0.05 mean_good_nu = 1.823167
    gamma=0.10 mean_good_nu = 1.829080
    gamma=0.20 mean_good_nu = 1.850367
```

These values are **not** a controlled before/after comparison because the parameter sets differ. They support only the narrower provenance statement that an early elliptic-boundary analysis was followed by local-exponent and free-boundary-normal fitting work.

Classification:

- `EARLY_MEASUREMENT_REDESIGN_CANDIDATE`
- `REPRESENTATION_REFINEMENT`
- `PARTIAL_PROVENANCE`

Current policy:

> Keep E02 in the supplementary provenance audit, but remove the unrecovered 2.63 -> 2.024 numerical claim from the main manuscript until the matching source is located.

This correction is itself an example of the paper's non-retroactivity rule applied to its own audit.

## E03 — B13/B13.1 corrected an attractive interpretation

B13/B13.1 remains supported by both the public BIG repository and retained raw artifacts.

The public B13.1 paper states that the shifted-coordinate single-selection response is better described by a logistic basin-boundary kernel than by a direct cos-squared law. The reported fit includes:

```text
single-selection cos-squared binned RMSE ~ 0.0738
logistic-kernel binned RMSE             ~ 0.0122
sequential cloud-model RMSE             ~ 0.0048
```

Retained Drive artifacts include the empirical-kernel fit metrics and later Gaussian-cloud convolution summaries.

Classification:

- `EARLY_INTERPRETATION_CORRECTION`
- `REPRESENTATION_REFINEMENT`
- `CLAIM_NARROWING`

The methodological point is not that a failed quantum analogy became a success. Later computation made the internal mechanism more specific and the external analogy less direct.

Public record:

https://github.com/Jun-Lucis/BIG-theory/tree/main/papers/B13_1_rotated_basis_observation

## E04 — B12.1c limitation motivated an ignition barrier

The B12 manuscript explicitly states:

```text
B12.1 and B12.1c supported the approach-lock-inheritance sequence,
but B12.1c still allowed deterministic low-noise lock.

B12.1d therefore introduced an ignition barrier in the resonance sector.
```

The refined scan reported:

```text
sigma_R at peak lock ~ 0.070
P_lock               ~ 0.861
P_full_success       ~ 0.856
```

Classification:

- `EARLY_NONSTANDARD_LIMITATION`
- `MODEL_REDESIGN`
- `MECHANISM_LOCALIZATION`

The earlier stage is not relabeled FAIL. The supported statement is that deterministic low-noise locking remained as a design limitation and directly motivated a new mechanism and rerun.

Public record:

https://github.com/Jun-Lucis/BIG-theory/tree/main/papers/B12_unified_boundary_dynamics

## E05 — B17 local readability did not transfer unchanged to B18

The B18 paper directly records a transfer limitation and successive readout enrichment.

For front suppression:

```text
B18.0 read-start local load      R^2 = 0.163
B18.1 path exposure              R^2 ~ 0.742
B18.2 threshold/interface-core   R^2 = 0.793
B18.3 best threshold path        R^2 = 0.807
```

The paper explicitly describes B18.0 as a useful negative result and states that B18.1 therefore introduced path-integrated readability.

Classification:

- `EARLY_TRANSFER_LIMIT`
- `STATE_ENRICHMENT`
- `READOUT_OPERATOR_REDESIGN`
- `REPRESENTATION_REFINEMENT`

This is the strongest early public example of a predictor/readout that did not transfer unchanged and therefore motivated a richer successor representation.

Public record:

https://github.com/Jun-Lucis/BIG-theory/tree/main/papers/B18_boundary_readout_operators

## Main-text policy after v0.2

Four early examples are strong enough for concise use in the main manuscript:

```text
E01 B6 retained-scan computational reuse
E03 B13/B13.1 interpretation correction
E04 B12 mechanism redesign
E05 B17->B18 transfer-driven readout enrichment
```

E02 remains in the supplement as a measurement-redesign candidate with partial provenance, but its unrecovered exact numerical pair is removed from the main text.

This choice avoids using a plausible but currently untraceable number merely because it supports the narrative.

## Important non-cases

Several B3-B18 transitions remain scientifically important but should not automatically be counted as failure salvage.

Examples include:

- B7 -> B8: local/global separation followed by a geometry-dependent threshold question;
- B9 -> B10 -> B11: separation, capture, and post-capture inheritance;
- B16 -> B17: stored history sharpened into readable history.

These are coherent progressions, but the currently available records do not require a negative or limiting parent result for the successor question.

## Current early-evidence status

The early audit now contains:

```text
4 main-text source-backed cases
1 supplementary partial-provenance candidate
```

They are not used to revise the standardized B19-B40 result:

```text
22 / 25 = 88.0%
```

because the early denominator has not been reconstructed stage by stage under a stable historical coding rule.

The correct statement remains:

> Explicit failure/limitation reuse is directly visible before B19, but the standardized quantitative estimate applies only to the coded B19-B40 interval.

## Remaining recovery targets

Priority archival targets are now:

1. the original source underlying the previously quoted E02 `nu ~ 2.63 -> 2.024 +/- 0.014` pair, if it exists;
2. a public immutable package for B6.3/B6.4 raw summary files;
3. any authoritative B9.1/B9.2 record documenting why the explicit shape-energy representation was introduced;
4. pre-B12 stage records if a more exact B12.1c run-level timestamp is needed.

None of these is required for the current four-case early main-text set.
