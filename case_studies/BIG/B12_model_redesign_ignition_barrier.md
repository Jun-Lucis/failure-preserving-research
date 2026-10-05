# Case study: B12.1c -> B12.1d — model redesign after deterministic low-noise lock

**Provenance status:** archive-verified from the B12 Zenodo-edition manuscript.

## 1. The limitation

The B12 reduced system was intended to reproduce, inside a unified approach-lock-inheritance model, the finite-noise locking structure previously studied in B10.

The B12 manuscript states that B12.1 and B12.1c could support the approach-lock-inheritance sequence, but that **B12.1c still allowed deterministic low-noise lock**.

That meant the unified model did not yet reproduce the intended B10-like finite-noise window.

## 2. The redesign

B12.1d introduced an explicit ignition barrier in the resonance sector,

```text
G_ignite(R_i)
```

so that low-noise trajectories could remain below the ignition threshold, intermediate noise could assist barrier crossing and sustained lock, and high noise could destroy coherence.

The refined scan reported:

```text
sigma_R at peak lock ~ 0.070
P_lock at peak       ~ 0.861
P_full_success       ~ 0.856
```

under the specified reduced-model protocol.

## 3. Methodological interpretation

The relevant lineage is:

```text
unified model supports locking
-> but deterministic low-noise locking survives
-> desired finite-noise mechanism not yet isolated
-> add an ignition barrier
-> rerun a refined scan
-> finite-noise R-lock window appears
```

This is best classified as:

- **MODEL_REDESIGN**
- **MECHANISM_LOCALIZATION**
- **EARLY_NONSTANDARD_VERDICT**

The B12.1c result should not be rewritten as a FAIL unless a formal historical verdict exists. The archive supports only the narrower statement that deterministic low-noise locking remained a limiting behavior and directly motivated the B12.1d redesign.

## 4. Why this matters

This case shows a constructive use of a mismatch between the intended mechanism and the actual model behavior.

The response was not to tune the success threshold until the old model looked stochastic-resonance-like. Instead, the mechanism itself was changed by adding a new state-dependent barrier, after which the finite-noise structure was tested again.

This is a useful example of the difference between:

```text
post-hoc reinterpretation of the old run
```

and

```text
explicit model revision followed by a new run
```

## Source

Public BIG repository:

https://github.com/Jun-Lucis/BIG-theory/tree/main/papers/B12_unified_boundary_dynamics
