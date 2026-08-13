---
layout: default
title: AI in Software Testing
nav_order: 5
has_children: true
---

# AI in Software Testing

A separate reference course (`sample_coursware/` in the repo) used as a style guide during this program, and independently tested end-to-end as part of this courseware pack. Two days, seven modules, seven labs — using AI to generate tests, reverse-engineer legacy code, measure coverage and mutation strength, explore edge cases, generate synthetic data, wire up CI/CD, and drive TDD with a real GitHub Copilot coding agent.

Everything below was verified by actually running it — real Python/Java code executed, a real JDK+Maven toolchain installed via WSL, real GitHub Actions runs on public repositories, and a real GitHub Copilot coding agent invocation — not simulated or described secondhand.

---

## New to Testing?

If software testing isn't your main role — you came from development, product, design, or somewhere else entirely — start here before Lab 1.1. It's not Microsoft-specific; it's the standard vocabulary and concepts the testing field itself uses.

- [Testing Fundamentals for Newcomers](testing-fundamentals) — what testing actually is, the vocabulary the course assumes you know, the testing pyramid, test design basics, and free resources (ISTQB, Ministry of Testing, Martin Fowler, Guru99) to go deeper
- [Free GitHub Copilot Walkthrough](free-github-copilot-walkthrough) — never used GitHub or Copilot before? Start here to get a free GitHub account and Copilot Free running in VS Code before Lab 1.1, no credit card required

## Lab Walkthroughs

Click-for-click guides with real screenshots and a "why" explanation at every step — usable as a standalone resource even without access to a lab machine.

| Lab | Topic |
|---|---|
| [Lab 1.1](lab1.1-walkthrough) | Manual Testing vs. AI-Assisted Testing |
| [Lab 1.2](lab1.2-walkthrough) | Reverse Engineering Legacy Code with AI |
| [Lab 1.3](lab1.3-walkthrough) | Coverage Gap Analysis and Mutation Testing |
| [Lab 2.1](lab2.1-walkthrough) | AI-Assisted Exploratory and Edge Case Testing |
| [Lab 2.2](lab2.2-walkthrough) | AI-Generated Test Data |
| [Lab 2.3](lab2.3-walkthrough) | Automated Testing in a CI/CD Pipeline |
| [Lab 2.4](lab2.4-walkthrough) | TDD with a GitHub Copilot Agent |
- [GitHub and GitHub Actions Primer](github-actions-primer) — beginner vocabulary and first commands for the GitHub workflow in Lab 2.3

## Reference

- [MS Learn Resource Mapping](ms-learn-resources) — Microsoft Learn content mapped to each of the 7 course modules, plus starting points for students new to Python or new to AWS
- [E2E Test Report](e2e-test-report) — Full findings from testing all 7 labs, including defects found and fixed in the original lab text
- [Original Labs vs. Walkthroughs and C# Migration Plan](original-vs-walkthrough-csharp-migration) — machine-verified gaps, student trip hazards, and a C#/.NET with Visual Studio delivery path
- [Day 2 Instructor Note: Tool Transitions](day2-instructor-note-tool-transitions) — plain-language explanations, first examples, and fallback guidance for the new tools introduced in Labs 2.1 through 2.4
