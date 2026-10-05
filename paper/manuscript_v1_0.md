# Failure-Preserving AI-Assisted Research

## A Nested Research Architecture for Individual Computational Science

### A longitudinal case study from Boundary Information Geometry

**Jun Lucis**  
Independent researcher

**Preprint v1.0 — 6 October 2026**

**DOI:** 10.5281/zenodo.23171698

## Author note

The author conducts this work as an independent researcher outside the scope of his primary employment. His primary professional role is non-technical and unrelated to the research described here. This research is not part of the author's employer's research activities and was conducted without employer-provided research funding, research supervision, or institutional research infrastructure. The research used only personally controlled resources and accounts, including a personal computer, personal Google/Colab, GitHub, ChatGPT, and cloud accounts, together with publicly available data. No employer-controlled computing resources, proprietary data, confidential information, or employer-provided research facilities were used. Human research activity was performed primarily during personal time, while some long-running computations continued unattended during periods when the author was sleeping or otherwise away from active research.

*Post-publication clarification: this author note was added after the initial Zenodo publication. No scientific claims, numerical results, verdicts, or audit statistics were changed.*

---


## Abstract

Recent reasoning-capable AI systems can substantially expand the amount of mathematical formulation, code generation, debugging, parameter exploration, comparison, and documentation that one individual researcher can carry out. The methodological consequence may be deeper than acceleration alone. When exploratory computation becomes cheaper to generate and when failed runs are systematically retained, the expected future value of failure can change.

This paper proposes a failure-preserving research architecture derived from a longitudinal individual computational research programme. The architecture contains three nested cycles. At the micro scale, AI-assisted reasoning alternates with externally executed numerical computation, so that equations and interpretations are repeatedly exposed to outputs not generated inside the conversational reasoning loop. At the meso scale, hypotheses are prospectively frozen, evaluated, assigned retained verdicts such as PASS, FAIL, INCONCLUSIVE, or INVALID, and replaced only through separately named redesigns. At the macro scale, the accumulated history of failed, limited, and successful experiments becomes a research-memory state that can later be re-read to constrain new hypotheses or support conceptual changes. A fourth component, experimental handoff, marks the boundary at which public data and simulation are insufficient and new measurements require laboratories, organizations, equipment, and domain expertise.

Boundary Information Geometry (BIG) is used as a case study of the process, not as a premise of the methodology. In the currently standardized B19-B40 coding pass, 25 negative or limiting source stages were identified and 22 had an explicit downstream backward link; this 88% figure is treated only as a descriptive statistic of the coded programme interval. An earlier audit version reported 84%; the change reflects recovery of one source-backed B29-T1-to-B30 lineage edge, not a changed verdict rule. A separate temporal audit finds higher observed backward-link prevalence in the later coded epoch (12/12 versus 10/13) but no statistically persuasive increase, while 14 comparable artifact-timestamp transitions have a median source-result-to-successor-freeze interval of about 1.20 h and show no evidence of shortening over time. Several documented sequences show retained negative results later contributing to model redesign without retrospective reclassification. One especially clear example is a failed constant-density boundary-functional transfer whose archived profiles motivated a retrospective coarea analysis and a new level-resolved predictor that was then tested prospectively on fresh held-out cases. A later timing sequence illustrates a broader representational pivot: repeated failure and numerical fragility of absolute timing quantities motivated a change toward relative and relational observables, followed by newly frozen prospective tests.

The paper does not claim that AI removes scientific error, that every failure is valuable, or that individual computational work replaces experimental science. Its narrower proposal is that AI-assisted research can increase individual research bandwidth while disciplined failure preservation converts part of the historical search path into a reusable scientific asset.

---

## 1. Introduction

A large fraction of research effort is normally invisible in the final paper. Unsuccessful parameterizations, abandoned observables, numerically invalid experiments, hypotheses that failed cleanly, and intermediate diagnostic calculations are often compressed into a short methods narrative or omitted entirely.

This compression is understandable. Research time is expensive. In organized science, a failed computational branch consumes salaries, shared attention, compute, deadlines, and explanation costs. A rational research group therefore has incentives to restrict exploration and to concentrate resources on paths with a plausible chance of producing useful results.

Independent research has the opposite asymmetry. An individual researcher may have considerable freedom to pursue unlikely paths, but historically lacked the human bandwidth required to implement, debug, scan, inspect, document, and revise a large numerical programme.

Reasoning-capable AI changes this balance. The relevant change is not simply that code can be written faster. A single researcher can potentially coordinate a larger fraction of the research pipeline: formulation, derivation, implementation, debugging, numerical experiment design, data organization, comparison, and writing. In this sense, the effective research bandwidth of the individual can increase even when the underlying compute hardware is ordinary.

This creates a methodological possibility. If the marginal cost of an exploratory computational branch falls while the output of that branch is retained, failure need not be modeled only as lost time. A failed experiment may later serve as a computational asset, a counterexample, a constraint on a hypothesis family, a signal of a missing state variable, or the raw material for a conceptual change.

The central proposal of this paper is therefore:

> AI-assisted computational research can change not only the cost of successful experiments but also the economics and future value of failed experiments.

This is not a claim that failure is intrinsically good. Most failures may remain uninformative. Nor is it a claim that AI-generated reasoning is reliable. The architecture described here depends on repeated exposure of AI-assisted reasoning to externally executed computation, explicit freezing of claim-bearing tests, retention of negative verdicts, and separation between retrospective discovery and prospective validation.

The paper develops the architecture as three nested cycles: a micro AI–external-computation loop, a meso prospective test–redesign loop, and a macro failure-salvage and research-memory loop. It then adds an experimental handoff layer to identify where individual AI-assisted computational research reaches the boundary of available physical evidence.

