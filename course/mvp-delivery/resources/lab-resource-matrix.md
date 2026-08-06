# Lab Resource Matrix

| Lab | Module | Delivery Tier | Repositories | Tools | Cloud/External Dependencies | Required Artifacts |
|---|---|---|---|---|---|---|
| Lab 01 | Module 1 Modernization Overview | Core | `course/repos/eShopOnWeb` | Git, VS Code, .NET SDK | None | Modernization candidate matrix, roadmap draft |
| Lab 02 | Module 2 ADO Work Tracking | Optional | `course/repos/eShopOnWeb` (context) | Browser | Azure DevOps org/project access | Board screenshots, query exports |
| Lab 03 | Module 3 Copilot Assisted C# | Core | `course/repos/eShopOnWeb`, `course/repos/samples` | VS Code or Visual Studio, .NET SDK, GitHub Copilot | Copilot license and sign-in | Refactor commit, tests, prompt log |
| Lab 04 | Module 4 Modern .NET API | Core | `course/repos/eShopOnWeb`, `course/repos/samples` | .NET SDK, SQL tooling | Optional Azure SQL, otherwise local SQL | API endpoint changes, integration test evidence |
| Lab 05 | Module 5 Tosca Automation | Optional | App from Lab 04 | Tosca, browser | Tosca license/server access, ADO/GitHub integration | Tosca execution report, quality gate checklist |
| Lab 06 | Module 6 Containerization | Core | `course/repos/eShopOnWeb` | Docker or Podman, .NET SDK | Optional ACR | Dockerfile updates, local run log, image tags |
| Lab 07 | Module 7 Kubernetes/OpenShift | Core | `course/repos/s2i-dotnetcore-ex`, `course/repos/eShopOnWeb` image | kubectl or oc, container runtime | OpenShift cluster or AKS fallback | Route URL, pod health output, HPA status |
| Lab 08 | Module 8 GitHub Actions CI/CD | Core | GitHub repo containing app code | Git, GitHub Actions | GitHub secrets, registry or deployment target creds | Workflow file, successful run logs |
| Lab 09 | Module 9 Azure Deployment/Ops | Optional | `course/repos/samples` and app repo | Azure CLI, Bicep | Azure subscription, quota, monitor services | Deployment output, dashboard/alert screenshots |
| Lab 10 | Module 10 Capstone | Optional/Stretch | Combined from prior labs | All relevant tools | ADO, GitHub, cluster, cloud services | End-to-end demo evidence, retrospective |

## Cross-Lab Shared Requirements

- Stable baseline branch for each repo used in class
- Instructor recovery path and reset instructions per lab
- Access validation completed before class day
- Time-boxed smoke test run before learner delivery
