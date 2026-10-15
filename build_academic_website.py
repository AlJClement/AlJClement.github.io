#!/usr/bin/env python3
"""Build Jekyll Markdown pages from the editable website_pages Python files."""
import argparse
import json
import re
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


def build_slideshow(root):
    from website_pages.slideshow import TITLE, INTERVAL_SECONDS, SLIDES
    folder = root / "images" / "slideshow"
    extensions = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}
    entries = SLIDES
    if not entries and folder.exists():
        entries = [{"image": p.name} for p in sorted(folder.iterdir())
                   if p.is_file() and p.suffix.lower() in extensions]
    slides = []
    for entry in entries:
        filename = entry["image"]
        image = folder / filename
        if Path(filename).name != filename or not image.is_file():
            raise ValueError(f"Slideshow photo not found in images/slideshow/: {filename}")
        default_title = re.sub(r"^\d+[-_ ]*", "", image.stem).replace("-", " ").replace("_", " ").strip() or image.stem
        title = entry.get("title", default_title)
        slides.append({"image": f"/images/slideshow/{filename}", "title": title,
                       "caption": entry.get("caption", ""),
                       "alt": entry.get("alt", title or image.stem.replace("-", " ").replace("_", " "))})
    data = {"title": TITLE, "interval_ms": max(3, INTERVAL_SECONDS) * 1000, "slides": slides}
    target = root / "_data" / "slideshow.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote _data/slideshow.json ({len(slides)} photos)")


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
    build_slideshow(root)


if __name__ == "__main__":
    main()
