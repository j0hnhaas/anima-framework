# Methodology

This document describes how ANIMA selects, verifies, summarises and maintains its sources. It is the basis for the scientific quality of the framework.

## 1. Source selection

A source is included if it meets **all** of the following criteria:

1. **Relevance:** it addresses AI, digital health or mental health in a way that affects at least one usage context (see [scope.md](scope.md)).
2. **Authority:** it is issued by a body with a recognised mandate (legislator, regulator, WHO, professional body) or is peer-reviewed.
3. **Availability:** an official, publicly accessible version exists and can be linked.
4. **Currency:** it is in force or current, or it is explicitly marked as historical.

Primary sources are always preferred over secondary sources (e.g. the AI Act in EUR-Lex rather than a commentary on it).

## 2. Source hierarchy

Sources carry different weight. Every requirement in ANIMA states which level it belongs to.

| Level | Type | Binding | Example |
|---|---|---|---|
| **L1** | Binding law | yes | EU regulations, Austrian federal law |
| **L2** | Official guidance by regulators | interpretative | European Commission guidelines, MDCG documents |
| **L3** | WHO recommendations | no | WHO global and WHO Europe guidance |
| **L4** | Professional guidelines and codes | for members | guidelines of professional associations |
| **L5** | Scientific literature | no | peer-reviewed studies and reviews |

If sources conflict, the higher level takes precedence for what is *required*. Lower levels may still describe what is *good practice*.

## 3. Summarising

- Every source is summarised with the [source summary template](../templates/source-summary.md).
- Summaries are written **in the contributor's own words**. Quotes are short, marked and only used where the exact wording matters.
- Each requirement extracted from a source receives a stable ID (e.g. `ANIMA-TRANS-001`) and is classified along the three scope axes.
- National law may be quoted in its original language, with an English summary.

## 4. Verification

1. **Four-eyes principle:** every new or changed summary is reviewed by at least one person other than the author before it is merged.
2. **Expertise:** legal content should be reviewed by someone with legal expertise, clinical content by someone with a background in psychology or psychotherapy, where available.
3. **Traceability:** each summary records the date on which the source was checked (`checked`) and by whom (`checked_by`).
4. **Open questions** that could not be resolved are recorded in the summary, not silently omitted.

## 5. Updates

- **Event-driven:** when a source changes (new law, amendment, new WHO guidance), the affected summaries are updated as soon as possible.
- **Scheduled:** every layer is reviewed at least **once a year**. Summaries whose `checked` date is older than 12 months are considered due for review.
- Changes are recorded in the [CHANGELOG](../CHANGELOG.md).

## 6. Versioning

ANIMA uses [Semantic Versioning](https://semver.org), adapted to a content framework:

| Change | Version step | Example |
|---|---|---|
| Structural change, requirement IDs removed or redefined | **MAJOR** (1.0.0 → 2.0.0) | new axis in the scope |
| New sources, new requirements, new country | **MINOR** (0.1.0 → 0.2.0) | EU layer completed |
| Corrections, clarifications, updated `checked` dates | **PATCH** (0.1.0 → 0.1.1) | typo, outdated link |

Every release is archived on Zenodo and receives its own DOI. Requirement IDs are never reused.

## 7. Use of AI tools

ANIMA is a framework about AI, and AI tools may be used to help build it, for example for drafting, translating or structuring text. The following rules apply:

- AI-generated content is **never merged without human verification** against the original source.
- The person who submits AI-assisted content is responsible for its accuracy.
- Substantial AI assistance is disclosed in the pull request.

## 8. Limitations

ANIMA provides orientation. It does not replace the original sources, legal advice or professional judgement. Interpretations of law in ANIMA reflect the understanding of the contributors at the time of checking and may differ from the views of authorities or courts.
