# Search protocol

This protocol describes how ANIMA identifies, screens and selects sources for the pillars law, guidance and professional. It is written before the search and follows established practice for scoping reviews and grey-literature searches. Changes to the protocol are recorded in section 11.

| | |
|---|---|
| **Version** | 1.0 |
| **Date** | 2026-11-11 |
| **Status** | in force |
| **Applies to** | pillars `law`, `guidance`, `professional` |
| **Not covered** | the evidence pillar (scientific literature) – it receives its own protocol before it is filled |

## 1. Purpose and review question

**Review question:** *Which binding rules, official guidance, recommendations and professional standards apply to the use of AI systems in psychology as a profession, and to the psychological effects of AI systems on people?*

The question is framed with the **PCC** elements recommended for scoping reviews (Peters et al., 2020):

| Element | Definition in ANIMA |
|---|---|
| **Population** | practitioners (psychologists), clients and other people who are psychologically affected by AI systems – the nodes of the [triad](../model/README.md) |
| **Concept** | requirements, prohibitions and recommendations concerning AI systems – their design, use, oversight and effects |
| **Context** | the pillars law, guidance and professional; jurisdictions global, pan-European, EU, Austria, and international references (see [scope](scope.md)) |

## 2. Methodological basis

- **Conduct:** JBI methodology for scoping reviews (Peters et al., 2020).
- **Reporting:** PRISMA extension for scoping reviews, PRISMA-ScR (Tricco et al., 2018), and PRISMA-S for reporting the search itself (Rethlefsen et al., 2021).
- **Grey literature:** most sources in these pillars are grey literature – laws, guidelines, codes and statements published outside academic journals. ANIMA therefore combines **four complementary search strategies**, as proposed by Godin et al. (2015): (1) databases and registries, (2) web search engines, (3) targeted websites of issuers, and (4) consultation of experts. Two further strategies are added: (5) citation chasing in included documents and (6) AI-assisted searching (section 7).

## 3. Eligibility criteria

