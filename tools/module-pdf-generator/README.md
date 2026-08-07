# Module PDF Generator

Rebuilds the 10 module decks in `course/mvp-delivery/modules/*.pdf` from
`images_v2/*.png` plus the content baked into `generate_all.py`.

## Setup

```
pip install reportlab pillow numpy
```

## Rebuild the PDFs

```
python generate_all.py
```

Writes all 10 PDFs directly into `course/mvp-delivery/modules/`.

## Swapping in real Adobe Stock images

Each file in `images_v2/` is a drop-in replacement — `draw_image_box()` in
`build_module_pdfs.py` scales and center-crops whatever PNG is there to
fill its slide, so any replacement image works regardless of its native
size. See `../adobe-stock/image-plan.md` for the full list of 112 images,
their target filenames, and a generation prompt for each; `check_manifest.py`
there tracks which ones you've swapped in so far.

## Files

- `generate_all.py` — module content (objectives, facts, quiz questions,
  citations, real code excerpts...) and the per-module build loop.
- `build_module_pdfs.py` — the slide-layout engine (fonts, colors, chrome,
  diagram/code/quiz slide types, image placement).
- `images_v2/` — one PNG per image slot, named `m0X_slot.png`.
