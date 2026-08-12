---
layout: default
title: "E2E Test Report"
parent: AI in Software Testing
nav_order: 10
---

# E2E Test Report: `sample_coursware` — "AI in Software Testing" Course

**Date:** 2026-08-11
**Scope:** All 7 labs in `sample_coursware/AI-In-Software-Testing-main/` (Labs 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 2.4), plus a security review of the folder's contents.
**Method:** Local sandbox execution of every lab's exact starter code and commands, plus full live end-to-end verification of Labs 2.3 and 2.4 on real, public GitHub repositories using real GitHub Actions and the real GitHub Copilot coding agent.

---

## 1. Security findings (found while surveying the folder)

| Finding | File | Status |
|---|---|---|
| Real RSA private key (`-----BEGIN RSA PRIVATE KEY-----`, 27 lines) committed to git since the first commit (`f88ca8fa`), still tracked, repo is **public** on GitHub | `sample_coursware/AI-In-Software-Testing-main/my-ec2-key.pem` | **Unresolved — needs your decision.** Recommend rotating/terminating the AWS EC2 key pair immediately (independent of any git remediation, since only you have AWS access). A git-history rewrite to fully scrub it would need a force-push and explicit go-ahead before I'd perform it. |
| Plaintext AWS console password + access key/secret for an "Instructor01" account | `sample_coursware/labs.md` | Confirmed never committed to git (`git log --all`, `git ls-files` both empty for this path). Added to `.gitignore` as a precaution. Not publicly exposed. |
| Real AWS IAM credentials for 25 student accounts + 1 instructor account (access keys, secrets, console passwords, login URLs) | `sample_coursware/AI in Software Testing (8_12) - Sheet1.pdf` | Confirmed covered by the blanket `*.pdf` rule in `.gitignore`, never tracked, never committed. Not exposed. |
| Real ProTech remote-lab (HTML5/RDP) connection info — 14 login IDs (`PTACCESS570`–`583`) and host-VM admin credentials, all sharing the password `Pa$$w0rd`, for a live class running **August 12–13** | `sample_coursware/Innovation in Software Mail - Remote Lab Connection Info -AI in Software Testing.pdf` | Confirmed covered by the same blanket `*.pdf` rule, never tracked. Not exposed. |

**Net:** one real, live exposure (the `.pem` key, public repo) still needs your decision; everything else found was sensitive but not actually exposed.

---

## 2. Environment used for local testing

Python 3.11 sandbox (Windows). Packages installed: `pytest`, `pytest-cov`, `mutmut`, `flake8`, `fastapi`, `uvicorn`, `faker`, `flask`.

Gaps relative to what the labs assume:
- **No Java/Maven** — Lab 1.2 was verified by porting the grading logic to Python rather than compiling the real Java.
- **No `sqlite3` CLI** — Lab 2.2 used Python's built-in `sqlite3` module instead (functionally equivalent).
- The labs' own install scripts (`sudo dnf install ...`) target Amazon Linux/EC2, consistent with the AWS credentials found in the folder — these labs were designed to run on ProTech-provisioned AWS/Windows VMs, not arbitrary local machines.

---

## 3. Results by lab

### Lab 1 (1.1) — Manual vs. AI-Assisted Testing: ✅ Clean
Wrote 16 tests covering every business rule in the docstring plus every item in "Common Missed Cases." All 16 passed — the starter code is internally consistent with its own documentation. No issues found.

### Lab 2 (1.2) — Reverse-Engineering Legacy Java: ✅ Bug and numbers verified exactly
Ported the exact `ShippingCalculator` logic to Python (no Java/Maven available) and confirmed the documented case-sensitivity bug precisely:
- `"CA"` → $9.99, `"ca"` → $16.74 — a $6.75 / 67.6% overcharge, matching the lab's claims to the penny.
- Also confirmed: `wt=0` leaves `b=0` (falls through all weight tiers); negative `wt` is silently accepted.

No content issues. Environmental gap only: Java/Maven not preinstalled here, and the lab's own setup script assumes Amazon Linux (`dnf`), so Windows-laptop students need a different install path than the one given.

