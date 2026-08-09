# Final Course Outline - MVP Delivery

This version combines the structure of the original outline with the validated MVP lab sequence. It keeps the course narrative clear and delivery-ready while making the MVP labs the primary path for release.

## Course Shape

- Format: 2-day instructor-led course
- Audience: Developers, QA engineers, DevOps engineers, team leads, and architects
- Primary stack: C#/.NET, GitHub Copilot, Docker/Podman, Kubernetes/OpenShift, GitHub Actions, Azure
- Primary reference app: eShopOnWeb
- Supporting assets: eShop, samples, and related modernization references

## Course Purpose

This course teaches learners how to modernize a software delivery experience from planning through deployment. The storyline moves from discovery and AI-assisted implementation to containerization, automation, cloud deployment, and a final capstone deliverable.

## Course Goals

By the end of the course, learners should be able to:

1. Explain the modernization journey and identify candidate work for change.
2. Use GitHub Copilot responsibly to refactor code and generate tests.
3. Build and validate a modern .NET API backed by data access.
4. Containerize the application and verify it locally.
5. Deploy the workload to Kubernetes or OpenShift.
6. Create CI/CD workflows with quality gates and deployment evidence.
7. Produce a capstone package that demonstrates end-to-end modernization readiness.

## Day 1 - Modernization Foundations and AI-Assisted Delivery

### Module 1 - Software Modernization Overview
Status: Core

Lab: `labs/lab-01-modernization-discovery.md`
Module file: `modules/module-01-modernization-overview.md`

Courseware focus:
- Why modernization matters
- Rehost, refactor, rearchitect, and rebuild strategies
- How the reference app anchors the course

Lab outcome:
- Learner identifies modernization candidates and classifies them by strategy

Validation:
- Candidate matrix completed and reviewed by the instructor

### Module 2 - Azure DevOps Work Tracking
Status: Optional / supporting track

Lab: `labs/lab-02-ado-work-tracking.md`
Module file: `modules/module-02-ado-work-tracking.md`

Courseware focus:
- ADO concepts, work items, hierarchy, and sprint flow

MVP treatment:
- Use as instructor-led planning content or a guided demo when ADO access is available

### Module 3 - GitHub Copilot Assisted C# Development
Status: Core

Lab: `labs/lab-03-copilot-refactor-and-tests.md`
Module file: `modules/module-03-copilot-csharp.md`

Courseware focus:
- Prompting patterns for refactoring and implementation
- Generating tests and documentation with Copilot
- Governance and safe use of AI-assisted coding

Lab outcome:
- Learner refactors a controlled target and adds tests with Copilot assistance

Validation:
- Refactor compiles, tests pass, and the learner can explain the change

### Module 4 - Modern .NET API and Data Access
Status: Core

Lab: `labs/lab-04-modern-dotnet-api-sql.md`
Module file: `modules/module-04-modern-dotnet-api.md`

Courseware focus:
- Minimal APIs, dependency injection, configuration, async programming, and data access

Lab outcome:
- Learner adds a SQL-backed REST endpoint to the reference app

Validation:
- Endpoint returns expected responses and integration tests pass

## Day 2 - Automation, Containers, Cloud Delivery, and Capstone

### Module 5 - Test Automation with Tosca
Status: Optional / supporting track

Lab: `labs/lab-05-test-automation-quality-gates.md`
Module file: `modules/module-05-test-automation-tosca.md`

Courseware focus:
- Model-based testing, execution lists, and CI integration

MVP treatment:
- Keep as an instructor demo or phase-2 enrichment when Tosca access is not ready

### Module 6 - Containerization with Docker
Status: Core

Lab: `labs/lab-06-containerization-docker.md`
Module file: `modules/module-06-containerization.md`

Courseware focus:
- Multi-stage builds, image management, and local orchestration

Lab outcome:
- Learner containerizes the app and runs it locally with health checks

Validation:
- Image builds and starts cleanly, locally and in the pipeline

### Module 7 - Kubernetes and OpenShift
Status: Core

Lab: `labs/lab-07-kubernetes-openshift.md`
Module file: `modules/module-07-kubernetes-openshift.md`

Courseware focus:
- Kubernetes primitives, OpenShift specifics, routes, probes, and scaling

Lab outcome:
- Learner deploys the container to OpenShift or the selected Kubernetes fallback

Validation:
- Route or ingress is reachable and the workload is healthy

### Module 8 - CI/CD with GitHub Actions
Status: Core

Lab: `labs/lab-08-cicd-github-actions.md`
Module file: `modules/module-08-cicd-github-actions.md`

Courseware focus:
- Workflow structure, test gates, container publish, and deployment automation

Lab outcome:
- Learner creates a working build-test-deploy pipeline

Validation:
- Push triggers a successful workflow and failed tests block delivery

### Module 9 - Azure Deployment and Operations
Status: Optional / advanced track

Lab: `labs/lab-09-azure-deployment-operations.md`
Module file: `modules/module-09-azure-operations.md`

Courseware focus:
- Azure hosting options, identity, observability, Bicep, and cost awareness

MVP treatment:
- Keep as an advanced path when quotas and access are available

### Module 10 - Capstone End-to-End Modernization
Status: Stretch / synthesis track

Lab: `labs/lab-10-capstone-end-to-end.md`
Module file: `modules/module-10-capstone.md`

Courseware focus:
- Combining the full toolchain into a team delivery flow

MVP treatment:
- Use as a capstone checkpoint that packages the work completed across prior labs

## MVP Deliverables

For the first release, publish:

- Day 1 courseware in PDF format
- Day 2 courseware in PDF format
- Lab markdown for the core MVP labs
- Validation checklists for each core lab
- A sitemap page for navigation
- An instructor runbook with reset instructions

## Core MVP Learning Outcomes

By the end of the MVP, learners should be able to:

1. Explain the modernization path and identify candidate changes.
2. Use Copilot to refactor and test a C# module safely.
3. Add a modern .NET API endpoint backed by a data store.
4. Containerize the app and verify it locally.
5. Deploy the container to Kubernetes or OpenShift.
6. Automate build and test with GitHub Actions.

## Release Plan

1. Release the core modules first.
2. Add Azure DevOps and Tosca as optional instructor tracks.
3. Add Azure deployment and the capstone after the core track passes end-to-end validation.
