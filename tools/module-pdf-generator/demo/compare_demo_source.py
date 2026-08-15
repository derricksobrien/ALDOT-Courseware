import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from reportlab.pdfgen import canvas
from build_module_pdfs import (
    PAGE_W, PAGE_H, RED, DARK_RED, diagram_slide,
    icon_document, icon_person, icon_people, icon_gear, icon_chip_ai,
    icon_chart_up, icon_hourglass, icon_check, icon_cycle,
)

OUT = str(Path(__file__).resolve().parent / "compare_demo.pdf")

compare = dict(
    left=dict(
        header="TRADITIONAL REFACTORING",
        subheader="Manual & Time-Intensive",
        accent=DARK_RED,
        steps=[
            (icon_document, "MANUAL CODE REVIEW",
             "Developer reads through legacy methods line by line to find complexity."),
            (icon_person, "HAND-WRITTEN REFACTOR",
             "Developer rewrites logic manually, re-typing boilerplate and tests."),
            (icon_hourglass, "SLOW VALIDATION",
             "Manual re-testing before trusting the change is safe to merge."),
        ],
        outcome_icon=icon_hourglass,
        outcome="Slower cycles, inconsistent coverage, easy to miss edge cases.",
    ),
    right=dict(
        header="COPILOT-ASSISTED REFACTORING",
        subheader="Faster, Reviewed, Test-Backed",
        accent=RED,
        steps=[
            (icon_chip_ai, "COPILOT PROPOSES A PLAN",
             "Copilot analyzes the target class and suggests a scoped refactor."),
            (icon_check, "HUMAN REVIEW",
             "Developer validates correctness, security, and readability before accepting."),
            (icon_cycle, "TESTS GENERATED + RUN",
             "Copilot drafts unit tests; developer runs them to confirm behavior."),
        ],
        outcome_icon=icon_chart_up,
        outcome="Faster delivery, consistent test coverage, human stays in control.",
    ),
    center_label="COPILOT\nAUGMENTS\nTHE DEV",
)

c = canvas.Canvas(OUT, pagesize=(PAGE_W, PAGE_H))
diagram_slide(c, 1, "Concept Map", "Module 03",
              "Copilot changes where the effort goes in a refactor \u2014 not whether a human reviews it.",
              kind="compare", compare=compare)
c.save()
print("wrote", OUT)
