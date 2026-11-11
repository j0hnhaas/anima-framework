---
id: SRC-EU-900
title: "Example source used to test the validation script"
short_title: Example
issuer: ANIMA test fixture
pillar: law
jurisdiction: eu
bindingness: binding
reference: "Test fixture"
date: "2026-11-11"
url: https://github.com/j0hnhaas/anima-framework
checked: "2026-11-11"
checked_by: [test]
status: draft
requirements:
  - id: ANIMA-TRANS-900
    requirement: People are informed that they are interacting with an AI system.
    reference: "Section 1"
    edge: [C-AI]
    flow: [information]
    configuration: [1, 3, 4]
    addressee: provider
    topic: TRANS
    spectrum: [wellbeing, prevention, diagnostics-treatment]
  - id: ANIMA-CONS-900
    requirement: The practitioner informs the client before using an AI system in the assessment.
    reference: "Section 2"
    edge: [C-P, P-AI]
    flow: [information, responsibility]
    configuration: [2, 5]
    addressee: practitioner
    topic: CONS
    spectrum: [diagnostics-treatment]
---

# Example

Test fixture for `scripts/validate.py`. Not ANIMA content.
