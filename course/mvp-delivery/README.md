# MVP Delivery Pack

This folder contains the validated MVP course package for the modernization labs. It aligns the courseware, labs, tests, and automation helpers to the finalized course outline and the tested lab sequence.

## Course Structure

The package is organized around the following learning path:

- Core MVP labs: Lab 01, Lab 03, Lab 04, Lab 06, Lab 07, Lab 08
- Supporting or optional labs: Lab 02, Lab 05, Lab 09, Lab 10

## Module and Lab Mapping

| Lab | Module | Status | Primary files |
|---|---|---|---|
| Lab 01 | Module 01 - Software Modernization Overview | Core | `labs/lab-01-modernization-discovery.md`, `modules/module-01-modernization-overview.md` |
| Lab 02 | Module 02 - Azure DevOps Work Tracking | Supporting | `labs/lab-02-ado-work-tracking.md`, `modules/module-02-ado-work-tracking.md` |
| Lab 03 | Module 03 - Copilot Assisted C# Development | Core | `labs/lab-03-copilot-refactor-and-tests.md`, `modules/module-03-copilot-csharp.md` |
| Lab 04 | Module 04 - Modern .NET API and Data Access | Core | `labs/lab-04-modern-dotnet-api-sql.md`, `modules/module-04-modern-dotnet-api.md` |
| Lab 05 | Module 05 - Test Automation with Tosca | Supporting | `labs/lab-05-test-automation-quality-gates.md`, `modules/module-05-test-automation-tosca.md` |
| Lab 06 | Module 06 - Containerization with Docker | Core | `labs/lab-06-containerization-docker.md`, `modules/module-06-containerization.md` |
| Lab 07 | Module 07 - Kubernetes and OpenShift | Core | `labs/lab-07-kubernetes-openshift.md`, `modules/module-07-kubernetes-openshift.md` |
| Lab 08 | Module 08 - CI/CD with GitHub Actions | Core | `labs/lab-08-cicd-github-actions.md`, `modules/module-08-cicd-github-actions.md` |
| Lab 09 | Module 09 - Azure Deployment and Operations | Supporting | `labs/lab-09-azure-deployment-operations.md`, `modules/module-09-azure-operations.md` |
| Lab 10 | Module 10 - Capstone End-to-End Modernization | Supporting / Capstone | `labs/lab-10-capstone-end-to-end.md`, `modules/module-10-capstone.md` |

## How to Use This Package

1. Review the matching module and lab guide for the topic you are teaching or learning.
2. Run the corresponding validation script in `tests/` to confirm prerequisites and expected artifacts.
3. Use the startup helper to create a consistent lab workspace before beginning.
4. Use the assessment helper after completing the lab to generate evidence and feedback.

## Test Execution

Run all validation scripts from the repository root:

```powershell
Set-Location .\course\mvp-delivery\tests
.\run-all-lab-checks.ps1
```

Or run one lab check script at a time:

```powershell
.\test-lab-04.ps1
```

## Module PDF Rendering

If you update the module markdown files and want refreshed PDFs, run:

```powershell
python .\tools\render_module_pdfs.py
```

This regenerates the PDF companion files for all modules in `modules/`.

## Student Startup and Assessment Helpers

Use the automation helpers in `tools/` to make the lab experience more consistent:

```powershell
# Create a student workspace for a lab
.\tools\Initialize-Lab.ps1 -LabNumber 04

# Evaluate the completed work and generate a report
.\tools\Invoke-LabAssessment.ps1 -LabNumber 04 -StudentPath .\student-work\lab-04
```

The assessment script runs the matching validation script, writes a markdown report, and can optionally use AI if you configure OpenAI or Azure OpenAI credentials.