The primary case study is Boundary Information Geometry (BIG), a long-running boundary-centered mathematical and numerical research programme. The scientific validity of BIG is not assumed here. Indeed, the usefulness of the case study partly comes from the fact that its archive contains PASS, FAIL, INCONCLUSIVE, invalid, diagnostic, and replacement stages rather than a success-only record.

---

## 2. Relation to prior work

The individual components of this architecture have substantial precedents, and the present contribution should not be described as the first proposal to preserve failures, preregister hypotheses, record provenance, or use persistent memory in AI-assisted research.

### 2.1 AI-assisted scientific work

Recent work already treats AI as an augmentation layer across multiple stages of science. Zhang et al. (2025) review LLM use from hypothesis formation through experimental design and analysis. Agrawal, McHale, and Oettl (2026) describe a "jagged frontier" in AI for science, with returns differing across domains and workflow stages and human judgment remaining an important complement. Hao et al. (2026) report a related caution at ecosystem scale: AI-augmented researchers show substantial individual advantages while the collective topical range of science may narrow.

The present paper therefore does not claim that AI-assisted research itself is new. Its narrower object is the longitudinal organization of a single computational programme in which AI-assisted reasoning, external execution, prospective verdicts, and research-memory reuse are coupled explicitly.

### 2.2 Negative and null results

The scientific value and systematic under-reporting of negative results are long-established concerns. Curry et al. (2025) argue for coordinated mechanisms to surface null and negative findings. Rainford et al. (2026) explicitly frame failed experiments, unstable computational models, parameter studies, and tacit know-how as knowledge-preservation problems whose loss wastes resources and encourages duplicated effort.

Accordingly, the novelty claim here is not that failures can be useful. The more specific question is whether one can reconstruct an auditable chain

```text
retained negative result
-> later research action
-> redesigned question
-> fresh evaluation
```

inside a real longitudinal human-AI programme.

### 2.3 Preregistration and Registered Reports

The meso-scale freeze/verdict/redesign cycle is closely aligned with preregistration and Registered Reports. These practices make the distinction between exploratory and confirmatory analyses explicit and reduce outcome-dependent publication. Soderberg et al. (2021) found Registered Reports to be rated more highly than comparison papers on multiple dimensions of rigor and overall quality.

The additional object studied here is what happens **after** a negative frozen test: the parent verdict is retained, later diagnostics are marked as exploratory or calibration work, and any replacement claim receives a new frozen evaluation.

### 2.4 Computational provenance

Workflow systems such as AiiDA demonstrate that complex calculations can be represented with detailed provenance linking inputs, processes, and outputs. That literature largely answers the question "how was this result generated?"

The failure-salvage ledger proposed here adds a research-decision layer:

> How did this result change the next hypothesis, protocol, representation, or claim boundary?

The intended provenance object is therefore not only a graph of computations, but a graph of scientific decisions and retained verdicts.

### 2.5 Persistent memory and failure conversion in AI research systems

The overlap is strongest with a rapidly developing 2026 literature on persistent research memory and explicit trial-to-action conversion.

EvoScientist uses persistent ideation and experimentation memory; its ideation memory explicitly records previously unsuccessful directions. Agent-Native Research Artifacts (ARA) preserve branching exploration and failed traces rather than flattening them into a success-only paper, and report that preserved failure traces can both accelerate later extension work and constrain a capable agent if the old search history anchors it too strongly. Sibyl-AutoResearch is still closer to the present process architecture: its trial-and-error harness preserves positive and negative outcomes and formalizes **trial-to-behavior conversion**, linking trial signals to later research actions.

These developments mean that none of the following should be claimed as unique here:

```text
persistent scientific memory
preservation of unsuccessful directions
failure-trace retention
or
a generic result-to-later-action relation
```

The narrower contribution of the present paper is the combination and empirical instantiation of these ideas in a **human-led, single-researcher longitudinal computational programme** with:

1. an explicit **non-retroactivity rule** preserving parent PASS / FAIL / INCONCLUSIVE / INVALID identities;
2. separation of retrospective diagnosis from newly frozen claim-bearing evaluation;
3. a nested micro / meso / macro architecture linking AI-execution feedback, frozen-verdict redesign, and research-memory reuse;
4. a quantitative archive audit of backward-link prevalence and source-result-to-successor-freeze latency;
5. an explicit experimental-handoff boundary where missing physical evidence requires organized experimental science.

The failure-salvage ledger is therefore treated as an audit instrument in this case study, not as a uniquely invented data structure.

A further caution follows from ARA and related agent-memory work: preserved failure traces can be useful without being universally beneficial. A failure record must preserve **where, under what protocol, and for what claim** the direction failed. Otherwise research memory can harden a local negative result into an unjustified global prohibition.

---

## 3. A three-scale research architecture

![Figure 1. Nested architecture of failure-preserving AI-assisted research.](../figures/nested_cycles_v0_1.svg)

**Figure 1. Nested architecture of failure-preserving AI-assisted research.** At the micro scale, AI-assisted reasoning is repeatedly exposed to externally executed numerical computation. At the meso scale, hypotheses are prospectively frozen and assigned persistent verdicts before redesign. At the macro scale, the retained archive becomes a research-memory state from which earlier negative or limiting outcomes can be retrieved as discovery data. Experimental handoff marks the boundary at which decisive evidence requires new physical measurements.

### 3.1 Micro scale: AI–external computation

The smallest repeated unit is

```text
question
-> AI-assisted formulation
-> equation / code
-> external execution
-> numerical output
-> reconsideration
-> revised formulation
```

The key design feature is separation between the reasoning environment and the executable environment.

