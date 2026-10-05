# Temporal lineage audit — v0.2

**Date:** 5 October 2026  
**Stage audit:** `evidence/stage_lineage_B19_B40_v0_3.csv`  
**Latency table:** `evidence/failure_reuse_latency_v0_1.csv`  
**Previous audit:** `docs/temporal_lineage_audit_v0_1.md`

## 1. What changed from v0.1

Version 0.1 could test only the prevalence of explicit backward linkage. Most public GitHub records for later stages were deposited in integrated batches, so it correctly refused to treat GitHub commit spacing as research latency.

A second provenance pass recovered owner-side timestamps from retained Drive run artifacts: result summaries, protocol snapshots, frozen configuration files, and explicit "frozen before fresh trajectory" sentinel files.

This makes a limited latency analysis possible.

Private Drive URLs and file IDs are not published in this repository. The public table records only artifact names, timestamps, and provenance class. These timestamps are supplementary owner-side provenance, not independently immutable public evidence.

## 2. Prevalence across the two standardized epochs

The retrospective structural split remains:

```text
Epoch A: B19-B26
Epoch B: B27-B40
```

The split is scientifically interpretable because B19-B26 has an explicit programme closeout before B27 opens, but it was not frozen in advance for this methodology analysis.

| Epoch | Reused | Broad negative/limiting sources | Fraction | Wilson 95% interval |
| --- | ---: | ---: | ---: | ---: |
| B19-B26 | 10 | 13 | 76.9% | 49.7%-91.8% |
| B27-B40 | 12 | 12 | 100% | 75.8%-100% |

Fisher exact comparison:

```text
two-sided p = 0.220
one-sided p = 0.124
```

The direction is compatible with increasing reuse prevalence, but it is not statistically persuasive.

## 3. Exact artifact-timestamp latency subset

Fourteen source-to-successor transitions have timestamps that are sufficiently comparable for an exploratory latency analysis.

The measured interval is:

```text
source result summary / final source status
-> successor frozen protocol / architecture
```

It is not "time spent thinking." It can include breaks, unrelated work, file-writing delay, and unrecorded intermediate reasoning. Conversely, some successor design work may begin before the final source file is written.

The 14 observed intervals have:

```text
median = 1.199 h   (~1 h 12 min)
IQR    = 0.493-2.032 h
mean   = 1.904 h
range  = 0.205-5.732 h
```

The individual intervals are retained in `failure_reuse_latency_v0_1.csv`.

## 4. Does reuse become faster over time?

Using the source-result timestamp as the chronological variable:

```text
Spearman rho = 0.0505
p = 0.8637

Kendall tau = 0.0110
p = 1.000
```

There is no evidence of a monotonic shortening of source-to-successor freeze latency.

A simple exploratory split at 1 October gives:

| Subset | n | Median latency | Mean latency |
| --- | ---: | ---: | ---: |
| before 1 Oct | 9 | 0.692 h | 1.830 h |
| 1 Oct onward | 5 | 1.590 h | 2.036 h |

A one-sided Mann-Whitney test for "later is faster" gives approximately:

```text
p = 0.697
```

This provides no support for faster reuse in the later subset.

## 5. Interpretation

The temporal evidence now separates two ideas that were previously easy to conflate:

```text
A. How often does a retained limitation become explicitly linked to later work?
B. How quickly does the next frozen research action appear?
```

For A, the later epoch has a higher observed prevalence:

```text
76.9% -> 100%
```

but the sample is small and documentation maturity is a major confound.

For B, the available exact timestamp subset does **not** show acceleration.

The current evidence therefore supports a more precise interpretation:

> The later programme appears more systematic in preserving and explicitly connecting negative outcomes to successor work, but it is not demonstrably faster at converting a negative result into the next frozen protocol.

This is methodologically more informative than an unsupported acceleration story.

## 6. Why documentation maturity matters

Later BIG stages increasingly contain:

- machine-readable frozen protocols;
- explicit result summaries;
- named protocol snapshots;
- "frozen before any fresh trajectory" sentinels;
- retained verdict strings;
- explicit backward links;
- checkpoint-first persistence.

That change improves both research discipline and observability of the process.

Consequently, the higher later-epoch backward-link fraction may be partly a measurement effect:

```text
actual reuse behavior
+
better preservation
+
better lineage labeling
=
higher observed reuse
```

The methodology paper should present this as a central limitation rather than attempt to remove it rhetorically.

## 7. Representative fast transitions

The timestamp audit documents several short source-to-freeze transitions, including approximately:

- B32.1 -> B33.1: **12 min 18 s**
- B25.1 -> B25.1b: **19 min 40 s**
- B40.2 -> B40.2-P1B: **23 min 39 s**
- B35.2 -> B36.1: **25 min 53 s**
- B26 -> B26.1: **41 min 32 s**
- B39.3-P1 -> B39.3-P2: **48 min 28 s**

It also documents multi-hour redesigns, including B27.2 -> B28 (~5 h 17 min), B36.1 -> B36.2 (~4 h 50 min), and B37.2 -> B38.1 (~5 h 44 min).

Thus the archive contains rapid reuse, but not a simple monotonic acceleration.

## 8. Special provenance cases

### B27.2 -> B28

The B27.2 source time comes from the Drive summary file. The successor time uses the earlier public GitHub commit that freezes the B28 architecture, because the corresponding Drive output folder begins later. This is intentionally conservative about the meaning of "successor freeze."

### B40.1 -> B40.1-P1B

The B40.1 summary file was later modified during a documented runner correction. The latency table uses the final modified summary timestamp rather than the initial creation timestamp, so the parent failure is not treated as final before the correction was incorporated.

## 9. Claim boundary

Supported:

> In the coded BIG case study, many negative or limiting results were followed by a separately frozen successor action on timescales ranging from minutes to several hours.

Supported descriptively:

> Explicit backward linkage is more prevalent in the B27-B40 epoch than in the B19-B26 epoch under the current coding.

Not established:

> Failure reuse increased over time as a general behavioral trend.

Not supported by the timestamp subset:

> Failure reuse became faster over time.

Not established:

> Changes in AI model capability caused either the high reuse rate or the short observed latencies.

## 10. Next step

A stronger causal or temporal analysis would require an independently reconstructable timeline of:

```text
source completed
-> diagnosis recorded
-> successor idea recorded
-> protocol frozen
-> first fresh run
-> successor verdict
```

plus a model-capability timeline and controls for researcher learning, programme maturity, topic difficulty, compute load, and documentation practice.

For the present preprint, the correct stopping point is the descriptive result above.
