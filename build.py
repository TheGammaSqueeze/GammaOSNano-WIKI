#!/usr/bin/env python3
"""
GammaOS Nano wiki - static site generator.

Reads content/*.md (with a small YAML-ish frontmatter block), renders each page
through templates/page.html, builds a grouped sidebar, an on-page table of
contents, and a client-side search index. Output goes to build/.

No external template engine: plain string substitution keeps the build tiny and
dependency-light (only python-markdown + pygments).
"""
import os
import re
import json
import shutil
import html
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
TEMPLATES = os.path.join(ROOT, "templates")
ASSETS = os.path.join(ROOT, "assets")
BUILD = os.path.join(ROOT, "docs")

SITE_TITLE = "GammaOS Nano"
SITE_TAGLINE = "The handheld gaming OS, explained"

# Sidebar group order. Any group not listed falls to the end alphabetically.
GROUP_ORDER = [
    "Get Started",
    "The Interface",
    "Controls",
    "Games",
    "Emulators",
    "Media & Apps",
    "Connectivity",
    "Settings",
    "Help",
]


def parse_frontmatter(text):
    """Return (meta_dict, body). Frontmatter is a leading '---' fenced block."""
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block = text[3:end].strip()
            body = text[end + 4:].lstrip("\n")
            for line in block.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
            return meta, body
    return meta, text


def slugify(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s-]+", "-", s)
    return s.strip("-")


class TocExtension(markdown.treeprocessors.Treeprocessor):
    pass


def render_markdown(body):
    """Render markdown, collecting h2/h3 headings for a table of contents."""
    md = markdown.Markdown(
        extensions=["extra", "codehilite", "toc", "tables", "attr_list", "sane_lists"],
        extension_configs={
            "codehilite": {"guess_lang": False, "noclasses": False},
            "toc": {"anchorlink": True, "permalink": False},
        },
    )
    htmlout = md.convert(body)
    toc = []
    for tok in getattr(md, "toc_tokens", []):
        if tok["level"] == 2:
            toc.append({"id": tok["id"], "name": strip_tags(tok["name"]), "children": []})
            for c in tok.get("children", []):
                if c["level"] == 3:
                    toc[-1]["children"].append({"id": c["id"], "name": strip_tags(c["name"])})
    return htmlout, toc


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def text_for_search(body):
    """Plain-text extraction of markdown body for the search index."""
    t = re.sub(r"```.*?```", " ", body, flags=re.S)
    t = re.sub(r"`[^`]*`", " ", t)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[#>*_|=-]", " ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def load_pages():
    pages = []
    for fn in sorted(os.listdir(CONTENT)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(CONTENT, fn)
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        meta, body = parse_frontmatter(raw)
        slug = fn[:-3]
        out_name = "index.html" if slug == "index" else slug + ".html"
        pages.append({
            "slug": slug,
            "file": out_name,
            "title": meta.get("title", slug),
            "group": meta.get("group", "Misc"),
            "order": int(meta.get("order", "100")),
            "icon": meta.get("icon", ""),
            "desc": meta.get("desc", ""),
            "hero": meta.get("hero", ""),
            "body": body,
            "meta": meta,
        })
    return pages


def build_sidebar(pages, current_slug):
    groups = {}
    for p in pages:
        if p["slug"] == "index":
            continue
        groups.setdefault(p["group"], []).append(p)

    def group_key(g):
        return (GROUP_ORDER.index(g) if g in GROUP_ORDER else len(GROUP_ORDER), g)

    out = ['<a class="nav-home%s" href="index.html"><span class="nav-home-mark">&#9670;</span> Home</a>' % (
        " active" if current_slug == "index" else "")]
    for g in sorted(groups.keys(), key=group_key):
        items = sorted(groups[g], key=lambda x: (x["order"], x["title"]))
        out.append('<div class="nav-group"><div class="nav-group-title">%s</div><ul>' % html.escape(g))
        for p in items:
            active = " class=\"active\"" if p["slug"] == current_slug else ""
            ic = ('<span class="nav-ico">%s</span>' % p["icon"]) if p["icon"] else ""
            out.append('<li><a%s href="%s">%s%s</a></li>' % (active, p["file"], ic, html.escape(p["title"])))
        out.append("</ul></div>")
    return "\n".join(out)


def build_toc(toc):
    if not toc:
        return ""
    out = ['<div class="toc"><div class="toc-title">On this page</div><ul>']
    for h in toc:
        out.append('<li><a href="#%s">%s</a>' % (h["id"], html.escape(h["name"])))
        if h["children"]:
            out.append("<ul>")
            for c in h["children"]:
                out.append('<li><a href="#%s">%s</a></li>' % (c["id"], html.escape(c["name"])))
            out.append("</ul>")
        out.append("</li>")
    out.append("</ul></div>")
    return "\n".join(out)


def main():
    if os.path.exists(BUILD):
        shutil.rmtree(BUILD)
    os.makedirs(BUILD)

    # copy assets
    shutil.copytree(ASSETS, os.path.join(BUILD, "assets"))
    # jekyll off for gh-pages
    open(os.path.join(BUILD, ".nojekyll"), "w").close()

    with open(os.path.join(TEMPLATES, "page.html"), encoding="utf-8") as f:
        page_tpl = f.read()

    pages = load_pages()
    search_index = []

    for p in pages:
        body_html, toc = render_markdown(p["body"])
        sidebar = build_sidebar(pages, p["slug"])
        toc_html = build_toc(toc)
        is_home = p["slug"] == "index"

        hero_html = ""
        if is_home:
            with open(os.path.join(TEMPLATES, "hero.html"), encoding="utf-8") as f:
                hero_html = f.read()

        content_class = "content home" if is_home else "content"
        page = page_tpl
        page = page.replace("{{SITE_TITLE}}", SITE_TITLE)
        page = page.replace("{{TAGLINE}}", SITE_TAGLINE)
        page = page.replace("{{PAGE_TITLE}}", html.escape(p["title"]))
        page = page.replace("{{PAGE_DESC}}", html.escape(p["desc"]))
        page = page.replace("{{SIDEBAR}}", sidebar)
        page = page.replace("{{TOC}}", toc_html)
        page = page.replace("{{HERO}}", hero_html)
        page = page.replace("{{CONTENT_CLASS}}", content_class)
        page = page.replace("{{BODY}}", body_html)
        page = page.replace("{{HAS_TOC}}", "has-toc" if toc_html else "no-toc")

        with open(os.path.join(BUILD, p["file"]), "w", encoding="utf-8") as f:
            f.write(page)

        search_index.append({
            "title": p["title"],
            "url": p["file"],
            "group": p["group"],
            "desc": p["desc"],
            "text": text_for_search(p["body"])[:4000],
        })

    with open(os.path.join(BUILD, "search-index.json"), "w", encoding="utf-8") as f:
        json.dump(search_index, f, ensure_ascii=False)

    print("Built %d pages -> %s" % (len(pages), BUILD))


if __name__ == "__main__":
    main()
