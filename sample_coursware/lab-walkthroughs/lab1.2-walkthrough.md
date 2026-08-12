# Lab 1.2 Walkthrough — Reverse Engineering Legacy Code with AI

**Use this if:** you want to see exactly what this lab looks like, click for click, before sitting down at a lab machine — or if you're reviewing it afterward. Every result below is real: the Java code actually compiled, the tests actually ran against it (via a real JDK 21 + Maven 3.9 setup), and the bug reveal you'll read about genuinely happened, to the exact dollar amount the lab describes.

**Original lab:** `sample_coursware/AI-In-Software-Testing-main/1.2-reverse-engineer-legacy-code.md`

---

## What you're building toward

You've inherited a shipping calculator with no documentation, no tests, and no one left who remembers what it's supposed to do. The goal isn't just to understand it — it's to find the one input that makes it quietly charge the wrong price, without an error, without a crash, without anything flagging it. That's the class of bug this lab is built around: not the kind that breaks loudly, the kind that ships.

---

## Step 1 — Read the code yourself first, before any AI tool

Create the Maven project structure and paste in `ShippingCalculator.java` exactly as given.

![VS Code editor showing ShippingCalculator.java](images/01-editor-shippingcalculator.png)

> **Why does the lab insist on a manual read first?** Because the entire second half of this lab depends on you having a "before" state to compare against. If you let AI explain this code first, you'll never know which parts you genuinely couldn't follow versus which parts you'd have eventually worked out yourself. The variable names (`b`, `r`, `z`, `wt`, `xpr`, `cust`) are abbreviated on purpose — this is what actual inherited code looks like, and the discomfort of reading it cold is part of the exercise.
>
> Before moving on, try to answer honestly: what does `z` represent? What happens if `dest` is `"ca"` instead of `"CA"`? Don't look ahead — that second question is the whole lab.

---

## Step 2 — Ask AI to explain the code

Paste the function into your AI tool with the lab's suggested prompt:

![AI chat explaining the ShippingCalculator function line by line](images/02-chat-explain-code.png)

> **Notice what the explanation surfaced without being asked to hunt for bugs specifically** — it flagged the case-sensitivity gap as part of a plain "explain this" prompt. That's not guaranteed; a less specific prompt, or a different AI tool, might describe the same code correctly without ever mentioning that `.equals()` is case-sensitive in Java. Compare this against your own answer to "what happens if `dest` is `'ca'`" from Step 1 — did you catch it, did the AI catch it, or did neither of you until the next step made it explicit?

---

## Step 3 — Ask AI to find defects specifically

A more targeted prompt, asking specifically for problems rather than an explanation:

![AI chat listing defects: case sensitivity, zero weight, negative weight](images/03-chat-find-defects.png)

> **Why does asking for defects specifically surface more than asking for an explanation did?** An "explain this" prompt optimizes for a correct summary of what the code does. A "find defects" prompt optimizes for what's *wrong* with it — different task, different attention. This is the same lesson Lab 1.1 taught with test generation: the AI doesn't spontaneously audit code for you as a side effect of describing it. You have to ask for the audit directly.

---

## Step 4 — Generate tests, including one that targets the case-sensitivity gap directly

Create `ShippingCalculatorTest.java`. Alongside the usual zone/weight/discount tests, include one that compares uppercase and lowercase input directly against each other:

![VS Code editor showing ShippingCalculatorTest.java](images/04-editor-test-class.png)

> **Why write `testLowercaseDestinationShouldMatchUppercaseResult` as a comparison between two calls, instead of hard-coding an expected dollar amount?** Because the test's whole point is to check a *relationship* — "the same package to the same place should cost the same regardless of how the state code was typed" — not a specific number. A test that just asserts `calculateShipping("ca", ...) == 9.99` would require you to already know the correct answer, which defeats the purpose of using the test to *discover* that the two calls disagree.

---

## Step 5 — Run the tests against the original code

```bash
mvn test
```

![Terminal showing mvn test failing on the lowercase comparison test](images/05-terminal-mvn-test-fail.png)

> **This is the actual bug, caught in the act.** Seven tests pass. One doesn't — and the failure message tells you exactly what the lab's "Hidden Bug Reveal" section describes in prose: the same shipment, same weight, same everything except the letter case of the destination, comes back **$9.99 for `"CA"` and $16.74 for `"ca"`** — a $6.75, 68% difference, for input that any reasonable person would consider identical. This is exactly why the lab picked this specific bug to teach with: nothing crashes, nothing throws an exception, nothing looks wrong in a casual code review. It just quietly charges some customers more, based entirely on whether whatever system called this function happened to send uppercase or lowercase state codes.

---

## Step 6 — Trace it manually, then apply the one-line fix

Before fixing it, trace through both calls by hand:
- `"CA"` matches the zone-1 check directly → zone 1, rate $0.50/lb
- `"ca"` matches *none* of the zone 1–3 checks (all of them use `.equals()` against uppercase literals) → falls through to the `else` → zone 4, rate $2.00/lb, **plus** a $3.75 fuel surcharge that only applies when `z > 2`

Add one line, as the first line inside the method, before the zone comparisons:

![VS Code editor showing the one-line fix: dest = dest.trim().toUpperCase()](images/06-editor-the-fix.png)

> **Why `.trim()` in addition to `.toUpperCase()`?** The lab's fix line does both, and it's worth noticing why: `.toUpperCase()` alone fixes the case problem, but a stray leading or trailing space (`" CA"` from a copy-paste, a CSV export, a form field) would *still* fail every `.equals()` check even after uppercasing. Fixing exactly the bug you found, and not the adjacent one sitting right next to it, is how bugs like this survive a "fix" and come back a month later under a slightly different input.

---

## Step 7 — Re-run and confirm all 8 pass

```bash
mvn test
```

![Terminal showing all 8 tests passing after the fix](images/07-terminal-mvn-test-pass.png)

All 8 tests pass, including the one that was failing — confirming the fix resolves the exact discrepancy it was written to catch, not just a related symptom.

---

## Discussion questions (for your own notes, or the group)

1. Would this bug have survived a code review? Reading the original function top to bottom, is there anything that visually signals "this input isn't normalized"?
2. This bug never throws an exception or logs an error — it just returns a wrong-but-plausible number. What kind of test *category* (not this specific test) is designed to catch that class of bug in general?
3. The fix touches one line and adds `.trim()` alongside `.toUpperCase()` for a reason that isn't obvious from the bug report alone. What does that suggest about fixing a bug based only on the *specific* failing input you found, versus the general *class* of input the fix needs to handle?
4. If you'd only asked AI to "explain this code" and never asked it to "find defects," would you have caught this before writing tests?

---

## Key takeaway

The most dangerous bugs in inherited code aren't the ones that crash — they're the ones that return a wrong answer confidently and quietly. AI is genuinely good at recognizing this specific pattern (unnormalized string comparison) because it's seen it thousands of times before, but it surfaces reliably only when you ask the right question — "explain this" and "find defects in this" are different prompts that produce different depths of review, even against the exact same code.
