# Lab 01: Modernization Discovery

## Module Alignment
Module 1: Software Modernization Overview

## Timebox
60 minutes

## Objectives
- Inspect a legacy .NET application baseline.
- Identify modernization candidates using rehost, refactor, rearchitect, rebuild strategies.
- Create an initial modernization backlog draft.

## Prerequisites
- Git installed.
- .NET SDK installed.
- Access to `course/repos/eShopOnWeb`.
- If LocalDB is unavailable, be prepared to run the app with `UseOnlyInMemoryDatabase=true` for a local fallback.

## Step-by-Step
1. Open the repository in VS Code.
2. Build and run the solution locally. If SQL Server LocalDB is not installed, start the app with `UseOnlyInMemoryDatabase=true` so the app uses its in-memory store instead.
3. Document current architecture boundaries (UI, API, data, background jobs).
4. Identify at least 8 modernization opportunities.
5. Classify each item as rehost, refactor, rearchitect, or rebuild.
6. Prioritize by business impact and engineering effort.

## Validation Checks
- The app runs successfully locally, either with LocalDB or the in-memory fallback.
- A modernization candidate table is completed with strategy and priority.

## Deliverables
- `modernization-candidate-matrix.md`
- `initial-modernization-roadmap.md`

## Stretch Goals
- Add technical debt scoring (1-5) and risk scoring (1-5) for each item.