### Lab 3 (1.3) — Coverage & Mutation Testing: ⚠️ Two real issues
- The "you will see output similar to this" example in the lab text (`13 stmts, 69% cover, missing 15,25,27,30`) **does not match** what current `pytest-cov` actually reports for the exact starter code given. Actual: `15 stmts, 73% cover, missing 20,30,32,35`. The four *conceptual* gaps (ValueError raise, SAVE10, SAVE20, holiday lines) are correct — only the printed numbers are stale, likely from an older `pytest-cov` version.
- **`mutmut` 3.7.0 refuses to run natively on Windows at all** — it errors immediately: *"To run mutmut on Windows, please use the WSL."* This is a hard tool limitation, not a sandbox artifact. Part 6 (mutation testing) is a dead end for any student on a Windows laptop without WSL provisioned.
- Everything else (coverage climbing from 73%→100% with targeted tests, branch vs. line coverage gap) worked exactly as described.

### Lab 4 (2.1) — Exploratory/Edge-Case Testing (Flask): ✅ Confirmed, plus 2 gaps beyond the lab's own answer key
Every claim in "API Weaknesses Revealed" reproduced exactly: whitespace-only name → 201, `age=999` → 201 (no upper bound), `age=true` → 400 but for the documented "wrong reason" (`bool` is a subclass of `int` in Python), `email="alice@"` → 201, 10,000-char name → 201.

**Bonus finding not in the lab's answer key:** `name` has no type check at all — passing an integer or a JSON array for `name` also returns 201 (only `age` is type-checked in this code). Same class of bug the lab is teaching students to look for; worth adding to the discussion.

### Lab 5 (2.2) — Synthetic Data (FastAPI + SQLite + Faker): ✅ Fully works
Stood up the API, ran the exact `/products`, `POST /orders`, `/customers/{id}/orders` endpoints — all behaved as documented, including the 404 on a customer with no orders. Wrote and ran a Faker seed script meeting every stated Part 3 requirement (1,000 customers / 50 products / 10,000 orders, unique emails, 5 price-banded categories, weighted country distribution) in under half a second. All data-quality validation queries (duplicates, referential integrity, NULLs, distribution) came back clean — country distribution landed within a few points of the 40/15/10/10/25 target. No issues found. Minor: the lab's `sudo dnf install -y sqlite` step is Amazon-Linux-specific; Windows has no `sqlite3` CLI by default, though Python's stdlib `sqlite3` module covers everything the lab actually needs.

### Lab 6 (2.3) — CI/CD with GitHub Actions: ⚠️ Two real, **live-verified** defects
Fully executed live on a real public repo: **https://github.com/derricksobrien/discount-ci-lab**

| Step | Result |
|---|---|
| Baseline push | ✅ Green |
| Round 1 (lint failure) | ✅ Reproduced live — `E305` + `E501` |
| Round 1's documented "fix" (dict split across lines, 1 blank line) | ❌ **Still fails live** — `E305` persists |
| Round 1's real fix (2 blank lines) | ✅ Green |
| Round 2 (failing test) | ✅ Reproduced live, fixed, confirmed green |
| Round 3 (coverage drop, 3 of 5 tests removed) | ✅ Reproduced live (69% < 80% threshold), restored, confirmed green |
| Round 4 (branch coverage, `--cov-fail-under=75`) | ✅ **Stayed green** (92.9% branch coverage) — the lab's "may fail" claim does not hold with its own starter tests |

Both defects (Round 1's documented fix not actually fixing the problem, and Round 4's failure claim not materializing) are now confirmed on real GitHub Actions, not just local pytest-cov output. Minor: Round 3's instructions reference deleting "the holiday, coupon, and guest tests" but no test is named or related to "guest" among the 5 given tests — likely leftover phrasing from an earlier version of the file.

### Lab 7 (2.4) — TDD with a GitHub Copilot Agent: ⚠️ Structurally sound, two real defects found via full live run
Fully executed live, including a real Copilot coding-agent invocation, on: **https://github.com/derricksobrien/tdd-bank-lab** (PR #1)

