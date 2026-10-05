# Case study: B13 to B13.1 — interpretation corrected by later computation

B13/B13.1 provides an earlier example of research-memory use in which a promising initial analogy was weakened rather than amplified by later calculation.

## B13 baseline

In the B13 reduced binary observation model, ordinary basin selection did **not** automatically reproduce the Born-like reference curve.

The reported baseline RMSE against the cos-squared reference was approximately:

```text
RMSE = 0.2118
```

A restricted low-barrier finite-noise regime approached the reference more closely:

```text
b = 1.0
sigma = 0.35
best RMSE ~ 0.0629
```

The B13 conclusion was therefore already conditional: Born-like shape was a comparison target, not a derived law.

## B13.1 rotated-basis follow-up

The rotated-basis follow-up changed the interpretation further.

When the curves were organized by relative angle, a direct cos-squared description was not the best account of the single-selection response. The aggregate selection curve was substantially better described by an empirical logistic basin-boundary kernel.

Representative reported comparison:

```text
cos-squared RMSE: 0.0738
logistic-kernel RMSE: 0.0122
```

The later sequential calculation added another layer. Actual noisy post-selected states were finite-width clouds rather than ideal point resets. Averaging the logistic kernel over that finite-width cloud produced a cos-squared-like sequential response, with a reported fitted cloud width near 12 degrees and RMSE near 0.0048.

## Methodological interpretation

The useful chain is:

```text
initial Born-like comparison
-> baseline mismatch
-> restricted finite-noise resemblance
-> rotated-basis test
-> direct cos-squared interpretation weakens
-> logistic basin-boundary kernel
-> finite-width cloud averaging explains later cos-squared-like response
```

This is not a clean FAIL-to-PASS sequence and should not be forced into that vocabulary.

It is better classified as:

- **INTERPRETATION_CORRECTION**
- **REPRESENTATION_REFINEMENT**
- **CLAIM_NARROWING**

The later computation did not validate the stronger early analogy. It replaced it with a more specific internal mechanism.

## Why this matters for the methodology paper

Failure-preserving research is not only about retaining formal FAIL labels.

A research memory can also preserve:

- an imperfect reference comparison;
- the parameter regime in which the analogy improves;
- the conditions under which it breaks;
- the later observable that reveals why.

This case supports the broader principle:

> Later computation should be allowed to make the original interpretation less attractive.

That is a crucial protection against AI-assisted narrative momentum.

## Sources

BIG-B13 repository entry:

https://github.com/Jun-Lucis/BIG-theory/tree/main/papers/B13_boundary_folding_observation

BIG-B13.1 repository entry:

https://github.com/Jun-Lucis/BIG-theory/tree/main/papers/B13_1_rotated_basis_observation

B13 DOI:

https://doi.org/10.5281/zenodo.21072783

B13.1 DOI:

https://doi.org/10.5281/zenodo.21108338
