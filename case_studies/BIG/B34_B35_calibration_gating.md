# Case study: B34-B35 calibration gates — failure before claim-bearing execution

**Provenance status:** archive-verified from the integrated B30-B36 preprint.

The later BIG programme contains an important class of "failure" that is distinct from a scientific FAIL verdict:

> a calibration or readiness gate can fail before a claim-bearing experiment is allowed to open.

This is methodologically important because it prevents exploratory tuning from being mistaken for prospective evidence.

## B34 calibration chain

The B34 transfer experiment was not opened immediately.

The recorded sequence was:

```text
P0
-> source tail overlaps near-source response
-> off-source transfer cannot be interpreted cleanly

P0R
-> compact source removes direct forcing-tail ambiguity
-> no non-source probe meets the frozen readability rule
-> B34.1 remains closed

P0S
-> revised probe construction
-> calculation valid and small-amplitude linearity passes
-> administrative readiness still fails
-> no B34.1 claim opened

P0T
-> change observable to normalized complex transfer kernel
-> reproducible spatial nonuniformity becomes readable

P0U
-> resolution and shifted-sampling readiness checks pass
-> B34.1 is finally authorized
```

The integrated preprint explicitly states that the calibration stages should not be read as establishing propagation, standing waves, resonance, a wave equation, or a dispersion relation.

The fresh B34.1 protocol then used new source orientations and periods. All nine fresh primary cells passed the frozen B34.1 rule.

## B35 calibration chain

B35 provides an even sharper example.

B35-P0 was numerically valid, but descriptive distance fits were weak.

B35-P0R extended the time window. The source response closed, but **no off-source probe satisfied the frozen closure rule**, so:

```text
administrative_ready_for_B35_1 = False
```

The programme did not lower the closure gate retrospectively.

Instead, it changed the timing observable.

B35-P0S then calibrated peak-time ordering and produced strong descriptive ordering, authorizing a fresh B35.1 protocol.

The important point is that B35.1 subsequently received the formal verdict:

`DISTANCE_ORDERED_APPROX_LINEAR_PEAK_TIMING_FAIL`.

Thus:

```text
failed calibration gate
-> redesign observable
-> calibration succeeds
-> fresh claim-bearing test opens
-> claim-bearing test still FAILS
```

This is unusually useful evidence against a "tuning until PASS" interpretation.

## Methodological classification

These chains belong to a distinct category:

- **PRECLAIM_GATING**
- **CALIBRATION_REDESIGN**
- **OBSERVABLE_REDESIGN**
- **NON_RETROACTIVE_THRESHOLDING**

They should be analyzed separately from formal scientific FAIL verdicts.

A calibration failure can be scientifically productive while still preventing a claim.

## General principle

A failure-preserving workflow should distinguish at least three states:

```text
1. readiness not achieved -> claim-bearing test must not open
2. claim-bearing test opened -> PASS / FAIL / INCONCLUSIVE / INVALID
3. later redesign -> new protocol with its own status
```

This matters especially in AI-assisted work, because an AI can cheaply generate many alternative observables and thresholds. Without a readiness boundary, that flexibility can become hidden post-hoc selection.

The B34-B35 record instead demonstrates a safer pattern:

> use flexible exploration before the freeze, but make the transition into claim-bearing evaluation explicit and auditable.

## Source

Integrated B30-B36 preprint and repository status records:

https://github.com/Jun-Lucis/BIG-theory/tree/main/papers/B30_B36_integrated_response_to_pulse_timing
