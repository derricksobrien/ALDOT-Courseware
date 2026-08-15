# Diagram Style Upgrade — Matching `sample_coursware`

Documented: 2026-08-15. Status: engine change built and demo-validated;
module content not yet converted. Picking back up here.

See also `image-sourcing-workflow.md` — the separate, actively-in-progress
track for sourcing real photos into the `images_v2/*.png` wells (title, why,
real, labdiv, recap, etc.). This doc is specifically about the vector
concept-map/diagram engine (`draw_compare_diagram`), which is a different
piece of the same overall "match sample_coursware visually" effort.

## Why

Instruction: bring the module PDF images/diagrams closer to the visual
pattern used in `sample_coursware` (the "AI In Software Testing" reference
decks), specifically the flow diagrams and other inserted graphics.

## What we found (visual audit)

Reference decks inspected: `sample_coursware/AI_in_Software_Testing_Day1.pdf`
(104 pages) and `AI_Software_Testing_day2.pdf` (113 pages) — rendered to PNG
with PyMuPDF and reviewed page-by-page (title, logistics, workflow-comparison,
LLM-process-diagram, code, quiz, and recap slides across both decks).

Three slide patterns:

1. **Standard content slides** (~85%) — title + left-column bullets/text +
   right-column photographic image, thin vertical rule divider. Already
   matches `bullet_slide()` in `build_module_pdfs.py`.
2. **Flow/concept diagram slides — the actual gap.** e.g. "How AI Is Changing
   QA", "How an LLM Processes a Prompt". Dense, single-composition
   infographics: multi-column comparisons, numbered step badges, icon tiles,
   colored callout/outcome boxes. Our existing `images_v2/*.png` assets
   (compared side by side: `m01_title.png`, `m01_facts.png`) are flat
   gradient backgrounds with 1–2 generic silhouette icons — much lower
   information density.
3. **Full-image slides** — a few slides are just one infographic on white,
   no separate photo well (e.g. "Faker Data Type Catalog").

Code slides and quiz slides in the sample already closely match our
`code_slide()` / `quiz_slide()` — no gap there.

## Adobe Stock / Firefly API — attempted, currently blocked, not required

Explored using Adobe's official REST APIs (Stock + Firefly) via
server-to-server OAuth as a source for photographic well-images and/or
diagram graphics — deliberately *not* via Playwright/browser automation
against Adobe's web UI, because:
- Google-identity sign-in actively resists automation (security holds, 2FA
  challenges).
- Adobe Stock licensing draws real paid credits per download; scripted bulk
  downloads likely violate Adobe Stock's ToS.
- Handing an agent live account credentials is unnecessary risk when the
  official API + OAuth client-credentials flow exists instead.

Current state:
- Org-supplied Adobe account: Developer Console access is restricted, needs
  admin approval (Adobe Admin Console → Developer role). Not yet granted.
- 30-day trial account: Adobe Stock API is disabled (needs a paid Stock
  subscription tied to the account — expected, not a bug). Firefly Services
  catalog under the trial shows Express API / Audio & Video API variants
  greyed out; the plain "Firefly API" (text-to-image) card was not confirmed
  available.
- Partial credentials captured in `course/adobe.env` (gitignored — added
  `adobe.env` / `course/adobe.env` explicitly to `.gitignore` since neither
  `.env` nor `.env.*` patterns matched that filename). Client ID, Org ID,
  Technical Account ID present; **Client Secret still missing**, and scopes
  shown are only the generic baseline (`openid, AdobeID,
  additional_info.projectedProductContext, read_organizations`) — no
  Firefly-specific scope confirmed attached yet.

**Decision: don't block on this.** The higher-value fix (the diagram-density
gap) doesn't need Adobe at all — it needs richer vector layouts. Adobe API
access (Firefly, and Stock once/if the org account is approved) stays a
parallel stretch goal for the photographic well-images later, not a
dependency for the diagram work.

## Chosen approach: extend the vector rendering engine

