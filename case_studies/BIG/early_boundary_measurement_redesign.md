# Case study: early boundary-measurement redesign

**Provenance status:** archive-verified from an early BIG concise preprint.

This is an early example in which an apparent breakdown was traced to the measurement representation rather than immediately interpreted as a failure of the local boundary law.

## 1. Apparent breakdown under radial measurement

An early BIG concise preprint reports that non-radial ellipse-source simulations initially appeared to break the quadratic boundary exponent when analyzed by naive radial averaging.

The reported apparent exponent was approximately:

```text
nu_radial ~ 2.63
```

For a genuinely non-radial boundary, however, global radial distance is not the natural local coordinate.

## 2. Change of measurement coordinate

The analysis was redesigned around local inward-normal coordinates and a fitted boundary offset,

```text
phi(s) ~ A (s + s0)^nu
```

After this change, the reported local exponent became:

```text
nu = 2.024 +/- 0.014
```

with amplitude-law agreement below 1% in the cited case.

The same early preprint also records that naive central-difference explicit schemes produced unstable or inconsistent boundary exponents, whereas conservative finite-volume schemes produced stable asymptotic behavior.

## 3. Methodological interpretation

This is not a formal modern PASS/FAIL lineage. It predates the later BIG verdict discipline.

It is nevertheless a useful **measurement-redesign** pattern:

```text
apparent contradiction
-> inspect geometry / numerical representation
-> identify inappropriate radial coordinate
-> redesign measurement in local normal coordinates
-> recover a stable local asymptotic description
```

Coding tags:

- `EARLY_NONSTANDARD_VERDICT`
- `MEASUREMENT_REDESIGN`
- `REPRESENTATION_REFINEMENT`
- `NUMERICAL_METHOD_DIAGNOSIS`

## 4. Why this matters for AI-assisted research

An AI system can easily rationalize an apparent numerical breakdown in many directions. The safeguard here is not rhetorical confidence but a more operational question:

> Is the observable being measured in a coordinate system that matches the geometry of the object?

The case illustrates why the micro AI–external-computation loop should include explicit checks of discretization and measurement representation, not only repeated runs of the same code.

## 5. Claim boundary

The case should not be summarized as "a failed simulation became a success."

A more accurate statement is:

> An apparent loss of quadratic behavior under one measurement representation motivated a geometrically better local measurement, which produced a different and more stable numerical description.

The original radial result remains evidence about the inadequacy of radial averaging for that non-radial geometry.
