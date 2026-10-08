#!/usr/bin/env python3
"""
Sync files and directories listed in a manifest from source-repo checkouts
into this repo.  Directory entries are mirrored (including deletion of
retired files), giving the same effect as rsync --delete.

Usage:
  python .github/scripts/sync_json_data.py \
    --manifest .github/scripts/sync-json-data-manifest.json \
    --sources-root _sources \
    --dest .
"""
import argparse
import json
import shutil
import sys
from pathlib import Path


def mirror_directory(src: Path, dest: Path, changed: list[Path]) -> None:
    """Copy src → dest, then delete any extra files/dirs in dest."""
    dest.mkdir(parents=True, exist_ok=True)

    # Copy / update everything from source
    for item in src.iterdir():
        s = item
        d = dest / item.name
        if s.is_dir():
            if d.exists() and not d.is_dir():
                d.unlink()
            mirror_directory(s, d, changed)
        else:
            if not d.is_file() or s.read_bytes() != d.read_bytes():
                shutil.copyfile(s, d)
                changed.append(d)

    # Delete anything in dest that is no longer in source
    for item in list(dest.iterdir()):
        if not (src / item.name).exists():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
            changed.append(item)
            print(f"Deleted: {item}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--sources-root", required=True, type=Path)
    parser.add_argument("--dest", required=True, type=Path)
    args = parser.parse_args()

    entries = json.loads(args.manifest.read_text(encoding="utf-8"))
    changed: list[Path] = []

    for e in entries:
        src = args.sources_root / e["repo"] / e["source"].rstrip("/")
        dest = args.dest / e["dest"].rstrip("/")

        if not src.exists():
            print(f"ERROR: missing source {src}", file=sys.stderr)
            return 1

        if src.is_dir():
            # Directory → full mirror (copy + delete extras)
            mirror_directory(src, dest, changed)
        else:
            # Single file
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.is_file() or src.read_bytes() != dest.read_bytes():
                shutil.copyfile(src, dest)
                changed.append(dest)

    if changed:
        # Deduplicate while preserving order
        seen = set()
        unique = []
        for p in changed:
            if p not in seen:
                seen.add(p)
                unique.append(p)
        print(f"Changed {len(unique)} path(s)")
        for p in unique:
            print(f"  {p}")
    else:
        print("No changes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
