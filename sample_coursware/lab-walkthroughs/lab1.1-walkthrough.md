# Lab 1.1 Walkthrough — Manual Testing vs. AI-Assisted Testing

**Use this if:** you want to see exactly what this lab looks like, click for click, before you sit down at a lab machine — or if you're reviewing it afterward and don't have access to one anymore. Every screenshot below shows real, verified output: the code actually ran, the tests actually passed, in this exact form.

**Original lab:** `sample_coursware/AI-In-Software-Testing-main/1.1-testing-manual-vs-ai.md`

**New to VS Code or Python?** Start with **Step 0** below — it walks through opening VS Code, finding the terminal, checking that Python is installed, and creating your first file, before Step 1 picks up where the original lab begins. If you've used VS Code and a terminal before, skip straight to [Step 1](#step-1--create-discountpy).

---

## What you're building toward

By the end you'll have three separate test files for the same function — one you wrote by hand, one an AI wrote from a quick prompt, and one an AI wrote from a better prompt — and a side-by-side sense of what each one is actually good for. The point of the lab isn't the function itself; it's noticing *where* your manual tests and the AI's tests diverge, and why.

---

## Step 0 — Before You Start: Setting Up Your Environment

If you've never used VS Code, a terminal, or Python before, this step is for you. It covers everything between "logged into the lab machine" and "ready to start Step 1." None of this is in the original lab document — it's assumed knowledge there. If you already know this, skip to Step 1.

### 0a. Open VS Code

Your ProTech lab machine is a Windows desktop. Find **Visual Studio Code** the same way you'd find any other program:

- Click the **Start** button (bottom-left corner of the screen), type `Visual Studio Code`, and press **Enter**.
- Or double-click the **VS Code** icon on the desktop if one is provided.

VS Code will open to either a blank window or whatever was open last. That's fine either way — the next step fixes it.

### 0b. Create a folder for the lab and open it in VS Code

Everything you create in this lab (`discount.py`, your test files) needs to live in one folder so Python and pytest can find them together. Create that folder first:

1. In VS Code, go to the top menu: **File → Open Folder…**
2. In the dialog that appears, navigate to somewhere you'll remember — for example `C:\Users\<your username>\Documents`.
3. Click **New Folder**, name it `lab1.1`, and press **Enter**.
4. With `lab1.1` selected, click **Select Folder**.
5. If Windows asks "Do you trust the authors of the files in this folder?", click **Yes, I trust the authors**.

VS Code will reopen with `LAB1.1` shown at the top of the **Explorer** panel on the left (a blank panel, since the folder is empty). Everything you create from here on should go inside this folder.

> **Why does the folder matter?** `pytest` and Python's `import` statement both work relative to "where you are" when you run a command. If `discount.py` and `test_discount_manual.py` end up in different folders, the import in Step 3 (`from discount import calculate_discounted_price`) will fail with `ModuleNotFoundError`. One folder, all files in it, no exceptions.

### 0c. Open the integrated terminal

The **terminal** is where you type commands like `pip install pytest` and `pytest test_discount_manual.py -v` — it's a text-based way to run programs, instead of clicking icons. VS Code has one built in, so you never have to leave the editor:

1. Top menu: **Terminal → New Terminal**.
2. A panel opens at the bottom of the window with a blinking cursor next to a prompt (something like `PS C:\Users\you\Documents\lab1.1>`). This is PowerShell — Windows' default command-line shell.

Keep this terminal panel open for the rest of the lab. Every `pip` and `pytest` command in the steps below gets typed here, then run by pressing **Enter**.

> **If you accidentally close it:** repeat **Terminal → New Terminal**. VS Code always opens new terminals in the folder you have open, so you don't need to navigate anywhere first.

### 0d. Confirm Python is installed

Type the following into the terminal and press **Enter**:

```powershell
python --version
```

You should see output like `Python 3.11.x`. If instead you see an error (`python is not recognized...`), try:

```powershell
py --version
```

If **neither** command works, Python isn't installed or isn't on your `PATH`. Flag your instructor or ProTech support (contact info in [Lab Access & Credentials](../../docs/ai-software-testing/lab-access.md)) rather than trying to install it yourself mid-lab — the lab machines should have it preinstalled.

> **What is Python, exactly?** It's the programming language this whole course uses. When you type `python` in the terminal, you're telling Windows "run the Python program." The `--version` flag just asks it to print its version number and exit, so you can confirm it's there without actually running any code yet.

### 0e. What `pip` is (you'll use it in Step 2)

`pip` is Python's package installer — it downloads and installs libraries other people wrote, like `pytest`, so you can use them in your own code. You don't need to do anything with it yet; Step 2 has the exact command. It's mentioned here just so `pip install pytest` doesn't come out of nowhere.

### 0f. Create your first file: `discount.py`

This is the file Step 1 asks you to create. Here's how to actually do that in VS Code, click for click:

1. In the **Explorer** panel on the left (where your `LAB1.1` folder is shown), hover over the folder name until a row of small icons appears to the right of it.
2. Click the **New File** icon (a page with a `+` on it — the first icon in that row).
3. Type the filename exactly: `discount.py`, then press **Enter**.
4. The file opens automatically in the editor area, empty and ready for text.

> **Why does the `.py` matter?** The `.py` extension is what tells VS Code (and Python) "this is a Python file." Get the extension wrong (`discount.txt`, `discount` with no extension) and Python won't recognize it as code to run, and VS Code won't offer Python-specific help like syntax highlighting.

### 0g. Paste in the starter code and save

Copy the exact function below (this is the starter code the original lab provides) and paste it into your empty `discount.py`:

```python
def calculate_discounted_price(price, customer_type, coupon_code=None, is_holiday=False):
    """
    Calculate the final discounted price for a customer.

    Business rules:
    - premium customers receive 20% off
    - standard customers receive 10% off
    - guests receive no customer discount
    - coupon code SAVE10 gives an additional 10% off
    - coupon code SAVE20 gives an additional 20% off, but only for premium customers
    - holiday promotion gives an additional 5% off
    - discounts are applied sequentially
    - final price is rounded to 2 decimal places
    - price must be greater than or equal to 0
    - unknown customer types are treated as guests
    - unknown coupon codes are ignored
    """

    if price < 0:
        raise ValueError("price cannot be negative")

    customer_type = customer_type.lower()

    if customer_type == "premium":
        price = price * 0.8
    elif customer_type == "standard":
        price = price * 0.9

    if coupon_code == "SAVE10":
        price = price * 0.9
    elif coupon_code == "SAVE20" and customer_type == "premium":
        price = price * 0.8

    if is_holiday:
        price = price * 0.95

    return round(price, 2)
```

Then **save the file**: press **Ctrl+S**, or use **File → Save**. Look at the tab at the top of the editor — if the filename has a dot (`● discount.py`) instead of an X, it isn't saved yet. Always save before running anything; Python and pytest only ever see what's on disk, not what's on screen.

> **A quick sanity check before moving on:** in the terminal, run `python discount.py`. Nothing should happen — no output, no error, just a new blank prompt. That's expected: the file only *defines* a function, it doesn't *call* it. If you get an error instead, re-check the paste for missing indentation (Python is strict about it) and save again.

You're now caught up to where the original lab — and Step 1 below — begins.

---

## Step 1 — Create `discount.py`

*(Already done if you completed Step 0 — skim this for the "why," then continue to Step 2.)*

Create a new file named `discount.py` and paste in the starter function exactly as given.

![VS Code editor showing discount.py](images/01-editor-discount.png)