In the case study, equations and computational proposals generated or refined in conversation were repeatedly implemented and run externally in simple Python/Colab workflows. This does not make the numerical output independent of the researcher, because the researcher and AI still chose the model and code. It does, however, prevent verbal coherence inside the reasoning system from functioning as the final test of its own claims.

A wrong sign, nonexistent crossing, unstable scaling law, unexpected bifurcation, resolution sensitivity, or code failure is returned as an external constraint. The reasoning process must then account for the output rather than simply continue a persuasive internal narrative.

The value of simple code is important. When possible, keeping the mapping

```text
equation <-> code <-> numerical output
```

inspectable reduces the number of hidden transformations between the hypothesis and its computational consequence.

The micro loop does not guarantee correctness. Its purpose is narrower: to make sustained internally consistent error harder by repeatedly forcing the current formulation into an executable form.

### 3.2 Meso scale: prospective test and redesign

The second scale operates across complete experiments rather than individual calculations.

```text
hypothesis
-> predeclaration / freeze
-> claim-bearing run
-> retained verdict
-> diagnosis
-> redesigned hypothesis
-> new freeze
```

A crucial rule is that the parent verdict remains fixed. If a frozen protocol fails, the result remains a FAIL even if later diagnostics reveal why it failed. If a protocol is numerically invalid, its descriptive outputs may be retained, but they are not promoted to a scientific PASS or FAIL beyond what the predeclared rules allow.

This creates a lineage such as

```text
P1 -> FAIL
P1A -> diagnostic only
P2 -> PASS
```

rather than rewriting the lineage as

```text
P1 -> PASS after adjustment
```

The distinction matters because a successful successor test otherwise risks concealing the degree to which the hypothesis changed after the data were seen.

### 3.3 Macro scale: failure salvage and research memory

The third scale appears only after many experiments have accumulated.

Let

```text
R_t = {hypotheses, verdicts, parameters, outputs, code, diagnostics}_0:t
```

represent the retained research state at time `t`.

A conventional simplified picture of research might treat the next question as a function mainly of the current accepted model:

```text
Q_(t+1) = G(Q_t).
```

The failure-preserving picture is instead

```text
Q_(t+1) = G(Q_t, R_t).
```

The archive is not merely administrative. Earlier failures can become active inputs to later theory construction.

This reuse can occur at several levels. Cached computations can be reused directly. A failed law can remove a region of hypothesis space. A pattern of residuals can reveal that two contributions should be separated. A failed transfer can identify a boundary of applicability. More radically, a cluster of failures can become intelligible only after a change of observable or representation.

The last case is termed **representational salvage** in this paper.

A central integrity condition follows immediately. If archived failures are read in order to construct a new representation, those data are discovery data for the new representation. They cannot simultaneously be counted as independent validation. Claim-bearing support must therefore come from a new frozen or genuinely held-out test.

---

## 4. Failure as a reusable research object

The architecture distinguishes the historical verdict of an experiment from its later scientific usefulness.

A result can satisfy

```text
historical verdict = FAIL
later usefulness > 0
```

without contradiction.

This distinction yields a working salvage taxonomy:

- **computational reuse** — reuse of cached trajectories, profiles, roots, gradients, or scans;
- **constraint reuse** — a negative result removes part of the search space;
- **model redesign** — failure shape motivates a new equation;
- **state enrichment** — failure suggests missing history, geometry, path, or another state variable;
- **explanatory-variable change** — the same pattern is reconsidered under a different descriptive quantity;
- **decomposition** — a failed one-law description becomes a structured sum or factorization;
- **protocol repair** — a design problem is localized and a new protocol is independently frozen;
- **limit localization** — a broad failure gives way to a narrower surviving structure;
- **representational salvage** — multiple archived failures become informative after a conceptual pivot.

The repository accompanying this paper maintains an explicit failure-salvage ledger so that these categories can be audited rather than inferred only from retrospective narrative.

![Figure 2. Failure-salvage spiral.](../figures/failure_salvage_spiral_v0_1.svg)

**Figure 2. Failure-salvage spiral.** Historical failures are not reclassified as successes. They remain fixed outcomes while retained data and diagnostics may later influence a new hypothesis. If old data participate in redesign, they are discovery data; claim-bearing support for the replacement hypothesis requires a separately identified fresh or held-out evaluation.

### 4.1 Standardized lineage audit and sensitivity

A first stage-level coding pass has been completed for B19–B40. The current table contains 60 stage-like records, of which 57 are claim-bearing. Under a broad operational dictionary that includes formal FAIL, INVALID, INCONCLUSIVE, NOT_SUPPORTED, NOT_REALIZED, the B29 training-domain `T1_valid=False` status, and the B19 no-robust-scalar negative structural result, 25 records act as negative or limiting source stages.

A source was counted as explicitly reused only when a later coded stage named that source in its `inherited_from` field. In audit v0.3, 22 of 25 source stages have an explicit downstream backward link, an observed fraction of 88.0%. Audit v0.2 had reported 21/25 = 84%; rereading the integrated B30-B36 source recovered an explicit statement that B30 was frozen as a successor to the B29-T1 training-domain readability failure. The old table and value remain preserved, while v0.3 records the recovered edge.

This number should not be interpreted as a general "value of failure" estimate. The stages are not independent, the coding vocabulary evolved over time, later stages have less follow-up opportunity, and the current audit begins at B19 rather than at the beginning of BIG. Several unlinked outcomes are also deliberate terminal or closeout results. The statistic is useful for a narrower reason: it demonstrates that a success-only archive would discard information that is explicitly connected to a large fraction of later research actions in this programme.

The stronger hypothesis that failure reuse increased over time remains untested. The coding protocol is now frozen and status-definition sensitivity analyses have been performed, but a temporal trend requires dated lineage edges because B-number order does not reliably represent execution chronology.

The public coding table and audit notes are maintained in the companion repository.

