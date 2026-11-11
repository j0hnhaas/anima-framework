---
# ANIMA source file – copy this template to sources/<pillar>/<jurisdiction>/<short-name>.md
# Allowed values for all coded fields: docs/vocabulary.md
# Check your file with: python scripts/validate.py
id: SRC-EU-000                 # SRC-<JURISDICTION>-<NUMBER>, never reused
title: ""                      # official title
short_title: ""                # e.g. AI Act
issuer: ""                     # e.g. European Parliament and Council of the European Union
pillar: law                    # law | guidance | professional
jurisdiction: eu               # global | europe | eu | <cc> (ISO country code, lower case)
bindingness: binding           # law: binding · guidance: official | recommended · professional: professional
reference: ""                  # e.g. Regulation (EU) 2024/1689
date: "YYYY-MM-DD"             # adoption or publication; YYYY or YYYY-MM also allowed
version: ""                    # consolidated version or edition, if any
url: ""                        # link to the official version
license: ""                    # licence of the source text, e.g. CC BY-NC-SA 3.0 IGO
bibtex_key: ""                 # key in references.bib
checked: "YYYY-MM-DD"          # date the source was last checked
checked_by: [github-user]      # GitHub user name(s)
status: draft                  # draft | reviewed (see docs/methodology.md, section 5)
requirements:                  # one entry per requirement, see docs/methodology.md, section 3
  - id: ANIMA-TOPIC-000        # ANIMA-<TOPIC>-<NUMBER>, never reused
    requirement: ""            # the requirement in your own words, one sentence
    reference: ""              # article, section or page, e.g. Art. 50(1)
    edge: [C-AI]               # C-P | C-AI | P-AI | F-AI – main edge first
    flow: [information]        # information | influence | relationship | responsibility – one or two
    configuration: [1, 3, 4]   # 1–6: where the requirement can take effect
    addressee: provider        # practitioner | provider | institution | authority | client
    topic: TRANS               # see docs/vocabulary.md
    spectrum: [wellbeing, prevention, diagnostics-treatment]
    note: ""                   # mapping note where the mapping is not obvious
---

# <Short title>

## Summary

<!-- 3–6 sentences in your own words: what is the source, who does it address, why does it matter for psychology or for psychological effects of AI? -->

## Requirements on the triad

<!-- Optional: explain in a few sentences where the requirements sit in the triad and why, especially for mappings that are not obvious. The requirements themselves are listed in the front matter above. -->

## Application dates and transitional provisions

<!-- When do which obligations apply? Note pending amendments. -->

## Relation to other sources

<!-- Which other ANIMA sources does this one implement, specify or conflict with? -->

## Open questions

<!-- What is unclear or disputed? Leave nothing out silently. -->

## Short quotes

<!-- Only where the exact wording matters. Mark each quote and give the article or page. -->