- **Phase 1/2 (Red):** Wrote all 7 acceptance-criteria tests, confirmed 7/7 fail locally against the stub, pushed to `feature/transfer-funds`, opened the PR. CI ran automatically and correctly showed 7/7 failing.
- **Setup-verification gap (new finding):** Before any tests are written, the lab has students manually trigger the CI workflow to "confirm the setup works." With an empty `test_bank.py`, `pytest` exits code 5 ("no tests collected"), which GitHub Actions reports as a **failed** run. A student following this step literally sees a red ❌ at a checkpoint meant to just confirm the setup is fine — not called out anywhere in the lab text.
- **Phase 3 (Green):** Posted the exact `@copilot implement...` comment specified in the lab. The real Copilot coding agent (`copilot-swe-agent[bot]`) picked it up within ~2 minutes (👀 acknowledgment reaction, then a commit). The implementation correctly handles all 7 acceptance criteria, including the `isinstance(amount, bool)` trap, and only touched `bank.py` as instructed — did not modify `test_bank.py`.
- **Verification, not blind trust:** Pulled the agent's commit and ran the tests myself rather than assuming the agent's word — **7/7 passed locally.**
- **Defect 1 (new finding):** The agent's commit also included two `__pycache__/*.pyc` binary files. Root cause: unlike Lab 6, Lab 7's starter-file instructions never have students create a `.gitignore`.
- **Defect 2 (new finding):** The lab states "CI will rerun automatically" after the agent pushes. In practice, **GitHub gates any workflow run triggered by a Copilot-agent commit behind a manual "Approve and run" click every time** — confirmed live; the standard fork-PR-approve API endpoint explicitly does not cover this case, so it can only be approved through the web UI. The workflow sat in `action_required` status until manually approved, then went green. This is a materially different experience than "automatically," and would confuse students expecting the checks to update on their own.

---

## 4. Summary of defects worth fixing before a live class

| # | Lab | Defect | Severity | Live-verified? |
|---|---|---|---|---|
| 1 | 1.3 | `mutmut` will not run natively on Windows at all (needs WSL) | High — blocks the entire mutation-testing section for Windows students | Yes (tool-level error) |
| 2 | 2.3 | Round 1's documented lint "fix" still fails (`E305`); needs a 2nd blank line, not 1 | Medium — stalls students at a step meant to be a quick fix | **Yes, on real GitHub Actions** |
| 3 | 2.4 | Copilot-agent-triggered CI requires manual "Approve and run"; lab says it reruns automatically | Medium — confuses students watching for a status that won't update itself | **Yes, on real GitHub Actions** |
| 4 | 2.4 | Setup-verification step (empty test file) shows a false "failed" CI run before any code is written | Low-Medium — cosmetic but disorienting at the very first checkpoint | **Yes, on real GitHub Actions** |
| 5 | 1.3 | Example coverage output (13 stmts/69%/lines 15,25,27,30) doesn't match current `pytest-cov` output for the same code | Low — cosmetic, conceptually still correct | Yes |
| 6 | 2.3 | Round 4's "may fail" branch-coverage claim doesn't reproduce with the lab's own starter tests | Low — round completes without the intended teaching moment | **Yes, on real GitHub Actions** |
| 7 | 2.1 | `name` field has no type validation (int/array accepted) — not listed in the lab's own answer key | Low — a free bonus teaching point, not a defect | Yes |
| 8 | 2.4 | Copilot agent commits stray `__pycache__/*.pyc` files (no `.gitignore` provided in starter files) | Low | Yes |
| 9 | 2.3 | Round 3 references a non-existent "guest test" | Low — cosmetic wording issue | Yes |

---

## 5. What worked without any issues

Labs 1.1, 2.2, and the core mechanics of 1.2 and 2.1 all matched their documentation exactly, with zero discrepancies between what the lab promises and what actually happens when run. Both live GitHub repos (`discount-ci-lab`, `tdd-bank-lab`) are real, public, and left in a fully green state — Lab 6 cycled through all 4 break/fix rounds back to green, and Lab 7's PR shows a real, human-reviewed, AI-implemented, test-passing, CI-green pull request end to end.
