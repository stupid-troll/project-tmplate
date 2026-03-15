# Documentation Rules

Before generating or modifying documentation:

1. Read:
    - `docs/common/engineering/documentation-style.md`
    - `README.md`
    - relevant files under `docs/`

Project documentation rules take precedence over general best practices.

______________________________________________________________________

## Structure

- All docs must live under `docs/`.
- Every new page must be added to `nav:` in `mkdocs.yml`.
- Follow the required/optional sections defined in the documentation style guide.
- Do not invent new templates if one already exists.

______________________________________________________________________

## Formatting

- Markdown formatting is handled exclusively by `mdformat`.
- Do NOT manually reflow or wrap lines.
- Do NOT introduce additional Markdown linters.
- Assume formatting is enforced via `make docs-format` and pre-commit.

______________________________________________________________________

## Linking

- Use relative links only (`../`, `./`).
- Do not use absolute repository URLs for internal links.

______________________________________________________________________

## MkDocs / Material

- Use Material admonitions (`!!! note`, `!!! warning`, etc.) when appropriate.
- Use only supported `pymdownx` extensions.
- Do not introduce new documentation tooling.