The primary broad result is accompanied by three sensitivity views. A strict denominator containing formal FAIL, NOT_SUPPORTED, and the clean B19 negative structural result gives 14/16 = 87.5%. Excluding two explicit terminal/closeout sources from the broad denominator gives an opportunity-adjusted 22/23 = 95.65%. Coarse B-family aggregation gives 15/16 = 93.75% when a group counts as reused if any source is reused, but 13/16 = 81.25% when every broad negative source in the group must be reused. The named-stage 88.0% result remains the primary descriptive value because it preserves individual verdict and protocol identities.

![Figure 3. Sensitivity of the B19-B40 explicit backward-link fraction.](../figures/lineage_sensitivity_v0_1.svg)

**Figure 3. Lineage-audit sensitivity.** The broad named-stage 88.0% value is the primary descriptive statistic. The strict, B-family, and opportunity-adjusted bars use different denominators and are shown only to assess sensitivity of the qualitative conclusion; they are not interchangeable estimands or estimates of a universal failure-reuse rate.

### 4.2 Exploratory temporal-development audit

The archive also permits a limited test of the impression that failure reuse became more systematic as the programme matured. Two distinct quantities must be separated:

```text
reuse prevalence = how often a retained limitation is explicitly linked to later work
reuse latency    = how long until a separately frozen successor action appears
```

#### Prevalence

A retrospective structural split is placed at the documented B19-B26 programme closeout and opening of B27. Under the broad negative/limiting dictionary:

```text
B19-B26: 10 / 13 reused = 76.9%
B27-B40: 12 / 12 reused = 100%
```

Wilson 95% intervals are approximately 49.7-91.8% and 75.8-100%, respectively. An exploratory Fisher exact test gives a two-sided p-value of about 0.220 and a one-sided p-value of about 0.124.

The direction is compatible with increasing reuse prevalence, but the sample is too small to establish an increase. Documentation is also a major confound: later stages more consistently record frozen identities, persistent verdict strings, machine-readable protocols, and explicit backward links.

#### Latency

A second provenance pass recovered timestamps from retained run artifacts, including result summaries, frozen configuration files, protocol snapshots, and explicit "frozen before fresh trajectory" sentinels. Fourteen source-to-successor transitions are sufficiently comparable for an exploratory latency analysis.

Across those 14 transitions:

```text
median latency = 1.199 h  (~1 h 12 min)
IQR            = 0.493-2.032 h
range          = 0.205-5.732 h
```

Several successor freezes appeared within an hour of the retained source result, while others took approximately five to six hours.

There is, however, no evidence that these intervals shortened over chronological time:

```text
Spearman rho = 0.0505, p = 0.8637
Kendall tau  = 0.0110, p = 1.000
```

A simple pre-/post-1-October split also does not support faster later reuse: the median is approximately 0.692 h in the earlier subset and 1.590 h in the later subset; a one-sided Mann-Whitney test for "later is faster" gives p approximately 0.697.

These timestamps are provenance markers, not direct measurements of reasoning time. They may include pauses, unrelated work, file-write delays, and unrecorded intermediate reasoning.

The temporal-development result is therefore narrower than the initial intuition:

> Explicit backward linkage is descriptively more prevalent in the later coded epoch, but neither an increase in reuse prevalence nor an acceleration of reuse latency is established.

The stronger interpretation is procedural rather than temporal: later stages make the research-memory relation more explicit and auditable.

A supplementary latency figure and source table are maintained in the companion repository. Private Drive URLs and file IDs are not published; only artifact names, timestamps, and provenance classes are recorded.

### 4.3 Preclaim gating

Not every useful failure occurs after a scientific hypothesis has entered a claim-bearing test.

A calibration stage can fail a readability, resolution, closure, sampling, or implementation gate before a prospective claim is allowed to open. This is methodologically distinct from a scientific FAIL verdict.

The architecture therefore distinguishes:

```text
calibration / readiness failure
-> redesign before claim-bearing freeze
-> readiness achieved
-> fresh claim-bearing test
-> PASS / FAIL / INCONCLUSIVE / INVALID
```

This distinction matters particularly in AI-assisted research. AI can cheaply propose many alternative observables, thresholds, and parameterizations. If the transition from flexible calibration to claim-bearing evaluation is not explicit, that flexibility can become hidden post-hoc selection.

The later BIG record contains examples in which a failed readiness gate blocked the claim-bearing stage, the observable or protocol was redesigned, and the later fresh test was still allowed to FAIL. Those cases are treated separately from the 88% source-stage statistic.

---

## 5. Longitudinal case study: Boundary Information Geometry

### 5.1 Status of the case study

BIG is a mathematical and numerical research programme organized as a sequence of B-series studies. The programme has progressively adopted prospective freezes, explicit verdict rules, recovery audits, held-out tests, and retained negative outcomes.

This paper uses those records only to study research process. A disciplined process does not establish that BIG is a correct physical theory.

![Figure 4. Selected failure-salvage lineages in the BIG case study.](../figures/big_salvage_lineage_v0_1.svg)

**Figure 4. Selected audited BIG failure-salvage lineages.** Arrows indicate downstream influence or succession, not retrospective upgrading of the parent verdict. The examples show multiple roles for retained negative or limiting outcomes: external transfer, predictor redesign, state enrichment, explanatory-variable change, representational salvage, protocol repair, and limit localization.

### 5.2 Early pre-standardization cases

Several earlier BIG records exhibit the same basic process before the later PASS/FAIL/freeze vocabulary was standardized. They are therefore treated as supplementary `EARLY_NONSTANDARD_VERDICT` cases rather than mixed directly into the B19-B40 quantitative statistic.