> **Why this function, specifically?** A simpler discount function — one that only checks customer type — would let you write three tests and call it done. This one stacks five separate behaviors on top of each other: customer tier, two different coupon codes (one of which only works for one tier), a holiday flag, rounding, and negative-price rejection. That stacking is deliberate. It's what creates the gap between "tests that make the obvious cases pass" and "tests that actually pin down the business rules" — which is the entire thing this lab is trying to show you. A trivial function can't produce that gap.

**Read the docstring before you write anything.** Notice these two rules in particular, because they're the ones almost everyone misses on a first pass:
- `SAVE20` only applies **if the customer is premium** — a standard customer with a `SAVE20` code just... doesn't get it. No error, no warning, it's silently ignored.
- Unknown customer types (a typo, a new tier someone forgot to add) fall through to guest pricing rather than raising an error.

---

## Step 2 — Install pytest

Open a terminal in the same folder and run:

```bash
pip install pytest
```

![Terminal showing pip install pytest](images/02-terminal-pip-install.png)

> **Why pytest and not `unittest`?** No real reason specific to this lab — it's just the standard for Python testing at this point, and its `assert`-based syntax (no `self.assertEqual(...)` boilerplate) keeps the tests readable, which matters more than usual here since you're about to compare them side by side against AI output.

---

## Step 3 — Write your manual tests, *before* touching any AI tool

Create `test_discount_manual.py` the same way you created `discount.py` in Step 0 (hover the folder in Explorer → **New File** icon → type the name → **Enter**). It needs to sit in the same `lab1.1` folder, right next to `discount.py`, not in a subfolder. The lab gives you one example test to start from:

```python
from discount import calculate_discounted_price


def test_premium_customer_gets_20_percent_discount():
    result = calculate_discounted_price(100, "premium")
    assert result == 80.00
```

Now extend it yourself. Here's a representative set a careful student might write in the first pass — five tests covering the obvious cases:

![VS Code editor showing test_discount_manual.py](images/03-editor-test-manual.png)

> **Why write these before using AI at all?** This is the actual experiment, not busywork. If you use AI first, you'll anchor on whatever it suggests and lose the ability to notice what *you* would have thought of on your own versus what it caught that you didn't. The comparison only means something if your manual pass happens in isolation.
>
> Notice what's *not* in this list yet: nothing about `SAVE20` being premium-only, nothing about case sensitivity (`"PREMIUM"` vs `"premium"`), nothing about negative prices, nothing about rounding. That's not a mistake in this walkthrough — it's realistic. Those are exactly the cases the lab's "Common Missed Cases" section calls out, and they're the ones worth watching for when you get to the comparison step.

---

## Step 4 — Run your manual tests

```bash
pytest test_discount_manual.py -v
```

![Terminal showing 5 manual tests passing](images/04-terminal-manual-run.png)

All 5 pass — which tells you the tests are *correct*, not that they're *complete*. That distinction is the whole lesson of this lab.

---

## Step 5 — Use AI with a zero-shot prompt

Now bring in ChatGPT, Copilot Chat, or whatever AI tool you have access to. Use the lab's suggested zero-shot prompt — just the instruction, no extra guidance:

> *"Write pytest unit tests for the following Python function in `test_discount_ai.py`. Include normal cases and edge cases. [paste the function]"*

![AI chat showing zero-shot prompt and response](images/05-chat-zero-shot.png)

Save whatever it gives you as `test_discount_ai.py` and run it:

```bash
pytest test_discount_ai.py -v
```

![Terminal showing 8 zero-shot AI tests passing](images/06-terminal-ai-run.png)

