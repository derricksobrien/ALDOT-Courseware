# Updated Course Outline - MVP Release

This outline is the lean, delivery-ready version of the modernization course. It keeps the course story intact while focusing on the modules we can support reliably with the repos and assets already available.

## Course Shape

- Format: 2 days
- Audience: Developers, team leads, DevOps engineers, and architects
- Core stack: C#/.NET, GitHub Copilot, Docker or Podman, Kubernetes/OpenShift, GitHub Actions
- Primary reference app: `eShopOnWeb`
- Secondary reference assets: `eShop`, `samples`, `s2i-dotnetcore-ex`

## Day 1 - Modernization Foundations and AI-Assisted Coding

### Module 1 - Software Modernization Overview

Status: Core

Courseware focus:

- Why modernization matters
- Rehost, refactor, rearchitect, rebuild
- How the reference app anchors the course

Lab outcome:

- Learner identifies modernization candidates and classifies them by strategy

Validation:

- Candidate matrix completed and checked by the instructor

### Module 2 - Azure DevOps Work Tracking

Status: Optional

Courseware focus:

- ADO concepts, work item hierarchy, and sprint flow

MVP treatment:

- Teach as instructor-led planning content or a guided demo
- Move hands-on board setup to phase 2 unless ADO is already provisioned

### Module 3 - GitHub Copilot Assisted C# Development

Status: Core

Courseware focus:

- Prompting patterns
- Refactoring legacy code
- Generating tests and documentation
- Governance and safe usage

Lab outcome:

- Learner refactors a controlled target and adds tests with Copilot assistance

Validation:

- Refactor compiles, tests pass, and the learner can explain the change

### Module 4 - C# and .NET in the Modern Stack

Status: Core

Courseware focus:

- Minimal APIs, dependency injection, config, async, and data access

Lab outcome:

- Learner adds a SQL-backed REST endpoint to the reference app

Validation:

- Endpoint returns expected responses and integration tests pass

## Day 2 - Containerization, Orchestration, and Delivery Automation

### Module 5 - Test Automation with Tosca

Status: Optional

Courseware focus:

- Model-based testing, execution lists, and CI integration

MVP treatment:

- Keep as phase 2 or instructor demo if Tosca access is not ready

### Module 6 - Containerization with Docker

Status: Core

Courseware focus:

- Multi-stage builds, image management, and local orchestration

Lab outcome:

- Learner containerizes the app and runs it locally with health checks

Validation:

- Image builds and starts cleanly, locally and in the pipeline

### Module 7 - Kubernetes and OpenShift

Status: Core

Courseware focus:

- Kubernetes primitives, OpenShift specifics, routes, probes, and scaling

Lab outcome:

- Learner deploys the container to OpenShift or the selected Kubernetes fallback

Validation:

- Route or ingress is reachable and the workload is healthy

### Module 8 - CI/CD with GitHub Actions

Status: Core

Courseware focus:

- Workflow structure, test gates, container publish, and deployment automation

Lab outcome:

- Learner creates a working build-test-deploy pipeline

Validation:

- Push triggers a successful workflow and failed tests block delivery

### Module 9 - Azure Cloud Deployment and Operations

Status: Optional

Courseware focus:

- Azure hosting options, identity, observability, Bicep, and costs

MVP treatment:

- Keep as an advanced path if quotas and access are available

### Module 10 - Capstone End-to-End Modernization

Status: Stretch

Courseware focus:

- Combine the full toolchain into a team delivery flow

MVP treatment:

- Defer to release 2 after the core six modules are stable

## MVP Deliverables

For the first release, publish:

- `Day 1` PDF courseware
- `Day 2` PDF courseware
- Lab markdown for modules 1, 3, 4, 6, 7, and 8
- Validation checklist for each core lab
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

1. Release the six core modules first.
2. Add ADO and Tosca as optional instructor tracks.
3. Add Azure deployment and capstone after the core track passes e2e validation.