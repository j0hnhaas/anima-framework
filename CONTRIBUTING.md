# Contributing to ANIMA

Thank you for helping. ANIMA lives from the expertise of psychologists, psychotherapists, lawyers, developers and people with lived experience.

> **Never share personal health data.** Do not post information about clients, patients or other identifiable people in issues, pull requests or files, not even anonymised case examples, unless they are fully fictional.

## Ways to contribute

- **Propose a source:** open an issue with the document, its version and a link.
- **Summarise a source:** add or improve a summary in the matching layer folder.
- **Add a country:** see [04-national/README.md](04-national/README.md).
- **Report an error:** law changes. If something is outdated or wrong, open an issue.

## Rules for content

Please read the [methodology](docs/methodology.md) first and use the [source summary template](templates/source-summary.md) for every new source. Add the source to [references.bib](references.bib) and note your change in the [CHANGELOG](CHANGELOG.md) under *Unreleased*.

1. **Cite precisely.** Name the document, version or date, article or section, and link to the official source.
2. **Use your own words.** Summarise; quote only short passages and mark them as quotes. This is especially important for WHO documents (CC BY-NC-SA 3.0 IGO).
3. **Separate law from recommendation.** Make clear whether a requirement is binding or guidance.
4. **Stay neutral.** No promotion of specific products or vendors.
5. **Date your work.** Note the date on which you checked a source ("checked: YYYY-MM-DD").

## Workflow

1. Fork the repository and create a branch.
2. Make your changes.
3. Sign off every commit (see below).
4. Open a pull request and describe what you changed and which sources you used.

## Developer Certificate of Origin (DCO)

ANIMA uses the [Developer Certificate of Origin 1.1](https://developercertificate.org) instead of a contributor licence agreement. By signing off a commit, you confirm that you have the right to submit your contribution under the project's licences.

Sign off with the `-s` flag:

```bash
git commit -s -m "Add summary of AI Act Art. 50"
```

This adds a line like this to your commit message:

```
Signed-off-by: Jane Doe <jane.doe@example.org>
```

If you edit files directly on GitHub, add the `Signed-off-by` line to the commit message by hand.

## Licences of contributions

By contributing, you agree that your contribution is licensed under the licence assigned to the file in [REUSE.toml](REUSE.toml): CC BY 4.0 for content, CC0 1.0 for data and EUPL-1.2 for code.
