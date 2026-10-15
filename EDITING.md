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
