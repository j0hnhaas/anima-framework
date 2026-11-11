# Methodology

This document describes how ANIMA selects, maps, verifies and maintains its sources. It is the basis for the scientific quality of the framework. Codes are defined in [vocabulary.md](vocabulary.md), the model in [model/README.md](../model/README.md).

## 1. Source selection

A source is included if it meets **all** of the following criteria:

1. **Relevance:** it concerns psychology as a profession or psychological effects of AI (see [scope.md](scope.md)).
2. **Mappability:** at least one of its requirements or recommendations can be placed on the triad.
3. **Authority:** it is issued by a body with a recognised mandate (legislator, authority, international organisation, professional body) or, for the evidence pillar, is peer-reviewed.
4. **Availability:** an official, publicly accessible version exists and can be linked.
5. **Currency:** it is in force or current, or it is explicitly marked as historical.

Primary sources are always preferred over secondary sources (e.g. the AI Act in EUR-Lex rather than a commentary on it).

## 2. Pillars and bindingness

Each source belongs to one pillar – law, guidance or professional – and has one degree of bindingness. Evidence is a separate pillar and is assessed separately (section 7).

| Bindingness | Pillar | Weight |
|---|---|---|
| `binding` | law | defines what is **required** |
| `official` | guidance | shows how the law is **interpreted and applied** |
| `recommended` | guidance | describes **good practice** |
| `professional` | professional | describes **good practice**; binding for members where adopted |

**Precedence.** What is *required* is decided by binding law. Official guidance interprets it. Recommendations and professional standards describe good practice and may go further than the law, but never override it.

**Within binding law,** EU law takes precedence over national law. National law can specify or add to EU requirements where EU law allows it, for example in professional law or under opening clauses of the GDPR.

**International references** from outside the EU (e.g. United Kingdom, United States) are used as good practice only.

## 3. Mapping onto the triad

The unit of mapping is the **requirement**: a single obligation, prohibition or recommendation taken from a source. A source usually contains several requirements.

Each requirement is mapped as follows.

| Field | Question | Rule |
|---|---|---|
| **Edge** | Which relationship does the requirement govern? | `C-AI` if it governs what the AI system does towards the person who uses it or is affected by it; `P-AI` if it governs how the practitioner uses or oversees the AI system; `C-P` if it governs what the practitioner owes the client with regard to AI; `F-AI` if it governs AI use by an organisation or for third parties. Several edges are possible; the main edge comes first. |
| **Flow** | What does the requirement regulate? | `information`, `influence`, `relationship` or `responsibility`; one or two flows. |
| **Configuration** | In which situations can the requirement take effect? | List every configuration in which the requirement can apply. Example: a duty of the practitioner cannot take effect in configuration 3, because there is no practitioner. |
| **Addressee** | Who must act? | Follow the wording of the source. If the source addresses several parties, map each as a separate requirement. |
| **Topic** | Which topic does it belong to? | One topic from the vocabulary. |
| **Spectrum** | Where on the spectrum does it apply? | One or more stages. |

**Mapping notes.** Where a mapping is not obvious, the reasoning is written down in a short note next to the requirement.

**Gaps.** If no source assigns a duty for an edge, flow or configuration, this is recorded as a **gap** in the navigator. Gaps are never filled with assumptions.

## 4. Summarising

- Every source is summarised with the [source summary template](../templates/source-summary.md).
- Summaries are written **in the contributor's own words**. Quotes are short, marked and only used where the exact wording matters.
- Each requirement receives a stable ID (e.g. `ANIMA-TRANS-001`) and is mapped as described in section 3.
- National law may be quoted in its original language, with an English summary.

## 5. Verification

1. **Four-eyes principle:** every new or changed summary and mapping is reviewed by at least one person other than the author.
2. **Status:** content is marked `draft` until it has been reviewed, and `reviewed` afterwards. In the build-up phase (see [GOVERNANCE.md](../GOVERNANCE.md#build-up-phase-before-v10)) content can be merged as `draft`.
3. **Expertise:** legal content should be reviewed by someone with legal expertise, psychological content by a psychologist, where available.
4. **Traceability:** each summary records the date on which the source was checked (`checked`) and by whom (`checked_by`).
5. **Open questions** that could not be resolved are recorded in the summary, not silently omitted.

## 6. Updates

- **Event-driven:** when a source changes (new law, amendment, new guidance), the affected summaries are updated as soon as possible.
- **Scheduled:** every source is reviewed at least **once a year**. Summaries whose `checked` date is older than 12 months are considered due for review.
- Changes are recorded in the [CHANGELOG](../CHANGELOG.md).

## 7. Evidence *(planned)*

The evidence pillar will collect research on the psychological effects of AI and on AI use in psychological work. Its certainty will be rated separately from bindingness, following the logic of **GRADE** (high, moderate, low, very low). The detailed method – search strategy, inclusion criteria, rating – will be defined before the pillar is added.

## 8. Versioning

ANIMA uses [Semantic Versioning](https://semver.org), adapted to a content framework:

| Change | Version step | Example |
|---|---|---|
| Structural change, requirement IDs removed or redefined | **MAJOR** (1.0.0 → 2.0.0) | new element in the model |
| New sources, new requirements, new country | **MINOR** (1.0.0 → 1.1.0) | EU law completed |
| Corrections, clarifications, updated `checked` dates | **PATCH** (1.0.0 → 1.0.1) | typo, outdated link |

**Before version 1.0,** the structure is still being built. Structural changes are then released as MINOR versions (e.g. 0.1.0 → 0.2.0).

Every release is archived on Zenodo and receives its own DOI. Requirement IDs are never reused.

## 9. Use of AI tools

ANIMA is a framework about AI, and AI tools may be used to help build it, for example for drafting, translating or structuring text. The following rules apply:

- AI-generated content is **never merged without human verification** against the original source.
- The person who submits AI-assisted content is responsible for its accuracy.
- Substantial AI assistance is disclosed in the pull request.

## 10. Limitations

ANIMA provides orientation. It does not replace the original sources, legal advice or professional judgement. Interpretations of law in ANIMA reflect the understanding of the contributors at the time of checking and may differ from the views of authorities or courts. Mappings onto the triad are judgements and may be revised.
