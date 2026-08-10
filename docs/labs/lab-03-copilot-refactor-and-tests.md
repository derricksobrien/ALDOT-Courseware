---
layout: default
title: "Lab 03 — Copilot Refactor and Tests"
parent: Labs
nav_order: 3
---

# Lab 03: Copilot Refactor and Tests

## Module
Module 03 - Copilot Assisted C# Development

## Tier
Core MVP Lab

## Goal
Refactor one legacy component and generate useful tests with Copilot.

## Prerequisites

- Repository available: `course/repos/eShopOnWeb`
- Copilot enabled in IDE
- .NET SDK installed

## Instructor Demo: GitHub Copilot Upgrade Agent (5â€“10 min intro)
Before students start their own refactor, the instructor runs a short live demo of the GitHub Copilot upgrade agent against `eShopOnWeb` â€” this is the "GitHub Copilot Upgrade Agent / Extension" named in `course/design.md` for Module 1, shown here as the bridge into hands-on Copilot work.

- Install if needed: VS Code Extensions view â†’ search **"GitHub Copilot upgrade"** â†’ Install.
- In Copilot Chat: `@upgrade Upgrade my solution to .NET 9`, choose **Guided** mode.
- Walk through the generated `.github/upgrades/{scenarioId}/assessment.md` and `plan.md` live â€” a real, automated version of the candidate-finding work from Lab 01.
- Stop after the Planning stage; don't run Execution during the demo.

**Optional for students:** only if a GitHub Copilot for Business seat is confirmed active for them (see the Day-1 checklist in `assess-labs/copilot-for-business-deployment-plan-2026-08-09_1427.md`). Students with an active seat may repeat the same steps themselves, then compare the agent's assessment against their own read of the code before moving into the manual refactor below.

## Steps

1. Select one target class with known complexity issues.
2. Prompt Copilot for a refactor plan.
3. Apply the refactor incrementally.
4. Generate unit tests for happy-path and failure-path behavior.
5. Run `dotnet test --collect:"XPlat Code Coverage" --results-directory ./TestResults` and review the generated coverage report.
6. Review generated code for quality and security.

## Validation

- Project compiles after refactor.
- Tests pass for changed behavior.

## Evidence

- Refactor commit
- Test run output
- Prompt and review notes

