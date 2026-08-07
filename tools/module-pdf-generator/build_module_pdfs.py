# -*- coding: utf-8 -*-
"""
Generates one PDF slide deck per course module, styled after the
sample_coursware template (red title, right-edge accent bar, black
corner block, two-column bullet+image layout, pop-quiz slides).

Image slots are rendered as clearly labeled placeholder boxes with a
suggested Adobe Stock search phrase so real licensed images can be
dropped in later.
"""

import os
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

# ----------------------------------------------------------------------
# Page / theme constants
# ----------------------------------------------------------------------
PAGE_W, PAGE_H = 13.333 * inch, 7.5 * inch
MARGIN = 0.45 * inch
RED = HexColor("#C8202E")
DARK_RED = HexColor("#8C1620")
GRAY = HexColor("#6E6E6E")
LIGHT_GRAY = HexColor("#F3F3F3")
MID_GRAY = HexColor("#B9B9B9")
TEXT = HexColor("#1F1F1F")

CODE_BG = HexColor("#1E1E2A")
CODE_TEXT = HexColor("#E6E6EC")
CODE_DIM = HexColor("#9A9AB0")
DOT_RED = HexColor("#FF5F57")
DOT_YEL = HexColor("#FEBC2E")
DOT_GRN = HexColor("#28C840")

FOOTER_TEXT = "\u00a9 2026 ALDOT Course Team"
BAR_W = 0.16 * inch
CORNER_H = 0.38 * inch
CORNER_W = 0.62 * inch

FONT = "Helvetica"
FONT_B = "Helvetica-Bold"
FONT_I = "Helvetica-Oblique"

OUT_DIR = r"E:\Code\ALDOT\course\mvp-delivery\modules"
IMAGES_V2_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images_v2")


def img(slug):
    """Resolve a bespoke per-slide illustration by its m0X_slot slug."""
    return os.path.join(IMAGES_V2_DIR, f"{slug}.png")


# ----------------------------------------------------------------------
# Low-level helpers
# ----------------------------------------------------------------------
def wrap_text(c, text, font, size, max_width):
    c.setFont(font, size)
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if c.stringWidth(trial, font, size) <= max_width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_chrome(c, page_num):
    """Right accent bar, bottom-right corner block, footer."""
    # right vertical accent bar
    c.setFillColor(RED)
    c.rect(PAGE_W - BAR_W, CORNER_H, BAR_W, PAGE_H - CORNER_H, stroke=0, fill=1)
    # bottom-right black corner block
    c.setFillColor(black)
    c.rect(PAGE_W - CORNER_W, 0, CORNER_W, CORNER_H, stroke=0, fill=1)
    # page number in corner block
    c.setFillColor(white)
    c.setFont(FONT_B, 12)
    c.drawCentredString(PAGE_W - CORNER_W / 2, CORNER_H / 2 - 4, str(page_num))
    # footer copyright
    c.setFillColor(GRAY)
    c.setFont(FONT, 8)
    c.drawString(MARGIN, 0.2 * inch, FOOTER_TEXT)


def draw_header(c, title, kicker=None, small=False):
    """Red title top-left, thin rule beneath. Returns y of the rule."""
    kicker_y = PAGE_H - 0.4 * inch
    top_y = PAGE_H - 0.85 * inch
    if kicker:
        c.setFillColor(GRAY)
        c.setFont(FONT_B, 10.5)
        c.drawString(MARGIN, kicker_y, kicker.upper())
    c.setFillColor(RED)
    size = 20 if small else 25
    c.setFont(FONT_B, size)
    max_w = PAGE_W - MARGIN - BAR_W - 0.3 * inch
    lines = wrap_text(c, title.upper(), FONT_B, size, max_w)
    y = top_y
    for ln in lines[:2]:
        c.drawString(MARGIN, y, ln)
        y -= size * 1.05
    rule_y = min(y - 0.08 * inch, top_y - 0.1 * inch)
    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.75)
    c.line(MARGIN, rule_y, PAGE_W - BAR_W - 0.15 * inch, rule_y)
    return rule_y


