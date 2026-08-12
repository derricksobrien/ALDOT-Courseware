---
layout: default
title: "Testing Fundamentals for Newcomers"
parent: AI in Software Testing
nav_order: 1
---

# Software Testing Fundamentals — A Primer for People New to Testing

**Who this is for:** the AI in Software Testing course assumes you already think like a tester — Lab 1.1 opens with "write pytest tests" on the assumption you already know what a test *is*, what makes one good, and why "it passed" isn't the same as "it's correct." If your day job is development, product, design, or something else entirely and testing isn't your main discipline, this fills that gap before Day 1.

**None of this is Microsoft-specific.** These are the standard concepts and vocabulary used across the testing industry, sourced from the field's own reference material — the ISTQB syllabus, Martin Fowler's writing, and community resources like Ministry of Testing and Guru99.

**Created:** 2026-08-12

---

## 1. What Is Software Testing, Actually?

Software testing is the process of evaluating a system to find out whether it does what it's supposed to do — and, just as often, to find the specific inputs and conditions where it doesn't. It's easy to conflate this with debugging, but they're different jobs:

- **Testing** finds *that* something is wrong (and ideally, exactly which input triggers it).
- **Debugging** finds *why* it's wrong and fixes it.

A tester doesn't need to know how the code works internally to do their job well — they need to know what the code is *supposed* to do, and be systematic about checking whether it actually does that across the full range of inputs a real user (or attacker, or edge case) might throw at it. That's the entire premise behind Lab 2.1 in this course: an AI can generate the input categories a human tester would eventually think of, but slower.

## 2. Vocabulary You'll Hit Starting Day 1

The course uses these terms without defining them, on the assumption you already know them:

| Term | Meaning |
|---|---|
| **Test case** | One specific input plus the expected output — "if I call this function with X, I expect Y." |
| **Assertion** | The line of code that actually checks the expected result against the real one (`assert result == 80.00`). A test with no assertion doesn't test anything, even if it "runs." |
| **Test suite** | A collection of test cases, usually in one file, run together. |
| **Pass / Fail** | Whether the assertion held. A "passing" test only tells you the assertion was true for that one input — it says nothing about inputs you didn't test. |
| **Defect / Bug** | A flaw in the code that causes it to produce the wrong result. |
| **Failure** | The *observable* symptom of a defect — what you actually see go wrong. (The defect is the cause; the failure is the effect.) |
| **False positive** | A test reports a problem that isn't real (the test itself is broken, not the code). |
| **False negative** | A test reports success when there's actually a real problem (the test isn't checking the right thing — this is the failure mode Lab 1.3's mutation testing is specifically designed to catch). |
| **Regression** | A previously-working feature breaks because of a later change. Re-running old tests after new changes ("regression testing") is how you catch this. |
| **Coverage** | How much of the code your tests actually executed. High coverage is necessary but not sufficient for confidence — see Lab 1.3 for exactly why. |

## 3. Where Testing Fits in the Bigger Picture

Testing isn't a phase that happens after development is "done" — in modern practice it happens continuously, alongside writing the code (this course's whole premise, using AI to generate tests as you write functions, is a version of that). The general shift in the industry over the last ~15 years has a name: **"shift left"** — moving testing earlier in the process, because a bug caught while you're writing the function costs a lot less to fix than the same bug caught after it ships.

## 4. The Testing Pyramid

The most widely cited mental model for *how much* of each kind of test to write comes from Martin Fowler's ["Test Pyramid"](https://martinfowler.com/bliki/TestPyramid.html):

- **Base (most tests): Unit tests** — test one small piece of code in isolation. Fast, cheap, reliable. Everything in Labs 1.1–1.3 of this course is unit testing.
- **Middle: Integration/service tests** — test how pieces work together (e.g., does the API correctly talk to the database). Lab 2.2's FastAPI + SQLite exercise lives here.
- **Top (fewest tests): End-to-end tests** — test the whole system through the real interface a user would use. Slower, more brittle, more expensive to maintain — which is exactly why you want fewer of them.

The shape matters: a test suite with a handful of unit tests and dozens of slow, flaky end-to-end tests is upside-down, and it's a common enough mistake that it has its own name ("the ice cream cone anti-pattern").

