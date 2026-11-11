# ANIMA – AI Navigator for Informed Mental Health Applications

[![DOI](https://zenodo.org/badge/1454081110.svg)](https://doi.org/10.5281/zenodo.24138892)

**An open European framework for AI in psychology, from WHO guidance to national law.**

ANIMA brings together, in one place, what applies when artificial intelligence is used in psychology and mental health:

1. **WHO global** recommendations
2. **WHO Europe** recommendations
3. **EU law** (AI Act, GDPR, MDR, EHDS …)
4. **National law** (starting with Austria, open for other countries)

ANIMA is a navigator, not a norm. It helps practitioners, developers, institutions and individuals find their way through the requirements. It does not replace them.

> **Status:** early draft (v0.1). Structure and scope are being set up. Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Who is it for?

- **Psychologists and psychotherapists** who use AI in their practice
- **Clinics, universities and institutions** that write internal guidelines
- **Developers** of mental health and wellness apps
- **People who use AI on their own**, for example chatbots for emotional support

## Scope at a glance

ANIMA describes every requirement along three axes. Details are in [docs/scope.md](docs/scope.md).

| Axis | Values |
|---|---|
| **Regulatory layer** | WHO global → WHO Europe → EU → national |
| **Usage context** | professional-led · professional-supervised · self-directed |
| **Spectrum** | wellbeing → prevention → diagnostics and treatment |

*Mental health* is understood in the broad sense of the WHO: a state of mental well-being, not only the absence of illness. Wellness apps are therefore in scope.

## Repository structure

```
├── 01-who-global/     WHO global guidance
├── 02-who-europe/     WHO Regional Office for Europe
├── 03-eu/             EU law
├── 04-national/       national law, one folder per country
│   └── at/            Austria
├── crosswalk/         mapping: which requirement applies where
├── data/              machine-readable data (CSV/JSON)
├── docs/              scope, methodology, vocabulary
├── templates/         template for source summaries
└── references.bib     central bibliography
```

## Documentation

| Document | Content |
|---|---|
| [Model: the triad](model/README.md) | Client, practitioner and AI system – the model every source is mapped onto |
| [Scope and definitions](docs/scope.md) | What ANIMA covers: layers, usage contexts, spectrum |
| [Methodology](docs/methodology.md) | How sources are selected, weighted, verified and updated |
| [Controlled vocabulary](docs/vocabulary.md) | Codes for layers, levels, contexts, spectrum and topics |
| [Source summary template](templates/source-summary.md) | Structure every source summary follows |
| [Contributing](CONTRIBUTING.md) | How to contribute, DCO |
| [Governance](GOVERNANCE.md) | Roles, decision making, conflicts of interest |
| [Code of conduct](CODE_OF_CONDUCT.md) | How we work together |
| [Security](SECURITY.md) | How to report personal data or sensitive problems |
| [Changelog](CHANGELOG.md) | Changes per version, with DOIs |

## Languages

The framework is written in **English** so it can be used across Europe. National layers may quote the law in its original language (e.g. German for Austria) with an English summary.

## How to cite

If you use ANIMA, please cite it. The citation metadata is in [CITATION.cff](CITATION.cff); GitHub shows a ready-made citation under **"Cite this repository"** in the sidebar.

> Haas, J. G. (2026). *ANIMA – AI Navigator for Informed Mental Health Applications* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.24138892

This DOI always points to the latest version. Every release is archived on [Zenodo](https://doi.org/10.5281/zenodo.24138892) with its own version DOI; use that one if you need to cite a specific version.

| Version | DOI |
|---|---|
| 0.1.0 | [10.5281/zenodo.24138893](https://doi.org/10.5281/zenodo.24138893) |

## Maintainer

**Mag. John G. Haas** – initiator and maintainer · ORCID [0000-0002-4591-5015](https://orcid.org/0000-0002-4591-5015)

## Acknowledgements

The initial structure and documentation of ANIMA were drafted with the assistance of AI models – Claude (Anthropic) and ChatGPT (OpenAI) – and reviewed, revised and approved by the maintainer. AI models are tools, not authors; responsibility for all content lies with the maintainers. Content summaries are verified against the original sources in accordance with the [methodology](docs/methodology.md#7-use-of-ai-tools).

## Licence

- **Content** (texts, guides, checklists): [CC BY 4.0](LICENSES/CC-BY-4.0.txt)
- **Data** (`data/`): [CC0 1.0](LICENSES/CC0-1.0.txt)
- **Code** (website layout, scripts): [EUPL-1.2](LICENSES/EUPL-1.2.txt)

Licences are assigned per file in [REUSE.toml](REUSE.toml), following the [REUSE](https://reuse.software) specification of the FSFE.

Quoted WHO documents keep their own licences (usually CC BY-NC-SA 3.0 IGO). ANIMA therefore summarises them in its own words, quotes only briefly and links to the original.

## Disclaimer

ANIMA is an **independent initiative**. It is not affiliated with, endorsed by or acting on behalf of the WHO, the European Union or any national authority.

The content is provided for orientation only. It is **not legal advice** and **not a treatment recommendation**. Always check the original sources and, where needed, consult qualified professionals.

## Kurzfassung (Deutsch)

ANIMA ist ein offenes europäisches Framework für den Einsatz von KI in der Psychologie. Es führt WHO-Empfehlungen (global und Europa), EU-Recht und nationales Recht – beginnend mit Österreich – an einem Ort zusammen. ANIMA ist eine unabhängige Initiative und stellt keine Rechtsberatung und keine Behandlungsempfehlung dar.