First, a retained B6 dense scan was later reused in a crossing-only analysis rather than rerunning the full PDE. The recovered archive contains an explicit `B6_4_input_B6_3_summary.csv` followed by `B6_4_crossing_summary.csv`. The latter reports a bootstrap estimate `m_c ~ 0.64911` with a 95% interval of approximately `0.64566-0.65298`. This is direct computational reuse, but it is retrospective and is not presented as fresh validation.

Second, B12 provides an early model-redesign example. The B12 manuscript states that B12.1c still allowed deterministic low-noise lock. B12.1d therefore introduced an ignition barrier and reran a refined scan, producing a finite-noise locking window with peak lock probability near 0.861 at `sigma_R ~ 0.070`. The earlier stage is not retroactively called a formal FAIL; the record supports the narrower statement that a limiting behavior motivated a changed mechanism and a new calculation.

Third, B13/B13.1 corrected an attractive interpretation. A restricted finite-noise regime approached a Born-like reference, but the rotated-basis follow-up showed that the single-selection response was better described by a logistic basin-boundary kernel: the reported binned RMSE is about 0.0738 for the cos-squared reference and about 0.0122 for the logistic kernel. A later finite-width cloud average then explained the cos-squared-like sequential response with reported RMSE near 0.0048. Later computation therefore narrowed the earlier analogy rather than amplifying it.

Finally, B17-B18 gives an early transfer-failure/readout-enrichment chain. In B17, a read-start local history load organized response well in one positive-feedback free-boundary model. In the B18 inhibitory-front transfer, the analogous read-start variable had `R^2 = 0.163`, compared with about `0.742` for path exposure, `0.793` for an interface-core path exposure, and `0.807` for the best B18.3 threshold-path operator. A predictor that worked in one model was therefore not treated as universal; its transfer limitation motivated a richer readout operator.

A fifth early measurement-redesign candidate is retained in the supplementary audit but omitted from the evidential examples here. An earlier audit version quoted a specific non-radial exponent correction, but the current provenance recovery did not locate an immutable artifact supporting that exact numerical claim. The main manuscript therefore does not reproduce the unrecovered values.

These cases broaden the object being preserved. Before formal verdicts were standardized, the reusable research object could be an expensive numerical scan, a mechanism mismatch, an interpretation that weakened under follow-up, or a predictor that did not transfer. The supplementary measurement-redesign candidate also illustrates that the audit itself is subject to the same non-retroactivity and provenance rules as the case study.

### 5.3 B19/B19E: negative external validation and non-rescue mechanism diagnosis

B19 did not produce one robust ray-independent upstream scalar collapse in its tested synthetic vorticity families. Rather than treating that negative result as the end of the question, B19E froze a small set of B19-derived boundary/core descriptors and carried them into an independently maintained external flow solver.

The primary B19E holdout used untouched TIDE realizations and asked whether those frozen additions supplied incremental predictive information beyond a strong standard local-flow baseline. The retained A1 verdict was

`NULL_OR_INCONCLUSIVE`.

The point estimate for the incremental coefficient of determination was slightly negative, while the frozen hierarchical bootstrap interval crossed zero. The result therefore neither supported incremental predictive value nor justified a stronger theorem that boundary/core information can never help.

A later Stage-B audit used new realizations to close the exact finite-control-volume local budget. The budget closed to near machine precision, while the historical simplified production-minus-dissipation proxy remained weak at the primary local scale because omitted transport terms, especially advective boundary transport, were large.

Crucially, the source record states explicitly that Stage B was **not an A1 rescue**. This yields a useful methodological pattern:

```text
external predictive null / inconclusive
-> retain verdict
-> ask a different mechanism question
-> fresh exact-budget audit
-> explain part of the limitation
-> do not upgrade the predictive result
```

The scientific value of the later analysis was explanatory rather than classificatory.

### 5.4 B23/B23A: protocol repair and terminal narrowing

B23 provides a different form of failure preservation. Its original aggregate plan remained INCONCLUSIVE because the prediction-centered symmetric search window could not be executed for two endpoint-near targets. Later boundary-safe or corrective runs were reported as supplementary evidence rather than counted retroactively as successes of the original plan.

One repair run, E3R, was subsequently found to have dispatched the wrong ray. That implementation-invalid record was preserved, and E3R2 was described as a corrective replication rather than as a new blinded success.

B23A then asked a broader transfer question: which aspects of the local response-geometry construction survived changes of family, topology, observable, and approach protocol? The sequence retained a mixture of NOT_SUPPORTED, PASS, and INCONCLUSIVE outcomes and ended with a prospective rate-ordering test that was NOT_SUPPORTED. The branch then stopped under an explicit no-rescue rule.

This sequence shows that failure salvage need not culminate in a positive endpoint. A mature outcome can instead be a better-resolved map of what does not transfer.
### 5.5 B25: local salvage from a failed predictor

One of the clearest examples begins with B25.1.

The first A-to-B transfer model used a constant-density relation

```text
J_pred = sigma_1D P_rep
```

and received the formal verdict

`AB_CONSTANT_DENSITY_FAIL`.

The failed result was retained. A retrospective analysis then re-read only the archived B25.1 profiles using a coarea-based decomposition. Two systematic effects were identified: a finite boundary band contains a family of level-set perimeters rather than a single representative perimeter, and the two-dimensional profile amplitude differs from the one-dimensional reference amplitude.

That retrospective analysis was explicitly diagnostic. It did not upgrade the B25.1 result.

A replacement level-resolved predictor was then frozen before new trajectories were generated and evaluated on nine new shape/resolution cases. The formal verdict was

`AB_LEVEL_RESOLVED_BRIDGE_PASS`.

This sequence is methodologically important because it cleanly separates:

```text
FAIL data -> discovery / redesign
fresh held-out data -> validation
```

### 5.6 B27-B29: failures that enrich the state description

