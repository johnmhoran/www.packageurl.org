#!/usr/bin/env python3
"""
- Copy .md files from one or more source-repo checkouts into this repo's
tree, per sync-manifest.json.
- Supports renaming during the copy.
- Supports multiple source repos (each entry names which one it comes from).

- Manifest format (JSON, see sync-manifest.json):
[
  {
    "repo": "purl-spec",
    "source": "docs/specification/common-qualifiers.md",
    "dest": "website/docs/purl/common-qualifiers.md"
  },
  ...
]

- `repo` must match a subdirectory name under --sources-root.
- As sync_md_docs.yml provides, the sync command takes the following form:

python .github/scripts/sync_md_docs.py \
--manifest .github/scripts/sync-manifest.json \
--sources-root _sources \
--dest .

- Exits non-zero (and fails loudly) if any manifest source file is missing.
"""
import argparse
import json
import shutil
import sys
from pathlib import Path


def load_manifest(manifest_path: Path) -> list[dict]:
    with manifest_path.open("r", encoding="utf-8") as f:
        entries = json.load(f)
    for i, entry in enumerate(entries):
        missing_keys = {"repo", "source", "dest"} - entry.keys()
        if missing_keys:
            raise ValueError(f"Manifest entry {i} missing {missing_keys}: {entry}")
    return entries


def sync(entries: list[dict], sources_root: Path, dest_root: Path) -> list[str]:
    missing = []
    changed = []
    for entry in entries:
        src = sources_root / entry["repo"] / entry["source"]
        dest = dest_root / entry["dest"]
        if not src.is_file():
            missing.append(f"{entry['repo']}: {src}")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.is_file() or src.read_bytes() != dest.read_bytes():
            shutil.copyfile(src, dest)
            changed.append(str(dest))
    if missing:
        raise FileNotFoundError(
            "Missing expected source file(s), aborting sync:\n  " + "\n  ".join(missing)
        )
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument(
        "--sources-root", required=True, type=Path,
        help="directory containing one subfolder per source repo, e.g. _sources/purl-spec, _sources/vers-spec",
    )
    parser.add_argument("--dest", required=True, type=Path, help="root of this repo (destination)")
    args = parser.parse_args()

    entries = load_manifest(args.manifest)
    try:
        changed = sync(entries, args.sources_root, args.dest)
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        return 1

    if changed:
        print(f"Updated {len(changed)} file(s):")
        for path in changed:
            print(f"  {path}")
    else:
        print("No file content changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
