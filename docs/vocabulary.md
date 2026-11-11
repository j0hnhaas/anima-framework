# Controlled vocabulary

All codes and values used in ANIMA are defined here. Source files, the navigator and the data files use **only** these values. New values are added via pull request (see [GOVERNANCE.md](../GOVERNANCE.md)).

The same values are defined for machines in [schema/source.schema.json](../schema/source.schema.json). Both files must be changed together.

## Sources

### Pillar

| Code | Pillar | Typical bindingness |
|---|---|---|
| `law` | Binding law | `binding` |
| `guidance` | Guidance and interpretation by public bodies | `official` or `recommended` |
| `professional` | Standards of professional bodies | `professional` |
| `evidence` | Research *(planned)* | – |

### Jurisdiction

| Code | Meaning | Examples |
|---|---|---|
| `global` | worldwide | WHO, UNESCO |
| `europe` | pan-European, beyond the EU | WHO Regional Office for Europe, Council of Europe, EFPA |
| `eu` | European Union | EU regulations, European Commission |
| `<cc>` | a single country, ISO 3166-1 alpha-2 code in lower case | `at` Austria, `de` Germany, `gb` United Kingdom, `us` United States |

### Bindingness

| Code | Meaning | Example |
|---|---|---|
| `binding` | legally binding | EU AI Act, national laws |
| `official` | official interpretation or guidance by an authority; not binding itself, but shows how the law is applied | European Commission guidelines, guidance of a national ministry |
| `recommended` | recommendation by a public or international body | WHO guidance, NICE guidance |
| `professional` | code or guideline of a professional body; binding for its members where adopted | ethical codes of associations of psychologists |

Precedence and use of these levels are described in the [methodology](methodology.md#2-pillars-and-bindingness).

### Source ID

`SRC-<JURISDICTION>-<NUMBER>`, with the jurisdiction in upper case and a three-digit number, e.g. `SRC-EU-001`, `SRC-AT-001`, `SRC-GLOBAL-001`. IDs are never reused.

## Triad

The model is described in [model/README.md](../model/README.md).

### Edge

| Code | Edge |
|---|---|
| `C-P` | client – practitioner |
| `C-AI` | client – AI system |
| `P-AI` | practitioner – AI system |
| `F-AI` | frame – AI system |

### Flow

| Code | Flow |
|---|---|
| `information` | what is disclosed, processed and returned, and who knows about it |
| `influence` | who or what shapes decisions, behaviour or self-image |
| `relationship` | trust, attachment, working alliance |
| `responsibility` | accountability, duties, liability |

### Configuration

| Code | Configuration |
|---|---|
| `1` | full triad, open |
| `2` | practitioner-supported |
| `3` | client alone with the AI |
| `4` | client uses AI covertly |
| `5` | practitioner uses AI covertly |
| `6` | no direct client contact |

Edges that are active in each configuration. The main edge of a requirement must be active in every configuration listed for it; the validation script checks this.

| Configuration | Active edges |
|---|---|
| `1` | `C-P`, `C-AI`, `P-AI` |
| `2` | `C-P`, `P-AI` |
| `3` | `C-AI` |
| `4` | `C-P`, `C-AI` |
| `5` | `C-P`, `P-AI` |
| `6` | `P-AI`, `F-AI` |

### Addressee

| Code | Meaning |
|---|---|
| `practitioner` | the psychologist (node P) |
| `provider` | developer or operator of the AI system |
| `institution` | organisation that deploys, pays for or commissions the AI use |
| `authority` | legislator, regulator, supervisory body |
| `client` | the client, where a source addresses them directly |

## Classification

### Spectrum

| Code | Meaning |
|---|---|
| `wellbeing` | stress reduction, mindfulness, mood tracking |
| `prevention` | psychoeducation, early detection, screening |
| `diagnostics-treatment` | psychological assessment, diagnosis, treatment |

### Topic

Requirement IDs have the form `ANIMA-<TOPIC>-<NUMBER>`, e.g. `ANIMA-TRANS-001`. Numbers have three digits and are never reused.

| Code | Topic | Examples of questions |
|---|---|---|
| `PROH` | Prohibited practices | Is this use of AI forbidden altogether? |
| `TRANS` | Transparency | Do people know they are dealing with AI? |
| `CONS` | Informed consent and autonomy | Have clients agreed to the use of AI? |
| `DATA` | Data protection and privacy | How are personal and health data processed and protected? |
| `SAFE` | Safety and risk management | How are risks identified and reduced? |
| `CRIS` | Crisis and emergency handling | What happens when a person is at risk of harm? |
| `QUAL` | Quality, accuracy and validation | Is the system valid, reliable and evidence-based? |
| `EQUI` | Equity and non-discrimination | Does the system work fairly for all groups? |
| `OVERS` | Human oversight | Who checks and can override the AI? |
| `PROF` | Professional duties | What do professional law and codes require? |
| `LIT` | AI literacy and competence | What do practitioners and clients need to know? |
| `ACCT` | Accountability and liability | Who is responsible when something goes wrong? |

### Status

| Code | Meaning |
|---|---|
| `draft` | prepared by one person, not yet reviewed |
| `reviewed` | reviewed by a second person (four-eyes principle) |
