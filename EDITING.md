# Editing your website

Each main page has its own Python file in `website_pages/`:

| Page | File |
| --- | --- |
| About / home | `website_pages/about.py` |
| Education | `website_pages/education.py` |
| Experience | `website_pages/experience.py` |
| Publications | `website_pages/publications.py` |
| Teaching | `website_pages/teaching.py` |
| Volunteering | `website_pages/volunteering.py` |
| CV | `website_pages/cv.py` |

Edit the text between `CONTENT = r"""` and the closing `"""`. Keep those delimiters in place. The text uses Markdown: `## Heading`, `**bold**`, and `[link text](https://example.com)`.

To rebuild all pages locally, run from the repository folder:

```sh
python3 build_academic_website.py
```

To rebuild just one page:

```sh
python3 build_academic_website.py --page education
```

These commands replace the corresponding files in `_pages/`. Make content edits in the Python files so the next build preserves them. The generator preserves navigation and site settings.

Publish your edits:

```sh
git add website_pages _pages
git commit -m "Update website content"
git push
```

GitHub Actions also generates the pages automatically before deploying, so editing a Python page directly on GitHub works too.

Author/sidebar details and profile links are in `_config.yml`. Menu labels and order are in `_data/navigation.yml`. Template utility pages such as the sitemap remain in `_pages/`.

## Scrolling layout

The home page combines all seven Python content files into sections. The top bar scrolls to each section. Edit section text in the same Python files as before. The design is in `assets/css/scrolling.css` and the layout is in `_layouts/scrolling.html`. Older standalone page URLs still work.

## Photo slideshow

1. Put photos (`.jpg`, `.png`, `.webp`, `.gif`, or `.avif`) in `images/slideshow/`. Filename order controls the slideshow order; use names such as `01-Oxford.jpg` and `02-Conference.jpg`. Each photo displays for 5 seconds. Its filename becomes its visible title (for example, `01-Oxford.jpg` displays “Oxford”); you can override this in the Python file.
2. Edit `website_pages/slideshow.py` to change the title, rotation speed, and optional per-photo titles, captions, and descriptions. The commented example shows how to specify an order explicitly.
3. Run `python3 build_academic_website.py`, then commit and push the photos, Python file, and generated `_data/slideshow.json`. Deployment also regenerates this data automatically.

The slideshow appears below your About text once photos are added. It stays hidden when there are no photos. Multiple photos rotate automatically, with previous/next and pause controls. Photos retain their full image without cropping. A single photo displays without rotation controls.
