#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Build a compact release package and SHA-256 manifest.

Usage:
    python tools/build_release_package.py --manuscript paper/manuscript_v1_0.md
    python tools/build_release_package.py --manuscript paper/manuscript_v1_0_rc2.md --label rc2

The script intentionally includes only public repository artifacts. It does not
read private Drive URLs, IDs, or unpublished local files.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]

STATIC_FILES = [
    "README.md",
    "CITATION.cff",
    ".zenodo.json",
    "LICENSE",
    "tools/LICENSE",
    "tools/build_release_package.py",
    "protocols/lineage_coding_protocol_v0_1.md",
    "docs/quantitative_lineage_audit_v0_3.md",
    "docs/temporal_lineage_audit_v0_2.md",
    "docs/early_lineage_audit_B3_B18_v0_2.md",
    "docs/claim_boundary_table_v0_3.md",
    "docs/reference_verification_v0_1.md",
    "docs/source_action_authority_recheck_v1_0.md",
    "evidence/stage_lineage_B19_B40_v0_3.csv",
    "evidence/failure_salvage_ledger_v0_3.csv",
    "evidence/source_action_edges_v0_3.csv",
    "evidence/failure_reuse_latency_v0_1.csv",
    "evidence/early_verified_lineage_candidates_v0_2.csv",
    "evidence/early_provenance_manifest_v0_2.csv",
    "case_studies/BIG/failure_salvage_audit_v0_3.md",
    "case_studies/BIG/B34_B35_calibration_gating.md",
    "figures/figure_manifest_v1_0.md",
    "figures/nested_cycles_v0_1.svg",
    "figures/failure_salvage_spiral_v0_1.svg",
    "figures/lineage_sensitivity_v0_1.svg",
    "figures/big_salvage_lineage_v0_1.svg",
    "figures/relational_time_pivot_v0_1.svg",
    "figures/reuse_latency_v0_1.svg",
    "paper/manuscript_v1_0_Japanese_reference.md",
    "paper/zenodo_metadata_v1_0.md",
]


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manuscript", required=True)
    ap.add_argument("--label", default="v1_0")
    ap.add_argument("--out-dir", default="release")
    args = ap.parse_args()

    files = [args.manuscript, *STATIC_FILES]
    missing = [p for p in files if not (ROOT / p).is_file()]
    if missing:
        raise SystemExit("Missing release files:\n" + "\n".join(missing))

    out_dir = ROOT / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = out_dir / f"SHA256SUMS_{args.label}.txt"
    archive = out_dir / f"failure_preserving_research_{args.label}.zip"

    rows = []
    for rel in files:
        p = ROOT / rel
        rows.append(f"{sha256(p)}  {rel}")

    manifest.write_text("\n".join(rows) + "\n", encoding="utf-8")

    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for rel in files:
            zf.write(ROOT / rel, arcname=rel)
        zf.write(manifest, arcname=manifest.relative_to(ROOT))

    print(f"Wrote {manifest.relative_to(ROOT)}")
    print(f"Wrote {archive.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
