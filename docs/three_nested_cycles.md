# Three nested research cycles

## Overview

The architecture is organized across three time scales.

```text
MICRO
AI reasoning <-> external execution
        |
        v
MESO
freeze -> test -> verdict -> redesign
        |
        v
MACRO
retained history -> salvage -> conceptual pivot -> new programme state
```

These are nested rather than independent.

## Micro cycle: AI–external computation loop

Typical unit:

```text
question
-> AI-assisted derivation or implementation
-> simple executable code
-> external Python/Colab run
-> numerical output
-> discrepancy / confirmation / instability
-> revised derivation
```

The purpose of the external run is not to certify truth. It is to prevent a reasoning system from being the sole judge of its own output.

Simple code is often valuable because the mapping

```text
equation <-> implementation <-> numerical output
```

remains inspectable.

## Meso cycle: prospective test–redesign cycle

Typical unit:

```text
hypothesis
-> frozen protocol
-> claim-bearing computation
-> PASS / FAIL / INCONCLUSIVE / INVALID
-> diagnosis
-> new hypothesis
-> new frozen protocol
```

The previous verdict is immutable except for correction of a documented clerical or implementation error. A successor PASS does not upgrade a parent FAIL.

## Macro cycle: failure-salvage and research-memory cycle

Typical unit:

```text
many retained stages
-> cross-stage reading
-> recurring obstruction or pattern
-> conceptual change
-> mathematical redesign
-> new prospective programme
```

The macro cycle is where research history itself becomes an input.

Two forms are especially important:

- **local salvage**: one failed predictor directly motivates a corrected predictor;
- **representational salvage**: a cluster of failures becomes intelligible only after a change of variables, observable, or conceptual frame.

## Integrity condition

The macro cycle creates a risk of retrospective overfitting. The operational safeguard is separation:

```text
old archived data
-> discovery / diagnosis

new frozen data
-> validation
```

The BIG case study contains examples of both local and representational salvage.
