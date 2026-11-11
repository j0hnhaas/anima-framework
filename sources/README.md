# Sources

ANIMA organises its sources in three pillars. A fourth pillar, evidence, follows in a later version (see [evidence/](../evidence/)).

| Pillar | Folder | Question |
|---|---|---|
| **Law** | [`law/`](law/) | What is binding? |
| **Guidance** | [`guidance/`](guidance/) | What do public bodies recommend, and how do they interpret the law? |
| **Professional** | [`professional/`](professional/) | What do professional bodies require of their members or recommend? |

Pillars, jurisdictions and degrees of bindingness are defined in [docs/scope.md](../docs/scope.md) and [docs/vocabulary.md](../docs/vocabulary.md).

## Where source files go

Each source is one file, placed by pillar and jurisdiction:

```
sources/<pillar>/<jurisdiction>/<short-name>.md
```

Examples: `sources/law/eu/ai-act.md`, `sources/law/at/psychologengesetz.md`, `sources/professional/europe/efpa-meta-code.md`.

Folders for a jurisdiction are created together with the first source file. Each file follows the [source template](../templates/source-summary.md); its requirements are mapped onto the [triad](../model/README.md) as described in the [methodology](../docs/methodology.md#3-mapping-onto-the-triad).

## Candidate sources

Each pillar folder contains a list of **candidate sources**. These are sources that probably meet the selection criteria but have **not yet been checked**. Before a candidate is summarised, its title, version and current status must be verified against the official source.

## Adding a country

National sources are welcome for any country. Create the jurisdiction folder (ISO 3166-1 alpha-2 code in lower case, e.g. `de`) in the matching pillar, add the source following the template, and open a pull request (see [CONTRIBUTING.md](../CONTRIBUTING.md)). National law may be quoted in its original language, with an English summary.
