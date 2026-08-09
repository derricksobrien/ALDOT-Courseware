import os
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem


ROOT = Path(__file__).resolve().parents[2]
MODULES_DIR = ROOT / "course" / "mvp-delivery" / "modules"


def clean_text(text: str) -> str:
    text = text.replace("`", "")
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1 (\2)", text)
    return text


def parse_markdown_to_story(markdown_text: str):
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=24,
        spaceAfter=12,
        textColor=colors.HexColor("#0F4C81"),
    )
    heading2_style = ParagraphStyle(
        "Heading2Style",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        spaceBefore=10,
        spaceAfter=6,
        textColor=colors.HexColor("#1F4E79"),
    )
    heading3_style = ParagraphStyle(
        "Heading3Style",
        parent=styles["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        spaceBefore=8,
        spaceAfter=4,
        textColor=colors.HexColor("#2F4F4F"),
    )
    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=13,
        spaceAfter=4,
    )
    bullet_style = ParagraphStyle(
        "BulletStyle",
        parent=body_style,
        leftIndent=12,
        bulletIndent=0,
    )

    story = []
    lines = markdown_text.splitlines()
    paragraph_lines = []
    list_items = []

    def flush_paragraph():
        nonlocal paragraph_lines
        if paragraph_lines:
            text = " ".join(part.strip() for part in paragraph_lines if part.strip())
            if text:
                story.append(Paragraph(clean_text(text), body_style))
            paragraph_lines = []

    def flush_list():
        nonlocal list_items
        if list_items:
            story.append(ListFlowable([ListItem(Paragraph(clean_text(item), bullet_style)) for item in list_items], bulletType="bullet", bulletFontName="Helvetica", leftIndent=12))
            list_items = []

    for raw_line in lines:
        line = raw_line.rstrip()
        if not line.strip():
            flush_paragraph()
            flush_list()
            continue

        if line.startswith("# "):
            flush_paragraph()
            flush_list()
            story.append(Paragraph(clean_text(line[2:]), title_style))
        elif line.startswith("## "):
            flush_paragraph()
            flush_list()
            story.append(Paragraph(clean_text(line[3:]), heading2_style))
        elif line.startswith("### "):
            flush_paragraph()
            flush_list()
            story.append(Paragraph(clean_text(line[4:]), heading3_style))
        elif re.match(r"^[-*] ", line):
            flush_paragraph()
            list_items.append(line[2:].strip())
        elif re.match(r"^\d+\. ", line):
            flush_paragraph()
            list_items.append(line.split('.', 1)[1].strip())
        else:
            flush_list()
            paragraph_lines.append(line)

    flush_paragraph()
    flush_list()
    return story


for md_path in sorted(MODULES_DIR.glob("module-*.md")):
    if md_path.name.endswith(".pdf"):
        continue
    output_path = md_path.with_suffix(".pdf")
    markdown_text = md_path.read_text(encoding="utf-8")
    story = parse_markdown_to_story(markdown_text)
    doc = SimpleDocTemplate(str(output_path), pagesize=letter, leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54)
    doc.build(story)
    print(f"Rendered {md_path.name} -> {output_path.name}")
