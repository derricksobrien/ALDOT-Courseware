# MVP Lab Automation and Assessment Plan

## Objective

Make the MVP labs easier for students to start and easier for instructors to assess by providing:

1. starter scripts that initialize a consistent lab workspace for each lab
2. assessment scripts that validate lab completion and generate a structured report
3. optional AI-assisted evaluation for richer feedback when credentials are available

## Scope

This plan applies to the labs in the MVP-delivery course package and is intended to support the full learning flow:

- prepare the student workspace for a lab
- guide the student through the expected starting point
- validate the completed work against the existing lab checks
- generate a report that can be reviewed by an instructor or used as submission evidence

## Proposed Scripts

### 1. Startup script

File: `tools/Initialize-Lab.ps1`

Responsibilities:
- accept a lab number such as `01` through `10`
- create a workspace under `student-work/lab-XX`
- create starter files such as `README.md`, `lab-notes.md`, and `lab-state.json`
- record the lab guide and module references for that workspace

### 2. Assessment script

File: `tools/Invoke-LabAssessment.ps1`

Responsibilities:
- accept a lab number and optionally a student workspace path
- run the matching validation script in `tests/`
- write a markdown assessment report
- write a JSON summary file
- optionally call an AI model for qualitative evaluation

## Assessment Flow

1. The student starts a lab with `Initialize-Lab.ps1`.
2. The student completes the work in the generated workspace.
3. The instructor or student runs `Invoke-LabAssessment.ps1`.
4. The script produces:
   - `assessment-report.md`
   - `assessment-summary.json`
5. If AI credentials are configured, the report includes an AI-generated summary and next-step recommendations.

## AI Evaluation Options

### Option A: OpenAI API
Use when a simple API-based integration is preferred.

Required environment variable:
- `OPENAI_API_KEY`

### Option B: Azure OpenAI
Use when the course is hosted in a Microsoft or enterprise environment.

Required environment variables:
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_DEPLOYMENT`

### Option C: GitHub Models / Azure AI Foundry
Use when the organization already has access to managed model endpoints.

This option can be added later if the course needs a more enterprise-ready deployment model.

## Recommended Rollout

### Phase 1
- ship the startup and assessment scripts for all labs
- use the existing PowerShell test scripts as the deterministic validation layer

### Phase 2
- add richer rubrics and scoring for each lab
- include stronger artifact checks such as screenshots, URLs, and evidence files

### Phase 3
- connect the assessment output to an LMS or instructor dashboard
- support batch grading for classes or workshops

## Expected Benefits

- students get a consistent starting point for every lab
- instructors can grade more consistently with structured evidence
- assessment output is easy to review and archive
- AI can help highlight gaps and provide formative feedback without replacing the deterministic checks

## Notes

The deterministic validation scripts remain the primary source of truth. AI is intended to supplement that by providing explanation and coaching, not by replacing the actual evidence-based checks.