def draw_image_cover(c, img_path, x, y, w, h):
    """Draw an image scaled + center-cropped to fully cover (x, y, w, h),
    like CSS background-size: cover."""
    reader = ImageReader(img_path)
    iw, ih = reader.getSize()
    scale = max(w / iw, h / ih)
    dw, dh = iw * scale, ih * scale
    dx = x + (w - dw) / 2
    dy = y + (h - dh) / 2
    c.saveState()
    p = c.beginPath()
    p.rect(x, y, w, h)
    c.clipPath(p, stroke=0, fill=0)
    c.drawImage(reader, dx, dy, width=dw, height=dh, mask="auto")
    c.restoreState()


def draw_missing_image_fallback(c, x, y, w, h, path):
    """Defensive-only: a bespoke image should always exist for every slot.
    If one is somehow missing, fail visibly rather than silently."""
    c.setDash(4, 3)
    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(1.1)
    c.setFillColor(LIGHT_GRAY)
    c.rect(x, y, w, h, stroke=1, fill=1)
    c.setDash()
    c.setFillColor(RED)
    c.setFont(FONT_B, 10.5)
    c.drawCentredString(x + w / 2, y + h / 2, "MISSING IMAGE: " + os.path.basename(path))


def draw_image_box(c, x, y, w, h, img_path):
    """Fill (x, y, w, h) with the bespoke, purpose-built illustration at
    img_path \u2014 a finished concept diagram, not a stand-in for a stock photo."""
    if os.path.isfile(img_path):
        draw_image_cover(c, img_path, x, y, w, h)
    else:
        draw_missing_image_fallback(c, x, y, w, h, img_path)


def draw_bullets(c, x, y_top, w, bullets, size=13, leading=1.32, gap=0.14 * inch):
    c.setFillColor(TEXT)
    y = y_top
    for b in bullets:
        c.setFont(FONT_B, size)
        c.setFillColor(RED)
        c.drawString(x, y, "\u25AA")
        c.setFont(FONT, size)
        c.setFillColor(TEXT)
        lines = wrap_text(c, b, FONT, size, w - 0.28 * inch)
        for i, ln in enumerate(lines):
            c.drawString(x + 0.22 * inch, y, ln)
            if i < len(lines) - 1:
                y -= size * leading
        y -= size * leading + gap
    return y


# ----------------------------------------------------------------------
# Slide layouts
# ----------------------------------------------------------------------
def title_slide(c, page, kicker, title, subtitle, img_path):
    c.setFillColor(white)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setFillColor(GRAY)
    c.setFont(FONT, 9)
    c.drawRightString(PAGE_W - BAR_W - 0.15 * inch, PAGE_H - 0.4 * inch, FOOTER_TEXT)
    c.setFillColor(RED)
    c.setFont(FONT_B, 12)
    c.drawString(MARGIN, PAGE_H - 0.85 * inch, kicker.upper())
    c.setFont(FONT_B, 34)
    max_w = PAGE_W - 2 * MARGIN
    lines = wrap_text(c, title, FONT_B, 34, max_w)
    y = PAGE_H - 1.35 * inch
    for ln in lines[:2]:
        c.drawString(MARGIN, y, ln)
        y -= 38
    c.setFillColor(TEXT)
    c.setFont(FONT, 14)
    c.drawString(MARGIN, y - 4, subtitle)
    img_y = 0.55 * inch
    img_h = y - 4 - img_y - 0.35 * inch
    draw_image_box(c, MARGIN, img_y, PAGE_W - 2 * MARGIN - BAR_W, img_h, img_path)
    draw_chrome(c, page)
    c.showPage()