B27.2 tested whether a normalized history-induced response form survived connected-to-disconnected reconfiguration under a frozen identity covariance map. The result was

`RECONFIGURATION_COVARIANCE_FAIL`.

B28 replaced the identity-covariance hypothesis with a geometry-only component-resolved split transport. That also failed prospectively:

`GEOMETRY_CONDITIONED_LINEAGE_TRANSPORT_FAIL`.

B29 then asked whether retained history/path information added predictive value beyond instantaneous geometry. The programme closed before held-out evaluation because the inherited readability gates were not satisfied uniformly.

This chain does not end in a success. Its methodological value is that the negative outcomes successively constrained what a sufficient state representation might require.

### 5.7 B32-B36: from failed qualitative laws to structured descriptions

Later phases contain several examples in which a failed simple law leads to a weaker but more structured successor.

B32.1 retained

`DYNAMIC_COMPLEX_PARITY_MODE_FAIL`.

B33 reframed the observed behavior in terms of frequency- and period-dependent transverse node lifting and obtained prospective PASS verdicts.

Similarly, B35.1 and B35.2 rejected an approximately linear distance-ordered peak-timing law, and B36.1 rejected a stronger geometry-conditioned timing ordering. B36.2 then tested a decomposition into geometry and readout-sampling contributions on a fresh grid and obtained

`ADDITIVE_GEOMETRY_SAMPLING_DECOMPOSITION_PASS`.

These sequences illustrate a recurring pattern:

```text
simple global law FAIL
-> retain structure of the failure
-> decompose or change explanatory variable
-> test a narrower structured claim
```

The B34-B35 calibration record adds another layer. Before B34.1 was allowed to open, several non-claim-bearing stages failed source-tail, readability, or readiness conditions. The programme changed the source, probe construction, and finally the observable to a normalized complex transfer kernel; only after resolution and shifted-sampling checks passed was a fresh B34.1 protocol authorized.

B35 is even more informative methodologically. A calibration run remained numerically valid but no off-source probe satisfied the frozen closure rule, so the record kept `administrative_ready_for_B35_1=False`. Rather than lowering the gate, the programme changed the timing observable. A later calibration then authorized a fresh B35.1 experiment, which subsequently received the scientific verdict `DISTANCE_ORDERED_APPROX_LINEAR_PEAK_TIMING_FAIL`.

This sequence argues against a simple "tune until PASS" description:

```text
readiness gate fails
-> redesign
-> readiness passes
-> fresh scientific test opens
-> scientific test can still FAIL
```


---

## 6. Representational salvage: the relational-time pivot

The strongest macro-scale example in the current case study concerns timing.

### 6.1 Accumulated negative timing results

By B35-B37, several attempts to stabilize absolute peak-timing relations had failed.

B37.1 returned

`INTRINSIC_CONTOUR_REPARAMETERIZATION_FAIL`

and B37.2 returned

`FIXED_ARC_SUPPORT_TIMING_COLLAPSE_FAIL`.

The B37.2 failure was localized to an absolute peak-time cross-resolution criterion. Diagnostics showed substantial grid-phase sensitivity of the outer-probe peak timing. An existing-data alignment analysis also showed that the nonoscillatory pulse traces shared a reproducible waveform after temporal rephasing, while relative lag versus intrinsic probe distance was more stable than raw absolute peak time.

### 6.2 Change of observable

The response was not another retrospective repair of absolute timing. The programme changed the observable.

The new question became approximately:

> Which timing structures remain stable when timing is expressed relationally among probes, sources, receivers, operators, and readouts?

B38.1 prospectively tested relative boundary lag on fresh cases and returned

`RELATIVE_BOUNDARY_LAG_GEOMETRY_PASS`.

B38 then extended the relational programme through source/receiver swap tests, tangent-operator analysis, prospective operator-to-response prediction, gamma interventions, and weighted-dual readout tests.

The strongest retained B38 conclusion remained deliberately finite: measured timing asymmetry in the tested model depends strongly on the joint relation between operator, source, receiver, and readout.

![Figure 5. Representational salvage from absolute to relational timing.](../figures/relational_time_pivot_v0_1.svg)

**Figure 5. Representational salvage in the later BIG timing programme.** Repeated negative or fragile absolute-timing results were retained rather than erased. Their diagnostics contributed to a change of observable toward relative and relational timing. The old results served as discovery material, while later relational claims were evaluated in newly frozen prospective tests.

### 6.3 The old failures were not new validation data

The B35-B37 failures and diagnostics helped motivate the new observable. For that reason, they are discovery data for the relational formulation rather than independent confirmation of it.

Their role can be written as

```text
archived failure pattern
-> conceptual pivot
-> equation / observable refinement
-> new prospective tests
```

This is the central example of representational salvage in the present paper.

### 6.4 Later failures became more local

The relational programme did not eliminate failure.

B39.3-P1 retained

`INTEGRATION_LEVEL_REPARAMETERIZATION_COVARIANCE_FAIL`.

Diagnostics localized the failing conditions, a response-independent clock-map calibration was performed, and a new P2 protocol was frozen before fresh trajectories. P2 then returned

`INTRINSIC_CLOCK_MAP_INTEGRATION_COVARIANCE_PASS`.

The P2 result did not upgrade P1.

B40 again retained two formal parent failures:

- `CLOCK_MAP_FAMILY_TRANSFER_FAIL`
- `TARGET_EXCLUDED_RELATIONAL_RECONSTRUCTION_FAIL`

Later frozen tests localized these failures and identified narrower finite-grid transformation behavior.

The case-study interpretation is therefore not that the conceptual pivot ended failure. A more defensible observation is that later failures increasingly identified limits of coordinates, transfer rules, resolution, or reconstruction rather than repeatedly collapsing the entire research direction.

