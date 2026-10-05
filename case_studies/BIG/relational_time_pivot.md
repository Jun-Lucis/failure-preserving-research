# Case study: relational-time conceptual pivot

## Purpose

This note documents a methodological transition in the later BIG programme: a shift from increasingly fragile absolute timing claims toward relative and relational timing observables.

It is a research-process interpretation, not a new scientific verdict.

## 1. Accumulated obstruction before the pivot

The B30-B36 programme produced a mixture of positive and negative results. In the timing branch, the following formal failures were retained:

- B35.1: `DISTANCE_ORDERED_APPROX_LINEAR_PEAK_TIMING_FAIL`
- B35.2: `HIGHER_RESOLUTION_SAMPLING_STABLE_APPROX_LINEAR_PEAK_TIMING_FAIL`
- B36.1: `GEOMETRY_CONDITIONED_PEAK_TIMING_ORDERING_FAIL`

B36.2 then found a narrower additive geometry/readout decomposition rather than a universal timing law.

B37 continued to test whether absolute timing could be stabilized by changing spatial parametrization and support construction. Two claim-bearing tests remained negative:

- B37.1: `INTRINSIC_CONTOUR_REPARAMETERIZATION_FAIL`
- B37.2: `FIXED_ARC_SUPPORT_TIMING_COLLAPSE_FAIL`

The B37.2 failure was localized to absolute peak-time cross-resolution behavior. Diagnostics showed substantial grid-phase sensitivity of outer-probe peak timing.

## 2. Conceptual change

Instead of continuing to repair absolute peak time, the programme changed the observable.

Existing-data alignment analysis showed that pulse traces became highly similar after temporal rephasing and that relative lag was more stable than raw absolute peak time.

This motivated a new prospective question:

> Which timing structures remain stable when timing is treated relationally between probes, sources, receivers, operators, and readouts?

This is the key methodological pivot.

```text
repeated failure of absolute-timing claims
        +
diagnostics on retained traces
        |
        v
change of representation / observable
        |
        v
relative and relational timing hypotheses
```

## 3. Discovery data versus validation data

The archived B35-B37 failures and diagnostics are **not** counted as independent evidence for the later relational hypotheses if they were used to motivate those hypotheses.

Their role is:

```text
archived failures
-> discovery data
-> representation change
-> equation / observable refinement
```

Prospective evidence begins with newly frozen tests.

## 4. Fresh prospective sequence after the pivot

B38.1 prospectively tested relative lag and returned:

`RELATIVE_BOUNDARY_LAG_GEOMETRY_PASS`

B38 then developed the relational structure further:

- source/receiver swap asymmetry;
- D-weighted near-symmetry of the tangent operator;
- prospective tangent-to-response prediction;
- gamma intervention;
- weighted-dual readout suppression.

The strongest B38 conclusion remained finite and relational: the observed timing asymmetry depended strongly on the joint relation between operator, source, receiver, and readout.

B39 asked whether timing could be expressed using internally constructed relational coordinates. It produced both PASS and FAIL outcomes. In particular, B39.3-P1 remained a formal FAIL, while diagnostics and response-independent calibration led to a separately frozen B39.3-P2 PASS.

B40 then tested transfer to new clock-map families and target-excluded reconstruction. Both parent transfer claims failed, but the failures were localized and narrower transformation rules survived fresh tests.

## 5. Methodological interpretation

The notable pattern is not "after the pivot there were no failures."

A more defensible description is:

> After the pivot, failures increasingly localized the domain, coordinate, or transfer rule of a relational framework rather than repeatedly invalidating the entire research direction.

This can be represented as:

```text
EARLIER
FAIL -> perhaps the proposed global timing law is wrong

LATER
FAIL -> this coordinate / map / resolution / transfer rule does not survive here
```

This interpretation remains a case-study observation and should not be presented as a controlled measure of theory quality.

## 6. Why this matters for failure-preserving research

If the earlier failed timing data had been discarded, the later pivot would have had less structure to act on.

The archived failures provided:

- counterexamples to overly strong timing laws;
- traces that could be re-read under a different observable;
- resolution and phase-sensitivity information;
- boundaries on what the new formulation needed to explain;
- material for designing fresh prospective tests.

The methodological lesson is therefore:

> Retaining failures can preserve future optionality. A later conceptual change may make previously negative results informative without changing their original verdicts.
