# Crosswalk

The crosswalk maps requirements across the four layers. It answers: *Which requirement applies to my use case, and where does it come from?*

## Planned structure

Each requirement is one row with the fields below. Allowed values are defined in [docs/vocabulary.md](../docs/vocabulary.md).

| Field | Example |
|---|---|
| `id` | `ANIMA-TRANS-001` |
| `topic` | `TRANS` |
| `requirement` | Users must be informed that they are interacting with an AI system. |
| `source_id` | `SRC-EU-001` |
| `reference` | AI Act, Art. 50(1) |
| `layer` | `eu` |
| `level` | `L1` |
| `binding` | `true` |
| `usage_context` | `self-directed`, `professional-supervised` |
| `spectrum` | `wellbeing`, `prevention`, `diagnostics-treatment` |
| `related` | `ANIMA-TRANS-004` (WHO guidance on the same topic) |

The human-readable crosswalk lives here. The machine-readable version lives in [`data/`](../data/).