> **Why does the zero-shot version land at 8 tests instead of 5 or 20?** A bare "include edge cases" prompt gets you broad-but-shallow coverage — the AI reliably thinks of negative price and zero price (classic edge cases it's seen a thousand times), and it does test both coupon codes. What it typically *doesn't* do without being told is verify the **eligibility rule** — that `SAVE20` should silently fail for a standard customer, not just succeed for a premium one. It tested that SAVE20 works; it didn't test that SAVE20 *doesn't* work when it shouldn't. That's a subtle but real gap, and it's exactly the kind of thing a zero-shot prompt tends to skip: the AI doesn't know which parts of your docstring are the parts that actually matter until you tell it.

---

## Step 6 — Improve the prompt and try again

This time, name the specific things you want covered — including the negative case (SAVE20 *not* applying):

> *"Write a complete pytest test suite for this function in a new file. Focus on: customer types premium/standard/guest/unknown, valid coupons SAVE10 and SAVE20, invalid coupon codes, holiday and non-holiday pricing, negative prices, zero price, rounding behavior, combinations where multiple discounts apply, and cases where SAVE20 should NOT apply. Also include clear test names. [paste the function]"*

![AI chat showing improved prompt and response](images/07-chat-improved-prompt.png)

Save the result as `test_discount_ai_improved.py` and run it:

```bash
pytest test_discount_ai_improved.py -v
```

![Terminal showing 16 improved AI tests passing](images/08-terminal-ai-improved-run.png)

> **Why did naming the cases explicitly roughly double the test count?** Every phrase in that improved prompt maps to a test the zero-shot version was missing: "cases where SAVE20 should NOT apply" → the two negative-eligibility tests; "customer types ... unknown" → the case-insensitivity and unknown-type tests; "combinations where multiple discounts apply" → the sequential-not-additive test. This is the core prompting lesson of the whole course, not just this lab: **the AI didn't get smarter between these two prompts — you got more specific.** Everything it produced the second time was implicit in the function all along; it just needed to be asked for by name.

---

## Step 7 — Compare, honestly

Fill in the checklist from the lab yourself, using the three files you now have. Here's how the run above actually breaks down, if you want a reference point:

| Test Case | Manual (5 tests) | Zero-shot AI (8 tests) | Improved AI (16 tests) |
|---|:---:|:---:|:---:|
| Premium / standard / guest discount | ✅ | ✅ | ✅ |
| SAVE10 applies | ✅ | ✅ | ✅ |
| SAVE20 applies to premium | — | ✅ | ✅ |
| **SAVE20 does *not* apply to standard/guest** | — | — | ✅ |
| Holiday discount | ✅ | ✅ | ✅ |
| Negative price raises `ValueError` | — | ✅ | ✅ |
| Zero price allowed | — | ✅ | ✅ |
| **Unknown customer type → guest** | — | — | ✅ |
| **Unknown coupon code ignored** | — | — | ✅ |
| **Case-insensitive customer type** | — | — | ✅ |
| **Rounding behavior verified** | — | — | ✅ |
| **Multiple discounts apply sequentially, not additively** | — | — | ✅ |

> **Why does this table matter more than the pass/fail counts?** Because "16 tests passed" and "5 tests passed" both *sound* like success. A green checkmark tells you your tests didn't find a bug — it says nothing about whether your tests were even capable of finding one. The bold rows above are the ones where a genuinely wrong implementation could slip through the manual and zero-shot suites without either one noticing. That's the real risk this lab is trying to make visible: not "did the tests pass," but "what could break without any of these tests catching it."

---

## Discussion questions (for your own notes, or the group)

1. Which cases did you think of manually that the table above didn't predict?
2. Did the zero-shot AI find anything you'd genuinely missed, or just formalize things you'd have gotten to eventually?
3. Look at the bold rows in the table — would you have caught that gap in a code review, without running mutation testing or coverage tools first?
4. Now that you've seen the improved prompt's output, would you trust it without reading every assertion first? What would make you check one twice?

---

## Key takeaway

AI is fast at generating breadth once you tell it what breadth you need. It is not naturally good at inferring which of your business rules are the ones with a trap in them — that's still a reading-comprehension task, and it's still yours. The manual pass isn't a step you do *instead of* using AI; it's what teaches you which questions to ask it.
