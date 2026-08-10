---
layout: default
title: "Lab Resource Matrix"
parent: Resources
nav_order: 1
---

# Lab Resource Matrix

This matrix maps the validated MVP labs to the finalized course outline and the files that support them.

| Lab | Module | Delivery Tier | Repositories | Tools | Cloud/External Dependencies | Required Artifacts |
|---|---|---|---|---|---|---|
| Lab 01 | Module 01 - Software Modernization Overview | Core MVP | `course/repos/eShopOnWeb` | Git, VS Code, .NET SDK | None | Modernization candidate matrix, roadmap draft |
| Lab 02 | Module 02 - Azure DevOps Work Tracking | Supporting | `course/repos/eShopOnWeb` (context) | Browser | Azure DevOps org/project access | Board screenshots, query exports |
| Lab 03 | Module 03 - Copilot Assisted C# Development | Core MVP | `course/repos/eShopOnWeb` | VS Code or Visual Studio, .NET SDK, GitHub Copilot | Copilot license and sign-in | Refactor commit, tests, prompt log |
| Lab 04 | Module 04 - Modern .NET API and Data Access | Core MVP | `course/repos/eShopOnWeb` | .NET SDK, SQL tooling | Optional Azure SQL, otherwise local SQL | API endpoint changes, integration test evidence |
| Lab 05 | Module 05 - Test Automation with Tosca | Supporting | App from Lab 04 | Tosca, browser | Tosca license/server access from `tosca-secrets.md`, ADO/GitHub integration | Tosca execution report, quality gate checklist |
| Lab 06 | Module 06 - Containerization with Docker | Core MVP | `course/repos/eShopOnWeb` | Docker or Podman, .NET SDK | Optional ACR | Dockerfile updates, local run log, image tags |
| Lab 07 | Module 07 - Kubernetes and OpenShift | Core MVP | `course/repos/s2i-dotnetcore-ex`, `course/repos/eShopOnWeb` image | kubectl or oc, container runtime | OpenShift cluster or AKS fallback | Route URL, pod health output, HPA status |
| Lab 08 | Module 08 - CI/CD with GitHub Actions | Core MVP | Forked GitHub repo containing app code | Git, GitHub Actions | GitHub secrets, branch protection, registry or deployment target creds | Workflow file, successful run logs, failed gate evidence |
| Lab 09 | Module 09 - Azure Deployment and Operations | Supporting / advanced | `course/repos/samples` and app repo | Azure CLI, Bicep | Azure subscription, quota, monitor services, RBAC for role assignments | Bicep parameter file, dashboard/alert screenshots, alert policy proof |
| Lab 10 | Module 10 - Capstone End-to-End Modernization | Supporting / capstone | Combined from prior labs | All relevant tools | ADO, GitHub, cluster, cloud services, published MVP artifacts | End-to-end demo evidence, retrospective, packaged checkpoint |

## File Mapping

- Lab guides: `labs/`
- Courseware modules: `modules/`
- Validation scripts: `tests/`
- Student workspace helpers: `tools/`

## Cross-Lab Shared Requirements

- Stable baseline branch for each repo used in class
- Instructor recovery path and reset instructions per lab
- Access validation completed before class day
- Time-boxed smoke test run before learner delivery

