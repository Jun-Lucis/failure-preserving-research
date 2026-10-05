# Preliminary quantitative lineage audit — B24 to B40

**Version:** v0.1  
**Date:** 5 October 2026  
**Source table:** [stage_lineage_B24_B40_v0_1.csv](../evidence/stage_lineage_B24_B40_v0_1.csv)

## Purpose

The qualitative case study suggests that retained negative, invalid, or otherwise limiting outcomes were frequently reused in later BIG stages.

This note performs a first quantitative check on that impression.

It is **not yet a programme-wide result** because:

- the coded interval begins at B24 rather than B3;
- stage names and verdict vocabularies changed over time;
- source-to-successor links were coded manually from repository status documents;
- later stages have less follow-up time than earlier stages;
- related stages within one B-number are not statistically independent observations.

The goal is to establish an auditable baseline before a full B3–B40 coding pass.

---

## 1. Coding rule

A source stage is counted as a **negative/limited source** when its formal status contains one of the following operational forms:

- `FAIL`
- `IMPLEMENTATION_INVALID`
- `T1_valid=False`
- `TOPOLOGY_SPAN_NOT_REALIZED`

This is intentionally broader than scientific FAIL alone because the methodology studies retained research limitations that can influence later work.

A negative/limited source is counted as **explicitly reused** only when a later coded row names that source in `inherited_from`.

This definition measures documented backward linkage, not causal importance.

---

## 2. Overall result

Across the currently coded B24–B40 interval:

- negative/limited source stages: **16**
- source stages with an explicit later backward link: **14**
- observed reuse fraction: **87.5%**

The two coded sources without a later explicit backward link are:

- **B26.2** — `AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_FAIL`
- **B29-T1** — `T1_valid=False` / no held-out predictive verdict

B26.2 was also the terminal result of a formally closed programme segment, so absence of a direct successor should not be interpreted as evidence that the result had no later conceptual value.

---

## 3. Windowed exploratory comparison

Using coarse windows:

| Window | Negative / limited sources | Explicitly reused later | Observed reuse fraction |
| --- | ---: | ---: | ---: |
| B24–B26 | 4 | 3 | 75.0% |
| B27–B36 | 7 | 6 | 85.7% |
| B37–B40 | 5 | 5 | 100% |

The sequence

```text
75.0% -> 85.7% -> 100%
```

is **consistent with** the user's qualitative impression that later research increasingly read earlier failures back into new work.

It is **not sufficient to establish a temporal trend**.

Reasons include small counts, non-independent stages, right-censoring, and the possibility that later programme architecture made source references more explicit even if the underlying cognitive reuse rate had not changed.

---

## 4. Why a simple "salvage-stage rate" is misleading

A second possible metric is:

```text
stages explicitly classified as salvage
/
all claim-bearing stages
```

Under the current coding this metric does **not** increase monotonically, because successful descendants and replications expand the denominator.

For example, once a failure produces a productive new branch, that branch can contain several prospective PASS stages that are not themselves new salvage events.

Therefore the preferred object is not the fraction of all stages labelled "salvage", but the **fate of retained negative/limited source stages**.

This distinction should be preserved in the paper.

---

## 5. Provisional interpretation

The current coded interval supports the descriptive statement:

> **Most retained negative or limiting BIG stages in B24–B40 had an explicit downstream role in a later research question, protocol, representation, or localization test.**

The stronger statement

> "failure reuse increased over time"

remains a hypothesis pending complete B3–B40 coding and a predeclared treatment of stage granularity and right-censoring.

---

## 6. Next audit

The full audit should freeze the following before computing programme-wide statistics:

### Unit of analysis

Choose one:

- B-number;
- named claim-bearing stage;
- predeclared experiment;
- independent hypothesis lineage.

The current v0.1 table uses named stages.

### Negative/limited status dictionary

Predeclare whether the denominator includes:

- formal FAIL only;
- FAIL + INVALID;
- FAIL + INVALID + INCONCLUSIVE;
- early qualitative negative outcomes without standardized verdict strings.

### Reuse rule

A backward link should require at least one of:

1. prior raw output reused;
2. prior failure explicitly motivates the successor question;
3. prior failure sets a parameter/domain bound;
4. prior failure changes the representation or observable;
5. prior invalidity triggers a protocol repair.

### Right-censoring

A terminal failure should be given a fixed opportunity window before being labelled "not reused."

### Sensitivity analyses

Repeat the calculation under:

- strict FAIL-only denominator;
- FAIL + invalid/limited denominator;
- B-number-level aggregation;
- stage-level aggregation.

---

## 7. Research-method implication

Even without a confirmed time trend, the current 14/16 backward-link count is useful.

It shows why a success-only research archive would badly compress this particular programme. Many later stages are intelligible only when the preceding negative or limiting stage remains visible.

That is the core empirical motivation for the failure-preserving architecture.