That interpretation remains descriptive and should itself be tested more systematically.

---

## 7. Individual AI-assisted research and the experimental boundary

The proposed architecture has a clear limit.

AI-assisted individual research can support extensive theoretical development and public-data comparison, but it cannot generate measurements that require unavailable instruments or controlled physical interventions.

In the BIG programme, public databases or published measurements allow partial comparison with domains including nuclear fission and material-interface phenomena. Such data can be extremely useful, but they were collected for other scientific purposes. The exact parameter combination needed to distinguish a new model may simply not exist.

The physical frontier therefore has a different workflow:

```text
individual + AI
-> broad computational search
-> eliminate weak hypotheses
-> preserve failed alternatives
-> formulate measurable prediction
-> identify missing experiment
-> handoff to experimental group
```

The contribution of a laboratory or organization is not merely compute. It includes sample preparation, apparatus, calibration, safety, intervention, measurement design, replication, and tacit domain knowledge.

The architecture is therefore complementary. AI may allow an individual to arrive at the experimental frontier with a more specific package than an informal idea: equations, code, discarded alternatives, sensitivity maps, a frozen prediction, and an explicit measurement request.

---

## 8. From personal intuition to public testability

A broader motivation of the case study is that an individual's intuition or philosophical question can now be carried farther toward explicit quantitative confrontation.

The scientifically relevant transformation is:

```text
intuition
-> operational definition
-> mathematics
-> executable computation
-> prediction
-> possible failure
-> comparison with nature
```

The important endpoint is not preservation of the original intuition. It is exposure to possible failure.

This does not imply that philosophy becomes natural science merely by being formalized. It means that the practical cost of converting an informal idea into something testable may be falling.

For independent researchers, this may open a new path for ideas that originate outside established research programmes. The corresponding obligation is unusually strong claim discipline: the more cheaply hypotheses can be generated, the more important it becomes to preserve negative outcomes, freeze tests, distinguish discovery from validation, and identify the point at which real-world measurement is missing.

---

## 9. Role of model capability and simple external computation

The case study also contains a subjective but practically important observation: later generations of reasoning-capable AI appeared to increase the depth, speed, and continuity of mathematical investigation.

This paper does not treat that perception as controlled evidence. A rigorous comparison would require matched tasks, fixed compute budgets, blinded evaluation, and reproducible model access. The retained-artifact latency audit does not validate the perceived acceleration: within the 14 comparable failure-to-successor transitions, no monotonic shortening is detected. The subjective capability observation and the measured failure-reuse latency are therefore kept separate.

Nevertheless, the observation suggests a testable hypothesis for future work: there may be capability thresholds at which AI changes not merely the speed of isolated tasks but the feasible length and complexity of a continuous individual research programme.

The external Python loop may be essential to that effect. A more capable reasoning model can generate more sophisticated hypotheses, but without frequent external execution it can also generate more sophisticated coherent errors. The combined architecture is therefore not "stronger AI alone" but

```text
capable reasoning model
+ simple executable computation
+ persistent feedback
+ retained research memory
```

---

## 10. Limitations

First, the evidence is a single-researcher longitudinal case study. It cannot quantify general productivity gains.

Second, research-history salvage is vulnerable to retrospective overfitting. The separation between discovery data and fresh prospective tests is therefore essential but not sufficient to remove all researcher degrees of freedom.

Third, numerical execution constrains the implemented model, not nature. Numerical stability, coding correctness, discretization, and interpretation remain separate questions.

Fourth, public-data comparisons are selected by what has already been measured. This can create a severe external-validation bottleneck.

Fifth, the adjacent literature is evolving rapidly. Several 2026 agentic-research systems already preserve failed trials, exploration graphs, persistent research memory, or explicit trial-to-behavior conversion. The present paper therefore claims neither invention of failure preservation nor uniqueness of source-to-action lineage; its contribution is the audited human-led longitudinal implementation and the particular non-retroactive nested architecture described here.

Finally, the methodological value of the BIG archive is independent of whether its strongest scientific interpretations survive later external validation.

The early-history audit contains an additional provenance limitation. One previously quoted non-radial boundary-fit numerical comparison could not be traced to a recovered immutable source and is therefore excluded from the main evidential examples rather than treated as established evidence.

The 88.0% broad backward-link fraction remains an exploratory descriptive statistic of one programme. Sensitivity analyses give 87.5% under a strict FAIL/NOT_SUPPORTED-style denominator, 95.65% under an opportunity-adjusted broad denominator that excludes two explicit terminal/closeout outcomes, and 81.25% when B-family groups are counted only if every broad negative source in the group is reused. These alternatives show both robustness and dependence on the unit of analysis.

The temporal epoch comparison is likewise exploratory. Although the later epoch shows 12/12 explicit reuse compared with 10/13 in the earlier standardized epoch, the Fisher exact comparison is not statistically persuasive, and improved documentation can itself increase the detectability of backward links. A separate 14-transition artifact-timestamp analysis finds no evidence that source-to-successor freeze latency shortened over time (Spearman rho approximately 0.051, p approximately 0.864).

---

## 11. Testable methodological predictions

The architecture itself should generate hypotheses that can be tested on future research programmes.

Possible predictions include:

1. the fraction of new stages that explicitly reuse archived negative or inconclusive results may rise as preservation and lineage practice mature; this should be tested separately from reuse latency;
2. failure-salvage latency should be measured as a distinct outcome rather than inferred from the prevalence of backward links;
3. failure salvage should reduce repeated exploration of already-disfavored hypothesis regions;
4. programmes with immutable verdict ledgers should show fewer retrospective claim upgrades than unstructured AI-assisted workflows;
5. separating AI reasoning from external executable checks should reduce the duration of some classes of coherent implementation error;
6. experimental handoff packages containing explicit failed alternatives and falsification criteria should be easier for external laboratories to evaluate than idea-only proposals.

