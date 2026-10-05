# Expanded failure-salvage ledger v0.2 — audit notes

**Date:** 5 October 2026  
**Ledger:** `evidence/failure_salvage_ledger_v0_2.csv`

## What the ledger contains

The v0.2 ledger contains **21 explicit salvage / reuse chains**.

These are not 21 independent experiments and they are not the denominator used in the B19-B40 reuse fraction.

The ledger is an event table:

```text
source limitation
-> retained asset / information
-> later research action
-> later status
```

The B19-B40 quantitative audit is instead a source-stage table:

```text
negative / limiting source stage
-> was there any explicit downstream backward link?
```

These two objects answer different questions and should not be numerically conflated.

## Current chain composition

Of the 21 ledger chains:

- **5** are early pre-standardization / archive-supported chains;
- **16** come from the later standardized programme;
- **21 / 21** retain the parent verdict or parent historical status rather than rewriting it.

The current salvage-type counts are:

| Salvage type | Count |
| --- | ---: |
| PROTOCOL_REPAIR | 4 |
| MODEL_REDESIGN | 2 |
| CONSTRAINT_REUSE | 2 |
| STATE_ENRICHMENT | 2 |
| LIMIT_LOCALIZATION | 2 |
| EXPLANATORY_VARIABLE_CHANGE | 1 |
| DECOMPOSITION | 1 |
| REPRESENTATIONAL_SALVAGE | 1 |
| MECHANISM_DIAGNOSIS | 1 |
| OBSERVABLE_REDESIGN | 1 |
| COMPUTATIONAL_REUSE | 1 |
| QUESTION_REFORMULATION | 1 |
| MEASUREMENT_REDESIGN | 1 |
| INTERPRETATION_CORRECTION | 1 |
| READOUT_OPERATOR_REDESIGN | 1 |
| CLAIM_BOUNDARY_RETENTION | 1 |

Because a chain can carry more than one salvage tag, type counts can exceed the number of chains.

## Why this matters

The expanded ledger shows that "failure reuse" is not one mechanism.

At least five distinct functional roles are visible:

1. **repair** — fix protocol or implementation while retaining the old status;
2. **redesign** — change the model, observable, or state representation;
3. **localization** — convert a broad failure into a narrower boundary;
4. **reuse** — reanalyze retained numerical assets without rerunning the expensive computation;
5. **constraint** — keep a negative result as a boundary on later claims, even without producing a successor PASS.

This supports a more precise formulation than "failures become useful."

A better working statement is:

> Retained negative or limiting results can remain scientifically active through several distinct operations, including repair, redesign, localization, computational reuse, and claim-boundary enforcement.

## Important counting caution

The current B19-B40 source-stage audit gives:

```text
21 explicitly reused source stages / 25 negative-or-limiting source stages = 84%
```

The v0.2 salvage ledger also happens to contain 21 chains.

That numerical equality is accidental.

One source stage can generate multiple chains, and one chain can combine multiple source stages. The manuscript should therefore never infer the 84% figure from the chain ledger.

## Next quantitative extension

The next useful table is a **source-to-action bipartite graph** with unique source IDs and unique successor-action IDs.

That representation would allow:

- out-degree of each negative source;
- in-degree of each redesign stage;
- time-to-reuse;
- repeated reuse of old results;
- comparison of direct computational reuse versus conceptual reuse;
- identification of "hub failures" that influenced multiple later branches.

This is likely more informative than a single reuse percentage.
