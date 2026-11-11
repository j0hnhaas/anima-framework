# Changelog

All notable changes to ANIMA are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning follows the rules in [docs/methodology.md](docs/methodology.md#6-versioning). Every release is archived on Zenodo with its own DOI; the concept DOI [10.5281/zenodo.24138892](https://doi.org/10.5281/zenodo.24138892) always resolves to the latest version.

## [Unreleased]

### Added
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
