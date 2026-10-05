# Conceptual framework

## Central proposition

The proposed research architecture is based on a simple shift in the economics of computational research:

> AI may reduce the marginal cost of generating, implementing, checking, and revisiting numerical experiments, while disciplined retention can give failed exploration nonzero future value.

This proposition is narrower than "AI automates science." It depends on external execution, explicit verdicts, retained history, and later re-use.

## Six methodological components

1. **Expanded research bandwidth**  
   AI assists with formulation, coding, debugging, numerical planning, comparison, and documentation. The relevant quantity is not raw FLOPS alone but the amount of executable research a single person can design and inspect.

2. **Freedom to fail**  
   Individual research can sometimes tolerate exploratory branches that would be difficult to justify when they consume a team's shared labor budget.

3. **Failure preservation**  
   Parameters, code, outputs, verdicts, diagnostics, and invalid/inconclusive outcomes are retained rather than compressed into only successful end states.

4. **Failure salvage**  
   Earlier failures can later constrain the search space, reveal missing variables, motivate decomposition, or provide archived computational assets.

5. **AI–external computation feedback**  
   AI reasoning is repeatedly exposed to independently executed numerical calculations. The calculation can contradict the narrative and force revision.

6. **Experimental handoff**  
   Public data and simulation have a frontier. When the decisive measurement does not exist, the next step belongs to laboratories, organizations, instruments, and domain experts.

## History-bearing research

Let

```text
R_t = {hypotheses, verdicts, parameters, outputs, code, diagnostics}_0:t
```

denote the retained research state up to stage `t`.

A stylized update is

```text
Q_(t+1) = G(Q_t, R_t)
```

rather than `Q_(t+1)=G(Q_t)`.

The distinction matters because a later question can depend on information that was generated under an earlier hypothesis that failed.

## Discovery data versus validation data

A central integrity rule is:

- archived data used to invent or refine a replacement hypothesis are **discovery data**;
- a replacement claim must be tested on a new frozen or otherwise explicitly held-out evaluation if it is to count as prospective evidence.

A historical FAIL may therefore become useful without becoming a retroactive success.
