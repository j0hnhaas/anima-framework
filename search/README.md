# Search

The documented search for sources, following the [search protocol](../docs/search-protocol.md).

| File | Content |
|---|---|
| [search-log.csv](search-log.csv) | every search: where, when, how, with which result |
| [candidates.csv](candidates.csv) | every candidate document and the screening decisions |
| [flow.md](flow.md) | flow of documents from identification to inclusion – generated, do not edit |

Both CSV files can be opened in any spreadsheet program. Keep the column order, use UTF-8 and separate multiple values with `; `. Every pull request checks the allowed values (`scripts/validate.py`); `scripts/build.py` updates `flow.md`.

## Search log – `search-log.csv`

| Column | Content | Allowed values / format |
|---|---|---|
| `search_id` | ID of the search | `S-001`, `S-002` … never reused |
| `date` | date of the search | `YYYY-MM-DD` |
| `pillar` | pillar searched | `law`, `guidance`, `professional`, `all` |
| `strategy` | search strategy | `database`, `website`, `web_search`, `citation`, `expert`, `ai_assisted` |
| `resource` | name of the resource | e.g. EUR-Lex |
| `url` | address of the resource | `https://…` |
| `query` | exact search string, or the pages browsed | free text |
| `filters` | filters and limits used | free text, e.g. "document type: regulation; in force" |
| `results_total` | number of results shown by the resource | number, empty if not available |
| `results_screened` | number of results looked at | number |
| `candidates_added` | number of new entries in the register | number |
| `searcher` | who searched | GitHub user name |
| `notes` | remarks | free text |

## Candidate register – `candidates.csv`

| Column | Content | Allowed values / format |
|---|---|---|
| `candidate_id` | ID of the candidate | `CAND-0001`, `CAND-0002` … never reused |
| `title` | title of the document | as published |
| `issuer` | issuing body | e.g. European Commission |
| `year` | year of publication or adoption | `YYYY`, empty if unknown |
| `url` | official version | `https://…`, may be empty until checked |
| `pillar` | pillar | `law`, `guidance`, `professional`, `unknown` |
| `jurisdiction` | jurisdiction | as in the [vocabulary](../docs/vocabulary.md#jurisdiction), or `unknown` |
| `document_type` | type of document | `law`, `treaty`, `guideline`, `recommendation`, `code`, `statement`, `report`, `other` |
| `language` | language of the official version | ISO 639-1, e.g. `en`, `de` |
| `identified_via` | how it was found | `preliminary`, `database`, `website`, `web_search`, `citation`, `expert`, `ai_assisted` |
| `search_id` | search that found it | `S-…`; empty for `preliminary` |
| `date_identified` | date it was entered | `YYYY-MM-DD` |
| `title_screening` | decision at stage 1 | `pending`, `include`, `exclude`, `unclear` |
| `full_text_screening` | decision at stage 2 | `pending`, `include`, `exclude`, `unclear`, `not_reached` |
| `exclusion_reason` | reason if excluded | `E1` … `E8` (see the [protocol](../docs/search-protocol.md#exclusion-reasons)) |
| `source_id` | source file once included | `SRC-…` |
| `screened_by` | who screened | GitHub user name(s) |
| `notes` | remarks, e.g. on unclear decisions | free text |

### Rules

- Excluded at stage 1 → `full_text_screening` is `not_reached`, and an `exclusion_reason` is given.
- Excluded at stage 2 → an `exclusion_reason` is given.
- Only documents included at stage 2 receive a `source_id`.
- Every `search_id` must exist in the search log, except for `preliminary` entries.
