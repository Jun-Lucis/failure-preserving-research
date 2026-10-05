# Failure-salvage lineage coding protocol v0.1

**Status:** FROZEN FOR THE NEXT FULL-AUDIT PASS  
**Freeze date:** 5 October 2026

This protocol is frozen before the planned expansion from the current B19–B40 table to the earlier BIG record.

Its purpose is to reduce the freedom to redefine "failure reuse" after seeing the full historical pattern.

## 1. Primary question

> Among retained negative or limiting research outcomes, how often is there an auditable later research action that explicitly uses the earlier outcome without changing its original verdict?

This is a descriptive case-study question, not a causal productivity estimate.

## 2. Unit of analysis

### Primary unit

A **named stage** that has a distinct scientific question, protocol, or formal interpretation in an authoritative BIG paper, status document, or reproducibility record.

Examples:

- B25.1
- B25.1R
- B39.3-P1
- B39.3-P2

### Diagnostics

A diagnostic or calibration stage is coded as a separate row if it materially connects a source result to a later claim-bearing stage.

Diagnostic rows are **not** included in the denominator of claim-bearing-stage counts.

### Replications

A replication is a separate row when it uses fresh evaluation data or a separately identified corrective protocol.

## 3. Source-of-truth hierarchy

Evidence priority:

1. public BIG GitHub paper/status record;
2. archived Zenodo paper or reproducibility package;
3. project/library file with stable manuscript or data provenance;
4. prior conversation history only as a **candidate locator**.

A chain supported only by prior conversation history is not promoted into the formal quantitative ledger until a source in levels 1–3 is recovered.

## 4. Negative / limiting source dictionary

### Primary broad dictionary

A claim-bearing source qualifies when its authoritative status is one of:

- FAIL;
- NOT_SUPPORTED;
- NULL_OR_INCONCLUSIVE;
- INCONCLUSIVE;
- IMPLEMENTATION_INVALID / PROTOCOL_INVALID;
- required-domain or topology condition NOT_REALIZED;
- a formally recorded validity/readability gate failure that prevents held-out evaluation;
- a clearly documented negative structural result even if early work predates standardized verdict strings.

### Strict sensitivity dictionary

A second analysis will include only:

- FAIL;
- NOT_SUPPORTED;
- clean negative structural results with numerical integrity passing.

INCONCLUSIVE, INVALID, and NOT_REALIZED stages will be excluded from the strict denominator.

## 5. What counts as explicit reuse?

A source is coded as reused only if at least one later authoritative record supports one of the following:

### R1 — computational reuse

Earlier raw output, cached trajectory, profile, root, gradient, CSV, checkpoint, or equivalent numerical artifact is directly reused.

### R2 — constraint reuse

The earlier negative result explicitly narrows or excludes part of the next hypothesis space.

### R3 — model redesign

The structure of the earlier failure motivates a new equation or predictor.

### R4 — state enrichment

The earlier failure motivates adding history, path, geometry, state variables, or another information-bearing component.

### R5 — explanatory-variable change

A failed qualitative interpretation is replaced by a different explanatory quantity.

### R6 — decomposition

A failed single-law description motivates separation into multiple contributions.

### R7 — protocol repair

An invalid, non-realized, or flawed protocol leads to a new independently named protocol.

### R8 — limit localization

A broad transfer failure leads to a narrower test locating where structure survives or fails.

### R9 — representational salvage

A group of earlier results motivates a change of observable, coordinate, or conceptual representation.

### R10 — claim-boundary retention

A negative or unresolved result is explicitly used to prevent a stronger later interpretation, even if no successor PASS is sought.

## 6. What does not count as reuse?

Do not count:

- mere chronological succession;
- citation of an earlier paper without a changed research action;
- generic use of the same codebase or equations;
- a later PASS that does not explicitly depend on the earlier negative result;
- retrospective relabeling of the old result as a success.

## 7. Parent-verdict rule

For every reuse link record:

```text
parent_verdict_retained = yes / no
```

The primary methodology analysis requires **yes**.

If the historical verdict was corrected because of a verified implementation error, record:

- original invalid result;
- reason for correction;
- corrective replication separately.

Do not rewrite the original row.

## 8. Discovery versus validation

For every successor claim, code:

- old data entered redesign? yes/no;
- fresh or held-out evaluation? yes/no;
- successor was diagnostic only? yes/no.

If old data entered model construction, they are discovery data for the successor.

A successor PASS counts as prospectively separated only if its claim-bearing evaluation is fresh, held out, or frozen under a newly identified protocol before the claim-bearing outcome is inspected.

## 9. Primary descriptive statistics

Report:

1. total claim-bearing stages;
2. total broad negative/limiting sources;
3. total strict negative sources;
4. number and fraction with at least one explicit reuse link;
5. reuse-type frequencies;
6. fraction of reused sources whose parent verdict remained unchanged;
7. fraction of successor PASS claims with explicit fresh/held-out separation.

## 10. Terminal-stage and right-censoring rule

Two values will be reported.

### Conservative reuse fraction

```text
all explicitly reused negative/limiting sources
/
all negative/limiting sources
```

Terminal sources remain in the denominator.

### Opportunity-adjusted reuse fraction

Exclude a source from the denominator only if:

- it is explicitly designated terminal/closeout, **and**
- no later claim-bearing stage exists in the same declared research branch.

This adjustment must be reported alongside, never instead of, the conservative value.

## 11. Temporal trend analysis

No trend will be claimed from B-number alone.

Reason: later chronological revisits can carry old B numbers, such as B9 empirical Phase II.

A temporal trend requires actual execution/publication dates.

If dates are sufficiently recoverable, use predeclared calendar windows rather than post-hoc bins. Until then, statements such as "reuse increased recently" remain qualitative hypotheses.

## 12. Early-record policy

For B3–B18, standardized PASS/FAIL vocabulary was not always used.

Early cases may be coded if the source clearly records:

- a failed or misleading observable;
- a runtime/recovery event with retained data;
- a later reinterpretation explicitly dependent on the earlier result.

However, these cases must be flagged:

`EARLY_NONSTANDARD_VERDICT`

and analyzed separately in sensitivity tests.

## 13. Model-capability claims

Subjective impressions that a later AI model generation materially changed research depth/speed are not part of the lineage outcome coding.

They may appear in the qualitative case-study discussion but require a separate controlled design for quantitative claims.

## 14. Freeze rule

Any change to this coding protocol after the full B3–B40 audit begins must produce:

- a new protocol version;
- a documented reason;
- both old- and new-rule sensitivity results where feasible.

The v0.1 protocol must remain preserved.
