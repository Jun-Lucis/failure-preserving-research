# Early BIG lineage audit — B3 to B18, v0.1

**Date:** 5 October 2026  
**Protocol:** `protocols/lineage_coding_protocol_v0_1.md`

## Purpose

The later B19–B40 programme contains standardized prospective verdicts and explicit freeze records. Earlier BIG work does not consistently use the same vocabulary.

This audit therefore asks a narrower question:

> Can earlier archived records be identified in which a limitation, apparent contradiction, or unsuccessful transfer explicitly changed a later research action?

The answer is yes, but the early evidence should remain analytically separate from the B19–B40 quantitative lineage statistic.

## Audited early cases

### E01 — Dense B6 scan reused as a crossing-only analysis

A retained dense scan over `m=0.50...0.66` crossed `nu=2` between `m=0.64` and `m=0.66`.

A later archived output explicitly labeled `B6_4_crossing_only_analysis` reused those numerical summaries rather than rerunning the full PDE and reported a bootstrap estimate near

```text
m_c = 0.6491058
95% interval = 0.6456584 - 0.6529818
```

Classification:

- `EARLY_NONSTANDARD_VERDICT`
- `COMPUTATIONAL_REUSE`
- `QUESTION_REFORMULATION`
- `RETROSPECTIVE_ONLY`

This is the clearest early example of expensive numerical work retaining later value.

### E02 — Non-radial boundary measurement redesigned

An early concise preprint records an apparent loss of the quadratic exponent under naive radial averaging in ellipse geometry, with an apparent value around `nu_radial ~ 2.63`.

The measurement representation was changed to local inward-normal coordinates with a fitted boundary offset. In the cited case the local fit returned

```text
nu = 2.024 +/- 0.014
```

with sub-percent amplitude-law agreement.

Classification:

- `EARLY_NONSTANDARD_VERDICT`
- `MEASUREMENT_REDESIGN`
- `REPRESENTATION_REFINEMENT`
- `NUMERICAL_METHOD_DIAGNOSIS`

This should not be described as turning a failed simulation into a success. The original radial result remains evidence that the radial observable was a poor coordinate for the non-radial boundary.

### E03 — B13/B13.1 corrected an attractive interpretation

B13 showed that Born-like behavior was not automatic in the reduced selection model. A restricted low-barrier finite-noise regime approached the reference more closely, but the rotated-basis B13.1 follow-up changed the interpretation.

The single-selection response was better represented by a logistic basin-boundary kernel than by a direct cos-squared law. A finite-width cloud convolution then explained the later cos-squared-like sequential response.

Representative reported values include:

```text
single-selection cos-squared RMSE ~ 0.0738
logistic-kernel RMSE             ~ 0.0122
sequential cloud-model RMSE      ~ 0.0048
```

Classification:

- `EARLY_INTERPRETATION_CORRECTION`
- `REPRESENTATION_REFINEMENT`
- `CLAIM_NARROWING`

This case is important because later computation made the original analogy less direct rather than more persuasive.

### E04 — B12.1c limitation motivated an ignition barrier

The B12 manuscript states that B12.1 and B12.1c supported the approach-lock-inheritance sequence but that B12.1c still allowed deterministic low-noise lock.

B12.1d therefore introduced an ignition barrier in the resonance sector and reran the refined scan.

Representative result:

```text
sigma_R at peak lock ~ 0.070
P_lock               ~ 0.861
P_full_success       ~ 0.856
```

Classification:

- `EARLY_NONSTANDARD_LIMITATION`
- `MODEL_REDESIGN`
- `MECHANISM_LOCALIZATION`

The earlier stage is not relabeled FAIL; the source only supports the more limited statement that deterministic low-noise lock remained and directly motivated redesign.

### E05 — B17 local readability did not transfer unchanged to B18

B17 found that a read-start local retained-history load organized later response well in its positive-feedback moving-boundary model.

B18 then moved the idea to a propagating inhibitory front. The B18 manuscript explicitly identifies:

```text
B18.0: read-start local trace is insufficient
B18.1: path-integrated trace exposure is stronger
B18.2: test active-front / interface-core exposure
```

The resulting hierarchy became:

```text
stored history
-> locally readable history
-> path-readable history
-> interface-core path exposure
```

Classification:

- `EARLY_TRANSFER_LIMIT`
- `STATE_ENRICHMENT`
- `READOUT_OPERATOR_REDESIGN`
- `REPRESENTATION_REFINEMENT`

This is an early analogue of the later formal transfer-failure/redesign chains.

## Important non-cases

Several B3–B18 transitions are scientifically important but should **not** automatically be counted as failure salvage.

Examples include:

- B7 -> B8: local/global separation followed by a geometry-dependent threshold question;
- B9 -> B10 -> B11: separation, capture, and post-capture inheritance;
- B16 -> B17: stored history sharpened into readable history.

These are coherent research progressions, but the currently available records do not require a negative or limiting parent result for the successor question.

Keeping them out of the salvage denominator is important to avoid inflating the method's apparent prevalence.

## Current early-evidence status

The early audit currently contains five archive-verified lineage cases.

They are **not** yet used to revise the B19–B40 value

```text
21 / 25 = 84%
```

because the denominator for B3–B18 has not been reconstructed stage by stage under a stable historical coding rule.

The correct present statement is therefore:

> Explicit failure/limitation reuse is directly visible before B19, but the standardized quantitative estimate currently applies only to the coded B19–B40 interval.

## Next recovery targets

Priority archival targets are:

1. the exact B6 dense-scan source files and public immutable link;
2. the earliest non-radial boundary-fit source package;
3. any authoritative B9.1/B9.2 record documenting why the explicit shape-energy representation was introduced;
4. pre-B12 stage records that clarify whether deterministic low-noise lock was formally treated as a failed mechanism test or only as a design limitation;
5. the detailed B18.0/B18.1 tables for direct effect-size coding.

Until those are recovered, the five current cases remain a qualitative supplementary audit rather than a programme-wide early-period statistic.
