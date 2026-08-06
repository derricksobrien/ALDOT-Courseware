# Implementation and Test Plan for All Labs

## Purpose
Provide a repeatable, low-risk rollout plan for building and validating each module lab, including test strategy, evidence, and fallback paths.

## Delivery Strategy
- Use one branch per module: `lab/module-01` through `lab/module-10`.
- Use tagged checkpoints after each lab: `v-lab01`, `v-lab02`, and so on.
- Keep a baseline branch with known-good infrastructure manifests and pipeline templates.

## Global Test Layers
1. Unit tests: Required for all changed business logic.
2. Integration tests: Required for API and database interactions.
3. Container tests: Image build, startup, health endpoint.
4. Platform tests: Kubernetes/OpenShift deployment health and autoscaling checks.
5. Pipeline tests: CI gates, artifact publishing, deployment stage checks.
6. Operations tests: telemetry, dashboards, alerts, and rollback validation.

## Module-by-Module Implementation and Testing

### Module 1 Lab Implementation and Test
- Implement:
  - Establish reference app baseline and architecture notes.
  - Build modernization candidate matrix.
- Test:
  - Verify app launches and baseline functional path is documented.
  - Peer review matrix for strategy correctness and priority consistency.
- Evidence:
  - Candidate matrix file and architecture notes.

### Module 2 Lab Implementation and Test
- Implement:
  - Build ADO hierarchy and sprint board.
  - Create dashboard queries and metrics widgets.
- Test:
  - Confirm linkage from work items to commits/PRs.
  - Validate query outputs and velocity metrics populate.
- Evidence:
  - Board snapshots and exported queries.

### Module 3 Lab Implementation and Test
- Implement:
  - Copilot-driven refactor of one legacy component.
  - Add and tune unit tests.
- Test:
  - Run `dotnet test` and coverage threshold checks.
  - Security review of generated code and dependencies.
- Evidence:
  - Test report, coverage output, prompt log.

### Module 4 Lab Implementation and Test
- Implement:
  - Add SQL-backed endpoint with DI and config updates.
  - Move secrets to secure configuration source.
- Test:
  - Integration tests against SQL.
  - Contract checks for status codes, schema, and error handling.
- Evidence:
  - Endpoint test run and secure config proof.

### Module 5 Lab Implementation and Test
- Implement:
  - Create Tosca UI/API suites and execution lists.
  - Integrate test publication to ADO or pipeline.
- Test:
  - Execute smoke and regression runs.
  - Verify gate criteria for pass rate and defect severity.
- Evidence:
  - Tosca execution report and gate policy doc.

### Module 6 Lab Implementation and Test
- Implement:
  - Add production-grade Dockerfile and compose stack.
  - Push image to ACR.
- Test:
  - Container startup and health checks.
  - Vulnerability scan and remediation triage.
- Evidence:
  - Build logs, ACR tag list, scan report.

### Module 7 Lab Implementation and Test
- Implement:
  - Apply deployment manifests and environment configs.
  - Add probes, autoscaling, and rollout strategy.
- Test:
  - Validate route/ingress availability and readiness.
  - Run load check to validate HPA behavior.
- Evidence:
  - Cluster object status and rollout history.

### Module 8 Lab Implementation and Test
- Implement:
  - Create end-to-end GitHub Actions workflow.
  - Add branch protection and quality gate steps.
- Test:
  - Run success path and controlled failure path.
  - Verify blocked deploy on failed tests.
- Evidence:
  - Workflow run URLs and policy screenshots.

### Module 9 Lab Implementation and Test
- Implement:
  - Deploy Azure resources via Bicep.
  - Configure monitoring, alerts, and dashboard.
- Test:
  - Validate app health, telemetry ingestion, and alert firing.
  - Validate identity access and secret retrieval.
- Evidence:
  - Bicep deployment output and monitoring artifacts.

### Module 10 Lab Implementation and Test
- Implement:
  - Execute full modernization flow as a team.
  - Deliver demo and roadmap outputs.
- Test:
  - Validate all acceptance criteria and operational checks.
  - Run final rollback rehearsal.
- Evidence:
  - Demo package, architecture artifacts, retrospective notes.

## Cloud and Infrastructure Enhancements
Use available local infrastructure examples to raise realism and speed:
- Reuse existing Docker Compose and Kubernetes base manifests from your local project catalog.
- Reuse existing Azure Bicep modules and GitHub workflow templates from Azure-focused repositories.
- Standardize environment variables and secrets naming across all labs.

## Risk Controls and Fallbacks
- If OpenShift sandbox is unavailable, use AKS with equivalent Kubernetes objectives.
- If Tosca licensing is limited, run core API automation in pipeline and keep Tosca as instructor-led demo track.
- If cloud quotas are constrained, run App Service or Container Apps instead of AKS for selected teams.

## Test Exit Criteria by Lab
- Functional correctness: required.
- Security baseline checks: required.
- Deployment validation: required where applicable.
- Observability validation: required for modules 7 to 10.
- Documentation completeness: required for every module.

## Suggested Automation Backlog
1. One-click lab environment bootstrap script.
2. Seed database script pack.
3. Common pipeline reusable workflow templates.
4. Automated environment cleanup job.
5. Artifact collection script for grading.
