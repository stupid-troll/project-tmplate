#!/usr/bin/env python3
"""
docs.py — documentation tooling helper for tidy-ledger-docs.

Commands:
  format        Format all tracked Markdown files (mdformat).
  format-check  Check Markdown formatting without modifying files.
  lint          Alias for format-check.
  build         Build the MkDocs static site (--strict).
  linkcheck     Check hyperlinks in the built site/ (run build first).
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tomllib
from pathlib import Path

# ---------------------------------------------------------------------------
# Colour output — auto-disabled when stdout is not a TTY
# ---------------------------------------------------------------------------
_TTY = sys.stdout.isatty()

BOLD = "\033[1m" if _TTY else ""
GREEN = "\033[0;32m" if _TTY else ""
RED = "\033[0;31m" if _TTY else ""
CYAN = "\033[0;36m" if _TTY else ""
RESET = "\033[0m" if _TTY else ""


def info(msg: str) -> None:
    print(f"{CYAN}▶{RESET} {msg}")


def success(msg: str) -> None:
    print(f"{GREEN}✔{RESET} {msg}")


def fail(msg: str) -> None:
    print(f"{RED}✘{RESET} {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent


def _load_pyproject() -> dict:
    pyproject = REPO_ROOT / "pyproject.toml"
    with pyproject.open("rb") as fh:
        return tomllib.load(fh)


def _load_exclude_dirs() -> frozenset[str]:
    """Read tool.docs.exclude_dirs from pyproject.toml."""
    dirs = _load_pyproject().get("tool", {}).get("docs", {}).get("exclude_dirs", [])
    return frozenset(dirs)


def _load_linkchecker_cfg() -> dict:
    """Read tool.linkchecker settings from pyproject.toml."""
    return _load_pyproject().get("tool", {}).get("linkchecker", {})


EXCLUDE_DIRS = _load_exclude_dirs()


def git_md_files() -> list[Path]:
    """Return all Markdown files in the repo, skipping exclude_dirs."""
    return sorted(
        p
        for p in REPO_ROOT.rglob("*.md")
        if not any(part in EXCLUDE_DIRS for part in p.parts)
    )


def run_on_md_files(cmd: list[str]) -> None:
    """Run *cmd* on every tracked Markdown file, with progress output."""
    files = git_md_files()
    if not files:
        print("No tracked Markdown files found.")
        return

    label = " ".join(cmd)
    info(f"Running: {BOLD}{label}{RESET} on {len(files)} file(s)")
    for f in files:
        print(f"  {f.relative_to(REPO_ROOT)}")

    result = subprocess.run([*cmd, *files], cwd=REPO_ROOT)
    if result.returncode != 0:
        fail(f"Failed: {label}")
        sys.exit(result.returncode)

    success(f"Done: {label}")


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------
def cmd_format(_args: argparse.Namespace) -> None:
    run_on_md_files(["mdformat"])


def cmd_format_check(_args: argparse.Namespace) -> None:
    run_on_md_files(["mdformat", "--check"])


def cmd_build(_args: argparse.Namespace) -> None:
    info("Building MkDocs site (strict mode)…")
    env = {**os.environ, "MATERIAL_DISABLE_ANNOUNCEMENTS": "1"}
    result = subprocess.run(["mkdocs", "build", "--strict"], cwd=REPO_ROOT, env=env)
    if result.returncode != 0:
        fail("MkDocs build failed.")
        sys.exit(result.returncode)
    success("Site built → site/")


def cmd_linkcheck(_args: argparse.Namespace) -> None:
    cfg = _load_linkchecker_cfg()
    entry = cfg.get("entry", "site/index.html")
    entry_path = REPO_ROOT / entry
    if not entry_path.exists():
        fail(f"Entry point not found: {entry}. Run 'make build' first.")
        sys.exit(1)

    cmd: list[str] = ["linkchecker"]

    threads = cfg.get("threads")
    if threads is not None:
        cmd += ["--threads", str(threads)]

    timeout = cfg.get("timeout")
    if timeout is not None:
        cmd += ["--timeout", str(timeout)]

    if cfg.get("no_warnings"):
        cmd.append("--no-warnings")

    for pattern in cfg.get("ignore_url", []):
        cmd += ["--ignore-url", pattern]

    cmd.append(str(entry_path))

    info(f"Checking links starting from {entry}")
    result = subprocess.run(cmd, cwd=REPO_ROOT)
    if result.returncode != 0:
        fail("linkchecker reported broken links.")
        sys.exit(result.returncode)
    success("All links OK.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        prog=".scripts/docs.py",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", metavar="command")
    sub.required = True

    sub.add_parser("format",       help="Format tracked Markdown files in-place.")
    sub.add_parser("format-check", help="Check formatting (no modifications).")
    sub.add_parser("lint",         help="Alias for format-check.")
    sub.add_parser("build",        help="Build MkDocs static site (--strict).")
    sub.add_parser("linkcheck",    help="Check hyperlinks in built site/ (run build first).")

    args = parser.parse_args()

    dispatch = {
        "format":       cmd_format,
        "format-check": cmd_format_check,
        "lint":         cmd_format_check,
        "build":        cmd_build,
        "linkcheck":    cmd_linkcheck,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
