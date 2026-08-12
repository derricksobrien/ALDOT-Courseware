# Mojibake Explanation (Timestamped)

**Created:** 2026-08-10T22:04:22.744-06:00  
**Topic:** UTF-8 / encoding artifacts such as `â€”`, `â†’`, and similar text corruption

## What is mojibake?

**Mojibake** is garbled text caused by decoding bytes with the wrong character encoding.

Example:
- Intended character: `—` (em dash)
- Broken rendering: `â€”`

- Intended character: `→`
- Broken rendering: `â†’`

## Why this happens

Text is stored as bytes. If text is written as one encoding (commonly UTF-8) but later read as another encoding (commonly Windows-1252/Latin-1), characters get misinterpreted and appear corrupted.

## Typical occurrence path

1. Content is authored correctly in UTF-8.
2. A tool/editor/pipeline reads or rewrites it with a different encoding.
3. The site or file renders mojibake artifacts (for example, `â€”`, `â†’`, `ðŸ...`).

## Common sources of this issue

- Editor encoding mismatch between contributors
- Copy/paste through tools that alter encoding
- Build/render steps with inconsistent charset handling
- Stale CDN/browser cache briefly showing old content after a fix

## How to prevent it

- Standardize on UTF-8 across editors and pipelines
- Keep repository text files saved as UTF-8
- Avoid mixed encoding conversions in scripts/tools
- After deploying a fix, do a hard refresh or cache-busting URL check

## Quick diagnosis pattern

If you see text like `â€”`, `â†’`, `â€œ`, `ðŸ...`, it usually indicates UTF-8 bytes being interpreted as Windows-1252/Latin-1.

