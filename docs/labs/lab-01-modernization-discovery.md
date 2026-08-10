---
layout: default
title: "Lab 01 — Modernization Discovery"
parent: Labs
nav_order: 1
---

# Lab 01: Modernization Discovery

## Module
Module 01 - Software Modernization Overview

## Tier
Core MVP Lab

## Goal
Identify and prioritize modernization candidates in the baseline app.

## Prerequisites

- Repository available: `course/repos/eShopOnWeb`
- Tooling: Git, .NET SDK, VS Code
- If LocalDB is unavailable, use the in-memory fallback via `UseOnlyInMemoryDatabase=true`

## Steps

1. Open `eShopOnWeb` and run a local build; if SQL Server is unavailable, start with the in-memory fallback.
2. Identify major architecture boundaries and high-risk areas.
3. Record at least 8 modernization candidates.
4. Tag each item as rehost, refactor, rearchitect, or rebuild.
5. Prioritize by impact and implementation effort.

## Validation

- Baseline app builds successfully.
- Candidate matrix contains classification and priority.

## Evidence

- `modernization-candidate-matrix.md`
- `initial-modernization-roadmap.md`

