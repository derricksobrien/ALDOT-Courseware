# Lab 08: CI/CD with GitHub Actions

## Module Alignment
Module 8: CI/CD Pipelines with GitHub Actions

## Timebox
90 minutes

## Objectives
- Build a complete CI/CD workflow for .NET and containers.
- Enforce quality gates with tests and approvals.
- Deploy to OpenShift, AKS, or App Service.

## Prerequisites
- GitHub repository with Actions enabled.
- Secrets configured for cloud login and registry.

## Step-by-Step
1. Create workflow trigger rules for pull requests and main branch.
2. Add build and test jobs (`dotnet restore`, `dotnet build`, `dotnet test`).
3. Add container build and push job (`docker/build-push-action`).
4. Add deployment job for target platform.
5. Add test automation stage and publish results.
6. Add branch protection and required checks.
7. Add failure notifications and rollback procedure.

## Validation Checks
- Workflow runs end-to-end on a commit.
- Failed tests block deployment.
- Deployment artifacts and logs are traceable.

## Deliverables
- `.github/workflows/modernization-pipeline.yml`
- Pipeline execution logs.
- Branch policy configuration evidence.

## Stretch Goals
- Add canary or blue/green deployment pattern.
