# Controlled vocabulary

All codes and values used in ANIMA are defined here. Source summaries, the crosswalk and the data files use **only** these values. New values are added via pull request (see [GOVERNANCE.md](../GOVERNANCE.md)).

## Layers

| Code | Layer | Folder | Source ID prefix |
|---|---|---|---|
| `who-global` | WHO global | `01-who-global/` | `SRC-WHO-` |
| `who-europe` | WHO Regional Office for Europe | `02-who-europe/` | `SRC-WHOEU-` |
| `eu` | European Union | `03-eu/` | `SRC-EU-` |
| `national-<cc>` | National law, `<cc>` = ISO 3166-1 alpha-2 code | `04-national/<cc>/` | `SRC-<CC>-` |

Example: Austria → `national-at`, folder `04-national/at/`, source IDs `SRC-AT-001`, `SRC-AT-002` …

## Levels

| Code | Type | Binding |
|---|---|---|
| `L1` | Binding law | yes |
| `L2` | Official guidance by authorities and regulators | interpretative |
| `L3` | WHO recommendations | no |
| `L4` | Professional guidelines and codes of professional bodies | for members |
| `L5` | Scientific literature | no |

See [methodology.md](methodology.md#2-source-hierarchy) for how levels are weighted.

## Usage contexts

| Code | Meaning |
|---|---|
| `professional-led` | A professional uses AI in their own work. |
| `professional-supervised` | Clients use AI as part of, or alongside, a treatment. |
| `self-directed` | People use AI on their own, without a professional. |

## Spectrum

| Code | Meaning |
|---|---|
| `wellbeing` | Stress reduction, mindfulness, mood tracking |
| `prevention` | Early detection, psychoeducation, risk screening |
| `diagnostics-treatment` | Assessment, diagnosis, therapy |

## Topics

Requirement IDs have the form `ANIMA-<TOPIC>-<NUMBER>`, e.g. `ANIMA-TRANS-001`. Numbers have three digits and are never reused.

| Code | Topic | Examples of questions |
|---|---|---|
| `PROH` | Prohibited practices | Is this use of AI forbidden altogether? |
| `TRANS` | Transparency | Do users know they are dealing with AI? |
| `CONS` | Informed consent and autonomy | Have clients agreed to the use of AI? |
| `DATA` | Data protection and privacy | How are health data processed and protected? |
| `SAFE` | Safety and risk management | How are risks identified and reduced? |
| `CRIS` | Crisis and emergency handling | What happens when a user is at risk of harm? |
| `QUAL` | Quality, accuracy and validation | Is the system evidence-based and validated? |
| `EQUI` | Equity and non-discrimination | Does the system work fairly for all groups? |
| `OVERS` | Human oversight | Who checks and can override the AI? |
| `PROF` | Professional duties | What do professional laws and codes require? |
| `LIT` | AI literacy and competence | What do users and professionals need to know? |
| `ACCT` | Accountability and liability | Who is responsible when something goes wrong? |
