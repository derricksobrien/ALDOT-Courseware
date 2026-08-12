---
layout: default
title: "MS Learn Resource Mapping"
parent: AI in Software Testing
nav_order: 9
---

# Microsoft Learn Resource Mapping — AI in Software Testing Course

**Purpose:** A complement to the 7 modules in the "AI in Software Testing" course (`sample_coursware/AI-In-Software-Testing-main/`). For each module, this maps to real Microsoft Learn content that goes deeper into the same topic — plus a starting point for students who are new to Python or new to AWS, since both are prerequisites this course assumes but doesn't teach.

**Created:** 2026-08-12
**All links verified live against learn.microsoft.com at time of writing.** Where Microsoft Learn's catalog doesn't have a close match for a topic (this happens twice below — mutation testing, and Faker-style fixture data), that gap is called out explicitly rather than papered over with a loosely-related link.

---

## How to Use This Table

1. Find the module you just completed (matches the Day 1 / Day 2 agenda in the course slides).
2. Pick a path or module from the right column.
3. Check the **Match** column first — "Direct" means the MS Learn content covers the same skill; "Adjacent" means it covers a closely related Microsoft-ecosystem version of the same idea, useful for context but not a substitute for the lab itself.

---

## Module-to-MS-Learn Mapping

### Module 1 — Foundations of AI in Testing

