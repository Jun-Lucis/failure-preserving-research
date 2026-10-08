# BIG-B41 — A Retained Quantitative FAIL Followed by a Fresh Prospective Geometric Test

**Source research programme:** [Boundary Information Geometry (BIG)](https://github.com/Jun-Lucis/BIG-theory)  
**Source publication:** https://doi.org/10.5281/zenodo.23249677  
**Scope:** A documented **single-programme research-methodology case**, not evidence for general scientific productivity improvement.

## Why this case matters

B41 preserves a useful distinction in prospective research:

> A failed **frozen quantitative claim** can be localized post-hoc, used to construct a modified predictor, and then independently examined on newly frozen target data — without changing the original FAIL.

The tested scientific system is a **finite synthetic response family** computed by a three-dimensional periodic viscous vector-vorticity solver, with six fixed half-enstrophy response horizons and local Family-C parameter secants. This is a methodology case about the use of failure, not an independent demonstration of the scientific model.

## Source-to-successor sequence

| Stage | Status | Epistemic role |
| --- | --- | --- |
| **B41-P1** | `TRAJECTORY_RESPONSE_GEOMETRY_TRANSFER_PASS` | Prospective first-order local-to-finite response prediction; 32/32 target advantage, 97.7883% pooled weighted RMSE reduction |
| **B41-P2** | **`DIMENSIONLESS_REMAINDER_TRANSFER_FAIL`** | Fresh quantitative scalar second-order proxy tested with 48 targets; 19/24 cells met 20% mismatch, under the frozen acceptance requirement; gate C and anchor robustness gate E failed |
| **B41-P2 post-hoc** | **Diagnosis only** | All five >20%-mismatch cells localized to `E_u10` and `H_u16`; both had strongly anti-aligned tangent `V_h` and acceleration `A_h` |
| **B41-P3** | `FULL_SECOND_ORDER_GEOMETRIC_REMAINDER_TRANSFER_PASS` | Separately frozen no-fit signed full-second-order formula; 48 new target simulations, 24/24 cells within 20%, rho 0.997391, 93.1041% pooled tangent improvement |

### 1. What failed in P2?

The frozen scalar predictor was

```text
Q2_scalar(dp) = 0.5 * |dp| * ||A_h|| / ||V_h||
```

It retained the magnitudes of tangent and second-order acceleration but lost their relative orientation. Five quantitative mismatch cells exceeded 20%. The two responsible local families had nearly opposite `V_h` and `A_h`, with `cos(V_h,A_h)` approximately `-0.998970` and `-0.985142`.

Despite 43/48 tangent-transfer advantages and 88.1862% aggregate improvement, P2's **primary scalar quantitative transfer claim failed**. Its secondary 10% classifier PASS cannot rescue the parent verdict.

### 2. What did the failure reveal?

The post-hoc localization suggested that **signed finite second-order displacement** rather than a scalar norm ratio could matter when tangent and acceleration are anti-aligned. A new predictor retained both magnitude and orientation:

```text
Q2_full(dp) =
    [0.5 * dp^2 * ||A_h||] /
    [||dp * V_h + 0.5 * dp^2 * A_h|| + eps]
```

The formula introduced **zero fitted parameters**, but its retrospective calculation on previously revealed P2 outcomes was **not** a new prospective validation.

### 3. What was prospectively new in P3?

P3 used fresh anchors `I–L` and directions `u17–u24`; its eight local geometry families passed, and the 48 primary predictions were frozen **before any P3 target PDE was run**. The implementation audit was frozen pre-outcome and the formal evaluator was executed once.

- **48/48** target tangent transfers beat the nearest baseline.
- Aggregate pooled weighted RMSE improved **93.1041%**.
- The sign-sensitive remainder predictor achieved **24/24** cells within the predeclared 20% quantitative mismatch tolerance.
- Spearman correlation of predicted and observed sign-averaged relative error was **0.997391**; median mismatch was **0.6792%**.
- Newly included anti-aligned stress cases `J_u20` and `K_u22` formed part of the pre-outcome frozen set.

**Negative comparator statement:** In P3 the non-gating scalar formula also performed well: 24/24 qualifying cells, rho 0.997391, median mismatch **0.6755%**. Consequently, P3 does **not** establish generic superiority or universal necessity of retaining tangent–acceleration orientation. The scientific conclusion is narrower than the methodological usefulness of the P2 failure.

## Failure-preserving chain / evidence roles

```text
frozen P1 tangent prediction -> formal PASS
           |
new frozen scalar P2 remainder claim -> formal FAIL (immutable)
           |
post-hoc localization of anti-parallel orientation -> hypothesis generation ONLY
           |
separate freeze of full signed P3 predictor, 0/48 target integrations
           |
48 fresh target integrations + one formal evaluator -> P3 formal PASS
```

**The methodological unit is a newly frozen claim and its own unseen outcomes**, not a reanalysis of a previously opened dataset. P3's result adds evidence for its own finite-model claim; it does not change P2's original experimental result.

## Relation to the existing frozen methodology audit

The repository's standardized quantitative lineage audit **v0.3 covers B19–B40**. Its reported 25 negative/limiting source stages, 22 explicit backward links, and 88.0% descriptive rate remain unchanged. This B41 case is a **later supplementary worked example**, **not an additional row silently inserted into the frozen B19–B40 dataset**. A future separately versioned audit may examine it using the frozen coding protocol and additional source verification.

## Primary records and reproducibility

- [B41 Zenodo publication and reproducibility archive](https://doi.org/10.5281/zenodo.23249677)
- [BIG-theory B41 bounded status and results](https://github.com/Jun-Lucis/BIG-theory/blob/main/docs/research_status_update_B41.md)
- [BIG-theory B41 paper index](https://github.com/Jun-Lucis/BIG-theory/tree/main/papers/B41_trajectory_space_response_geometry)

The P3 target-stage archive is named `BIG_B41_P3_TARGET_STAGE_PACKAGE_v1_0.zip` and has the recorded SHA-256:

```text
dd2e3ef9fafa24c3eb5553f43fb4a0b99523472e63d8d69f2cfab41daee909e6
```

The general methodology of failure retention is a separately presented research proposal. This case neither proves the general value of AI assistance nor establishes that the underlying BIG model is physically universal.
