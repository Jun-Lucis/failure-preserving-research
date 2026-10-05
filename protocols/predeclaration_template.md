# Predeclaration template

Use this template before a claim-bearing computational test.

## Identity

- Study / phase:
- Date frozen:
- Author:
- Repository commit / archive hash:
- AI model or reasoning environment used:
- External execution environment:
- Code version:

## Question

State one question that can receive a negative answer.

## Hypothesis

State the claim in operational terms.

## Inputs frozen before evaluation

- model equations:
- parameter family:
- training / calibration data:
- held-out data:
- initial conditions:
- numerical resolution:
- timestep / solver controls:
- observable definitions:

## Primary prediction

Specify the predicted sign, ordering, interval, error bound, transfer property, or other measurable outcome.

## PASS rule

State all required components.

## FAIL rule

State what constitutes a valid negative result.

## INCONCLUSIVE rule

State conditions under which the experiment cannot decide the claim.

## INVALID rule

State numerical, implementation, integrity, or protocol violations that prevent a scientific verdict.

## Prohibited post-hoc changes

List changes that are not allowed after claim-bearing outputs are inspected, for example:

- extending the search domain;
- replacing a failed target;
- changing tolerance;
- changing observable;
- changing resolution gate;
- adding a new fit parameter.

Any such change requires a new named phase and a new freeze.

## Data-retention plan

Specify which raw outputs, summaries, code, logs, hashes, and failed cases will be retained.

## Successor rule

If this test fails, specify whether diagnostics are allowed and how a successor test must be separated from the parent verdict.
