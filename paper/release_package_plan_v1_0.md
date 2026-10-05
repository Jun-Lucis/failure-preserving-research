# Release package plan — v1.0

**Date:** 6 October 2026  
**Current manuscript:** `paper/manuscript_v1_0.md`

## Release package principle

The first Zenodo package should be compact enough to audit directly while preserving the data needed to reconstruct the methodology claims.

The package should contain:

1. the frozen English manuscript PDF and manuscript source;
2. the lineage-coding protocol;
3. the standardized B19-B40 stage table;
4. the failure-salvage ledger and normalized source-action edges;
5. the temporal/reuse-latency table;
6. the early-history audit and provenance manifest;
7. the claim-boundary, reference-verification, and source/action recheck documents;
8. the main vector figures and frozen figure manifest;
9. a SHA-256 manifest;
10. optional compact ZIP containing the same public audit materials.

## Public release files already identified

```text
paper/manuscript_v1_0.md                 # after final freeze
paper/manuscript_v1_0_Japanese_reference.md # Japanese reference translation after final freeze
paper/zenodo_metadata_draft.md
protocols/lineage_coding_protocol_v0_1.md

docs/quantitative_lineage_audit_v0_3.md
docs/temporal_lineage_audit_v0_2.md
docs/early_lineage_audit_B3_B18_v0_2.md
docs/claim_boundary_table_v0_3.md
docs/reference_verification_v0_1.md
docs/source_action_authority_recheck_v1_0.md

evidence/stage_lineage_B19_B40_v0_3.csv
evidence/failure_salvage_ledger_v0_3.csv
evidence/source_action_edges_v0_3.csv
evidence/failure_reuse_latency_v0_1.csv
evidence/early_verified_lineage_candidates_v0_2.csv
evidence/early_provenance_manifest_v0_2.csv

case_studies/BIG/failure_salvage_audit_v0_3.md
case_studies/BIG/B34_B35_calibration_gating.md

figures/figure_manifest_v1_0.md
figures/nested_cycles_v0_1.svg
figures/failure_salvage_spiral_v0_1.svg
figures/lineage_sensitivity_v0_1.svg
figures/big_salvage_lineage_v0_1.svg
figures/relational_time_pivot_v0_1.svg
figures/reuse_latency_v0_1.svg
```

## Package builder

`tools/build_release_package.py` generates:

```text
release/SHA256SUMS_<label>.txt
release/failure_preserving_research_<label>.zip
```

It includes only public repository artifacts and intentionally excludes private Drive URLs, Drive IDs, credentials, and unpublished local files.

Example after v1.0 freeze:

```bash
python tools/build_release_package.py \
  --manuscript paper/manuscript_v1_0.md \
  --label v1_0
```

## Assigned DOI

`10.5281/zenodo.23171698`

https://doi.org/10.5281/zenodo.23171698

This DOI should be used consistently in the frozen English manuscript, Japanese reference translation, `CITATION.cff`, README, BIG methodology bridge, release manifest, and Zenodo package metadata.

## Items that must wait

The following should not be finalized until the license and manuscript freeze are complete:

- `paper/manuscript_v1_0.md`;
- final PDF;
- Git tag/release;
- SHA-256 release manifest;
- Zenodo DOI is already assigned: `10.5281/zenodo.23171698`;
- `CITATION.cff` DOI;
- README / BIG-bridge DOI insertion.

## Current release blockers

At RC2, the scientific/audit content is effectively frozen. Remaining decisions are:

```text
1. license
2. Git tag + full audit-package SHA-256 manifest/archive
3. Zenodo upload/publication under DOI `10.5281/zenodo.23171698`
```
