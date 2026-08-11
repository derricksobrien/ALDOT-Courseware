---
layout: default
title: "Lab 10 — Capstone"
parent: Labs
nav_order: 10
---

# Lab 10: Capstone End-to-End Modernization

## Module
Module 10 - Capstone End-to-End Modernization

## Tier
Optional or Stretch MVP Lab

## Goal
Execute a full modernization slice from planning through deployment verification.

## Prerequisites

- Core modules 1, 3, 4, 6, 7, and 8 completed
- Optional module artifacts from 2, 5, and 9 collected if available
- Team roles assigned
- If any optional module is unavailable, use the published artifacts from the remediated MVP labs.

## Azure Ubuntu VM Fallback Path

For this cohort, `vm-ubuntu-sdm-2026-aug10` can serve as the capstone runtime target when platform-specific deployment paths are blocked.

Use it to preserve end-to-end traceability:

- Build and package in CI (Lab 08)
- Deploy container to VM over SSH
- Run health verification and smoke checks
- Attach runtime evidence to capstone package

## Steps

1. Define acceptance criteria and sprint slice.
2. Gather the working artifacts from the remediated MVP labs.
3. Implement one small modernization change and track it end to end.
4. Build and test through CI pipeline.
5. Deploy to the target environment.
6. Validate operations and present outcomes.
7. Assemble the final capstone package and retrospective notes.

### VM fallback evidence add-on

Include:

- SSH command transcript (`labadmin` on `vm-ubuntu-sdm-2026-aug10`)
- `docker ps` output for running capstone container
- Health endpoint result and timestamp
- Short note describing why VM fallback was used

## Validation

- Acceptance criteria are met.
- Pipeline and deployment evidence are complete.
- The capstone package can be reproduced from the published MVP artifacts.

## Evidence

- Final demo notes
- Architecture and runbook artifacts
- Retrospective summary
- Packaged capstone checkpoint
- VM runtime proof (if fallback path used)
