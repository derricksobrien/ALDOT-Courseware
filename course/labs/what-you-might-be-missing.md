# What You Might Be Missing

This is a practical gap check based on the curriculum and lab design.

## 1. Environment Readiness and Access Governance
- Identity setup timeline for all tools (Azure, ADO, GitHub, OpenShift, Tosca).
- Least-privilege role matrix for learners vs instructors.
- Day-0 access validation script or checklist.

## 2. Cost and Quota Controls
- Per-team budget ceiling and auto-shutdown policy.
- Naming and tagging convention for cost attribution.
- Quota pre-check for ACR, AKS/ARO, and Azure SQL.

## 3. Golden Path Starter Assets
- Prebuilt branch per lab to avoid time loss.
- Instructor recovery branches for failed learner states.
- Seed data scripts for consistent database behavior.

## 4. Security and Compliance Controls
- Secret scanning in pipelines.
- Dependency and container vulnerability scanning threshold.
- Required policy checks (CodeQL, branch protections, signed artifacts where possible).

## 5. Operational Excellence Criteria
- Explicit SLO targets for latency, error budget, and availability.
- Incident response runbook exercise (rollback, hotfix, communication).
- Observability acceptance checklist before capstone signoff.

## 6. Assessment and Scoring Model
- Rubric per module with points and minimum pass criteria.
- Team and individual scoring split.
- Artifact-based grading checklist.

## 7. Failure Injection and Resilience Practice
- A deliberate fault in each day to train recovery skills.
- Backup and restore checkpoints for app and database.
- Validation of autoscaling and rolling update behavior under load.

## 8. Accessibility and Inclusive Delivery
- Screen reader and color contrast checks for demo UI work.
- Captioned recordings and text alternatives for all critical demos.
- Multiple pace tracks (standard and advanced).

## 9. Operational Logistics
- Timekeeper plan and buffer per module.
- Instructor-to-learner support ratio.
- Defined escalation path for blocked labs.

## 10. Post-Course Continuation Plan
- 30/60/90 day modernization backlog template.
- Production adoption checklist.
- Internal community of practice and office hours schedule.
