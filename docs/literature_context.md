# Literature context and positioning

**Working literature review — 5 October 2026**

This note positions the failure-preserving research architecture against adjacent work. It is intentionally conservative: the project should not claim that preserving failures, preregistering tests, recording provenance, or using persistent AI research memory are individually new ideas.

## 1. AI across the scientific workflow

Recent literature already treats AI as an augmentation layer across multiple stages of science.

Zhang et al. (2025), *Exploring the role of large language models in the scientific method: from hypothesis to discovery*, reviews LLM involvement from hypothesis formation through experimental design, analysis, and discovery, while emphasizing human alignment and evaluation.

- DOI: https://doi.org/10.1038/s44387-025-00019-5

Agrawal, McHale, and Oettl (2026), *AI in Science*, frame AI as augmentation of search over combinatorial spaces and emphasize a "jagged frontier": returns differ across domains and workflow stages, while human judgment remains important.

- NBER Working Paper 34953
- DOI: https://doi.org/10.3386/w34953

Hao et al. (2026), *Artificial intelligence tools expand scientists’ impact but contract science’s focus*, report observational evidence that AI-augmented scientists gain individual professional advantages while scientific topic coverage may narrow collectively. This is relevant because higher individual bandwidth should not automatically be equated with broader or better science.

- DOI: https://doi.org/10.1038/s41586-025-09922-y

**Position of this project:** the present architecture does not attempt to model the full AI-science ecosystem. It focuses on a narrower unit: how one individual computational research programme can structure repeated AI-assisted reasoning, external execution, retained failures, and later reuse.

## 2. Negative and null results

The value and under-publication of negative results are established concerns.

Curry et al. (2025), *Ending publication bias: A values-based approach to surface null and negative results*, argues that null and negative results remain systematically under-shared and proposes coordinated changes across funders, institutions, publishers, societies, and researchers.

- PLOS Biology 23(9): e3003368
- DOI: https://doi.org/10.1371/journal.pbio.3003368

Rainford et al. (2026), *Knowledge preservation in the era of big science and AI: strategies for sustainable scientific research*, goes further and explicitly discusses failed attempts, unstable computational models, parameter sensitivity analyses, tacit knowledge, and scientific failure as preservation problems. It argues that knowledge of what did not work can prevent duplicated effort and support future research.

- Nature Communications 17, 4069 (2026)
- DOI: https://doi.org/10.1038/s41467-026-72667-3

**Position of this project:** the novelty is not the claim that negative results have value. The narrower contribution is to model **how a retained negative result changes a later research action**, using an auditable longitudinal ledger of source verdict -> salvage operation -> successor question -> fresh validation.

## 3. Preregistration and Registered Reports

The distinction between exploratory and confirmatory evidence is also well established.

Registered Reports evaluate questions and methods before outcomes are known, thereby reducing outcome-dependent publication and making negative results publishable by design. Soderberg et al. (2021) found that Registered Reports were rated higher than comparison papers on multiple dimensions of rigor and overall quality.

- Soderberg et al. (2021), Nature Human Behaviour 5, 990–997
- DOI: https://doi.org/10.1038/s41562-021-01142-4

The Center for Open Science describes preregistration as a mechanism for making the exploratory/confirmatory distinction explicit. PLOS guidance for Registered Reports similarly stresses that data-dependent exploratory analyses should be labelled exploratory and later subjected to confirmatory testing.

- COS Registered Reports: https://www.cos.io/initiatives/registered-reports
- COS Preregistration: https://www.cos.io/initiatives/prereg
- PLOS Computational Biology: https://doi.org/10.1371/journal.pcbi.1010571

**Position of this project:** the BIG workflow's "freeze -> verdict -> redesign -> new freeze" principle is aligned with preregistration logic. The additional object of study is the **post-failure lineage**: how an immutable failed test is allowed to influence later exploration without being retroactively upgraded.

## 4. Computational provenance

Scientific workflow systems already show that complete computational lineage can be represented as a graph.

AiiDA records calculation inputs, outputs, processes, and transformations in provenance graphs and supports high-throughput reproducible computational workflows.

