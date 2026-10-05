# Case study: B17 -> B18 — from local readable history to path-integrated readout

**Provenance status:** public-repository and archive verified.

## 1. B17 result

B17 separated **stored history** from **readable history**.

In its reduced moving-boundary model, later adaptive response was much better organized by the locally sampled retained-history load in the current moving-boundary frame than by global history summaries.

Representative values reported in the public BIG record include approximately:

```text
R^2 ~ 0.9940 for effective local load eta_S * m_local
R^2 ~ 0.8923 for global history mass
R^2 ~ 0.9002 for global history peak
```

in the cited positive-feedback regime.

This supported a local-readability interpretation inside that model.

## 2. B18.0 transfer limitation

B18 moved the readout idea into a different reaction-diffusion-inspired inhibitory front.

The B18 manuscript states explicitly:

> read-start local trace is insufficient

for organizing later front suppression in this new system.

Thus the B17-local variable did not simply transfer unchanged.

## 3. Successor redesign

B18.1 replaced the read-start snapshot with **path-integrated trace exposure**.

B18.2 then asked whether the relevant portion of that path exposure was specifically the trace overlapping the active front / interface core.

The B18.2 design note records the sequence explicitly:

```text
B18.0:
read-start local trace insufficient

B18.1:
path-integrated trace exposure much stronger

B18.2:
test active-front / interface-core weighted exposure
```

The integrated B18 interpretation became:

```text
stored history
-> locally readable history
-> path-readable history
-> interface-core path exposure
```

## 4. Methodological interpretation

This chain is valuable because a variable that worked well in one model was not treated as universal when it weakened in another.

The failure/limitation produced **state/readout enrichment**:

- **TRANSFER_LIMIT**
- **STATE_ENRICHMENT**
- **READOUT_OPERATOR_REDESIGN**
- **REPRESENTATION_REFINEMENT**

The later operator is not a rescue of the B17 local-readout result. It is a broader representation motivated by the transfer limitation.

## 5. General lesson

A successful predictor in one regime can become discovery data for a richer predictor when transferred elsewhere.

Failure preservation therefore applies not only to explicit FAIL verdicts but also to:

```text
previously successful variable
-> unsuccessful transfer
-> richer representation
```

This pattern later reappears in the more formal B25-B40 programme.

## Sources

B17 repository entry:

https://github.com/Jun-Lucis/BIG-theory/tree/main/papers/B17_readable_history

B18 repository entry:

https://github.com/Jun-Lucis/BIG-theory/tree/main/papers/B18_boundary_readout_operators
