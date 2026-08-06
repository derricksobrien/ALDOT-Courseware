# Courseware Production Plan

This document turns the modernization curriculum into a repeatable production process for one PDF courseware file and one matching lab set per module.

## What the Sample Courseware Shows

The `sample_coursware/AI-In-Software-Testing-main` folder is the style guide for the output package. Its structure is consistent:

- A short course or day description
- One lab per topic, with a strong problem statement
- A fixed lab template with duration, audience, tools, goal, scenario, starter code, steps, prompts, and validation tables
- Enough detail to work independently, but not so much that the learner stops thinking
- A test-first, iterative tone that emphasizes execution and validation over theory dumps

### Sample Assets Inventory

PDF courseware in the sample folder:

- `sample_coursware/AI-In-Software-Testing-main/AI_in_Software_Testing_Day1.pdf`
- `sample_coursware/AI-In-Software-Testing-main/AI_Software_Testing_day2.pdf`

Markdown lab/source files in the sample folder:

- `sample_coursware/AI-In-Software-Testing-main/1.1-testing-manual-vs-ai.md`
- `sample_coursware/AI-In-Software-Testing-main/1.2-reverse-engineer-legacy-code.md`
- `sample_coursware/AI-In-Software-Testing-main/1.3-coverage-mutation-testing.md`
- `sample_coursware/AI-In-Software-Testing-main/2.1-exploratory-testing.md`
- `sample_coursware/AI-In-Software-Testing-main/2.2-synthetics.md`
- `sample_coursware/AI-In-Software-Testing-main/2.3-cicd-github-actions.md`
- `sample_coursware/AI-In-Software-Testing-main/2.4-tdd.md`

### Current Modernization Lab Inventory

The modernization course already has these lab markdown files:

- `course/labs/modules/lab-01-modernization-discovery.md`
- `course/labs/modules/lab-02-ado-work-tracking.md`
- `course/labs/modules/lab-03-copilot-refactor-and-tests.md`
- `course/labs/modules/lab-04-modern-dotnet-api-sql.md`
- `course/labs/modules/lab-05-test-automation-quality-gates.md`
- `course/labs/modules/lab-06-containerization-docker.md`
- `course/labs/modules/lab-07-kubernetes-openshift.md`
- `course/labs/modules/lab-08-cicd-github-actions.md`
- `course/labs/modules/lab-09-azure-deployment-operations.md`
- `course/labs/modules/lab-10-capstone-end-to-end.md`

## Recommended Look and Feel

Use the sample courseware as a pattern, but adapt the content depth to the modernization audience:

- Courseware PDFs should be narrative and visual, with module story, objectives, diagrams, and a clear delivery flow.
- Lab markdown should stay operational, with step-by-step actions, prompts, checkpoints, validation, and deliverables.
- Each PDF should end with the exact lab entrypoint and expected learner outcome.
- Each lab should include a short "what success looks like" section and a list of evidence to capture.

### Document Depth Target

- PDF courseware: medium depth, instructor-friendly, learner-readable, enough detail to guide execution but not duplicate every lab step.
- Lab markdown: high detail, hands-on, with explicit commands, screenshots or validation points, and troubleshooting notes.
- Capstone: highest detail for orchestration, dependencies, and end-to-end verification.

## Staged Production Plan

### Stage 0 - Baseline and Provisioning Readiness

Goal: make the environment predictable before authoring content.

- Confirm all reference repos and lab source repos are available.
- Confirm Azure, GitHub, ADO, OpenShift, and Tosca access.
- Confirm local runner tools: .NET, Docker/Podman, Python, SQL tooling, and browser validation.
- Confirm a clean naming convention for course assets.

Exit criteria:

- Every module has a known target repo, target environment, and target validation path.

### Stage 1 - Courseware Outline per Module

Goal: define the PDF narrative before expanding the lab steps.

- Write a one-page narrative for each module.
- Include learning outcomes, why the topic matters, and where it fits in the modernization lifecycle.
- Add a small architecture sketch or workflow diagram for each module.
- Map each module to the lab file that will operationalize it.

Exit criteria:

- Every module has an instructor outline and a learner-facing summary.

### Stage 2 - Lab Drafting

Goal: draft the lab markdown to match the courseware storyline.

- Use the same pattern across modules: duration, audience, tools, goal, scenario, starter code or starter repo, step-by-step tasks, prompts, validation, and deliverables.
- Keep the lab directions actionable and testable.
- Keep each lab focused on one primary outcome.

Exit criteria:

- Each module has a draft lab that can be followed without ambiguity.

### Stage 3 - End-to-End Validation

Goal: prove each lab works before release day.

- Run every lab end to end in a clean environment.
- Verify the lab starts from the stated prerequisites.
- Verify any referenced repo, artifact, template, or cloud resource is actually available.
- Capture the exact failure points and simplify the instructions where needed.

Exit criteria:

- Every lab executes cleanly in a fresh environment with no hidden setup.

### Stage 4 - PDF Production

Goal: turn the module narrative into polished courseware PDFs.

- Build the PDF from the module outline and approved visuals.
- Add callouts for prerequisites, architecture, and success criteria.
- Link directly to the matching lab markdown or lab page.

Exit criteria:

- Every module has a shareable PDF courseware file.

### Stage 5 - Packaging and Delivery

Goal: release the course with a consistent structure.