def section_slide(c, page, kicker, title, img_path):
    c.setFillColor(white)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    rule_y = draw_header(c, title, kicker=kicker)
    img_y = 0.55 * inch
    img_h = rule_y - img_y - 0.3 * inch
    draw_image_box(c, MARGIN, img_y, PAGE_W - 2 * MARGIN - BAR_W, img_h, img_path)
    draw_chrome(c, page)
    c.showPage()


def bullet_slide(c, page, title, kicker, bullets, img_path, intro=None, source_note=None):
    c.setFillColor(white)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    rule_y = draw_header(c, title, kicker=kicker)

    col_split = PAGE_W * 0.56
    text_w = col_split - MARGIN - 0.25 * inch
    y = rule_y - 0.4 * inch
    if intro:
        c.setFillColor(TEXT)
        c.setFont(FONT, 12.5)
        for para in intro:
            lines = wrap_text(c, para, FONT, 12.5, text_w)
            for ln in lines:
                c.drawString(MARGIN, y, ln)
                y -= 17
            y -= 8
        y -= 4

    draw_bullets(c, MARGIN, y, text_w, bullets)

    if source_note:
        c.setFillColor(GRAY)
        c.setFont(FONT_I, 8.5)
        note_lines = wrap_text(c, source_note, FONT_I, 8.5, text_w)
        ny = 0.32 * inch + (len(note_lines) - 1) * 10.5
        for ln in note_lines:
            c.drawString(MARGIN, ny, ln)
            ny -= 10.5

    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.75)
    c.line(col_split, 0.5 * inch, col_split, rule_y - 0.15 * inch)

    img_x = col_split + 0.3 * inch
    img_w = PAGE_W - BAR_W - 0.3 * inch - img_x
    img_h = rule_y - 0.15 * inch - 0.5 * inch
    draw_image_box(c, img_x, 0.5 * inch, img_w, img_h, img_path)

    draw_chrome(c, page)
    c.showPage()


def cards_slide(c, page, title, kicker, cards):
    """cards: list of (heading, source, application)"""
    c.setFillColor(white)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    rule_y = draw_header(c, title, kicker=kicker)

    full_w = PAGE_W - BAR_W - 0.3 * inch - MARGIN
    n = len(cards)
    top = rule_y - 0.25 * inch
    bottom = 0.5 * inch
    gap = 0.14 * inch
    card_h = (top - bottom - gap * (n - 1)) / n

    y = top
    for heading, source, application in cards:
        card_y = y - card_h
        c.setFillColor(LIGHT_GRAY)
        c.roundRect(MARGIN, card_y, full_w, card_h, 6, stroke=0, fill=1)
        c.setFillColor(RED)
        c.rect(MARGIN, card_y, 0.09 * inch, card_h, stroke=0, fill=1)

        tx = MARGIN + 0.28 * inch
        tw = full_w - 0.5 * inch
        c.setFillColor(DARK_RED)
        c.setFont(FONT_B, 12.5)
        c.drawString(tx, card_y + card_h - 0.28 * inch, heading)

        c.setFillColor(TEXT)
        c.setFont(FONT_B, 10.5)
        src_lines = wrap_text(c, source, FONT_B, 10.5, tw)
        sy = card_y + card_h - 0.52 * inch
        for ln in src_lines[:2]:
            c.drawString(tx, sy, ln)
            sy -= 13

        c.setFillColor(GRAY)
        c.setFont(FONT_I, 10)
        app_lines = wrap_text(c, application, FONT_I, 10, tw)
        ay = sy - 4
        for ln in app_lines[:2]:
            c.drawString(tx, ay, ln)
            ay -= 12

        y = card_y - gap

    draw_chrome(c, page)
    c.showPage()


