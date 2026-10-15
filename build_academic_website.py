#!/usr/bin/env python3
"""Build Jekyll Markdown pages from the editable website_pages Python files."""
import argparse
from importlib import import_module
from pathlib import Path

PAGE_NAMES = ("about", "education", "experience", "publications", "teaching", "volunteering", "cv")


def build_pages(root, names):
    for name in names:
        content = import_module(f"website_pages.{name}").CONTENT
        target = root / "_pages" / f"{name}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        print(f"Wrote _pages/{name}.md")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", nargs="?", type=Path,
                        default=Path(__file__).resolve().parent,
                        help="Destination repository (default: this script's directory)")
    parser.add_argument("--page", choices=PAGE_NAMES, help="Build only one page")
    parser.add_argument("--force", action="store_true",
                        help="Accepted for compatibility; builds replace generated Markdown")
    args = parser.parse_args()
    root = args.repository.expanduser().resolve()
    if not (root / "_config.yml").exists():
        parser.error(f"{root} is missing _config.yml")
    build_pages(root, (args.page,) if args.page else PAGE_NAMES)


if __name__ == "__main__":
    main()