These are not established results. They define a path from the present case study toward comparative research.

---

## 12. Conclusion

The proposed method treats research as a history-bearing dynamic process.

At the micro scale, AI-assisted reasoning is repeatedly exposed to external numerical execution. At the meso scale, hypotheses are frozen, tested, assigned persistent verdicts, and redesigned without rewriting history. At the macro scale, the accumulated archive becomes research memory: failures can be retrieved, reinterpreted, and used to construct new questions.

Between exploratory calibration and claim-bearing evaluation, explicit readiness gates provide an additional safeguard: unsuccessful calibration can trigger redesign without being counted as evidence for the later claim.

The resulting view of failure is neither celebratory nor dismissive.

```text
FAIL != success
FAIL != necessarily waste
```

A failed result remains a failed test of its original hypothesis. Its future value depends on whether it contains reusable computational, structural, diagnostic, or representational information.

The final boundary remains physical. When the decisive measurement does not exist, simulation and public-data analysis cannot manufacture it. At that point the appropriate next step is experimental handoff.

The main methodological claim is therefore modest but consequential: AI-assisted individual research may make a larger region of the hypothesis space economically explorable, while failure preservation allows part of that exploration history to remain scientifically active.

---

## Data, code, and audit trail

Methodology repository:

https://github.com/Jun-Lucis/failure-preserving-research

Primary case-study repository:

https://github.com/Jun-Lucis/BIG-theory

Reserved / assigned Zenodo DOI for this methodology paper: **10.5281/zenodo.23171698** (https://doi.org/10.5281/zenodo.23171698).

Current audit artifacts include:

- `protocols/lineage_coding_protocol_v0_1.md`
- `evidence/stage_lineage_B19_B40_v0_3.csv`
- `docs/quantitative_lineage_audit_v0_3.md`
- `docs/early_lineage_audit_B3_B18_v0_2.md`
- `evidence/early_verified_lineage_candidates_v0_2.csv`
- `evidence/early_provenance_manifest_v0_2.csv`
- `evidence/failure_salvage_ledger_v0_3.csv`
- `evidence/source_action_edges_v0_3.csv`
- `evidence/dated_negative_source_lineage_v0_1.csv`
- `docs/temporal_lineage_audit_v0_2.md`
- `evidence/failure_reuse_latency_v0_1.csv`
- `figures/reuse_latency_v0_1.svg`
- `case_studies/BIG/failure_salvage_audit_v0_3.md`
- `case_studies/BIG/B34_B35_calibration_gating.md`
- `docs/claim_boundary_table_v0_3.md`
- `docs/reference_verification_v0_1.md`
- `docs/source_action_authority_recheck_v1_0.md`
- `figures/figure_manifest_v1_0.md`
- vector and Mermaid figure sources under `figures/`.

---

## References

1. Zhang, Y., Khan, S. A., Mahmud, A. et al. (2025). *Exploring the role of large language models in the scientific method: from hypothesis to discovery*. npj Artificial Intelligence 1, 14. https://doi.org/10.1038/s44387-025-00019-5

2. Agrawal, A. K., McHale, J. & Oettl, A. (2026). *AI in Science*. NBER Working Paper 34953. https://doi.org/10.3386/w34953

3. Hao, Q., Xu, F., Li, Y. et al. (2026). *Artificial intelligence tools expand scientists’ impact but contract science’s focus*. Nature 649, 1237–1243. https://doi.org/10.1038/s41586-025-09922-y

4. Curry, S., Mercado-Lara, E., Arechavala-Gomeza, V. et al. (2025). *Ending publication bias: A values-based approach to surface null and negative results*. PLOS Biology 23(9), e3003368. https://doi.org/10.1371/journal.pbio.3003368

5. Rainford, P. F., Occhipinti, A., Wang, B. et al. (2026). *Knowledge preservation in the era of big science and AI: strategies for sustainable scientific research*. Nature Communications 17, 4069. https://doi.org/10.1038/s41467-026-72667-3

6. Soderberg, C. K., Errington, T. M., Schiavone, S. R. et al. (2021). *Initial evidence of research quality of registered reports compared with the standard publishing model*. Nature Human Behaviour 5, 990–997. https://doi.org/10.1038/s41562-021-01142-4

7. Center for Open Science. *Registered Reports*. https://www.cos.io/initiatives/registered-reports

8. Center for Open Science. *Preregistration*. https://www.cos.io/initiatives/prereg

9. Henderson, E. L. & Chambers, C. D. (2022). *Ten simple rules for writing a Registered Report*. PLOS Computational Biology 18(10), e1010571. https://doi.org/10.1371/journal.pcbi.1010571

10. Huber, S. P. et al. (2020). *AiiDA 1.0, a scalable computational infrastructure for automated reproducible workflows and data provenance*. Scientific Data 7, 300. https://doi.org/10.1038/s41597-020-00638-4

11. Lyu, Y., Zhang, X., Yi, X. et al. (2026). *EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery*. arXiv:2603.08127. https://arxiv.org/abs/2603.08127

12. Liu, J., Pei, J., Huang, J. et al. (2026). *The Last Human-Written Paper: Agent-Native Research Artifacts*. arXiv:2604.24658. https://arxiv.org/abs/2604.24658

13. Wang, C., Xie, Q., He, W. et al. (2026). *Sibyl-AutoResearch: Autonomous Research Needs Self-Evolving Trial-and-Error Harnesses, Not Paper Generators*. arXiv:2605.22343. https://arxiv.org/abs/2605.22343

Case-study source materials are linked through the BIG repository, its status documents, and its Zenodo publication map.
