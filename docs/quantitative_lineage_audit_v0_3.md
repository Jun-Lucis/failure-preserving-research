# Quantitative lineage audit — B19 to B40, v0.3

**Date:** 5 October 2026
**Primary table:** evidence/stage_lineage_B19_B40_v0_3.csv
**Frozen protocol:** protocols/lineage_coding_protocol_v0_1.md

## 1. Why v0.3 changes the broad reuse fraction

Audit v0.2 reported 21 / 25 = 84% for the broad B19-B40 negative/limiting source-stage reuse fraction.

During the early-history and calibration audit, the integrated B30-B36 source was reread. It explicitly states that the B30 architecture was frozen as a successor to the B29-T1 training-domain readability failure.

The v0.2 stage table had coded B30.1 only as inheriting from generic B29, so the automated exact-source linkage test failed to recognize B29-T1 as reused.

No scientific verdict changed. No denominator category changed. One previously under-specified lineage edge was made explicit in stage_lineage_B19_B40_v0_3.csv.

The corrected broad count is therefore:

    22 explicitly reused sources / 25 broad negative-or-limiting sources = 88.0%

The old v0.2 table and 84% result remain preserved as audit history.

## 2. Broad primary sensitivity result

The broad frozen dictionary includes FAIL, INVALID, INCONCLUSIVE, NOT_SUPPORTED, NOT_REALIZED, T1_valid=False, and the B19 no-robust-scalar negative structural result.

| Quantity | Value |
| --- | ---: |
| Broad negative/limiting source stages | 25 |
| Explicitly reused later | 22 |
| Conservative reuse fraction | **88.0%** |
| Not explicitly linked under current coding | 3 |

The three currently unlinked broad sources are B20.6 (INCONCLUSIVE), B23A-P6 (NOT_SUPPORTED_RATE_ORDERED_LOCAL_RESPONSE_RECONFIGURATION), and B26.2 (AB_TOPOLOGY_STRADDLING_FIXED_COEFFICIENT_TRANSFER_FAIL).

B23A-P6 and B26.2 are explicit terminal/closeout outcomes in their local programmes. B20.6 remains a retained INCONCLUSIVE result; B21 and B22 explicitly state that they do not repair or upgrade it.

## 3. Strict negative-result sensitivity analysis

The strict dictionary includes formal FAIL, formal NOT_SUPPORTED, and the B19 clean negative structural result. It excludes INCONCLUSIVE / NULL_OR_INCONCLUSIVE, IMPLEMENTATION_INVALID, NOT_REALIZED, and T1_valid=False.

| Quantity | Value |
| --- | ---: |
| Strict negative source stages | 16 |
| Explicitly reused later | 14 |
| Strict reuse fraction | **87.5%** |
| Unlinked strict sources | B23A-P6, B26.2 |

The similarity between 88.0% and 87.5% is useful: the high observed backward-link rate is not produced only by counting invalid or inconclusive stages. It remains a descriptive property of this one coded research programme.

## 4. Opportunity-adjusted sensitivity analysis

The frozen protocol permits a denominator that excludes a source only when it is explicitly terminal/closeout and no later claim-bearing stage exists in the same declared branch. Under the current coding, B23A-P6 and B26.2 meet this condition.

    22 / 23 = 95.65%

This value should not replace the conservative 88.0% result. It is a sensitivity analysis showing how much the conservative denominator is affected by deliberate terminal stopping points.

## 5. B-family aggregation sensitivity

Named stages are the primary unit. The 25 broad source stages occupy 16 programme groups: B19, B19E, B20, B23, B23A, B25, B26, B27, B28, B29, B32, B35, B36, B37, B39, and B40.

| Group rule | Reused groups | Total groups | Fraction |
| --- | ---: | ---: | ---: |
| at least one source in group reused | 15 | 16 | **93.75%** |
| every broad source in group reused | 13 | 16 | **81.25%** |

The range demonstrates why the named-stage level remains preferable. B-family aggregation can hide terminal outcomes inside otherwise productive branches.

## 6. What the sensitivity analysis supports

Three conservative views are now available:

    broad named-stage:  22/25 = 88.0%
    strict named-stage: 14/16 = 87.5%
    all-sources-per-B:  13/16 = 81.25%

All remain high within the coded programme, although they answer different questions.

> Across the standardized B19-B40 audit, explicit downstream reuse of retained negative or limiting outcomes is common and is not an artifact of one permissive status definition.

This does not support a causal productivity estimate, a universal percentage for research, a claim that every failure is useful, or a demonstrated increase of reuse frequency over calendar time.

## 7. Why the v0.2 -> v0.3 correction matters

The change from 84% to 88% did not come from altering a criterion after seeing an undesirable result. It came from recovering a source-backed lineage statement that the automated exact-link rule had missed.

The appropriate response is to retain v0.2, document the missing provenance edge, create v0.3, and recompute the sensitivity results rather than silently overwriting the old table.

## 8. Remaining quantitative limitation

A true temporal-development claim still requires dated lineage edges. B-number order is insufficient because some earlier-numbered programmes were revisited later.

The next quantitative extension should add source date, successor-action date, salvage latency, research branch, and terminal/active status. Until then, the hypothesis that failure reuse became more frequent as the programme matured remains open.
