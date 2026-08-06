from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from flask import Flask, abort, render_template, url_for
from markdown import markdown


@dataclass(frozen=True)
class ContentPage:
    slug: str
    title: str
    path: Path
    kind: str

    @property
    def relative_path(self) -> str:
        return str(self.path.relative_to(ROOT_DIR)).replace("\\", "/")


ROOT_DIR = Path(__file__).resolve().parents[1]
LAB_DIR = ROOT_DIR / "labs"
MODULE_DIR = LAB_DIR / "modules"
MVP_DIR = ROOT_DIR / "mvp-delivery"
MVP_MODULE_DIR = MVP_DIR / "modules"
MVP_LAB_DIR = MVP_DIR / "labs"
MVP_RESOURCE_DIR = MVP_DIR / "resources"

COURSE_PAGE_MAP = {
    "course-design": ROOT_DIR / "design.md",
    "courseware-plan": ROOT_DIR / "courseware-production-plan.md",
    "mvp-gap-analysis": ROOT_DIR / "mvp-priority-gap-analysis.md",
    "mvp-course-outline": ROOT_DIR / "updated-course-outline-mvp.md",
    "mvp-delta-outline": ROOT_DIR / "mvp-delta-outline.md",
    "mvp-delivery-overview": MVP_DIR / "README.md",
    "mvp-lab-resource-matrix": MVP_RESOURCE_DIR / "lab-resource-matrix.md",
    "implementation-plan": LAB_DIR / "implementation-and-test-plan.md",
    "missing-items": LAB_DIR / "what-you-might-be-missing.md",
    "repo-sources": LAB_DIR / "repo-source-status.md",
}


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def read_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_title(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def extract_summary(markdown_text: str) -> str:
    for line in markdown_text.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            continue
        if stripped_line.startswith("#"):
            continue
        if stripped_line.startswith("|"):
            continue
        return stripped_line
    return ""


def markdown_to_html(markdown_text: str) -> str:
    return markdown(
        markdown_text,
        extensions=["fenced_code", "tables", "toc", "smarty"],
        output_format="html5",
    )


def build_pages() -> list[ContentPage]:
    pages: list[ContentPage] = []
    for slug, path in COURSE_PAGE_MAP.items():
        markdown_text = read_markdown(path)
        pages.append(
            ContentPage(
                slug=slug,
                title=extract_title(markdown_text, slug.replace("-", " ").title()),
                path=path,
                kind="course",
            )
        )

    for path in sorted(MODULE_DIR.glob("lab-*.md")):
        markdown_text = read_markdown(path)
        pages.append(
            ContentPage(
                slug=path.stem,
                title=extract_title(markdown_text, path.stem.replace("-", " ").title()),
                path=path,
                kind="lab",
            )
        )

    for path in sorted(MVP_MODULE_DIR.glob("module-*.md")):
        markdown_text = read_markdown(path)
        pages.append(
            ContentPage(
                slug=f"mvp-{path.stem}",
                title=extract_title(markdown_text, path.stem.replace("-", " ").title()),
                path=path,
                kind="course",
            )
        )

    for path in sorted(MVP_LAB_DIR.glob("lab-*.md")):
        markdown_text = read_markdown(path)
        pages.append(
            ContentPage(
                slug=f"mvp-{path.stem}",
                title=extract_title(markdown_text, path.stem.replace("-", " ").title()),
                path=path,
                kind="lab",
            )
        )

    return pages


PAGES = build_pages()
PAGES_BY_SLUG = {page.slug: page for page in PAGES}


def page_to_record(page: ContentPage) -> dict[str, str]:
    markdown_text = read_markdown(page.path)
    return {
        "slug": page.slug,
        "title": page.title,
        "kind": page.kind,
        "relative_path": page.relative_path,
        "summary": extract_summary(markdown_text),
        "html": markdown_to_html(markdown_text),
    }


def sitemap_records() -> list[dict[str, str]]:
    records = [page_to_record(page) for page in PAGES]
    records.extend(
        [
            {
                "slug": "home",
                "title": "Home",
                "kind": "nav",
                "relative_path": "/",
                "summary": "Landing page for the course web app.",
                "html": "",
            },
            {
                "slug": "labs-index",
                "title": "Labs",
                "kind": "nav",
                "relative_path": "/labs",
                "summary": "Index of all step-by-step lab pages.",
                "html": "",
            },
            {
                "slug": "sitemap",
                "title": "Sitemap",
                "kind": "nav",
                "relative_path": "/sitemap",
                "summary": "Navigation page that lists the full site structure.",
                "html": "",
            },
        ]
    )
    return records


app = Flask(__name__)


@app.context_processor
def inject_globals() -> dict[str, object]:
    labs = [page for page in PAGES if page.kind == "lab"]
    course_pages = [page for page in PAGES if page.kind == "course"]
    return {
        "site_title": "Software Development Modernization",
        "nav_labs": labs,
        "nav_course_pages": course_pages,
    }


@app.route("/")
def index() -> str:
    design_page = page_to_record(PAGES_BY_SLUG["course-design"])
    lab_pages = [page_to_record(page) for page in PAGES if page.kind == "lab"]
    return render_template("index.html", design_page=design_page, lab_pages=lab_pages)


@app.route("/page/<slug>")
def page_detail(slug: str) -> str:
    page = PAGES_BY_SLUG.get(slug)
    if page is None:
        abort(404)
    return render_template("page.html", page=page_to_record(page))


@app.route("/labs")
def labs_index() -> str:
    lab_pages = [page_to_record(page) for page in PAGES if page.kind == "lab"]
    return render_template("labs.html", lab_pages=lab_pages)


@app.route("/labs/<slug>")
def lab_detail(slug: str) -> str:
    page = PAGES_BY_SLUG.get(slug)
    if page is None or page.kind != "lab":
        abort(404)
    return render_template("lab.html", page=page_to_record(page))


@app.route("/api/labs")
def labs_api() -> dict[str, object]:
    return {
        "labs": [
            {
                "slug": page.slug,
                "title": page.title,
                "path": page.relative_path,
                "url": url_for("lab_detail", slug=page.slug),
            }
            for page in PAGES
            if page.kind == "lab"
        ]
    }


@app.route("/sitemap")
def sitemap() -> str:
    pages = sitemap_records()
    return render_template("sitemap.html", pages=pages)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=True)