| MS Learn Content | Match | Level |
|---|---|---|
| [Introduction to generative AI and agents](https://learn.microsoft.com/en-us/training/modules/fundamentals-generative-ai/) | Direct | Beginner |
| [Introduction to prompt engineering with GitHub Copilot](https://learn.microsoft.com/en-us/training/modules/introduction-prompt-engineering-with-github-copilot/) | Direct | Beginner |
| [GitHub Copilot Fundamentals Part 1 of 2](https://learn.microsoft.com/en-us/training/paths/copilot/) | Direct | Beginner |

The prompt-engineering module is the closest match in the whole table — it covers zero-shot vs. few-shot style prompting and how an LLM processes a prompt, which is exactly what Module 1's "How an LLM Processes a Prompt" and "Zero-Shot vs Few-Shot" slides cover.

### Module 2 — AI-Driven Test Case Generation

| MS Learn Content | Match | Level |
|---|---|---|
| [Develop unit tests using GitHub Copilot tools](https://learn.microsoft.com/en-us/training/modules/develop-unit-tests-using-github-copilot-tools/) | Direct | Intermediate |
| [Get Started with AI-Assisted Development](https://learn.microsoft.com/en-us/training/paths/accelerate-app-development-using-github-copilot/) | Direct | Beginner |

"Develop unit tests using GitHub Copilot tools" is a one-to-one match for Lab 1.1 — it walks through the Generate Tests smart action and Copilot Chat's Ask/Edit/Agent modes specifically for writing unit tests, in VS Code.

### Module 3 — Coverage, Mutation Testing, and Refactoring

| MS Learn Content | Match | Level |
|---|---|---|
| [Use code coverage for unit testing (.NET docs)](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-code-coverage) | Direct (concept), different language | Reference |
| [Refactor large functions using GitHub Copilot Agent](https://learn.microsoft.com/en-us/training/modules/refactor-large-functions-github-copilot/) | Direct | Intermediate |
| [Consolidate duplicate logic using GitHub Copilot Agent](https://learn.microsoft.com/en-us/training/modules/consolidate-duplicate-logic-github-copilot-agent/) | Direct | Intermediate |

**Honest gap:** Microsoft Learn has no module on mutation testing — it's a Python-testing-tool-specific concept (`mutmut`, `mutpy`) with little overlap in Microsoft's own catalog, which is .NET/Azure-centric. The coverage concept transfers (line vs. branch coverage means the same thing in `dotnet-coverage` as it does in `pytest-cov`), but for mutation testing specifically, the better reference is [mutmut's own documentation](https://mutmut.readthedocs.io/) rather than anything on Microsoft Learn.

### Module 4 — Exploratory and Edge Case Testing

| MS Learn Content | Match | Level |
|---|---|---|
| [Develop unit tests using GitHub Copilot tools](https://learn.microsoft.com/en-us/training/modules/develop-unit-tests-using-github-copilot-tools/) | Direct (edge-case focus) | Intermediate |
| [Architecture strategies for security testing](https://learn.microsoft.com/en-us/azure/well-architected/security/test) | Adjacent | Advanced |
| [Implement platform protection (AZ-500)](https://learn.microsoft.com/en-us/training/paths/implement-platform-protection/) | Adjacent | Advanced |

The security-testing content here is framed at the enterprise-architecture level (Azure Well-Architected Framework), not "here's how to send a SQL injection payload to a Flask endpoint" — useful for understanding *why* the lab's SQL injection and XSS checks matter in production, less useful as a step-by-step guide.

### Module 5 — Synthetic Test Data Generation

| MS Learn Content | Match | Level |
|---|---|---|
| [Describe concepts of relational data](https://learn.microsoft.com/en-us/training/modules/describe-concepts-of-relational-data/) | Adjacent (schema concepts) | Beginner |
| [Run evaluations and generate synthetic datasets](https://learn.microsoft.com/en-us/training/modules/run-evaluations-generate-synthetic-datasets/) | Adjacent (different kind of "synthetic") | Intermediate |

**Honest gap:** this is the weakest match in the table. "Synthetic data" on Microsoft Learn almost always means synthetic *evaluation* data for testing an LLM's responses (via the Azure AI Evaluation SDK) — a different problem than seeding a SQLite database with realistic fake customers via Faker, which is what Lab 2.2 actually does. The relational-data module at least covers the schema concepts (primary/foreign keys, table relationships) that the lab's customer/product/order schema relies on. For the actual data-generation technique, [Faker's own documentation](https://faker.readthedocs.io/) is the better primary reference.

### Module 6 — AI in CI/CD Pipelines

| MS Learn Content | Match | Level |
|---|---|---|
| [Automate your workflow with GitHub Actions](https://learn.microsoft.com/en-us/training/paths/automate-workflow-github-actions/) | Direct | Beginner |
| [Learn continuous integration with GitHub Actions](https://learn.microsoft.com/en-us/training/modules/learn-continuous-integration-github-actions/) | Direct | Beginner |

Both are strong, direct matches — the course's own Lab 2.3 workflow (lint → test → coverage gate) is a smaller version of exactly what these paths teach.

### Module 7 — Test-Driven Development with AI

| MS Learn Content | Match | Level |
|---|---|---|
| [Perform code maintenance tasks using GitHub Copilot Agent](https://learn.microsoft.com/en-us/training/paths/perform-code-maintenance-tasks-github-copilot-agent/) | Direct | Intermediate |
| [Test-driven development (Visual Studio docs)](https://learn.microsoft.com/en-us/visualstudio/test/quick-start-test-driven-development-with-test-explorer?view=vs-2022) | Direct (concept), different IDE | Reference |

The "Perform code maintenance tasks" path is the best single match in this entire document. It's a 6-module path built specifically around using the GitHub Copilot coding agent, and one of its modules — [Resolve GitHub issues using GitHub Copilot Agent](https://learn.microsoft.com/en-us/training/modules/resolve-github-issues-github-copilot-agent/) — walks through the same real workflow as Lab 2.4: assign work to the agent via GitHub, review the PR it opens, confirm CI. If a student only follows up on one link in this whole document, this is the one worth pointing at Module 7.

---

## New to Python? Start Here

This course assumes comfort writing and running Python scripts. If that's not you yet:

| Resource | What it's for |
|---|---|
| [Get Started with Python Programming: Part 1 — Fundamentals](https://learn.microsoft.com/en-us/training/paths/get-started-with-python-fundamentals/) | Microsoft Learn's own beginner path — 4 modules, covers first program, variables/data, VS Code + Copilot setup, and conditionals. No prior experience assumed. |
| [Python for Beginners (video series)](https://learn.microsoft.com/en-us/shows/intro-to-python-development/) | Microsoft's free 44-part video series, good if you'd rather watch than read. |
| [Real Python — Python Basics](https://realpython.com/python-basics/) | A well-regarded, free, text-based alternative with exercises; goes further than the MS Learn path. |
| [Official Python.org — Getting Started](https://www.python.org/about/gettingstarted/) | The canonical starting point maintained by the Python Software Foundation itself — links to the official tutorial and IDE recommendations. |
| [learnpython.org](https://www.learnpython.org/) | Interactive, run-in-browser exercises — no local install needed if you just want to try syntax before setting up your machine. |

**Specific to this course:** every lab uses `pip install <package>` and `pytest`. If you finish the MS Learn path above and want one more thing before Lab 1.1, skim `pytest`'s own [Getting Started guide](https://docs.pytest.org/en/stable/getting-started.html) — the whole course assumes you can read a pytest terminal output (PASSED/FAILED, the `-v` flag) without translation.

---

## New to AWS? Start Here

Several labs reference AWS EC2 setup scripts (Lab 1.2's Amazon-Linux install script) and the credentials table format in this folder implies these labs were originally designed to run on AWS-provisioned VMs. If AWS is unfamiliar:

| Resource | What it's for |
|---|---|
| [AWS Skill Builder](https://skillbuilder.aws/) | AWS's own free training platform — 600+ free on-demand courses, no credit card required. |
| [AWS Cloud Practitioner Essentials](https://aws.amazon.com/training/learn-about/cloud-practitioner/) | A free, ~6-hour foundational course covering core AWS concepts, services, security, and pricing. The standard first stop for total beginners. |
| [AWS re/Start](https://aws.amazon.com/training/restart/) | A free, cohort-based program (400+ hours) for people with little or no tech background — covers Linux, Python, networking, and core AWS skills together. More of a commitment, but the most thorough zero-to-competent path AWS offers. |
| [AWS Educate](https://aws.amazon.com/education/awseducate/) | Free, self-paced cloud content for students specifically, including labs you can run without your own billing account. |

**Specific to this course:** you won't need to learn AWS deeply to complete these labs — the credentials in this folder are meant to connect to an already-provisioned instructor environment, not to teach AWS account setup from scratch. The Cloud Practitioner Essentials course is enough context to understand *what* an EC2 instance and IAM credentials are, which is as far as these labs actually go.

---

*All URLs verified against learn.microsoft.com, skillbuilder.aws, and aws.amazon.com as of 2026-08-12. Microsoft Learn paths are restructured periodically — if a link breaks, search the title directly on [learn.microsoft.com](https://learn.microsoft.com/training/).*
