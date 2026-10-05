# Failure-retention protocol

## Principle

A failed, inconclusive, or invalid result is a persistent research object.

The record should preserve enough information for a later researcher to answer:

1. What exactly was predicted?
2. What was frozen before evaluation?
3. What actually happened?
4. Why was the verdict assigned?
5. Which numerical assets still exist?
6. Was the result later used for redesign?
7. If so, was the successor tested on fresh data?

## Minimum retained record

For each claim-bearing phase retain, where applicable:

- predeclaration;
- code or notebook version;
- parameter manifest;
- random seeds;
- solver settings;
- raw or checkpointed outputs;
- summary tables;
- numerical-integrity checks;
- formal verdict;
- explanation of FAIL / INCONCLUSIVE / INVALID;
- hashes or immutable archive identifiers.

## Immutable verdict rule

A successor result does not overwrite the parent verdict.

Preferred notation:

```text
P1 -> FAIL
P1A -> diagnostic only
P2 -> PASS
```

Avoid:

```text
P1 -> PASS after repair
```

unless the original verdict was genuinely caused by a documented clerical error and the correction procedure itself is explicitly audited.

## Salvage annotation

If an old result is later reused, add a separate salvage record:

- source phase;
- source verdict;
- retained asset;
- date / later phase of reuse;
- salvage type;
- what was learned;
- whether the old data entered model construction;
- what fresh data were used for later validation.

## Discovery/validation separation

If old data influenced the new hypothesis, they cannot be presented as independent validation of that hypothesis.

Label them explicitly as:

`DISCOVERY_DATA`

and label the new held-out / prospectively frozen evaluation as:

`VALIDATION_DATA`

when that distinction is justified.
