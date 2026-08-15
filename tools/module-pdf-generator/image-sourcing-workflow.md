# Image Sourcing Workflow — Module PDFs

Documented: 2026-08-15. This is the process we landed on for replacing the
generic `images_v2/*.png` placeholder art with real photorealistic images,
module by module. It's been working well over Modules 1 and 2 — write it
down so it's repeatable without re-deriving it each time.

## The loop, per module

1. **Assess the module's theme** from its content dict in `generate_all.py`
   (objectives, narrative, field_facts, etc.) — what's the visual mood
   (server room? agile board? code editor?).
2. **Pick curated high-impact slots.** Not all 12 image wells need bespoke
   photos every time — default to ~5 of the highest narrative-impact ones:
   `title`, `why`, `real` (or `facts` if the module has no `real_example`),
   `labdiv`, `recap`. Offer to cover the rest (objectives, focus, assets,
   quiz1/quiz2) if asked.
3. **Give a search term + AI-generation prompt per slot**, matching the
   established photorealistic style (see `diagram-style-upgrade.md` for the
   sample deck's visual language this is chasing).
4. **User finds/generates the image and saves it** to
   `course/mvp-delivery/images/` (Adobe Stock downloads keep their
   `AdobeStock_<id>.jpeg` filename — that's fine, we don't rename at this
   stage).
   - **Gotcha**: pasting an image into the chat only renders it for me to
     *view* — it does not write anything to disk. The user has to actually
     save the file separately (Save As / drag out of the chat window). Every
     module so far has needed at least one reminder about this.
5. **Detect newly saved files** by diffing the folder's mtimes rather than
   guessing filenames:
   ```
   find course/mvp-delivery/images -maxdepth 1 -type f -printf "%T@ %p\n" | sort -n
   ```
   Compare against the last known listing to isolate what's new.
6. **Visually confirm each new file** with the Read tool before touching
   anything — match it against what was pasted in chat by content, not by
   assumed ordering. (We hit a false alarm in Module 2 where dimension
   captions appeared out of order; the actual file content via `Read` on the
   exact path is the trustworthy source, not caption sequence.)
7. **Check for license red flags** before using an image — e.g. an Adobe
   Stock filename suffixed `_Editorial_Use_Only` restricts use to news/
   commentary contexts and excludes commercial or training material. Hold
   those back and ask rather than assuming it's fine.
8. **Sanity-check thematic fit**, not just license — an on-brand, well-lit
   photo can still be the wrong image (Module 2 surfaced a factory-robots +
   financial-dashboard photo that didn't relate to Agile work tracking at
   all). Flag mismatches instead of silently accepting whatever was pasted.
9. **Convert JPEG → PNG with the exact required filename** into
   `tools/module-pdf-generator/images_v2/`:
   ```python
   from PIL import Image
   Image.open(src).convert('RGB').save(dst, 'PNG')
   ```
   Filenames are load-bearing — `build_module_pdfs.py`'s `img()` looks up
   `images_v2/m{module}_{slot}.png` exactly, `.png` only. `.ai` (Illustrator)
   files can't be opened this way at all — flag those back to the user.
10. **Downscale before rebuilding.** Adobe Stock originals run 6000–8000px+ per side; reportlab embeds them at full resolution with no compression, which blew module PDFs out to 100–200MB each (every one over GitHub's 100MB push limit). Resize to a 2000px max dimension before saving into `images_v2/`:
    ```python
    from PIL import Image
    im = Image.open(path)
    if max(im.size) > 2000:
        scale = 2000 / max(im.size)
        im = im.convert('RGB').resize(
            (round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    im.save(path, 'PNG', optimize=True)
    ```
    No visible quality loss at slide resolution; took module PDFs from 100–200MB down to 15–27MB.
11. **Rebuild only the affected module**, not the full batch, for speed:
    ```python
    from generate_all import MODULES, build_module_pdf
    mod = next(m for m in MODULES if m['file'] == 'module-0N-...')
    build_module_pdf(mod)
    ```
12. **Render the specific changed pages to PNG** (PyMuPDF) and look at them
    before declaring done — don't just trust the file landed, confirm the
    crop and placement read correctly on the actual slide.
13. **Surface leftovers** — extra images the user saved beyond what was
    asked for don't get silently discarded or silently used; ask what they're
    for, or suggest a module they'd fit better.

## Known gotchas recap

- Paste ≠ saved to disk. Always confirm via the mtime diff, not the user's
  say-so alone (we've had "it's saved" turn out to be not-yet-saved once).
- Trust `Read`-by-exact-path content over any inferred ordering when
  matching files to what was pasted.
- Editorial-only stock licenses are a real block for training material —
  check filenames for the `_Editorial_Use_Only` suffix.
- `.ai` files need conversion outside this pipeline (Illustrator/Photoshop,
  or export to PNG) before they're usable here.
- Dimensions don't matter for placement — `draw_image_box()` cover-crops
  automatically — so don't worry about matching aspect ratios exactly.

## Progress tracker

- Module 1 (Software Modernization Overview) — ✅ done, 2026-08-15
- Module 2 (Azure DevOps Work Tracking) — ✅ done, 2026-08-15
- Modules 3–10 — not started

## Reference

- Companion doc: `diagram-style-upgrade.md` (the vector concept-map engine
  work — separate track from this photo-sourcing workflow)
- Images land in: `tools/module-pdf-generator/images_v2/`
- Sources staged in: `course/mvp-delivery/images/`
- Rebuild single module: see step 10 above
- Rebuild everything: `python generate_all.py` from
  `tools/module-pdf-generator/`
