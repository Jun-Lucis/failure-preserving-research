# Figure source — Three nested cycles

This Mermaid diagram is the source for the paper's core architecture figure.

```mermaid
flowchart TB
    subgraph MICRO["Micro cycle — AI ↔ external computation"]
        A["Question / intuition"] --> B["AI-assisted formulation"]
        B --> C["Equation / simple code"]
        C --> D["External Python / Colab execution"]
        D --> E["Numerical output / contradiction / support"]
        E --> B
    end

    subgraph MESO["Meso cycle — prospective test and redesign"]
        F["Hypothesis"] --> G["Predeclaration / freeze"]
        G --> H["Claim-bearing computation"]
        H --> I["PASS / FAIL / INCONCLUSIVE / INVALID"]
        I --> J["Diagnosis"]
        J --> K["New hypothesis"]
        K --> G
    end

    subgraph MACRO["Macro cycle — failure salvage and research memory"]
        L["Retained research history R_t"] --> M["Retrieve earlier limits / failures"]
        M --> N["Pattern extraction / conceptual pivot"]
        N --> O["Mathematical redesign"]
        O --> P["New prospective programme"]
        P --> L
    end

    E --> F
    I --> L

    subgraph HANDOFF["Experimental handoff"]
        Q["Public-data frontier"] --> R["Frozen measurable prediction"]
        R --> S["Laboratory / organization / domain experts"]
        S --> T["New physical evidence"]
    end

    P --> Q
```

## Caption draft

**Figure 1. Nested architecture of failure-preserving AI-assisted research.**  
At the micro scale, AI-assisted reasoning is repeatedly exposed to externally executed numerical computation. At the meso scale, hypotheses are prospectively frozen and assigned persistent verdicts before redesign. At the macro scale, the retained archive becomes a research-memory state from which earlier negative or limiting outcomes can be retrieved as discovery data. Experimental handoff marks the boundary at which decisive evidence requires new physical measurements.
