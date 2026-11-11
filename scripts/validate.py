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
import csv
import datetime as dt
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from common import ACTIVE_EDGES, ROOT, SEARCH_DIR, SOURCES_DIR, load_schema, read_front_matter, source_files

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


# --- Search log and candidate register (search/README.md) ---------------------

LOG_COLUMNS = ["search_id", "date", "pillar", "strategy", "resource", "url", "query", "filters",
               "results_total", "results_screened", "candidates_added", "searcher", "notes"]
CANDIDATE_COLUMNS = ["candidate_id", "title", "issuer", "year", "url", "pillar", "jurisdiction", "document_type",
                     "language", "identified_via", "search_id", "date_identified", "title_screening",
                     "full_text_screening", "exclusion_reason", "source_id", "screened_by", "notes"]
STRATEGIES = {"database", "website", "web_search", "citation", "expert", "ai_assisted"}
DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")


def read_csv(path: Path, columns: list[str]) -> tuple[list[dict], list[str]]:
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != columns:
            return [], [f"columns must be: {', '.join(columns)}"]
        return list(reader), []


def check_search(search_dir: Path) -> dict[str, list[str]]:
    """Check search-log.csv and candidates.csv against the rules in search/README.md."""
    problems: dict[str, list[str]] = {}
    log_path, cand_path = search_dir / "search-log.csv", search_dir / "candidates.csv"
    if not log_path.exists() and not cand_path.exists():
        return problems

    log, errors = read_csv(log_path, LOG_COLUMNS) if log_path.exists() else ([], ["file is missing"])
    search_ids: set[str] = set()
    for n, row in enumerate(log, start=2):
        where = f"line {n} ({row.get('search_id') or '?'})"
        sid = row["search_id"]
        if not re.fullmatch(r"S-[0-9]{3}", sid):
            errors.append(f"{where}: search_id must look like S-001")
        if sid in search_ids:
            errors.append(f"{where}: search_id is used twice")
        search_ids.add(sid)
        if not DATE.match(row["date"]):
            errors.append(f"{where}: date must be YYYY-MM-DD")
        if row["pillar"] not in {"law", "guidance", "professional", "all"}:
            errors.append(f"{where}: unknown pillar '{row['pillar']}'")
        if row["strategy"] not in STRATEGIES:
            errors.append(f"{where}: unknown strategy '{row['strategy']}'")
        if not row["resource"] or not row["query"]:
            errors.append(f"{where}: resource and query are required")
        for col in ("results_total", "results_screened", "candidates_added"):
            if row[col] and not row[col].isdigit():
                errors.append(f"{where}: {col} must be a number")
    if errors:
        problems[str(log_path.relative_to(ROOT)) if log_path.is_relative_to(ROOT) else str(log_path)] = errors

    rows, errors = read_csv(cand_path, CANDIDATE_COLUMNS) if cand_path.exists() else ([], ["file is missing"])
    cand_ids: set[str] = set()
    for n, row in enumerate(rows, start=2):
        where = f"line {n} ({row.get('candidate_id') or '?'})"
        cid = row["candidate_id"]
        if not re.fullmatch(r"CAND-[0-9]{4}", cid):
            errors.append(f"{where}: candidate_id must look like CAND-0001")
        if cid in cand_ids:
            errors.append(f"{where}: candidate_id is used twice")
        cand_ids.add(cid)
        if not row["title"] or not row["issuer"]:
            errors.append(f"{where}: title and issuer are required")
        if row["year"] and not re.fullmatch(r"[0-9]{4}", row["year"]):
            errors.append(f"{where}: year must be YYYY")
        if row["url"] and not row["url"].startswith(("http://", "https://")):
            errors.append(f"{where}: url must start with http(s)://")
        if row["pillar"] not in {"law", "guidance", "professional", "unknown"}:
            errors.append(f"{where}: unknown pillar '{row['pillar']}'")
        if not re.fullmatch(r"global|europe|eu|unknown|[a-z]{2}", row["jurisdiction"]):
            errors.append(f"{where}: unknown jurisdiction '{row['jurisdiction']}'")
        if row["document_type"] not in {"law", "treaty", "guideline", "recommendation", "code", "statement", "report", "other"}:
            errors.append(f"{where}: unknown document_type '{row['document_type']}'")
        if not re.fullmatch(r"[a-z]{2}", row["language"]):
            errors.append(f"{where}: language must be an ISO 639-1 code, e.g. en")
        via = row["identified_via"]
        if via not in STRATEGIES | {"preliminary"}:
            errors.append(f"{where}: unknown identified_via '{via}'")
        if via == "preliminary":
            if row["search_id"]:
                errors.append(f"{where}: preliminary entries have no search_id")
        elif row["search_id"] not in search_ids:
            errors.append(f"{where}: search_id '{row['search_id']}' not found in the search log")
        if not DATE.match(row["date_identified"]):
            errors.append(f"{where}: date_identified must be YYYY-MM-DD")

        title, full = row["title_screening"], row["full_text_screening"]
        reason, source_id = row["exclusion_reason"], row["source_id"]
        if title not in {"pending", "include", "exclude", "unclear"}:
            errors.append(f"{where}: unknown title_screening '{title}'")
        if full not in {"pending", "include", "exclude", "unclear", "not_reached"}:
            errors.append(f"{where}: unknown full_text_screening '{full}'")
        if title == "exclude" and full != "not_reached":
            errors.append(f"{where}: excluded at title screening, so full_text_screening must be not_reached")
        if title != "exclude" and full == "not_reached":
            errors.append(f"{where}: full_text_screening is not_reached, but the title was not excluded")
        if title == "pending" and full != "pending":
            errors.append(f"{where}: full text cannot be screened before the title")
        excluded = title == "exclude" or full == "exclude"
        if excluded and not re.fullmatch(r"E[1-8]", reason):
            errors.append(f"{where}: excluded documents need an exclusion_reason E1–E8")
        if not excluded and reason:
            errors.append(f"{where}: exclusion_reason given, but the document is not excluded")
        if source_id and (full != "include" or not re.fullmatch(r"SRC-[A-Z]+-[0-9]{3}", source_id)):
            errors.append(f"{where}: source_id only for documents included at full text, format SRC-XX-000")
    if errors:
        problems[str(cand_path.relative_to(ROOT)) if cand_path.is_relative_to(ROOT) else str(cand_path)] = errors
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--sources", type=Path, default=SOURCES_DIR, help="folder with source files")
    parser.add_argument("--bib", type=Path, default=ROOT / "references.bib", help="bibliography file")
    parser.add_argument("--search", type=Path, default=SEARCH_DIR, help="folder with search log and candidate register")
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
    search_problems = check_search(args.search.resolve())
    problems.update(search_problems)
    print(f"Checked search log and candidate register in {args.search}.")
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
