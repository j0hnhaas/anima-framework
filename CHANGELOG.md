# Changelog

All notable changes to ANIMA are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning follows the rules in [docs/methodology.md](docs/methodology.md#8-versioning). Every release is archived on Zenodo with its own DOI; the concept DOI [10.5281/zenodo.24138892](https://doi.org/10.5281/zenodo.24138892) always resolves to the latest version.

## [Unreleased]

### Added
- **Search protocol** (`docs/search-protocol.md`) following JBI scoping-review methodology, PRISMA-ScR and PRISMA-S: review question (PCC), eligibility criteria and exclusion reasons E1–E8, information sources per pillar, search terms, process, AI assistance, two-stage screening, data management, updates
- **Search log and candidate register** (`search/`), with the preliminary list of 34 candidates; generated search flow (`search/flow.md`)
- Validation of the search log and candidate register; test fixture with deliberate errors
- **Roadmap** (`ROADMAP.md`) with the next phases – incl. a bilingual website and further EU languages – and criteria proposed for version 1.0
- **Glossary** (`docs/glossary.md`) with the terms defined so far; **FAQ** (`docs/faq.md`) with answers about ANIMA and planned content questions per audience; concept for **practice guides** (`guides/`)
- Glossary and FAQ in the website navigation

### Changed
- Candidate sources moved from the pillar READMEs to the candidate register

## [0.2.0] – 2026-11-11

DOI: [10.5281/zenodo.24145323](https://doi.org/10.5281/zenodo.24145323)

ANIMA is restructured around one model, the **triad of client, practitioner and AI system**, and re-scoped to psychology as a profession and psychological effects of AI. The structure is complete; sources are listed as candidates and have not yet been summarised. See the roadmap in [#10](https://github.com/j0hnhaas/anima-framework/issues/10).

### Added
- **Model:** the triad with nodes, edges, flows, configurations 1–6, frame and addressee; figure; origin in the literature (`model/`)
- **Sources in pillars:** `sources/law`, `sources/guidance`, `sources/professional` with candidate sources (to be verified), incl. Council of Europe AI convention, UNESCO, OECD, EFPA, and international references (NICE, MHRA, BfArM, FDA, APA, BPS)
- **Evidence pillar** prepared (`evidence/`), to be rated following GRADE
- **Navigator** (`navigator/`): all requirements on the triad, with coverage and gaps
- **Data format and validation:** one file per source with YAML front matter; JSON Schema; `scripts/validate.py` and `scripts/build.py`; workflow that tests the validator, validates sources and checks the navigator
- **Methodology:** source selection, pillars and bindingness, rules for mapping onto the triad, gaps, verification with status `draft`/`reviewed`, updates, versioning, use of AI tools
- **Controlled vocabulary** (`docs/vocabulary.md`) incl. active edges per configuration
- **Governance** with rules for the build-up phase before v1.0, declarations of the maintainer; **code of conduct**; **security policy**
- **Website** layout with privacy-friendly page-view counting (GoatCounter, no cookies) and a privacy notice
- Issue forms, central bibliography, Dependabot, `.gitignore`, this changelog
- EUPL-1.2 licence for code; `.zenodo.json` so releases are archived as a dataset
- Acknowledgements disclosing AI assistance (Claude, ChatGPT)

### Changed
- **Scope:** psychology as a profession and psychological effects of AI, also without any practitioner; psychotherapy and psychiatry out of scope as professions
- Sources organised in pillars with jurisdiction and bindingness instead of geographic layers
- Usage contexts replaced by the configurations of the triad
- README, citation metadata and contributing guidelines rewritten for the new structure

### Removed
- Folders `01-who-global`, `02-who-europe`, `03-eu`, `04-national` and `crosswalk/`
- Psychotherapy law from the candidate sources (out of scope)

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

[Unreleased]: https://github.com/j0hnhaas/anima-framework/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/j0hnhaas/anima-framework/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/j0hnhaas/anima-framework/releases/tag/v0.1.0