No sourced/licensed images — pure `reportlab` primitives, same as the
existing `code_slide()` / `quiz_slide()` machinery. Reproducible, free,
diffable in git, no per-call cost or ToS exposure.

Changes made to `build_module_pdfs.py`:

- **10 vector icon glyphs**: `icon_document`, `icon_person`, `icon_people`,
  `icon_gear`, `icon_chip_ai`, `icon_chart_up`, `icon_hourglass`,
  `icon_check`, `icon_grid`, `icon_cycle` — plus `draw_icon_badge()` to drop
  any of them into a colored circle badge.
- **`draw_compare_diagram()`** — the two-column "traditional vs. AI-assisted"
  workflow layout: numbered step badges with dotted connectors down each
  column, icon+title+description cards, an outcome band per column, and a
  bidirectional connector callout in the gap between columns. Uses the
  course's existing red/black palette (not the sample's blue) to stay
  consistent with the rest of the deck's chrome.
- **`kind="compare"`** wired into `diagram_slide()` alongside the existing
  `flow` / `converge` kinds, via a new `compare=` kwarg
  (`compare=dict(left=..., right=..., center_label=...)`). Existing module
  dicts in `generate_all.py` don't need to change until a module opts in.
- Regression-tested: re-rendered existing `flow` and `converge` diagrams
  after the signature change (`diagram_slide(..., steps=None, ...,
  compare=None)`) — pixel-identical to before.

## Demo (for evaluation)

Built a one-off demo slide (not wired into real module content) reframing
Module 3 ("Copilot-Assisted C# Development") as a traditional-vs-Copilot
refactor comparison — chosen because it's the closest thematic parallel to
the sample's own "Traditional QA vs AI-Assisted QA" slide, so it's a fair
apples-to-apples test.

Files (copied into the repo so they persist, originally rendered to the
session scratchpad):
- `demo/compare_demo.pdf` / `demo/compare_demo.png` — our output
- `demo/sample-reference-how-ai-is-changing-qa.png` — the sample slide it's
  modeled on (Day 1 deck, page 11)
- `demo/compare_demo_source.py` — the script that generated it; self
  contained, run with `python compare_demo_source.py` from
  `tools/module-pdf-generator/demo/` and it overwrites `demo/compare_demo.pdf`

## Open questions / not yet decided

Comparing the demo against the sample side by side, deliberate vs.
incidental differences:

**Deliberate (kept on purpose):**
- Color: red/dark-red (ours) vs. navy/blue (sample) — matches our existing
  chrome instead of introducing a new color family.
- Step connectors: dotted line through numbered badges (ours) vs. small ↓
  arrow icons between cards (sample) — matches our existing flow/converge
  diagram language.

**Incidental — worth revisiting:**
- Card style: sample uses white cards with a thin gray border (lighter,
  more "floating"); ours uses flat solid light-gray fill.
- Icon badge tint: sample tints the badge background to match each column's
  accent color; ours is plain white on both sides, so the columns read as
  less color-coded at a glance.
- Icon detail: sample's icons are slightly more bespoke per concept
  (pencil-on-paper, spreadsheet-with-X, gear+play+dots); ours are simpler.
  `icon_cycle` is the weakest match of the set.

## Next steps

1. Decide on the card-style / icon-tint polish items above.
2. Go through the 10 modules and decide which existing concept-map diagrams
   (currently all `flow` or one `converge`) should switch to `compare`
   instead — not all of them are natural before/after comparisons.
3. Write the real step/outcome copy for whichever modules get converted, in
   `generate_all.py`.
4. Revisit Adobe Firefly/Stock API access later (org approval, or a paid
   tier) to cover the photographic well-images — separate, lower-priority
   track.

## Reference

- Engine: `tools/module-pdf-generator/build_module_pdfs.py`
- Content: `tools/module-pdf-generator/generate_all.py`
- Rebuild command: `python generate_all.py` (from this directory)
- Adobe credentials (partial, gitignored): `course/adobe.env`
