SHELL := /usr/bin/env bash

.PHONY: install help \
		format format-check lint \
		serve build \
		clean linkcheck

install: ## Install dev dependencies and register pre-commit hooks
	poetry install --no-root --with dev
	poetry run pre-commit install

help: ## Show this help
	@echo "Available targets:"
	@grep -E '^[a-zA-Z0-9_@\-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "} {printf "  %-20s %s\n", $$1, $$2}'


format: ## Format all tracked Markdown files (mdformat)
	poetry run python .scripts/docs.py format

format-check: ## Check formatting (mdformat --check)
	poetry run python .scripts/docs.py format-check

lint: ## Check formatting (format-check)
	poetry run python .scripts/docs.py lint

serve: ## Start MkDocs dev server for docs (http://localhost:8000)
	MATERIAL_DISABLE_ANNOUNCEMENTS=1 poetry run mkdocs serve -f mkdocs.yml --dev-addr 0.0.0.0:8000

build: ## Build docs static site into site/
	MATERIAL_DISABLE_ANNOUNCEMENTS=1 poetry run mkdocs build -f mkdocs.yml --strict

linkcheck: ## Check hyperlinks in built site/ (runs build first)
	$(MAKE) build
	poetry run python .scripts/docs.py linkcheck

clean: ## Remove generated site/ directory
	rm -rf site
