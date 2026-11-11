# Changelog

All notable changes to ANIMA are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning follows the rules in [docs/methodology.md](docs/methodology.md#6-versioning). Every release is archived on Zenodo with its own DOI; the concept DOI [10.5281/zenodo.24138892](https://doi.org/10.5281/zenodo.24138892) always resolves to the latest version.

## [Unreleased]

### Added
- Data format: one file per source with YAML front matter holding the source metadata and its requirements mapped onto the triad; JSON Schema (`schema/source.schema.json`)
- Validation script (`scripts/validate.py`): schema, file location, IDs, bindingness per pillar, consistency of edges and configurations
- Navigator generator (`scripts/build.py`): `navigator/requirements.md` with coverage and gaps, `data/navigator.json`, `data/navigator.csv`
- Workflow that validates sources and checks the navigator in every pull request; test fixtures for the validator
- Model: the triad of client, practitioner and AI system with edges, flows, configurations, frame and addressee (`model/README.md`)
- Website layout for GitHub Pages with privacy-friendly page-view counting (GoatCounter, no cookies) and a privacy notice (`privacy.md`)
- EUPL-1.2 licence for code (`LICENSES/EUPL-1.2.txt`)
- Acknowledgements in the README: disclosure of AI assistance (Claude, ChatGPT)
- Methodology: source selection, hierarchy (L1–L5), verification, updates, versioning, use of AI tools (`docs/methodology.md`)
- Source summary template (`templates/source-summary.md`)
- Central bibliography (`references.bib`)
- Governance, code of conduct and this changelog
- Issue forms for source proposals and error reports
- Zenodo metadata (`.zenodo.json`) so releases are archived as a dataset
- Controlled vocabulary for layers, levels, usage contexts, spectrum and topics (`docs/vocabulary.md`)
- Security policy for sensitive reports and personal data (`SECURITY.md`)
- Dependabot for GitHub Actions, `.gitignore`

### Changed
- Source template and issue form use the new fields (pillar, jurisdiction, bindingness, triad)
- New folder structure: `sources/law`, `sources/guidance`, `sources/professional`, `evidence/` (planned) and `navigator/` replace the folders `01-who-global` to `04-national` and `crosswalk/`
- Candidate sources revised to the new scope: psychotherapy law removed; added Council of Europe AI convention, UNESCO, OECD, Commission guidelines, Austrian authorities, EFPA, BÖP, and international references (NICE, MHRA, BfArM, FDA, APA, BPS) – all to be verified
- Scope: psychology as a profession and psychological effects of AI; psychotherapy and psychiatry out of scope as professions (`docs/scope.md`)
- Sources organised in pillars (law, guidance, professional; evidence planned) with jurisdiction and bindingness, replacing the geographic layers and levels L1–L5
- Vocabulary: new codes for pillar, jurisdiction, bindingness, edge, flow, configuration, addressee and status; usage contexts replaced by the configurations of the triad (`docs/vocabulary.md`)
- Methodology: rules for mapping requirements onto the triad, gaps, status `draft`/`reviewed`, evidence pillar based on GRADE (planned), versioning before v1.0 (`docs/methodology.md`)
- Governance: rules for the build-up phase before v1.0 (`GOVERNANCE.md`)
- Crosswalk fields aligned with the vocabulary (`source_id`, `level`, coded values)
- Austrian ministry guidelines classified as official guidance (L2)
- Methodology: precedence of EU law over national law within L1
- Workflow runs with read-only permissions
- Contributing: explicit ban on sharing personal health data

### Fixed
- Full CC BY 4.0 legal code in `LICENSE` so GitHub detects the licence

## [0.1.0] – 2026-11-11

DOI: [10.5281/zenodo.24138893](https://doi.org/10.5281/zenodo.24138893)

### Added
- Initial structure: four regulatory layers (WHO global, WHO Europe, EU, Austria), crosswalk and data folders
- Scope and definitions (`docs/scope.md`)
- Licences (CC BY 4.0 for content, CC0 1.0 for data) via REUSE
- Contribution guidelines with DCO, pull request template, REUSE compliance check
- Citation metadata (`CITATION.cff`) with ORCID, Zenodo DOI

[Unreleased]: https://github.com/j0hnhaas/anima-framework/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/j0hnhaas/anima-framework/releases/tag/v0.1.0
