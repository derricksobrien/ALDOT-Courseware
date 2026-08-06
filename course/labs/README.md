# Software Development Modernization Lab Series

This folder contains a full 2-day, 10-module hands-on lab sequence aligned to the curriculum and the reference design materials.

## Lab Flow

1. [Lab 01 - Modernization Discovery](modules/lab-01-modernization-discovery.md)
2. [Lab 02 - Azure DevOps Work Tracking](modules/lab-02-ado-work-tracking.md)
3. [Lab 03 - GitHub Copilot Refactor and Unit Tests](modules/lab-03-copilot-refactor-and-tests.md)
4. [Lab 04 - Modern .NET API with SQL](modules/lab-04-modern-dotnet-api-sql.md)
5. [Lab 05 - Test Automation and Quality Gates](modules/lab-05-test-automation-quality-gates.md)
6. [Lab 06 - Containerization with Docker](modules/lab-06-containerization-docker.md)
7. [Lab 07 - Kubernetes and OpenShift Deployment](modules/lab-07-kubernetes-openshift.md)
8. [Lab 08 - CI/CD with GitHub Actions](modules/lab-08-cicd-github-actions.md)
9. [Lab 09 - Azure Deployment and Operations](modules/lab-09-azure-deployment-operations.md)
10. [Lab 10 - Capstone End-to-End Modernization](modules/lab-10-capstone-end-to-end.md)

## Local Baseline Repositories

Expected clone location: `course/repos`

- `dotnet-architecture/eShopOnWeb`
- `dotnet/eShop`
- `dotnet/samples`
- `redhat-developer/s2i-dotnetcore-ex` (OpenShift .NET sample)

Not all repositories listed in the original curriculum document are currently reachable by the same URL. Where that occurs, equivalent replacements are provided in the module labs.

## Recommended Infrastructure Reuse

Use existing examples in your local environment for accelerated setup:

- Kubernetes manifests and kustomize overlays from local projects
- Docker Compose examples from local projects
- Bicep templates and GitHub Actions workflow examples from existing Azure-focused repos

## Instructor Notes

- Each lab includes timebox, objectives, prerequisites, step-by-step tasks, validation checks, and expected deliverables.
- A full rollout and test strategy is in [implementation-and-test-plan.md](implementation-and-test-plan.md).
- Additional planning gaps and readiness checklist are in [what-you-might-be-missing.md](what-you-might-be-missing.md).
- Repository availability details are tracked in [repo-source-status.md](repo-source-status.md).
