# Governance

This document describes how decisions are made in ANIMA.

## Principles

- **Openness:** all decisions about content are made in public, in issues and pull requests.
- **Evidence:** content decisions are based on sources, following the [methodology](docs/methodology.md).
- **Independence:** ANIMA is not affiliated with, endorsed by or acting on behalf of the WHO, the European Union, any national authority, any employer of its contributors or any company.

## Roles

| Role | Who | Responsibilities |
|---|---|---|
| **Contributor** | anyone who submits an issue or pull request | proposes sources, writes or improves summaries, reports errors |
| **Reviewer** | contributors with proven expertise, invited by the maintainers | reviews pull requests in their field (e.g. law, clinical psychology) |
| **Maintainer** | see below | merges pull requests, creates releases, resolves disputes, looks after this governance |

### Current maintainers

| Name | ORCID | Since |
|---|---|---|
| Mag. John G. Haas | [0000-0002-4591-5015](https://orcid.org/0000-0002-4591-5015) | 2026 (initiator) |

## Decision making

1. **Content changes** are made via pull requests. Every pull request needs at least **one approving review** by someone other than the author (four-eyes principle).
2. **Lazy consensus:** if no one objects within a reasonable time (normally 7 days for substantial changes), a reviewed pull request can be merged.
3. **Disagreement** is discussed openly in the pull request. If no consensus is reached, the maintainers decide and document their reasons.
4. **Changes to this governance, the methodology or the scope** are announced in an issue and remain open for comments for at least 14 days.

### Build-up phase (before v1.0)

While ANIMA is being built and has no reviewers yet, the rules above cannot all be applied. Until **version 1.0 is released or at least one reviewer has been appointed**, whichever comes first, the following applies:

- The maintainer may merge pull requests **without a second review** and **without the 14-day comment period**.
- Every change is still made via a pull request and recorded in the [CHANGELOG](CHANGELOG.md). Larger changes are announced in an issue beforehand.
- Content merged without a second review keeps the status **`draft`** (see the [methodology](docs/methodology.md#5-verification)). It becomes `reviewed` only after a second person has checked it.

From then on, the rules above apply in full.

## Becoming a reviewer or maintainer

Contributors who have made several substantial, high-quality contributions can be invited as reviewers. Reviewers can be proposed as maintainers by an existing maintainer. The goal is to have maintainers from more than one country and more than one discipline.

## Conflicts of interest and funding

Everyone with a role in ANIMA should disclose interests that could reasonably be seen to influence their contributions, for example employment by or financial ties to providers of AI products in mental health.

- Contributors disclose relevant interests in their pull request.
- Reviewers and maintainers disclose relevant interests in the table below.
- Any external funding of ANIMA is listed here.

### Declarations

As of 2026-11-11.

| Name | Role | Funding | Declared interests |
|---|---|---|---|
| Mag. John G. Haas | Maintainer | None (voluntary, independent initiative) | None declared |
