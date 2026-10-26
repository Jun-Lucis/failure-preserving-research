# Beyond Failure Preservation: Research-Orientation Continuity for Long-Horizon Human–AI Science

**A rights-preserving design and evaluation proposal**  
**Jun Lucis — Independent Researcher**  
**Proposal v0.1 — 26 October 2026**

**Status:** Public discussion draft. The proposed architecture has not been tested in an independent controlled study. No claim of product implementation, superior scientific performance, or physical validation is made.

**Parent methodological paper:** [Failure-Preserving AI-Assisted Research](https://doi.org/10.5281/zenodo.23171698)  
**Parent methods repository:** [failure-preserving-research](https://github.com/Jun-Lucis/failure-preserving-research)  
**Longitudinal motivating case:** [Boundary Information Geometry (BIG)](https://github.com/Jun-Lucis/BIG-theory)

## Executive proposal

Research agents are becoming capable of carrying substantial scientific work through many successive steps. Yet two forms of continuity remain distinct:

1. **Operational continuity:** reliably recovering what was formulated, executed, checked, refuted, frozen, published, and left unfinished.
2. **Research-orientation continuity:** recovering **how and why the questions worth asking changed** through mathematical findings, failed hypotheses, human judgments, AI proposals, and conceptual reconsideration.

A searchable archive or durable chat summary is helpful, but neither by itself guarantees accurate recovery of either form of continuity. Retaining a researcher's original philosophy as an immutable preference can also be harmful: the direction of inquiry may legitimately change in response to evidence.

This note proposes **Research-Orientation Continuity (ROC)** as an additional, explicitly user-controlled capability for long-horizon AI-assisted research. An earlier working name for the architecture was *Evolving Research-Orientation Architecture (EROA)*. ROC is the design requirement; EROA is a possible implementation and evaluation framework, **not an established new scientific theory**.

The proposal is to store an **authoritative research state** and a separately **versioned, corrigible research-orientation record**, linked by auditable **research decision events**. Scientific judgments must remain governed by their mathematical or empirical evidence and predeclared protocols, not by the researcher's preferences or the AI's narrative.

## 1. Why this is not simply a longer memory

A researcher can retain all code, notebooks, failed tests, and manuscripts while still having to reconstruct a new agent's understanding after a context loss or session transition:

- Which version of a hypothesis is authoritative?
- Was a run completed, proposed, or blocked before opening outcomes?
- Which earlier FAIL must remain a FAIL?
- Did the research direction change because of new evidence, a human conceptual choice, an AI suggestion, or some combination?
- Is an earlier philosophical idea a current research question, a rejected interpretation, or merely historical motivation?
- What may the new agent read, infer, record, or disclose?

A single persistent user-preference profile cannot answer all these questions. Nor should an agent silently infer a person's philosophy from their conversation history.

## 2. Motivating experience and scope of evidence

The [published failure-preserving methodology](https://doi.org/10.5281/zenodo.23171698) describes micro-, meso-, and macro-level research loops: AI-assisted reasoning checked with external computation; frozen tests whose PASS/FAIL/INCONCLUSIVE/INVALID verdicts remain distinguishable; and reuse of prior limits and failures to design subsequent questions.

Its public [source and audit repository](https://github.com/Jun-Lucis/failure-preserving-research) includes claim-boundary tables, lineage protocols, supplementary cases, and a longitudinal BIG case. For example:

- [BIG-B41 case](../case_studies/BIG/B41_P2_failure_to_P3_fresh_test.md): a failed frozen scalar remainder claim is preserved; a newly formulated predictor is subsequently tested on fresh targets. The later PASS does not reclassify the earlier FAIL. The alternative scalar comparator also performed strongly, limiting any superiority claim.
- [Claim-boundary table](claim_boundary_table_v0_3.md): explicitly avoids treating the frequency of failure reuse as a causal productivity gain or general law.

The case also motivated a **qualitative** observation: later research questions need not simply refine the original intuition. Mathematical obstacles and unexpected response structures can motivate changes in what the researcher wants to investigate.

**Evidence boundary:** BIG is a single, deeply involved, self-documented research programme. It is valuable as an *origin story, requirements case, and source of counterexamples*, but **not** an unbiased or independent validation set for ROC/EROA. The correctness of BIG as a physical theory is not assumed and is not evaluated here. This proposal does **not** publish private chat transcripts or private philosophy archives.

## 3. An implementable separation of records

### 3.1 Authoritative research state

At a stage \(t\), let \(R_t\) contain the current hypothesis identifiers, formal protocols, preserved verdicts, source artifact references, dependencies, running/blocked status, and unresolved tasks.

A handoff should explicitly separate: **verified**, **reported but not independently rerun**, **hypothesized**, **refuted**, **inconclusive**, **blocked**, and **unknown**. The agent should report inaccessible artifacts rather than infer their contents.

### 3.2 Research-orientation record

Let \(\theta_t\) denote a **provisional, interpretable** description of the researcher's current question-selection orientation: scientific interests, conceptual concerns, unresolved interpretive tensions, and conditional preferences among legitimately testable research directions.

Do not treat \(\theta_t\) as a fixed psychological profile, as proof of the person's private beliefs, or as an objective statement about nature. Where appropriate, let the researcher correct, contest, disable, or erase an inferred orientation record within the applicable product controls and retention rules.

### 3.3 Research decision events

Proposed audit unit:

\[
E_k=(S_k,A_k,U_k,S_{k+1},O_k;P_k)
\]

Here \(S_k\) is the research state before the decision; \(A_k\) is the AI's presented alternatives; \(U_k\) is the human's intervention or choice (possibly none); \(S_{k+1}\) is the resulting research state; \(O_k\) is a later observable outcome; and \(P_k\) records provenance, timestamps, and the accessible evidence supporting each attribution.

The schema must allow **unknown, shared, or unresolvable authorship** of a conceptual move. A decision event can document temporal association; it does **not**, by itself, establish that a human intervention causally improved scientific performance.

### 3.4 Independent validity gate

Research orientation can shape the generation and ranking of questions, but it cannot redefine the success criterion of a frozen test after outcomes are seen. Schematic separation:

\[
q_{t+1}\sim\pi(q\mid R_t,\theta_t,H_t),\qquad
V_q=\mathcal E(D_q,P_q),
\]

where \(H_t\) is retained history, \(D_q\) the evidence for question \(q\), and \(P_q\) a predeclared evaluation protocol. **The scientific verdict does not depend on \(\theta_t\)**.

A proposed update \(\widetilde\theta_{t+1}\) should identify the evidence or interpretation that motivates it, the earlier position affected, competing readings, and whether the researcher approved it. Prior versions remain traceable.

## 4. Minimal product workflow

**Checkpoint:** At meaningful milestones, propose a compact, human-reviewable change to (i) the authoritative research-state record and (ii) a *separate* orientation/decision record. Nothing is silently promoted from a chat claim to scientific evidence.

**Handoff:** On a new chat, model, or execution environment, read the authorized records; verify their versions and artifact links; list unknowns, conflicts, pending work, and excluded private contexts; only then resume.

**Orientation review:** Instead of guessing at a stable personal philosophy, allow a user to see and change the *specific research-direction inferences* that might influence question generation.

**Counterproposal:** The agent should suggest genuinely different research directions when warranted by evidence, even when they challenge the current orientation. Persistent orientation should not become ideological lock-in or automatic agreement.

**Portability:** Prefer plain-text/structured export with stable source links and reviewable diffs. Provider-specific integrations should not make users dependent on a single conversational context or model.

**Checkpoint failure:** If a session terminates unexpectedly, preserve the last **confirmed** checkpoint, explicitly recording the gap to the last unconfirmed operation.

## 5. Participant rights are a prerequisite, not an appendix

Scientific research using real AI conversation histories can reveal unpublished research ideas and highly personal or sensitive information. Permission for a service to use conversations for model improvement **must not automatically be treated as informed permission** for granular profiling or public research on a person's intellectual history.

The following are requirements for any human-subjects evaluation of this proposal, subject to applicable law and institutional review:

- **Purpose-specific, voluntary informed consent** for this type of conversational analysis, with a comprehensible description of what will be inferred and used.
- **User control over scope:** which projects, periods, conversations, and artifacts may be analyzed; private material excluded by default.
- **Data minimization and access controls:** secure processing, retention limitations, separation of identifiers, and safeguards against re-identification.
- **Correction, objection, withdrawal, and deletion mechanisms** with clearly stated limits, including the treatment of already aggregated findings.
- **Intellectual property and attribution:** protect unpublished research, confidential collaborators, original ideas, and contributions by both participants and agents. Opt-in to participation must not be presented as a blanket transfer of rights.
- **No covert psychological classification:** research-orientation features are for a bounded research purpose, not inferred permanent personal beliefs or generalized eligibility decisions.
- **Independent oversight** and documentation of possible selection bias and downstream use.

Rights-preserving consent is necessary but not sufficient: sampling, evaluator independence, and the scientific validity of the proposed outcome measures still require scrutiny.

## 6. Proposed independent evaluation

**Do not use the BIG conversations as the primary confirmatory test data.** They informed the proposal, and both the investigator and the agents have already discussed the research hypothesis. Historical replay from the same programme is appropriate for debugging annotation rules, not confirming benefits.

A test with independently recruited and explicitly consenting research participants should compare, with matched research starting points, model access, retrieval conditions, task budgets, and assessment criteria:

| Arm | Handoff information |
| --- | --- |
| A | Authoritative scientific state only |
| B | A + static original research-orientation summary |
| C | A + latest reviewable orientation summary |
| D | A + versioned orientation revisions + provenance-linked decision events |
| E | A + matched-length irrelevant, shuffled, or otherwise non-informative decision history as a control |

**Primary outcomes:** (i) accuracy of verifiable state and decision recovery; (ii) changes in researcher correction burden and resumption time; (iii) blinded scientific quality and diversity of proposed next questions; and (iv) protocol/verdict errors. Track token and tool cost, unwarranted confidence, excessive agreement, and privacy failures.

**Evaluation design:** Preregister sampling, exclusion rules, annotator instructions, primary endpoints, and statistical analysis. Use genuinely future outcomes or held-out projects for confirmatory evaluation; do not present historical imitation of an already known choice as scientific discovery. Include paired or random assignment, inter-rater agreement, and checks for contamination by prior exposure. Report failed, null, and harmful effects.

**Falsifiable expectation:** Versioned decision history may improve recovery of evolving research objectives while increasing the risk of overfitting to past preferences. If blind quality, time, or burden do not improve under resource-matched conditions, reject the improvement claim even if personalization feels better.

## 7. Relation to existing proposals and work

This note **does not claim to invent persistent AI memory, experiment logs, preference learning, hypothesis revision, research journals, or human oversight**.

Some directly related public proposals and field reports include:

- [Persistent, Auditable Research Journals Across ChatGPT, Work, and Model Versions](https://community.openai.com/t/feature-request-persistent-auditable-research-journals-across-chatgpt-work-and-model-versions/1405456) (OpenAI Developer Community, 11 October 2026). Covers authoritative checkpoints, failures, provenance, and cross-session continuity.
- [Context-Aware Long-Term Memory and Reliable Conversation Continuity](https://community.openai.com/t/feature-proposal-context-aware-long-term-memory-and-reliable-conversation-continuity-in-chatgpt/1406633) (OpenAI Developer Community, October 2026). Covers persistent, user-controlled memory and contextual retrieval.
- [Scientific computing in the age of agentic AI](https://openai.com/index/scientific-computing-agentic-ai/) (OpenAI, 28 July 2026). Documents the increasing importance of human validation, orchestration, and long-term stewardship as coding agents improve.
- [Using thousands of AI agents to uncover new leads in biological data](https://openai.com/index/scaling-ai-research-for-complex-biological-data/) (OpenAI, 21 October 2026). Highlights AI-assisted generation of possible new scientific questions and prioritization of follow-up experiments.

**Potential additional contribution for evaluation:** track not only *which hypothesis changed*, or *what project state is authoritative*, but **how interactions among human direction-setting, agent proposals, negative evidence, and conceptual interpretation changed the criteria used to choose subsequent questions**. The value and distinctiveness of this added record are hypotheses to test, not established facts.

This is an invitation to compare adjacent designs and to revise or abandon ROC/EROA if other mechanisms already solve the problem more effectively.

## 8. Discussion questions for researchers and AI system designers

1. Which minimal decision-event fields are sufficient to restore research-direction choices without recreating a full private conversation?
2. Can a versioned orientation record improve scientific question quality **without** increasing confirmation bias or user-dependence?
3. Where should the product draw a boundary between helping the researcher select questions and asserting an independently valid scientific conclusion?
4. What explicit consent and technical safeguards are required before using conversational archives to investigate researchers' evolving thought processes?
5. Would this capability be better implemented as a generic opt-in project journal, an evaluation dataset, or a research-agent API rather than an always-on user memory?

## 9. Non-claims and invitation

This is **not** a new theorem derived from BIG, proof of human superiority over AI, causal evidence for productivity gain, demonstration of a universal research philosophy, or request to mine private conversations under a broad default training opt-in.

It is a bounded, falsifiable **research environment design proposal**, informed by a documented longitudinal case and intended to be evaluated on independent projects with participants' rights preserved.

Feedback is welcome, especially pointing to equivalent existing architectures, counterexamples, evaluation flaws, and safeguards omitted here.

---

**Citation and rights:** Parent scholarly materials in this repository are licensed as described in [LICENSE](../LICENSE), subject to any file-specific exceptions. This proposal contains no unpublished conversation transcript. Public links are included for attribution and evaluation only.
