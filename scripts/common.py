"""Shared helpers for the ANIMA scripts: reading source files and the model rules."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "source.schema.json"
SOURCES_DIR = ROOT / "sources"

# Edges that are active in each configuration of the triad (model/README.md, section 4).
ACTIVE_EDGES = {
    1: {"C-P", "C-AI", "P-AI"},
    2: {"C-P", "P-AI"},
    3: {"C-AI"},
    4: {"C-P", "C-AI"},
    5: {"C-P", "P-AI"},
    6: {"P-AI", "F-AI"},
}

EDGES = ["C-P", "C-AI", "P-AI", "F-AI"]
FLOWS = ["information", "influence", "relationship", "responsibility"]


def _stringify_dates(value):
    """YAML turns ISO dates into date objects; the schema expects strings."""
    if isinstance(value, (dt.date, dt.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _stringify_dates(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_stringify_dates(v) for v in value]
    return value


def read_front_matter(path: Path) -> dict:
    """Return the YAML front matter of a Markdown file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("file does not start with YAML front matter ('---')")
    try:
        _, block, _ = text.split("---\n", 2)
    except ValueError as exc:
        raise ValueError("front matter is not closed with '---'") from exc
    data = yaml.safe_load(block) or {}
    if not isinstance(data, dict):
        raise ValueError("front matter is not a mapping")
    return _stringify_dates(data)


def source_files(sources_dir: Path) -> list[Path]:
    """All source files below sources_dir, excluding README files."""
    return sorted(p for p in sources_dir.rglob("*.md") if p.name.lower() != "readme.md")


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
