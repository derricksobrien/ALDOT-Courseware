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
Deliver a high-energy, team-based capstone that proves one full modernization slice from planning through operations, then presents it in a final demo showdown.

## Competition kit

Use the published capstone competition resources when you want to run Lab 10 as a scored Red Team vs Blue Team event:

- `docs/resources/lab-10-capstone-competition-kit.md`
- `docs/resources/lab-10-capstone-scoreboard.html`
- `docs/resources/lab-10-capstone-scorecard-template.json`
- `docs/resources/lab-10-capstone-sample-data.json`

These resources give both teams the same starter expectations, the same sample data, and the same transparent scoring rules.

## Prerequisites

- Core modules 1, 3, 4, 6, 7, and 8 completed
- Optional module artifacts from 2, 5, and 9 collected if available
- Team roles assigned
- If any optional module is unavailable, use the published artifacts from the remediated MVP labs.

## Capstone Challenge Format (Suggested: 90-120 minutes)

This final lab runs as a timed challenge with a public scorecard and final demo.

### Team roles (3-5 learners per team)

- Delivery Lead: owns scope and acceptance criteria
- Build Engineer: owns CI pipeline evidence
- Platform Engineer: owns deployment/runtime verification
- Ops Analyst: owns monitoring, alerts, and SLO checks
- Storyteller (optional): owns final demo flow and artifacts

### Mission objective

Ship one thin vertical slice that is:

- Traceable (plan -> code -> pipeline -> deploy -> operate)
- Reliable (quality gates + health checks)
- Explainable (clear tradeoffs, not just screenshots)

---

## Round-Based Execution

### Round 1 - Mission Brief (15 min)

1. Define one realistic change request for your app.
2. Write 3-5 acceptance criteria.
3. Create ownership tasks in your board/tooling.

**Round output:** scope statement + acceptance criteria + owner map.

### Round 2 - Build and Gate (20 min)

1. Implement the smallest code/config change that satisfies the mission.
2. Run CI with required checks.
3. Capture one successful run and one blocked/failing gate scenario.

**Round output:** commit SHA + two run links + gate explanation.

### Round 3 - Deploy and Operate (25 min)

1. Deploy to your target runtime.
2. Verify app health and runtime behavior.
3. Capture telemetry/ops evidence and one risk callout.

**Round output:** deploy proof + health proof + operations proof.

### Round 4 - Demo Showdown (20-30 min)

Each team gets 5 minutes:

1. What changed and why
2. How quality was enforced
3. How runtime behavior was validated
4. One lesson learned and one next improvement

**Round output:** final capstone package + live walkthrough.

## Azure Ubuntu VM Fallback Path

For this cohort, `vm-ubuntu-sdm-2026-aug10` can serve as the capstone runtime target when platform-specific deployment paths are blocked.

Use it to preserve end-to-end traceability:

- Build and package in CI (Lab 08)
- Deploy container to VM over SSH
- Run health verification and smoke checks
- Attach runtime evidence to capstone package

## Steps (Technical Minimum)

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

## Scoring Rubric (Instructor)

| Dimension | Points | What earns full credit |
|---|---:|---|
| End-to-end traceability | 25 | Clear chain from requirement to runtime evidence |
| CI/CD quality gates | 25 | Correct required checks and meaningful pass/fail proof |
| Runtime reliability | 25 | Health, monitoring, and operational readiness demonstrated |
| Demo clarity | 15 | Crisp narrative, role handoffs, and evidence quality |
| Retrospective quality | 10 | Honest lessons learned with concrete next actions |

Total: 100 points

### Bonus missions (optional, +10 each)

- Chaos check: intentionally break one dependency and show recovery.
- Cost check: identify one optimization to reduce cloud/runtime cost.
- Security check: remove one secret from config via managed identity/secret store pattern.

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

## Why this finale works

This format turns Lab 10 into a live delivery simulation, not a documentation exercise.  
Students finish with momentum because they compete, collaborate, and tell a coherent modernization story under time pressure.