## 5. Types of Testing You'll Hear About

A few axes testers use to describe what kind of testing they're doing — useful vocabulary for reading any testing-related job description, ticket, or conversation:

- **Functional vs. non-functional** — does it do the right thing (functional), vs. does it do it fast enough / securely enough / reliably enough (non-functional: performance, security, usability).
- **Black-box vs. white-box vs. gray-box** — black-box testing checks behavior without looking at the code (exactly what Lab 1.2's "read the code, then use AI to explain it" exercise pushes against); white-box testing is written with full knowledge of the internal implementation; gray-box is a mix.
- **Manual vs. automated** — a human clicking through the app, versus code that runs the checks for you. This whole course is about automated testing, accelerated further with AI.
- **Smoke testing** — a quick "does the build even start" check, usually run first.
- **Exploratory testing** — testing without a fixed script, using what you find to decide what to try next (this is Lab 2.1, by name).

## 6. Test Design Basics (This Underpins Lab 2.1)

Two classic test-design techniques, which Lab 2.1 uses without naming them explicitly:

- **Equivalence partitioning** — group inputs into "buckets" that should all behave the same way, and test one representative from each bucket instead of every possible value. (Testing `age=25` and `age=40` both as "should succeed" is redundant once you understand they're in the same equivalence class.)
- **Boundary value analysis** — the edges of those buckets are where bugs cluster. If the rule is "age must be 18 or older," the interesting test values are 17, 18, and 19 — not 25 or 40. This is exactly the "boundary value" prompt used in Lab 2.1.

Knowing the *names* of these techniques isn't required to do them — but it helps to recognize that "test the edges, not just the middle" is a formal, well-studied practice, not just a hunch.

## 7. Writing (and Reading) a Bug Report

When a test fails, or you find something wrong during exploratory testing, the value of that finding depends entirely on how well you can describe it to someone who has to fix it. A useful bug report has:

- **A clear title** — specific enough to understand the problem without opening the report.
- **Steps to reproduce** — the exact sequence that triggers it, every time.
- **Expected result** vs. **actual result** — stated separately and precisely.
- **Environment/context** — what input, what version, what conditions.

This is the same discipline behind Lab 1.2's bug write-up: "same input, different case, $6.75 more, 68% overcharge" is a good bug report because it's specific and reproducible — "the shipping calculator seems off sometimes" is not.

---

## Free Resources to Go Deeper

None of these require a Microsoft account, and all are free:

| Resource | What it's for |
|---|---|
| [ISTQB Foundation Level Syllabus](https://astqb.org/syllabus/) | The global standard curriculum for software testing fundamentals — free PDF, no prerequisites. If you want one structured, comprehensive document, this is it. |
| [ISTQB Standard Glossary of Testing Terms](https://www.astqb.org/documents/Glossary-of-Software-Testing-Terms-v3.pdf) | The industry's own reference dictionary — useful to keep open while reading any testing material, including this one. |
| [Martin Fowler — "Test Pyramid"](https://martinfowler.com/bliki/TestPyramid.html) | Short, canonical, widely cited — the single most useful 10-minute read on how to think about test strategy. |
| [Ministry of Testing — Taking Your First Steps in Software Testing](https://www.ministryoftesting.com/articles/taking-your-first-steps-in-software-testing) | Written specifically for career-changers and people new to testing as a discipline — addresses the "I don't know the vocabulary yet" anxiety directly. |
| [Ministry of Testing — Software Testing Glossary](https://www.ministryoftesting.com/software-testing-glossary/what-is-testing) | Short-form definitions with video explainers for testing terms, browsable by topic. |
| [Guru99 — Software Testing Tutorial](https://www.guru99.com/software-testing.html) | A full free tutorial series covering the SDLC, testing types, test case design, and defect lifecycle in more depth than fits here. |
| [How to Write a Good Bug Report — Software Testing Help](https://www.softwaretestinghelp.com/how-to-write-good-bug-report/) | Practical, example-driven guide with templates. |

**Recommended order if you're starting from zero:** read this page first, skim the Ministry of Testing "first steps" article for the human side of it, then use the ISTQB syllabus as your reference document to return to as testing terms come up in the actual labs.
