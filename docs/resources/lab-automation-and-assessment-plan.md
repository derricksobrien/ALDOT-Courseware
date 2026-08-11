---
layout: default
title: "Lab Automation and Assessment Plan"
parent: Resources
nav_order: 3
---

# Lab Startup and Assessment Automation Plan

This plan introduces two script families for the MVP lab package:

1. Startup scripts that help students reach a consistent starting point for each lab.
2. Assessment scripts that validate the work after completion and optionally use AI to provide a qualitative evaluation.

## 1. Startup scripts

### Purpose

These scripts make it easy for a learner to begin a lab with the correct workspace structure, references, and checklist.

### Proposed script

- `tools/Initialize-Lab.ps1`

### What it should do

- Accept a lab number such as `01` through `10`
- Create a lab workspace folder under `student-work/lab-XX`
- Write a starter `README.md` with:
  - the lab title
  - links to the matching module and lab guide
  - the expected outcome
  - a simple checklist for the learner
- Create a `lab-notes.md` file for the learner to capture observations
- Write a small `lab-state.json` file so the assessment script can read the workspace context later

### Benefits

- Students always start from the same structure
- Instructors can easily reset or rehydrate a lab workspace
- The lab entry experience is consistent across all labs

## 2. Assessment scripts

### Purpose

These scripts evaluate whether the student completed the lab work and whether the expected evidence exists.

### Proposed script

- `tools/Invoke-LabAssessment.ps1`

### What it should do

- Accept a lab number and an optional student workspace path
- Run the matching validation script in `tests/`
- Capture pass/fail results and any error output
- Inventory the artifact files in the student workspace
- Generate a markdown report and a JSON summary
- Optionally call an AI model for a qualitative assessment of completeness, understanding, and risks

### Suggested evaluation flow

1. Student completes the lab
2. Student or instructor runs the assessment script
3. The script writes a report such as:
   - `student-work/lab-04/assessment-report.md`
   - `student-work/lab-04/assessment-summary.json`

## 3. AI-assisted evaluation

The assessment script can use an AI model when configured. This is helpful for:

- summarizing the student’s work in plain language
- assessing whether the learner understood the lab goals
- highlighting missing evidence or weak implementation choices
- recommending next steps

### Recommended AI options

- Azure OpenAI (recommended for enterprise or classroom scenarios)
- OpenAI API (simple for small deployments)
- GitHub Models or Azure AI Foundry for managed access

### Environment variables for AI enablement

- `OPENAI_API_KEY` for OpenAI-compatible endpoints
- `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY` for Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` for the deployment name

### AI evaluation behavior

If AI credentials are available, the assessment script sends:

- the lab title
- the validation result
- the artifact inventory
- a short prompt requesting a structured assessment

If credentials are not available, the script still produces a deterministic report based on the validation checks and marks the AI section as skipped.

## 4. Suggested student workflow

```powershell
# Start a lab
./tools/Initialize-Lab.ps1 -LabNumber 04

# Complete the lab work in the created workspace

# Assess the completed lab
./tools/Invoke-LabAssessment.ps1 -LabNumber 04 -StudentPath ./student-work/lab-04
```

## 5. Recommended rollout

- Phase 1: ship the bootstrap and validation scripts for all labs
- Phase 2: add richer AI-based scoring and rubric output
- Phase 3: connect the assessment output to a LMS or instructor dashboard