The selection criteria of the [methodology](methodology.md#1-source-selection) apply. They are operationalised as follows.

### Inclusion

A document is included if **all** of the following apply:

1. It contains at least one requirement, prohibition or recommendation that concerns AI systems, or that applies to AI systems even if it does not name them (e.g. data protection law, professional duties of psychologists).
2. It concerns psychology as a profession or psychological effects of AI (see [scope](scope.md#1-subject)).
3. It is issued by a legislator, an authority, an international organisation or a professional body.
4. An official version is publicly accessible.
5. It is in force or current on the date of screening.

**No date limit** is set: older documents are included if they are still in force or current (e.g. ethics codes, data protection law).

**Languages:** English and German. Documents in other languages are included if an official English version exists.

**Drafts and proposals** (e.g. legislative proposals, consultation drafts) are not included as sources, but recorded with a note so they can be followed up.

### Exclusion reasons

Each excluded document receives **one** reason – the first that applies, in this order:

| Code | Reason |
|---|---|
| `E1` | **Topic:** does not concern AI systems, or concerns AI without relevance to psychology or psychological effects |
| `E2` | **Profession out of scope:** concerns psychotherapy or psychiatry as professions only |
| `E3` | **Issuer:** not issued by a legislator, authority, international organisation or professional body (e.g. commentary, news, vendor material) |
| `E4` | **Not current:** repealed, superseded or withdrawn |
| `E5` | **Duplicate:** another version or a duplicate of a document already recorded |
| `E6` | **No requirement:** contains no requirement or recommendation that can be mapped onto the triad |
| `E7` | **Not accessible:** no official, publicly accessible version |
| `E8` | **Language:** neither English nor German, and no official English version |

## 4. Information sources

The following resources are searched. The list can be extended; every addition is recorded as an amendment (section 11).

### Law

| Resource | Strategy |
|---|---|
| EUR-Lex – EU legislation | database |
| Council of Europe Treaty Office | database |
| RIS – Rechtsinformationssystem des Bundes (Austria) | database |

### Guidance

| Resource | Strategy |
|---|---|
| WHO Institutional Repository for Information Sharing (IRIS) | database |
| WHO Regional Office for Europe – publications | website |
| European Commission – AI Office and digital strategy pages | website |
| Medical Device Coordination Group (MDCG) – guidance documents | website |
| European Data Protection Board – guidelines | website |
| OECD.AI policy observatory; UNESCO | website |
| Austrian Federal Ministry responsible for health; RTR (AI service desk); Datenschutzbehörde | website |
| International references: NICE, MHRA (United Kingdom), BfArM (Germany), FDA (United States) | website |

### Professional

| Resource | Strategy |
|---|---|
| EFPA – European Federation of Psychologists' Associations | website |
| Member associations of EFPA, starting with BÖP (Austria) | website |
| International references: American Psychological Association (APA), British Psychological Society (BPS) | website |

### Across all pillars

| Resource | Strategy |
|---|---|
| General web search engine | web search |
| References in included documents (backward) and documents citing them (forward) | citation chasing |
| Experts in psychology, law and AI governance – via the repository (issues, discussions) and professional networks | expert consultation |

## 5. Search terms

Searches combine three concept blocks. Block C is used where a resource returns too many results.

| Block | English | German |
|---|---|---|
| **A – AI** | artificial intelligence, AI, machine learning, algorithm\*, chatbot\*, large language model\*, generative AI, automated decision\* | künstliche Intelligenz, KI, maschinelles Lernen, Algorithm\*, Chatbot\*, Sprachmodell\*, generative KI, automatisierte Entscheidung\* |
| **B – Psychology** | psycholog\*, mental health, wellbeing, psychological assessment, psychological test\*, emotion\* | Psycholog\*, psychische Gesundheit, Wohlbefinden, psychologische Diagnostik, psychologische\* Test\*, Emotion\* |
| **C – Normative** | guideline\*, guidance, recommendation\*, code of ethics, code of conduct, regulation, standard\* | Leitlinie\*, Richtlinie\*, Empfehlung\*, Ethikkodex, Berufsethik, Verordnung, Gesetz |

**Combination:** A AND B, optionally AND C. Example: `("artificial intelligence" OR chatbot*) AND (psycholog* OR "mental health")`.

Resources differ in their search functions. The exact string used in each resource – or, for websites without a search function, the pages browsed – is recorded in the search log.

## 6. Search process

1. Every search is recorded in the **search log** ([search/search-log.csv](../search/search-log.csv)) with date, resource, strategy, exact query, filters and number of results.
2. **Websites** are searched with their own search function where available, and their publication pages are browsed.
3. **Web search engines:** the first **50 results** per query are screened. Searches are run without being signed in, to reduce personalisation.
4. **Citation chasing** is done for every document included at full-text stage.
5. Every potentially relevant document is entered in the **candidate register** ([search/candidates.csv](../search/candidates.csv)) with the ID of the search that found it. Documents found more than once are entered only once; the first search is recorded.

## 7. Use of AI tools in the search

AI tools may be used to propose search terms, find candidate documents and summarise documents for screening. The [rules for AI tools](methodology.md#9-use-of-ai-tools) apply, and in addition:

- Candidates found with AI assistance are recorded with `identified_via = ai_assisted`.
- Every such candidate is checked against the **official source** before screening: title, issuer, date and current status.
- **Screening decisions are made by a person**, not by an AI tool.

## 8. Screening and selection

Screening takes place in two stages, as is usual in scoping reviews:

1. **Title and summary:** title, abstract, executive summary or table of contents.
2. **Full text:** against all eligibility criteria (section 3).

Decisions are `include`, `exclude` or `unclear`. *Unclear* at stage 1 leads to full-text screening; *unclear* at stage 2 is resolved by discussion and documented in a note.

**Screeners.** Best practice is independent screening by two people. In the [build-up phase](../GOVERNANCE.md#build-up-phase-before-v10), screening is done by one person (the maintainer). This is a **limitation** and is reported as such. Once reviewers are available, at least **20 %** of the decisions at each stage are screened independently by a second person, and agreement is reported.

**Preliminary list.** Before this protocol was written, a list of likely sources was compiled from the maintainer's knowledge, with AI assistance. These documents are recorded in the register with `identified_via = preliminary` and go through the same screening as all other candidates.

## 9. Data management

- **Search log** and **candidate register** are kept as CSV files in [`search/`](../search/), with the fields described in [search/README.md](../search/README.md). Their values are checked automatically in every pull request.
- **Reference management:** bibliographic records of all candidates are kept in a **Zotero** library. Each record is tagged with its candidate ID (e.g. `CAND-0001`) and its screening decision, so that the library and the register stay aligned. Included documents are exported to [references.bib](../references.bib).
- **Included documents** become source files in [`sources/`](../sources/). The register links each included document to its source file (`source_id`).
- **Scientific references** cited in ANIMA – for example in the model and in this protocol – are checked for retractions and corrections before they are cited.
- **Full-text copies** of documents are kept privately by the maintainers for screening and summarising. They are not published in the repository, because many sources are protected by copyright or published under licences that do not allow redistribution.

## 10. Reporting and updates

- The **flow of documents** through identification, screening and inclusion is generated from the register by `scripts/build.py` and published in [search/flow.md](../search/flow.md), following the flow diagram of PRISMA-ScR.
- The search is **updated** before each MINOR release and at least **once a year**. Update searches cover the period since the last search; their date is recorded in the search log.

## 11. Amendments

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-11-11 | First version |

## References

Godin, K., Stapleton, J., Kirkpatrick, S. I., Hanning, R. M., & Leatherdale, S. T. (2015). Applying systematic review search methods to the grey literature: A case study examining guidelines for school-based breakfast programs in Canada. *Systematic Reviews, 4*, 138. https://doi.org/10.1186/s13643-015-0125-0

Peters, M. D. J., Marnie, C., Tricco, A. C., Pollock, D., Munn, Z., Alexander, L., McInerney, P., Godfrey, C. M., & Khalil, H. (2020). Updated methodological guidance for the conduct of scoping reviews. *JBI Evidence Synthesis, 18*(10), 2119–2126. https://doi.org/10.11124/JBIES-20-00167

Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., Ayala, A. P., Moher, D., Page, M. J., Koffel, J. B., & PRISMA-S Group. (2021). PRISMA-S: An extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. *Systematic Reviews, 10*, 39. https://doi.org/10.1186/s13643-020-01542-z

Tricco, A. C., Lillie, E., Zarin, W., O'Brien, K. K., Colquhoun, H., Levac, D., Moher, D., Peters, M. D. J., Horsley, T., Weeks, L., Hempel, S., Akl, E. A., Chang, C., McGowan, J., Stewart, L., Hartling, L., Aldcroft, A., Wilson, M. G., Garritty, C., … Straus, S. E. (2018). PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and explanation. *Annals of Internal Medicine, 169*(7), 467–473. https://doi.org/10.7326/M18-0850
