# Reference and adjacent-work verification — v0.1

**Date:** 6 October 2026  
**Target manuscript:** `paper/manuscript_v0_11.md`

## Purpose

This audit verifies the external references used in the methodology manuscript and rechecks the novelty boundary against closely adjacent 2026 AI-research systems.

The verification rule is simple:

- journal articles are checked against publisher or authoritative bibliographic pages where available;
- Center for Open Science items are checked against official COS pages;
- current AI-agent papers are treated as arXiv preprints unless a peer-reviewed venue is independently established;
- close conceptual overlap is used to narrow the manuscript claim rather than rhetorically distinguish the work.

## Reference verification

| # | Reference | Status | Verification / correction |
| --- | --- | --- | --- |
| 1 | Zhang et al. (2025), *Exploring the role of large language models in the scientific method: from hypothesis to discovery* | VERIFIED | npj Artificial Intelligence 1, 14; DOI 10.1038/s44387-025-00019-5 |
| 2 | Agrawal, McHale & Oettl (2026), *AI in Science* | VERIFIED | NBER Working Paper 34953; DOI 10.3386/w34953 |
| 3 | Hao et al. (2026), *Artificial intelligence tools expand scientists’ impact but contract science’s focus* | VERIFIED | Nature 649, 1237-1243; DOI 10.1038/s41586-025-09922-y |
| 4 | Curry et al. (2025), *Ending publication bias: A values-based approach to surface null and negative results* | VERIFIED | PLOS Biology 23(9), e3003368; DOI 10.1371/journal.pbio.3003368 |
| 5 | Rainford et al. (2026), *Knowledge preservation in the era of big science and AI: strategies for sustainable scientific research* | VERIFIED | Nature Communications 17, article 4069; DOI 10.1038/s41467-026-72667-3 |
| 6 | Soderberg et al. (2021), *Initial evidence of research quality of registered reports compared with the standard publishing model* | VERIFIED | Nature Human Behaviour 5, 990-997; DOI 10.1038/s41562-021-01142-4 |
| 7 | Center for Open Science, *Registered Reports* | VERIFIED | Official COS page; describes peer review before results are known and in-principle acceptance |
| 8 | Center for Open Science, *Preregistration* | VERIFIED | Official COS page; defines advance specification and planned/unplanned distinction |
| 9 | *Ten simple rules for writing a Registered Report* | **CORRECTION REQUIRED** | The manuscript incorrectly attributed this to Hardwicke et al. Correct authors: **Emma L. Henderson & Christopher D. Chambers (2022)**; PLOS Computational Biology 18(10), e1010571; DOI 10.1371/journal.pcbi.1010571 |
| 10 | Huber et al. (2020), *AiiDA 1.0...* | VERIFIED | Scientific Data 7, 300; DOI 10.1038/s41597-020-00638-4 |
| 11 | Lyu et al. (2026), *EvoScientist...* | VERIFIED AS PREPRINT | arXiv:2603.08127; persistent ideation memory records unsuccessful directions and experimentation memory stores reusable implementation knowledge |
| 12 | Liu et al. (2026), *The Last Human-Written Paper: Agent-Native Research Artifacts* | VERIFIED AS PREPRINT | arXiv:2604.24658; preserves an exploration graph including failures and reports that preserved failure traces can both accelerate and constrain later extension work |
| 13 | Wang et al. (2026), *Sibyl-AutoResearch...* | VERIFIED AS PREPRINT | arXiv:2605.22343; explicitly preserves positive and negative trial outcomes and formalizes trial-to-behavior conversion |

## Authoritative / primary verification URLs

- Ref. 1: https://doi.org/10.1038/s44387-025-00019-5
- Ref. 2: https://doi.org/10.3386/w34953
- Ref. 3: https://doi.org/10.1038/s41586-025-09922-y
- Ref. 4: https://doi.org/10.1371/journal.pbio.3003368
- Ref. 5: https://doi.org/10.1038/s41467-026-72667-3
- Ref. 6: https://doi.org/10.1038/s41562-021-01142-4
- Ref. 7: https://www.cos.io/initiatives/registered-reports
- Ref. 8: https://www.cos.io/initiatives/prereg
- Ref. 9: https://doi.org/10.1371/journal.pcbi.1010571
- Ref. 10: https://doi.org/10.1038/s41597-020-00638-4
- Ref. 11: https://arxiv.org/abs/2603.08127
- Ref. 12: https://arxiv.org/abs/2604.24658
- Ref. 13: https://arxiv.org/abs/2605.22343

## Novelty-boundary recheck

The closest overlap is stronger than a generic "persistent memory" comparison.

### EvoScientist

EvoScientist already uses persistent ideation and experimentation memory. Its ideation memory explicitly records unsuccessful directions so that later agents do not simply repeat them.

Therefore the methodology paper cannot claim novelty for:

```text
persistent scientific memory
or
remembering unsuccessful research directions
```

### Agent-Native Research Artifacts (ARA)

ARA explicitly argues that linear papers discard branching exploration and failed experiments, and it preserves an exploration graph and evidence grounding. It also reports that preserved failure traces can improve open-ended extension work while sometimes over-constraining a capable agent.

Therefore the methodology paper cannot claim novelty for:

```text
preserving the branching search tree
or
preserving failure traces for future agents
```

### Sibyl-AutoResearch

Sibyl is the closest methodological neighbor. It explicitly defines a trial-and-error harness that preserves positive and negative outcomes and routes lessons into later planning and validation. It also formalizes **trial-to-behavior conversion**, which is conceptually close to a source-result -> later-action lineage edge.

Therefore the methodology paper should **not** present the failure-salvage ledger, by itself, as a unique concept.

## Narrowed contribution after verification

The defensible contribution is the **combination and empirical instantiation** of several elements in a human-led longitudinal programme:

1. a real single-researcher human-AI computational case history rather than an autonomous-agent benchmark alone;
2. an explicit non-retroactivity rule preserving parent PASS / FAIL / INCONCLUSIVE / INVALID identities;
3. separation of retrospective diagnosis from newly frozen claim-bearing evaluation;
4. quantitative reconstruction of backward-link prevalence and artifact-timestamp source-to-successor latency in the case archive;
5. a nested micro / meso / macro architecture connecting external execution, frozen verdicts, and research-memory reuse;
6. an explicit experimental-handoff boundary for questions requiring new physical measurement.

This is narrower than "we invented failure-preserving research" and stronger because it is directly auditable.

## Required manuscript changes

- Correct reference 9 to Henderson & Chambers.
- Tighten Section 2.5 so that ARA and Sibyl overlap is stated explicitly.
- Remove any implication that a source-to-action ledger is unique.
- Present the present contribution as a human-led longitudinal case, non-retroactive verdict architecture, quantitative lineage audit, and experimental-handoff boundary.
- Keep references 11-13 labeled as preprints in the bibliography and discussion.

## Current verdict

```text
REFERENCE_METADATA: PASS after one correction
NOVELTY_BOUNDARY: PASS after narrowing
LITERATURE_OVERLAP: substantial but compatible with publication
```

The overlap does not remove the value of the paper. It changes the appropriate claim from "new concept of preserving failures" to "audited human-AI longitudinal implementation and quantitative lineage analysis of a failure-preserving research architecture."
