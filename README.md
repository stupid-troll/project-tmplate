# Project Documentation Template

## Project Overview

This repository contains the documentation site for the Project Documentation Template, built with [MkDocs](https://www.mkdocs.org/) and [mkdocs-material](https://squidfunk.github.io/mkdocs-material/). The site is managed using [Poetry](https://python-poetry.org/) for Python dependencies and [pre-commit](https://pre-commit.com/) for code quality automation.

### Tech Stack

- **Python**: Programming language (version: >=3.12, \<4.0)
- **MkDocs**: Static site generator for project documentation (version: >=1.6, \<2.0) — [MkDocs Documentation](https://www.mkdocs.org/)
- **mkdocs-material**: Modern theme for MkDocs (version: >=9.5) — [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)
- **Poetry**: Python dependency and environment management (version: >=3.8) — [Poetry Documentation](https://python-poetry.org/docs/)
- **pre-commit**: Automation for linting and formatting (version: >=3.8) — [pre-commit Documentation](https://pre-commit.com/)
- **mdformat**: Markdown formatting tool (version: >=0.7) — [mdformat Documentation](https://mdformat.readthedocs.io/en/stable/)
- **linkchecker**: Link validation tool (version: ^10.6.0) — [linkchecker Documentation](https://linkchecker.github.io/linkchecker/)

## Quickstart

1. **Install Make** (if not installed):

    - macOS: Make is pre-installed. If not, install via Homebrew:

```bash
    brew install make
```

```
- Linux: Use your package manager, e.g.:
```

```bash
    sudo apt-get install make
```

```
- Windows: Use [Chocolatey](https://chocolatey.org/) or install via WSL.
```

1. **Install Poetry** ([docs](https://python-poetry.org/docs/)):

```bash
    curl -sSL https://install.python-poetry.org | python3 -
```

1. **Install dependencies**:

```bash
    poetry install
```

1. **Build documentation site**:

```bash
    make build
```

1. **Serve documentation locally**:

```bash
    make serve
```

```
After running `make serve`, open your browser and go to:

- http://127.0.0.1:8000 or http://localhost:8000
    to view the documentation site locally.
```

## Command Mini-Guide

### Using Make

- `make install` — Install dev dependencies and register pre-commit hooks
- `make build` — Build the documentation site to the `site/` directory
- `make serve` — Start a local server for preview (http://localhost:8000)
- `make lint` — Run markdown formatting and lint checks
- `make format` — Format all tracked Markdown files
- `make format-check` — Check formatting of Markdown files
- `make linkcheck` — Validate links in the built site (runs build first)
- `make clean` — Remove generated `site/` directory
- `make help` — Show available Makefile targets

### Without Make

- `poetry install --no-root --with dev` — Install dev dependencies
- `poetry run pre-commit install` — Register pre-commit hooks
- `poetry run mkdocs build -f mkdocs.yml --strict` — Build docs static site
- `poetry run mkdocs serve -f mkdocs.yml --dev-addr 0.0.0.0:8000` — Start local server for docs
- `poetry run python .scripts/docs.py format` — Format Markdown files
- `poetry run python .scripts/docs.py format-check` — Check Markdown formatting
- `poetry run python .scripts/docs.py lint` — Run lint checks
- `poetry run python .scripts/docs.py linkcheck` — Validate links in built site
- `rm -rf site` — Remove generated site directory
- `poetry run pre-commit run --all-files` — Run all pre-commit hooks
