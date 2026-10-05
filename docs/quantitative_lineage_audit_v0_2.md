# Preliminary quantitative lineage audit — B19 to B40

**Version:** v0.2  
**Date:** 5 October 2026  
**Source table:** [stage_lineage_B19_B40_v0_2.csv](../evidence/stage_lineage_B19_B40_v0_2.csv)

## Purpose

This audit extends the first B24–B40 coding backward to B19 and the B23A universality-audit branch.

The goal is to test a narrow process question:

> When a BIG stage produced a negative, inconclusive, invalid, or otherwise limiting result, was that retained result explicitly used in a later research action?

This is not a productivity estimate and not evidence that failure itself causes progress.

## Coding

The current table contains:

- **60** coded stages / stage-like records;
- **57** claim-bearing records;
- **25** negative or limiting source records under the current broad dictionary.

The broad "negative / limiting" dictionary currently includes formal strings containing:

- `FAIL`
- `INVALID`
- `INCONCLUSIVE`
- `NOT_SUPPORTED`
- `NOT_REALIZED`
- `T1_valid=False`
- the B19 no-robust-scalar negative structural result.

A source is counted as explicitly reused only when a later row names it in `inherited_from`.

## Result

Of the 25 coded negative / limiting sources:

- **21** have an explicit downstream backward link;
- **4** do not under the current coding.

Observed explicit-reuse fraction:

```text
21 / 25 = 84%
```

The four currently unlinked sources are:

1. **B20.6 — INCONCLUSIVE**
2. **B23A-P6 — NOT_SUPPORTED_RATE_ORDERED_LOCAL_RESPONSE_RECONFIGURATION**
3. **B26.2 — AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_FAIL**
4. **B29-T1 — T1_valid=False / no held-out verdict**

Three of these are natural terminal or closeout outcomes in their local programmes. B20.6 is also a retained incompleteness rather than a clean scientific negative.

Therefore "not explicitly reused" must not be read as "useless."

## Representative backward links added in v0.2

### B19 -> B19E

B19 did not support one robust ray-independent upstream scalar collapse. B19E carried frozen B19 boundary/core additions into an independently maintained TIDE solver and tested whether they added prospective predictive information beyond a strong local-flow baseline.

Primary B19E-A1 result:

`NULL_OR_INCONCLUSIVE`

A later Stage-B exact local-budget audit used fresh realizations and closed the resolved budget to near machine precision, while showing that the historical P-D proxy omitted large transport terms. The B19E record explicitly states that Stage B **does not rescue A1**.

This is a strong example of a negative external holdout leading to mechanism diagnosis rather than verdict repair.

### B23 implementation-invalid repair

The original B23 aggregate remained INCONCLUSIVE because parts of the symmetric search-window protocol were not executable.

One E3 repair was later found to dispatch the wrong ray and was preserved as an implementation-invalid record. E3R2 was a corrective replication and was not counted as a retroactive original-plan success.

This is an unusually clean example of protocol repair with non-retroactivity.

### B23A terminal narrowing

B23A repeatedly converted stronger failed or inconclusive transfer claims into narrower prospective questions:

```text
smooth-normal transfer NOT SUPPORTED
-> branch-level orientation test
-> topology-sensitive piecewise/reset representation
-> non-topological reset INCONCLUSIVE
-> finite-window susceptibility INCONCLUSIVE
-> new-speed rate-ordering test NOT SUPPORTED
-> terminal no-rescue stop
```

The terminal result is not a success chain. It is a map of where quantitative universality stops.

## Interpretation

The current v0.2 audit supports this descriptive statement:

> **In the coded B19–B40 interval, most retained negative or limiting stages were explicitly connected to a later research action while their original verdicts remained unchanged.**

The current 84% value is not a general property of research. It is a descriptive statistic of this coded programme interval.

## What is still not established

The user's qualitative impression that failure reuse became **more frequent over time** remains plausible but unproven.

A valid trend analysis still requires:

- full B3–B40 coding;
- frozen stage-granularity rules;
- a stable negative/limited dictionary;
- right-censoring rules for terminal stages;
- sensitivity analysis at both stage and B-number level.

The earlier B24–B40 exploratory windows produced high reuse fractions, but the small counts and changing programme architecture make a trend claim premature.

## Next step

The next coding pass should prioritize:

1. B3–B18 source recovery;
2. explicit provenance for early runtime-recovery / measurement-redesign cases;
3. B9 empirical Phase II as a late revisit of an early model;
4. strict separation between repository-verified links and conversation-recovered candidate links.

The methodology paper should report only the audited subset in its main text and place candidate / incomplete provenance chains in supplementary material until verified.