- Huber et al. (2020), *AiiDA 1.0, a scalable computational infrastructure for automated reproducible workflows and data provenance*
- Scientific Data 7, 300
- DOI: https://doi.org/10.1038/s41597-020-00638-4

**Position of this project:** provenance systems primarily answer "where did this result come from?" The failure-preserving architecture adds a research-decision layer: "how did this negative result alter the next hypothesis, protocol, or representation?" The proposed failure-salvage ledger is therefore closer to a provenance graph over **research decisions and claim scope**, not only over calculations.

## 5. Persistent memory in AI research systems

This area has moved rapidly in 2026 and directly overlaps with parts of the present proposal.

Lyu et al. (2026), *EvoScientist*, introduces persistent ideation and experimentation memory, including records of unsuccessful directions, to help multi-agent research systems avoid repeating infeasible paths.

- arXiv:2603.08127
- https://arxiv.org/abs/2603.08127

Liu et al. (2026), *The Last Human-Written Paper: Agent-Native Research Artifacts*, argues that conventional papers flatten branching research histories and discard failures. Its Agent-Native Research Artifact preserves scientific logic, executable code, an exploration graph, and evidence records. It reports that preserved failure traces can accelerate later agent work, while also warning that inherited failures can constrain exploration.

- arXiv:2604.24658
- https://arxiv.org/abs/2604.24658

Wang et al. (2026), *Sibyl-AutoResearch*, explicitly proposes Scientific Trial-and-Error Harnesses that preserve positive and negative outcomes and route them into later planning, validation, claim scope, and system repair.

- arXiv:2605.22343
- https://arxiv.org/abs/2605.22343

**Position of this project:** these works mean that "persistent research memory" or "preserve failed trials" should not be claimed as unique. The distinctive contribution here is instead:

1. a **human-led, single-researcher longitudinal case study**, rather than a primarily autonomous-agent architecture;
2. a three-scale structure separating micro AI/external-execution feedback, meso frozen verdict/redesign, and macro research-memory salvage;
3. an explicit **non-retroactivity rule** for scientific verdicts;
4. an empirical **failure-salvage ledger** linking old negative results to later theory changes and fresh tests;
5. an **experimental handoff boundary** that treats unavailable real-world measurements as a structural limit of individual computational research;
6. a route from private intuition to public testability that is framed as increased exposure to falsification, not validation of the intuition itself.

## 6. Current novelty claim

The safest working claim is therefore not:

> "We introduce the first system to preserve scientific failures."

That would be false or at least unsupportable in 2026.

A defensible claim is:

> **We present a longitudinal human–AI case study and an auditable nested architecture for converting retained computational failures into later research actions without retroactively changing their original verdicts.**

A stronger but still plausible formulation for later validation is:

> **The contribution is the explicit coupling of prospective verdict immutability, failure-to-action lineage, and fresh-test separation across micro, meso, and macro research timescales in an individual AI-assisted computational programme.**

## 7. Important tension: memory can help and constrain

The literature also supplies an important caution.

The Agent-Native Research Artifact work reports that preserved failure traces can accelerate extension tasks but can also constrain a capable agent to remain inside the prior exploration box. This is directly relevant to the present method.

Therefore failure preservation should not imply:

```text
old FAIL -> permanently forbidden direction
```

Instead, the archive should preserve:

```text
what failed
under which representation
under which protocol
at which resolution / domain
with what integrity status
```

A conceptual pivot is allowed to revisit the same raw region under a new question. This is exactly why the BIG case distinguishes historical verdict from later usefulness.

## 8. Research gap this repository can test

The most useful empirical question is no longer whether failures should be preserved.

It is:

> **Can we reconstruct, from a real longitudinal human–AI research programme, when and how retained failures measurably changed later research decisions?**

The failure-salvage ledger is designed to answer that question.

Potential measurable quantities include:

- number of stages with explicit backward links to prior FAIL/INCONCLUSIVE/INVALID results;
- salvage latency in phases or days;
- salvage type frequency;
- whether a successor used fresh validation data;
- whether the parent verdict remained unchanged;
- whether reuse narrowed, decomposed, enriched, or changed the representation;
- whether the relative rate of historical-data reuse increased as the programme matured.

These quantities would move the paper from a methodological essay toward a documented longitudinal case study.
