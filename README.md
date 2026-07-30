# GammaOS Nano Wiki

The source for the GammaOS Nano documentation site.

Live site: https://thegammasqueeze.github.io/GammaOSNano-WIKI/

## What is this

A small static-site generator plus the Markdown content for the GammaOS Nano user guide:
themes, controls, games and emulators, media, connectivity, and the full settings reference.

## Layout

- `content/` - the pages, one Markdown file each, with a small frontmatter block.
- `templates/` - the HTML shell (`page.html`) and the landing hero (`hero.html`).
- `assets/` - CSS, JavaScript, brand art, and screenshots.
- `research/` - code-verified reference notes the pages are written from.
- `build.py` - the generator. Reads `content/`, writes the finished site to `docs/`.
- `docs/` - the generated site (served by GitHub Pages from the `main` branch `/docs` folder).

## Building

Requires Python 3 with `markdown` and `pygments`:

```
pip install markdown pygments
python3 build.py
```

Then open `docs/index.html`, or serve the folder:

```
python3 -m http.server -d docs 8000
```

## Adding a page

Create `content/<name>.md` starting with frontmatter:

```
---
title: My Page
group: Games
order: 6
icon: 🎮
desc: One sentence used for search and the meta description.
---
```

Then write Markdown. Rebuild with `python3 build.py`. The sidebar, search index, and
on-page table of contents are generated automatically.
