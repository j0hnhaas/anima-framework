# Navigator

The navigator brings all requirements together and places them on the [triad](../model/README.md). It answers: *Which requirements apply to my situation, where do they come from, and who must act?*

## How it works

Every source file lists its requirements, each mapped onto the triad (see the [methodology](../docs/methodology.md#3-mapping-onto-the-triad)). The navigator collects them into one table. It can be filtered by any field – for example all requirements at the edge `C-AI` in configuration `3` (a person alone with a chatbot).

## Fields

Allowed values are defined in [docs/vocabulary.md](../docs/vocabulary.md).

| Field | Example |
|---|---|
| `id` | `ANIMA-TRANS-001` |
| `requirement` | People must be informed that they are interacting with an AI system. |
| `source_id` | `SRC-EU-001` |
| `reference` | AI Act, Art. 50 |
| `pillar` | `law` |
| `jurisdiction` | `eu` |
| `bindingness` | `binding` |
| `edge` | `C-AI` |
| `flow` | `information` |
| `configuration` | `1`, `3`, `4` |
| `addressee` | `provider` |
| `topic` | `TRANS` |
| `spectrum` | `wellbeing`, `prevention`, `diagnostics-treatment` |
| `status` | `draft` |

*The example illustrates the form of an entry; it is not verified content.*

## Gaps

The navigator also shows **gaps**: combinations of edge, flow and configuration for which no source assigns a duty. Gaps are findings in their own right – they show where regulation or guidance is missing.

## Status

The navigator is generated automatically from the source files. The generator follows with the data structure in a later step of the [roadmap](https://github.com/j0hnhaas/anima-framework/issues/10). The machine-readable version will be placed in [`data/`](../data/).
