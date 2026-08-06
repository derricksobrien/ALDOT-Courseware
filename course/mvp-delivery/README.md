# MVP Delivery Pack

This folder contains a complete module-by-module MVP course package:

- Courseware module files in `modules/`
- Matching lab guides in `labs/`
- Lab verification scripts in `tests/`
- Resource requirements matrix in `resources/`

## MVP Scope

Core delivery modules:

1. Module 1 - Modernization Overview
2. Module 3 - Copilot Assisted C# Development
3. Module 4 - Modern .NET API and Data Access
4. Module 6 - Containerization with Docker
5. Module 7 - Kubernetes and OpenShift
6. Module 8 - CI/CD with GitHub Actions

Optional or phase-2 modules are included for planning continuity:

- Module 2 (ADO), Module 5 (Tosca), Module 9 (Azure Ops), Module 10 (Capstone)

## How to Execute

1. Review one module in `modules/`.
2. Run the matching lab in `labs/`.
3. Execute the test script in `tests/` to validate prerequisites and expected artifacts.
4. Capture evidence listed in each lab file.

## Test Execution

Run all validation scripts:

```powershell
Set-Location e:\Code\ALDOT\course\mvp-delivery\tests
.\run-all-lab-checks.ps1
```

Or run one lab check script at a time (example):

```powershell
.\test-lab-04.ps1
```