def quiz_slide(c, page, module_label, question, options, img_path, reveal_index=None):
    c.setFillColor(white)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    top_y = PAGE_H - 0.7 * inch
    c.setFillColor(RED)
    c.setFont(FONT_B, 22)
    c.drawString(MARGIN, top_y, "KNOWLEDGE CHECK:")
    kc_w = c.stringWidth("KNOWLEDGE CHECK: ", FONT_B, 22)
    c.setFillColor(TEXT)
    c.setFont(FONT, 22)
    c.drawString(MARGIN + kc_w, top_y, module_label)

    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.75)
    c.line(MARGIN, top_y - 0.18 * inch, PAGE_W - BAR_W - 0.15 * inch, top_y - 0.18 * inch)

    y = top_y - 0.55 * inch
    c.setFillColor(TEXT)
    c.setFont(FONT_B, 14)
    q_lines = wrap_text(c, question, FONT_B, 14, PAGE_W - 2 * MARGIN - BAR_W)
    for ln in q_lines:
        c.drawString(MARGIN, y, ln)
        y -= 19
    y -= 0.12 * inch

    letters = ["A", "B", "C", "D"]
    for i, opt in enumerate(options):
        is_answer = reveal_index is not None and i == reveal_index
        c.setFont(FONT_B if is_answer else FONT, 13)
        c.setFillColor(RED if is_answer else TEXT)
        line = f"{letters[i]}. {opt}"
        lines = wrap_text(c, line, FONT_B if is_answer else FONT, 13, PAGE_W - 2 * MARGIN - BAR_W - 0.3 * inch)
        for j, ln in enumerate(lines):
            c.drawString(MARGIN + (0.25 * inch if j else 0), y, ln)
            y -= 18
        y -= 6

    # Tall enough to keep the cover-crop close to the wide master's own
    # aspect ratio — at the old 1.55in height, icons were being cropped in
    # half. There's ample unused space above the band even in the worst
    # case (4 two-line options + a two-line question), so this is safe.
    band_h = 2.4 * inch
    draw_image_box(c, MARGIN, 0.5 * inch, PAGE_W - 2 * MARGIN - BAR_W, band_h, img_path)

    draw_chrome(c, page)
    c.showPage()


