# Lab 08: CI/CD with GitHub Actions — Visual Walkthrough

**Course:** Software Development Modernization  
**Module:** 08 — CI/CD with GitHub Actions  
**Pipeline path shown:** Forked repo workflow with build, test, container publish, and deployment guardrails  
**Screenshots taken:** 2026-08-10/11 across live course site, GitHub, and GitHub Docs  
**Audience:** Students using this as a step-by-step guide or instructor reference  
**Tier:** Core MVP Lab

---

> **How to use this document**  
> This walkthrough mirrors Labs 05–07: each screen maps to a concrete lab action, expected result, and modernization reason.

---

## Why This Lab Matters — App Modernization Context

By Lab 07 you can build and run modernized workloads. Lab 08 makes that repeatable and enforceable.

1. **Automation replaces manual release gates.** Every push is validated with the same steps.
2. **Quality gates become policy.** Failed tests block deployment automatically.
3. **Traceability improves audit readiness.** You can prove what commit deployed, when, and under which checks.

> **Key concept:** CI/CD is the control plane for modernization delivery. It links code changes to measurable quality and deploy outcomes.

---

## What You Will Build

| Artifact | What it is | Where it lives |
|---|---|---|
| Workflow YAML | Trigger + jobs + dependencies | `.github/workflows/*.yml` |
| Build/Test gate | Required checks before deploy | Workflow job graph |
| Container publish stage | Image build and registry push | GitHub Actions job |
| Deployment environment rules | Manual approvals/guardrails | GitHub Environments |
| Branch protection policy | Required status checks | Repo settings |
| Run evidence | Successful + blocked runs | Actions run URLs |

---

## Prerequisites

| Item | How to verify |
|---|---|
| Forked GitHub repository | Repo exists under your account |
| Actions enabled | Actions tab visible/runnable |
| Required secrets | Repository secrets configured |
| Prior lab code | App builds/tests locally |

---

## Part 1 — Confirm Lab 08 Scope

![Local course Lab 08 page showing goals, steps, validation, and evidence requirements](lab-08-screenshots/ss01-lab08-local-page.png)

**What you are looking at:**  
The prescriptive Lab 08 checklist: triggers, jobs, quality gates, deploy controls, and branch protection.

---

## Part 2 — Start from a Fork Target

![Public GitHub repository view used as a fork target for student pipelines](lab-08-screenshots/ss02-github-repo-fork-target.png)

**What you are looking at:**  
A public repository layout suitable for forking and using as a workflow target.

**Why this matters:**  
Students should run CI/CD in their own fork to avoid cross-team collisions while preserving a real pull-request workflow.

---

## Part 3 — Define Workflow Triggers and Job Graph

![Workflow YAML file example in GitHub showing actions, triggers, and job definitions](lab-08-screenshots/ss03-workflow-yaml-example.png)

**What you are looking at:**  
A workflow file pattern with triggers and multi-job structure.

**Core structure to include:**

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build-test:
  container-publish:
    needs: build-test
  deploy:
    needs: container-publish
```

---

## Part 4 — Validate Runs and Gate Behavior

![GitHub Actions workflow runs list with pass/fail state indicators](lab-08-screenshots/ss04-github-actions-runs.png)

**What you are looking at:**  
The run history where you confirm successful and failed runs.

**Evidence to capture:**
- One successful end-to-end run URL
- One failed run URL where tests or checks blocked progression

---

## Part 5 — Build and Test .NET in CI

![GitHub Docs page for building and testing .NET in Actions](lab-08-screenshots/ss05-build-test-dotnet-docs.png)

**What you are looking at:**  
GitHub’s official pattern for restore/build/test on .NET.

**Typical step set:**

```yaml
- uses: actions/checkout@v4
- uses: actions/setup-dotnet@v4
  with:
    dotnet-version: '8.0.x'
- run: dotnet restore
- run: dotnet build --no-restore
- run: dotnet test --no-build --collect:"XPlat Code Coverage"
```

---

## Part 6 — Add Container Build/Publish Stage

![GitHub Docs page for publishing Docker images from GitHub Actions](lab-08-screenshots/ss06-publish-docker-images-docs.png)

**What you are looking at:**  
Reference for authentication, image tagging, and publish flow.

**Example pattern:**

```yaml
- uses: docker/login-action@v3
- uses: docker/build-push-action@v6
  with:
    push: true
    tags: ghcr.io/<owner>/<image>:${{ github.sha }}
```

> ⚠️ **Snag — permissions/secrets:** Ensure token/registry permissions are set or publish fails even when build/test pass.

---

## Part 7 — Configure Deployment Environments and Guardrails

![GitHub Docs page for deployment environments and approvals](lab-08-screenshots/ss07-environment-guardrails-docs.png)

**What you are looking at:**  
Environment protections: required reviewers, wait timers, and secrets scoping.

**Why this matters:**  
This prevents direct auto-deploy to protected environments without approval.

---

## Part 8 — Enforce Required Checks with Branch Protection

![GitHub Docs page for protected branches and required status checks](lab-08-screenshots/ss08-protected-branches-docs.png)

**What you are looking at:**  
Policy controls that require passing checks before merge.

**Minimum branch protection for Lab 08:**
- Require pull request before merge
- Require status checks to pass (`build-test`, coverage gate, etc.)
- Block force-push/deletion on protected branch

---

## Validation Checklist (Student Submission)

- [ ] Workflow triggers on push and PR
- [ ] Build and tests run and report status
- [ ] Failed test run blocks deploy path
- [ ] Container publish step succeeds with expected tag
- [ ] Deployment environment has guardrails
- [ ] Branch protection requires CI checks
- [ ] Successful run URL and failed run URL included

---

## Common Snags and Fixes

| Snag | Symptom | Fix |
|---|---|---|
| Actions disabled on fork | No runs start | Enable Actions in fork settings |
| Missing secret | Auth/publish step fails | Add required secrets and rerun |
| Wrong workflow trigger | PR doesn’t run checks | Add `pull_request` trigger on protected branch |
| Deploy runs despite failures | Gate misconfigured | Add `needs` chain and required checks |
| Branch protection not effective | Bad merge still allowed | Apply required status checks to target branch |

---

## Summary

Lab 08 converts your modernization work into a governed, repeatable delivery system.  
From this point forward, code quality and deployment readiness are enforced automatically rather than manually.

