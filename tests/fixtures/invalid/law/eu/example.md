---
id: SRC-AT-901
title: "Example source with deliberate errors"
short_title: Broken example
issuer: ANIMA test fixture
pillar: law
jurisdiction: eu
bindingness: recommended
url: https://github.com/j0hnhaas/anima-framework
checked: "2026-11-11"
checked_by: [test]
status: draft
requirements:
  - id: ANIMA-TRANS-901
    requirement: The practitioner checks every output of the AI system.
    reference: "Section 1"
    edge: [P-AI]
    flow: [responsibility]
    configuration: [3]
    addressee: practitioner
    topic: OVERS
    spectrum: [wellbeing]
  - id: ANIMA-DATA-902
    requirement: Uses a value that is not in the vocabulary.
    reference: "Section 2"
    edge: [C-X]
    flow: [information]
    configuration: [7]
    addressee: provider
    topic: DATA
    spectrum: [wellbeing]
---

# Broken example

Test fixture for `scripts/validate.py`. Contains deliberate errors: source ID does not match the jurisdiction, bindingness does not fit the pillar, requirement ID does not match the topic, main edge not active in configuration 3, practitioner duty in configuration 3, unknown edge and configuration. Not ANIMA content.