# ----------------------------------------------------------------------
# Diagram primitives (real vector graphics, not photos)
# ----------------------------------------------------------------------
def draw_flow_diagram(c, x, y, w, h, steps):
    """steps: list of (title, subtitle) drawn as a left-to-right arrow chain."""
    n = len(steps)
    gap = 0.32 * inch
    box_w = (w - gap * (n - 1)) / n
    box_h = min(h * 0.7, 2.75 * inch)
    box_y = y + (h - box_h) / 2
    centers = []
    for i, (title, sub) in enumerate(steps):
        bx = x + i * (box_w + gap)
        c.setFillColor(white)
        c.setStrokeColor(RED)
        c.setLineWidth(1.3)
        c.roundRect(bx, box_y, box_w, box_h, 8, stroke=1, fill=1)
        c.setFillColor(RED)
        c.roundRect(bx, box_y + box_h - 0.1 * inch, box_w, 0.1 * inch, 3, stroke=0, fill=1)
        c.setFillColor(DARK_RED)
        c.circle(bx + 0.24 * inch, box_y + box_h - 0.36 * inch, 0.14 * inch, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont(FONT_B, 10)
        c.drawCentredString(bx + 0.24 * inch, box_y + box_h - 0.405 * inch, str(i + 1))

        c.setFillColor(TEXT)
        c.setFont(FONT_B, 11.5)
        title_lines = wrap_text(c, title, FONT_B, 11.5, box_w - 0.28 * inch)
        ty = box_y + box_h - 0.72 * inch
        for ln in title_lines[:2]:
            c.drawCentredString(bx + box_w / 2, ty, ln)
            ty -= 14

        c.setFont(FONT, 8.8)
        c.setFillColor(GRAY)
        sub_lines = wrap_text(c, sub, FONT, 8.8, box_w - 0.26 * inch)
        sy = ty - 8
        for ln in sub_lines[:5]:
            c.drawCentredString(bx + box_w / 2, sy, ln)
            sy -= 10.5
        centers.append((bx, bx + box_w))

    ay = box_y + box_h / 2
    for i in range(n - 1):
        x1 = centers[i][1] + 0.04 * inch
        x2 = centers[i + 1][0] - 0.04 * inch
        c.setStrokeColor(MID_GRAY)
        c.setLineWidth(1.5)
        c.line(x1, ay, x2 - 6, ay)
        c.setFillColor(MID_GRAY)
        p = c.beginPath()
        p.moveTo(x2, ay)
        p.lineTo(x2 - 7, ay + 5)
        p.lineTo(x2 - 7, ay - 5)
        p.close()
        c.drawPath(p, stroke=0, fill=1)


def draw_converge_diagram(c, x, y, w, h, top_items, bottom_title, bottom_sub):
    n = len(top_items)
    gap = 0.18 * inch
    box_w = (w - gap * (n - 1)) / n
    top_h = h * 0.36
    top_y = y + h - top_h
    centers = []
    for i, label in enumerate(top_items):
        bx = x + i * (box_w + gap)
        c.setFillColor(LIGHT_GRAY)
        c.setStrokeColor(MID_GRAY)
        c.setLineWidth(0.9)
        c.roundRect(bx, top_y, box_w, top_h, 6, stroke=1, fill=1)
        c.setFillColor(DARK_RED)
        c.setFont(FONT_B, 9.3)
        lines = wrap_text(c, label, FONT_B, 9.3, box_w - 0.14 * inch)
        ty = top_y + top_h / 2 + (len(lines) - 1) * 5.5
        for ln in lines[:3]:
            c.drawCentredString(bx + box_w / 2, ty, ln)
            ty -= 11
        centers.append(bx + box_w / 2)

    bottom_h = h * 0.32
    bottom_y = y
    c.setFillColor(RED)
    c.roundRect(x, bottom_y, w, bottom_h, 10, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont(FONT_B, 16)
    c.drawCentredString(x + w / 2, bottom_y + bottom_h * 0.62, bottom_title)
    c.setFont(FONT, 10)
    sub_lines = wrap_text(c, bottom_sub, FONT, 10, w - 1.2 * inch)
    sy = bottom_y + bottom_h * 0.62 - 16
    for ln in sub_lines[:2]:
        c.drawCentredString(x + w / 2, sy, ln)
        sy -= 12

    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(1.2)
    for cx0 in centers:
        c.line(cx0, top_y, cx0, bottom_y + bottom_h + 0.05 * inch)
        p = c.beginPath()
        p.moveTo(cx0, bottom_y + bottom_h)
        p.lineTo(cx0 - 5, bottom_y + bottom_h + 9)
        p.lineTo(cx0 + 5, bottom_y + bottom_h + 9)
        p.close()
        c.setFillColor(MID_GRAY)
        c.drawPath(p, stroke=0, fill=1)


def diagram_slide(c, page, title, kicker, caption, steps, kind="flow", bottom=None):
    c.setFillColor(white)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    rule_y = draw_header(c, title, kicker=kicker)

    y = rule_y - 0.3 * inch
    if caption:
        c.setFillColor(GRAY)
        c.setFont(FONT_I, 11)
        for ln in wrap_text(c, caption, FONT_I, 11, PAGE_W - 2 * MARGIN - BAR_W):
            c.drawString(MARGIN, y, ln)
            y -= 15
        y -= 6

    area_x = MARGIN
    area_w = PAGE_W - BAR_W - 0.3 * inch - MARGIN
    area_y = 0.5 * inch
    area_h = y - area_y
    if kind == "converge":
        draw_converge_diagram(c, area_x, area_y, area_w, area_h, steps, bottom[0], bottom[1])
    else:
        draw_flow_diagram(c, area_x, area_y, area_w, area_h, steps)

    draw_chrome(c, page)
    c.showPage()


def code_slide(c, page, title, kicker, source_label, code_lines, note=None):
    c.setFillColor(white)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    rule_y = draw_header(c, title, kicker=kicker, small=True)

    y = rule_y - 0.32 * inch
    c.setFillColor(DARK_RED)
    c.setFont(FONT_B, 10.5)
    c.drawString(MARGIN, y, "REAL CODE — " + source_label)
    y -= 0.18 * inch

    box_x = MARGIN
    box_w = PAGE_W - BAR_W - 0.3 * inch - MARGIN
    note_h = 0.4 * inch if note else 0.12 * inch
    box_y = 0.5 * inch + note_h
    box_h = y - box_y

    c.setFillColor(CODE_BG)
    c.roundRect(box_x, box_y, box_w, box_h, 8, stroke=0, fill=1)

    dot_y = box_y + box_h - 0.26 * inch
    for i, col in enumerate([DOT_RED, DOT_YEL, DOT_GRN]):
        c.setFillColor(col)
        c.circle(box_x + 0.24 * inch + i * 0.22 * inch, dot_y, 0.055 * inch, stroke=0, fill=1)

    c.setFont("Courier", 10.2)
    ly = dot_y - 0.32 * inch
    max_line_w = box_w - 0.4 * inch
    line_no = 0
    for raw in code_lines:
        if ly < box_y + 0.16 * inch:
            break
        display = raw if c.stringWidth(raw, "Courier", 10.2) <= max_line_w else raw[:int(len(raw) * max_line_w / c.stringWidth(raw, "Courier", 10.2))] + "…"
        color = CODE_DIM if display.strip().startswith(("#", "//", "<!--", "'''")) else CODE_TEXT
        c.setFillColor(color)
        c.drawString(box_x + 0.24 * inch, ly, display)
        ly -= 13.6
        line_no += 1

    if note:
        c.setFillColor(GRAY)
        c.setFont(FONT_I, 9)
        ny = 0.5 * inch + note_h - 0.22 * inch
        for ln in wrap_text(c, note, FONT_I, 9, box_w):
            c.drawString(MARGIN, ny, ln)
            ny -= 11.5

    draw_chrome(c, page)
    c.showPage()


def sources_slide(c, page, title, kicker, citations, local_paths):
    c.setFillColor(white)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    rule_y = draw_header(c, title, kicker=kicker)

    full_w = PAGE_W - BAR_W - 0.3 * inch - MARGIN
    y = rule_y - 0.4 * inch

    if citations:
        c.setFillColor(DARK_RED)
        c.setFont(FONT_B, 12.5)
        c.drawString(MARGIN, y, "EXTERNAL DOCUMENTATION")
        y -= 0.28 * inch
        for name, url in citations:
            c.setFillColor(RED)
            c.setFont(FONT_B, 12)
            c.drawString(MARGIN, y, "▪")
            c.setFillColor(TEXT)
            c.setFont(FONT_B, 11.5)
            for ln in wrap_text(c, name, FONT_B, 11.5, full_w - 0.28 * inch):
                c.drawString(MARGIN + 0.22 * inch, y, ln)
                y -= 14.5
            c.setFillColor(GRAY)
            c.setFont(FONT, 10)
            for ln in wrap_text(c, url, FONT, 10, full_w - 0.28 * inch):
                c.drawString(MARGIN + 0.22 * inch, y, ln)
                y -= 13
            y -= 0.14 * inch
        y -= 0.12 * inch

    c.setFillColor(DARK_RED)
    c.setFont(FONT_B, 12.5)
    c.drawString(MARGIN, y, "REFERENCED IN THIS REPOSITORY")
    y -= 0.28 * inch
    for p in local_paths:
        c.setFillColor(RED)
        c.setFont(FONT_B, 12)
        c.drawString(MARGIN, y, "▪")
        c.setFillColor(TEXT)
        c.setFont("Courier", 10.5)
        for ln in wrap_text(c, p, "Courier", 10.5, full_w - 0.28 * inch):
            c.drawString(MARGIN + 0.22 * inch, y, ln)
            y -= 13.5
        y -= 0.08 * inch

    draw_chrome(c, page)
    c.showPage()
