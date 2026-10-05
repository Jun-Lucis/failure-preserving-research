# Figure source — Relational-time pivot in the BIG case study

```mermaid
flowchart TB
    A["B35.1 / B35.2
linear peak-timing FAILs"] --> B["B36.1
geometry-conditioned ordering FAIL"]
    B --> C["B36.2
geometry/readout decomposition PASS"]
    C --> D["B37.1
intrinsic contour reparameterization FAIL"]
    D --> E["B37.2
fixed arc-support timing collapse FAIL"]
    E --> F["Diagnostics:
absolute peak timing is phase/resolution sensitive"]
    F --> G["Existing-trace alignment:
relative lag is more stable"]
    G --> H["Conceptual pivot:
absolute timing → relational timing"]
    H --> I["B38.1 fresh freeze
RELATIVE_BOUNDARY_LAG_GEOMETRY_PASS"]
    I --> J["B38.2–B38.6
source / receiver / operator / readout relations"]
    J --> K["B39–B40
clock-map and reconstruction transfer tests"]
    K --> L["Later FAILs localize
map / grid / orientation limits"]

    E -. "old FAILs remain FAILs" .-> H
```

## Caption draft

**Figure 5. Representational salvage in the later BIG timing programme.**  
Repeated negative or fragile absolute-timing results were retained rather than erased. Their diagnostics contributed to a change of observable toward relative and relational timing. The old data therefore served as discovery material, while the later relational claims were evaluated in newly frozen prospective tests. Subsequent FAILs remained present but increasingly localized transfer, discretization, and reconstruction limits rather than retroactively changing the earlier verdicts.