- Publish the PDFs and lab markdown together.
- Publish the site map and courseware navigation.
- Prepare an instructor runbook and a troubleshooting guide.

Exit criteria:

- Learners can navigate from the module overview to the matching lab and complete it without extra guidance.

## Module-by-Module Execution Plan

### Module 1 - Software Modernization Overview

Courseware focus:

- What modernization means
- Rehost, refactor, rearchitect, rebuild
- Why the reference app matters

Lab focus:

- Inspect the reference app and identify modernization candidates

Validation:

- Learner can identify at least 8 candidates and classify each by strategy

Provisioning gaps:

- Reference app clone must be verified
- Learners need a simple baseline runbook

### Module 2 - Azure DevOps Work Tracking

Courseware focus:

- ADO concepts, work item hierarchy, sprint flow, dashboards

Lab focus:

- Create and manage a sprint backlog for the modernization project

Validation:

- Board, queries, and links to commits/PRs are functioning

Provisioning gaps:

- ADO project/template must be pre-created or scripted
- Need consistent permission model and demo data source

### Module 3 - GitHub Copilot Assisted C# Development

Courseware focus:

- Prompting, refactoring, tests, XML docs, governance

Lab focus:

- Refactor a legacy module and generate tests

Validation:

- Copilot is enabled in the chosen IDE and the repo supports a safe refactor target

Provisioning gaps:

- Copilot licensing and IDE setup must be confirmed before class
- Need a known-good code target for all learners

### Module 4 - Modern .NET Stack

Courseware focus:

- Minimal APIs, DI, config, SQL access, Key Vault

Lab focus:

- Add a SQL-backed REST endpoint

Validation:

- API runs locally and against SQL with tests

Provisioning gaps:

- SQL Server/SQL Database and seed data must be ready
- Secret handling path must be pre-decided

### Module 5 - Test Automation with Tosca

Courseware focus:

- MBT, execution lists, API/UI automation, CI integration

Lab focus:

- Create and execute automated tests and publish results

Validation:

- Tosca projects can connect to the target app and publish results

Provisioning gaps:

- Tosca licenses, runner access, and extension availability
- Publish path to ADO or pipeline must be tested ahead of time

### Module 6 - Containerization with Docker

Courseware focus:

- Images, layers, multi-stage builds, ACR, security scanning

Lab focus:

- Containerize the app and push to ACR

Validation:

- Image builds locally and in CI, then runs with health checks

Provisioning gaps:

- Docker/Podman runtime selection must be standardized
- ACR permissions and naming must be pre-created

### Module 7 - Kubernetes and OpenShift

Courseware focus:

- K8s primitives, OpenShift specifics, probes, autoscaling, storage

Lab focus:

- Deploy the app and configure autoscaling

Validation:

- Route/ingress works and autoscaling responds under load

Provisioning gaps:

- OpenShift sandbox or AKS fallback must be provisioned
- Cluster credentials and namespace ownership must be ready

### Module 8 - GitHub Actions CI/CD

Courseware focus:

- Workflow structure, secrets, deployment strategies, quality gates

Lab focus:

- Build a complete CI/CD pipeline from code commit to deploy

Validation:

- Pipeline runs on push/PR and blocks failed quality checks

Provisioning gaps:

- GitHub repo permissions, secrets, and branch protection must be set
- Deployment target credentials must be stored safely

### Module 9 - Azure Deployment and Operations

Courseware focus:

- App Service, AKS, Container Apps, SQL, identity, observability, Bicep

Lab focus:

- Deploy the full stack to Azure with monitoring

Validation:

- Infrastructure, telemetry, and alerts all work end to end

Provisioning gaps:

- Azure subscription, quotas, and tagging standards
- Bicep templates and parameter files need a preflight check

### Module 10 - Capstone End-to-End Modernization

Courseware focus:

- Bring all modules together into a realistic team delivery flow

Lab focus:

- Execute the full modernization journey from backlog to monitored deployment

Validation:

- All prior module checks pass in one coherent scenario

Provisioning gaps:

- Team roles and scoring rubric need to be fixed before the capstone
- Environment recovery and rollback paths must be rehearsed

## Lab Provisioning Gap Checklist

These are the highest-risk gaps to close before delivery day:

1. Access and identity for Azure, GitHub, ADO, OpenShift, and Tosca.
2. A single reference app baseline that every learner can clone and run.
3. Known-good cloud quotas and cost controls.
4. Seed data and reset scripts for SQL and any stateful services.
5. Preconfigured ADO project and GitHub repo permissions.
6. A clear OpenShift or AKS fallback if the primary cluster is unavailable.
7. CI/CD secrets and branch protection rules already in place.
8. A smoke-test script for each lab to validate the environment before class.
9. An instructor recovery path for broken learner environments.
10. A final lab acceptance checklist that can be used as the go/no-go gate.

## Recommended Output Package Per Module

For each module, publish the following together:

- One PDF courseware file
- One matching lab markdown file
- Any starter repo or branch links
- Any required seed data or manifest files
- A short validation checklist

## Execution Order

Do the work in this order:

1. Stage 0 readiness and provisioning
2. Stage 1 courseware outline
3. Stage 2 lab drafting
4. Stage 3 e2e validation
5. Stage 4 PDF production
6. Stage 5 packaging and delivery

That keeps the content grounded in what can actually be delivered, and it reduces the risk of creating polished PDFs for labs that later fail in practice.