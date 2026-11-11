"""Validate all ANIMA source files.

Checks the front matter of every source file against the JSON Schema and
against the rules of the methodology (file location, IDs, consistency with
the triad). Exits with status 1 if any error is found.

Usage:
    python scripts/validate.py                          # checks sources/
    python scripts/validate.py --sources tests/fixtures/valid
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from common import ACTIVE_EDGES, ROOT, SOURCES_DIR, load_schema, read_front_matter, source_files

BINDINGNESS_BY_PILLAR = {
    "law": {"binding"},
    "guidance": {"official", "recommended"},
    "professional": {"professional"},
}


def bibtex_keys(bib_path: Path) -> set[str]:
    if not bib_path.exists():
        return set()
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib_path.read_text(encoding="utf-8")))


def check_file(path: Path, data: dict, sources_dir: Path, bib_keys: set[str]) -> list[str]:
    """Rules that go beyond the schema."""
    errors: list[str] = []

    # File location: <pillar>/<jurisdiction>/<name>.md
    parts = path.relative_to(sources_dir).parts
    if len(parts) != 3:
        errors.append("file must be located at <pillar>/<jurisdiction>/<name>.md")
    else:
        if parts[0] != data.get("pillar"):
            errors.append(f"folder '{parts[0]}' does not match pillar '{data.get('pillar')}'")
        if parts[1] != data.get("jurisdiction"):
            errors.append(f"folder '{parts[1]}' does not match jurisdiction '{data.get('jurisdiction')}'")

    # Source ID matches jurisdiction
    jurisdiction = str(data.get("jurisdiction", ""))
    source_id = str(data.get("id", ""))
    if source_id and not source_id.startswith(f"SRC-{jurisdiction.upper()}-"):
        errors.append(f"source ID '{source_id}' does not match jurisdiction '{jurisdiction}'")

    # Bindingness fits the pillar
    pillar = data.get("pillar")
    if pillar in BINDINGNESS_BY_PILLAR and data.get("bindingness") not in BINDINGNESS_BY_PILLAR[pillar]:
        allowed = ", ".join(sorted(BINDINGNESS_BY_PILLAR[pillar]))
        errors.append(f"bindingness '{data.get('bindingness')}' does not fit pillar '{pillar}' (allowed: {allowed})")

    # Checked date is not in the future
    checked = data.get("checked")
    if isinstance(checked, str):
        try:
            if dt.date.fromisoformat(checked) > dt.date.today():
                errors.append(f"checked date {checked} is in the future")
        except ValueError:
            pass  # reported by the schema

    # BibTeX key exists
    key = data.get("bibtex_key")
    if key and key not in bib_keys:
        errors.append(f"bibtex_key '{key}' not found in references.bib")

    # Requirements and the triad
    for req in data.get("requirements") or []:
        rid = req.get("id", "?")
        topic = req.get("topic")
        if topic and isinstance(rid, str) and rid.count("-") == 2 and rid.split("-")[1] != topic:
            errors.append(f"{rid}: ID does not match topic '{topic}'")
        edges = req.get("edge") or []
        main_edge = edges[0] if edges else None
        for config in req.get("configuration") or []:
            if main_edge and config in ACTIVE_EDGES and main_edge not in ACTIVE_EDGES[config]:
                errors.append(f"{rid}: main edge {main_edge} is not active in configuration {config}")
        if req.get("addressee") == "practitioner" and 3 in (req.get("configuration") or []):
            errors.append(f"{rid}: a duty of the practitioner cannot take effect in configuration 3 (no practitioner)")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--sources", type=Path, default=SOURCES_DIR, help="folder with source files")
    parser.add_argument("--bib", type=Path, default=ROOT / "references.bib", help="bibliography file")
    args = parser.parse_args()

    sources_dir = args.sources.resolve()
    validator = Draft202012Validator(load_schema())
    bib_keys = bibtex_keys(args.bib)

    files = source_files(sources_dir)
    problems: dict[str, list[str]] = {}
    seen_sources: dict[str, Path] = {}
    seen_requirements: dict[str, Path] = {}

    for path in files:
        rel = str(path.relative_to(sources_dir))
        try:
            data = read_front_matter(path)
        except Exception as exc:  # noqa: BLE001 - report any parsing problem
            problems[rel] = [f"cannot read front matter: {exc}"]
            continue

        errors = [
            f"{'/'.join(str(p) for p in err.absolute_path) or '(root)'}: {err.message}"
            for err in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
        ]
        errors += check_file(path, data, sources_dir, bib_keys)

        sid = data.get("id")
        if sid in seen_sources:
            errors.append(f"source ID {sid} is also used in {seen_sources[sid].relative_to(sources_dir)}")
        elif sid:
            seen_sources[sid] = path
        for req in data.get("requirements") or []:
            rid = req.get("id")
            if rid in seen_requirements:
                errors.append(f"requirement ID {rid} is also used in {seen_requirements[rid].relative_to(sources_dir)}")
            elif rid:
                seen_requirements[rid] = path

        if errors:
            problems[rel] = errors

    print(f"Checked {len(files)} source file(s) with {len(seen_requirements)} requirement(s) in {sources_dir}.")
    if problems:
        for rel, errors in problems.items():
            print(f"\n{rel}")
            for err in errors:
                print(f"  - {err}")
        print(f"\n{sum(len(e) for e in problems.values())} error(s) found.")
        return 1
    print("No errors found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
