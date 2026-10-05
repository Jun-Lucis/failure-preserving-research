# Failure-Preserving AI-Assisted Research

**A research-methodology project for individual computational science**

This repository develops and documents a research architecture that emerged during a long-running individual mathematical and numerical research programme.

Its central proposition is:

> **AI can change not only the cost of successful research, but also the economics and future value of failed experiments.**

The primary longitudinal case study is **Boundary Information Geometry (BIG)**:

https://github.com/Jun-Lucis/BIG-theory

BIG is used here as a case study of research process. The methodological claims in this repository do **not** depend on BIG being correct as a physical theory.

## Core architecture

The method is organized as three nested research cycles plus an experimental handoff.

### Micro cycle — AI–external computation loop

```text
question
  -> AI-assisted formulation
  -> equation / code
  -> external Python execution
  -> numerical output / discrepancy
  -> AI-assisted reconsideration
  -> revised equation / code
  -> ...
```

The reasoning environment and executable environment are deliberately separated. In the BIG case, AI-assisted reasoning was repeatedly tested outside the conversational model through direct numerical execution, commonly in Python/Colab. External computation is not treated as proof; it is used as an executable constraint that can expose errors, instabilities, or missing structure.

### Meso cycle — prospective test, retained failure, redesign

```text
hypothesis
  -> predeclaration / freeze
  -> prospective computation
  -> PASS / FAIL / INCONCLUSIVE / INVALID
  -> diagnosis
  -> redesigned hypothesis
  -> new freeze
  -> fresh test
```

A failed frozen test is not edited until it becomes a success. Its verdict remains part of the record. A later successful test answers a new, separately frozen question.

### Macro cycle — failure salvage and research memory

```text
retained research history
  -> retrieval of earlier failures
  -> pattern extraction
  -> conceptual or mathematical redesign
  -> new prospective test
  -> expanded research history
```

The research programme is treated as a history-bearing dynamic process rather than a sequence in which only successful end states survive.

A useful abstraction is

```text
H_t = retained research history up to time t
Q_(t+1) = G(Q_t, H_t)
```

where the next research question depends not only on the current theory but also on archived FAIL, INCONCLUSIVE, INVALID, parameter, output, and diagnostic information.

### Experimental handoff

AI-assisted individual research can move far through model construction, numerical exploration, public-data comparison, and prospective prediction. It does not remove the boundary imposed by unavailable physical measurements.

```text
individual + AI exploration
  -> public-data comparison
  -> frozen measurable prediction
  -> experimental handoff
  -> laboratory / organization / domain experts
  -> new physical evidence
```

The method therefore proposes complementarity, not replacement of organized experimental science.

## Why preserve failures?

A failed experiment may later support:

1. **Computational reuse** — cached trajectories, profiles, roots, gradients, or scans.
2. **Constraint reuse** — removal of a region of hypothesis space.
3. **Model redesign** — identifying a missing variable, decomposition, or transformation.
4. **Protocol repair** — exposing a design flaw without reclassifying the old result.
5. **Limit localization** — turning a broad failure into a narrower surviving structure.
6. **Representational salvage** — after a conceptual pivot, using earlier failures as discovery data for a new representation.

> **A historical FAIL can remain a FAIL under its original hypothesis while becoming useful data for designing a different hypothesis.**

One clear BIG example is:

```text
B25.1
AB_CONSTANT_DENSITY_FAIL
  -> archived profiles re-read retrospectively
  -> coarea obstruction analysis
  -> replacement predictor frozen
  -> B25.1b
AB_LEVEL_RESOLVED_BRIDGE_PASS
```

A later timing sequence shows a broader representational pivot from fragile absolute timing hypotheses toward relative and relational timing, followed by fresh prospective tests.

## Personal intuition and public testability

This project also explores a broader but deliberately limited observation:

> **AI-assisted computation may lower the barrier between private intuition and public testability.**

A personal intuition, philosophical question, or informal conceptual model is not evidence. But it can increasingly be translated into:

```text
intuition
  -> operational definition
  -> mathematics
  -> executable model
  -> prospective prediction
  -> comparison with public data
  -> experimental handoff
```

The claim is not that philosophy becomes physics by being formalized. The narrower claim is that the cost of transforming an intuition into something that can fail publicly and quantitatively may be falling.

## Repository map

The repository is organized around five functions:

- `docs/` — conceptual framework, literature positioning, and quantitative audit notes;
- `case_studies/BIG/` — audited BIG examples, including early cases, B9 failure retention, B17-B18 readout enrichment, and B34-B35 calibration gating;
- `evidence/` — source-stage lineage tables, expanded failure-salvage ledger, normalized source-action edges, and the salvage taxonomy;
- `protocols/` — predeclaration, failure-retention, experimental-handoff, and frozen lineage-coding rules;
- `paper/` — versioned manuscript snapshots and Zenodo metadata draft;
- `figures/` — reproducible diagram sources for the nested cycles, failure-salvage spiral, and relational-time pivot.

Important current audit files include `stage_lineage_B19_B40_v0_3.csv`, `failure_salvage_ledger_v0_2.csv`, `source_action_edges_v0_2.csv`, and `early_verified_lineage_candidates_v0_1.csv`.

## Relationship to BIG and Zenodo

```text
methodology paper (Zenodo)
        <->
this methodology repository
        <->
BIG-theory repository
        <->
BIG papers / data / reproducibility archives (Zenodo)
```

BIG repository: https://github.com/Jun-Lucis/BIG-theory

The methodology-paper DOI will be added after the first formal Zenodo release.

## Scope and limitations

This is currently a **single-researcher longitudinal case study**, not a controlled productivity trial.

It does not establish that AI-generated reasoning is reliable without external checking, that more computation automatically produces better science, that every failed experiment has future value, or that external Python execution proves a model correct.

Public databases can support substantial external comparison, but they cannot substitute for purpose-built measurements. Individual AI-assisted research does not replace laboratories, teams, institutions, experimental craft, calibration, or domain expertise.

The method should be judged separately from the scientific theory used as its primary case study.

## Audit status

The current standardized lineage audit covers B19-B40. Under the broad frozen coding dictionary, 25 negative or limiting source stages have been identified and 22 have an explicit downstream backward link (88.0%). Audit v0.2 reported 84%; v0.3 recovered one explicit B29-T1-to-B30 lineage edge from the integrated source record while preserving the old audit version. The percentage is a descriptive statistic for the coded BIG interval, not a general estimate of the value of failure.

Earlier B3-B18 records are being audited separately because formal verdict vocabulary was not yet standardized. Five archive-verified early cases are currently documented, including measurement redesign, computational reuse, model redesign, interpretation correction, and readout-operator enrichment.

Key audit files:

- [Frozen lineage coding protocol](protocols/lineage_coding_protocol_v0_1.md)
- [B19-B40 quantitative lineage audit v0.3](docs/quantitative_lineage_audit_v0_3.md)
- [B3-B18 early lineage audit](docs/early_lineage_audit_B3_B18_v0_1.md)
- [Early verified lineage candidates](evidence/early_verified_lineage_candidates_v0_1.csv)

## Working paper

**Failure-Preserving AI-Assisted Research: A Nested Research Architecture for Individual Computational Science**

Working subtitle:

**A Longitudinal Case Study from Boundary Information Geometry**

The current manuscript snapshot is [paper/manuscript_v0_6.md](paper/manuscript_v0_6.md).

## Author

**Jun Lucis**  
Independent researcher
