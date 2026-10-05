# Temporal lineage audit — v0.1

**Date:** 5 October 2026  
**Source table:** `evidence/dated_negative_source_lineage_v0_1.csv`  
**Status table:** `evidence/stage_lineage_B19_B40_v0_3.csv`

## Question

The qualitative impression motivating this audit is that later BIG work increasingly reused earlier FAIL / INCONCLUSIVE / limiting outcomes as active inputs to the next research step.

A genuine temporal claim requires more than B-number order. Some programmes were revisited later, and many public repository updates were deposited in batches after several internal stages had already completed.

This audit therefore separates two questions:

1. **epoch-level prevalence:** did explicit backward linkage become more common in the later programme?
2. **reuse latency:** did the time from source failure to successor redesign become shorter?

Only the first can currently be tested meaningfully from the public record.

## Date-quality rule

Public GitHub timestamps are coded into four practical classes:

- **direct_result_commit** — commit message directly records a result or verdict;
- **publication/phase proxy** — commit records an integrated result or publication but may lag execution;
- **integrated batch proxy** — several scientific stages were deposited together, so internal latency cannot be inferred;
- **none** — no successor exists under current coding.

Commit spacing is **not** automatically treated as research latency. For example, a result commit followed two seconds later by a protocol file is repository-write cadence, not evidence that the scientific redesign took two seconds.

## Structural epoch split

For an exploratory temporal comparison, the standardized programme is split at the documented B19-B26 closeout and opening of B27.

This split is scientifically interpretable but was selected during retrospective archive analysis, not prospectively frozen before the outcomes. Statistical results are therefore descriptive/exploratory.

### Epoch A — B19 through B26

Broad negative/limiting sources:

```text
13
```

Explicitly reused:

```text
10 / 13 = 76.9%
```

Wilson 95% interval:

```text
49.7% – 91.8%
```

The three unlinked sources are B20.6, terminal B23A-P6, and terminal B26.2.

### Epoch B — B27 through B40

Broad negative/limiting sources:

```text
12
```

Explicitly reused:

```text
12 / 12 = 100%
```

Wilson 95% interval:

```text
75.8% – 100%
```

## Exploratory significance check

For the 2×2 table

```text
             reused   not reused
B19-B26        10        3
B27-B40        12        0
```

Fisher's exact test gives approximately:

```text
two-sided p = 0.220
one-sided p = 0.124
```

The direction is compatible with the original impression, but the sample is too small to establish a statistically persuasive increase.

The correct conclusion is therefore:

> **Explicit failure/limitation reuse is descriptively more prevalent in the later coded BIG epoch, but an increase over time is not established.**

## Why the apparent increase may not be behavioral

The later programme also became much more explicit about:

- frozen protocols;
- retained verdict strings;
- machine-readable stage identities;
- `inherited_from` relations;
- recovery audits;
- no-rescue rules.

Therefore the observed 76.9% -> 100% difference can arise from at least two mechanisms:

```text
true change in research behavior
+
improved documentation / lineage detectability
```

The current archive cannot cleanly separate them.

This is not a nuisance to be hidden. It is part of the methodological result: once lineage is recorded systematically, reuse becomes more observable.

## Reuse latency

A full latency analysis is **not yet valid**.

Most B23A, B30-B36, B37-B38, B39, and B40 internal stages are available publicly as integrated or batch records. Their scientific order is explicit, but their individual execution timestamps are not.

The strongest timestamped transition currently visible in the public repository is:

```text
B27.2 covariance FAIL recorded:
2026-09-28 15:50:53 UTC

B28 formal lineage-transport architecture frozen:
2026-09-28 21:04:24 UTC

recorded interval:
5 h 13 min 31 s
```

This shows that a retained FAIL could feed a formally frozen successor within the same public-record day, but one example cannot establish a temporal trend.

## What would be needed for a stronger test

The next provenance layer should recover, where available:

- notebook/run completion timestamps;
- frozen-protocol creation timestamps;
- Drive file modification timestamps;
- Zenodo deposition timestamps;
- checkpoint timestamps;
- explicit predeclaration timestamps.

For each source-action edge, the preferred variables are:

```text
source_completed_at
successor_idea_recorded_at
successor_frozen_at
successor_first_run_at
successor_verdict_at
```

That would allow separate measurement of:

- diagnosis latency;
- redesign latency;
- validation latency;
- total source-to-successor latency.

## Current claim boundary

Supported now:

> Later BIG stages show a higher observed prevalence of explicit backward linkage than the earlier standardized epoch (100% versus 76.9% under the current broad coding).

Not supported now:

> Failure reuse definitely increased over time.

Also not supported:

> AI capability improvements caused the apparent increase.

The latter would require an independent model-capability timeline and a design capable of separating model capability from researcher learning, protocol maturation, topic changes, and documentation improvements.

## Methodological implication

This audit slightly changes the emphasis of the paper.

The strongest current evidence is not a temporal acceleration law. It is the existence of a documented research-memory architecture in which negative outcomes remain active across many successor stages.

The temporal-development hypothesis should remain in the paper as a **testable methodological prediction**, not a concluded result.
