# MVP Priority Gap Analysis

This analysis identifies the minimum set of gaps that must be closed to ship a usable version of the course quickly using the repos and assets already in the workspace.

## Decision Frame

The fastest viable product is not the full 10-module course on day one. The MVP should deliver a complete learning arc using the most reliable existing material, then defer the highest-friction dependency-heavy modules.

### Primary Source Material We Can Reuse Right Now

- `course/repos/eShopOnWeb` as the main modernization reference app
- `course/repos/eShop` as a stretch or advanced reference for a service-oriented variant
- `course/repos/samples` as a library of .NET examples and patterns
- `course/repos/s2i-dotnetcore-ex` as the OpenShift deployment baseline
- `sample_coursware/AI-In-Software-Testing-main` as the structure and pacing guide

## Priority List

### P0 - Blockers for Any MVP Release

These gaps must be closed before the course can be delivered to learners.

| Gap | Why It Matters | MVP Action |
|---|---|---|
| Stable reference app baseline | Every lab depends on a known starting point | Use `eShopOnWeb` as the primary baseline and freeze a known-good branch |
| Local dev toolchain | Learners need a repeatable setup | Standardize `.NET`, Python, Docker or Podman, Git, and a browser check |
| Lab reset path | Delivery-day failures are most often environment drift | Add reset steps and seed data for every lab that mutates state |
| Container runtime choice | Lab instructions must be unambiguous | Pick Docker Desktop or Podman as the default and document the fallback |
| Cluster target | K8s/OpenShift labs need a real deployment path | Use `s2i-dotnetcore-ex` plus one named cluster or a known fallback namespace |
| Repo and branch permissions | Students cannot work if they cannot commit or pull | Precreate repos/branches and validate access before the course |

### P1 - Required to Make the MVP Feel Complete

These are not hard blockers, but they materially affect the learner experience.

| Gap | Why It Matters | MVP Action |
|---|---|---|
| SQL target path | Module 4 needs a working data store | Use local SQL Server/LocalDB or SQLite for MVP, Azure SQL as stretch |
| CI workflow starter | Module 8 needs a repeatable pipeline | Preseed `.github/workflows` from an existing repo and simplify the job graph |
| ACR access | Container delivery needs an image registry | Provide one shared registry or delay registry push to the optional track |
| Copilot enablement | Module 3 depends on AI-assisted editing | Confirm licensing and IDE sign-in before the session starts |
| Documentation templates | The course must be consistent and readable | Reuse the sample courseware tone and structure for all PDFs |

### P2 - Can Be Deferred Without Breaking the MVP

These items are valuable, but they are not required for the first shippable version.

| Gap | Why It Can Wait | MVP Decision |
|---|---|---|
| ADO full demo generator setup | Adds setup overhead and tenant dependency | Keep as optional or instructor-led demo content |
| Tosca licensing and execution plumbing | High setup cost and licensing risk | Keep as optional or phase 2 |
| Azure Monitor/App Insights full depth | Adds cloud cost and extra setup time | Make the Azure operations path optional in MVP |
| Full capstone integration | Depends on all preceding toolchains | Move to a later release once core labs are stable |

## MVP Product Definition

The MVP product is a two-day course package with the following minimum deliverables:

1. One PDF courseware file for Day 1
2. One PDF courseware file for Day 2
3. A matching lab markdown file for each core module
4. A single reference app baseline that works for all core hands-on steps
5. A short instructor validation checklist for every lab
6. A sitemap that links the course pages and lab pages together

## MVP Scope

### Core Modules to Ship in MVP

These are the modules that give learners the end-to-end modernization flow with the fewest moving parts.

| Module | MVP Status | Reason |
|---|---|---|
| Module 1 - Software Modernization Overview | Core | Establishes the course story and the reference app |
| Module 3 - GitHub Copilot Assisted C# Development | Core | Delivers the AI-assisted coding objective with low infrastructure overhead |
| Module 4 - C# and .NET in the Modern Stack | Core | Produces a working API and gives the course technical depth |
| Module 6 - Containerization with Docker | Core | Introduces the operational deployment path |
| Module 7 - Kubernetes and OpenShift | Core | Demonstrates container orchestration in a realistic platform |
| Module 8 - CI/CD Pipelines with GitHub Actions | Core | Connects code, test, container, and deploy into one workflow |

### Modules to Defer or Reduce

| Module | MVP Status | MVP Treatment |
|---|---|---|
| Module 2 - Azure DevOps Work Tracking | Optional | Keep as instructor-led demo or phase 2 unless ADO is fully provisioned |
| Module 5 - Test Automation with Tricentis Tosca | Optional | Keep as phase 2 or demo-only unless licensing and access are ready |
| Module 9 - Azure Cloud Deployment and Operations | Optional | Include as an advanced path if Azure quotas and monitoring are ready |
| Module 10 - Capstone End-to-End Modernization | Stretch | Move to release 2 after the core labs are stable |

## Recommended MVP Learning Path

1. Module 1: explain the modernization path and inspect the reference app.
2. Module 3: use Copilot to refactor a controlled code target and generate tests.
3. Module 4: add a REST endpoint and connect it to a data store.
4. Module 6: containerize the app and run it locally.
5. Module 7: deploy the container to OpenShift or the chosen K8s fallback.
6. Module 8: wire the repo into GitHub Actions and run the build/test/deploy path.

## E2E Lab Validation Standard

Every core lab in the MVP must pass this checklist before delivery day:

- The starting repo branch is known-good
- The learner can complete the lab from a clean clone
- The lab instructions match the current repo state
- The lab includes an expected output or screenshot target
- The lab ends with a reproducible verification step
- The instructor can reset the environment in less than 10 minutes

## Highest-Risk Provisioning Gaps

These are the items most likely to cause delivery-day snags:

1. ADO and Tosca access if they remain part of the live path.
2. OpenShift or AKS credentials if cluster access is not prevalidated.
3. SQL connection and seed data if Module 4 uses a live database.
4. Registry access if Module 6 or Module 8 pushes images.
5. Copilot sign-in and policy approval for Module 3.

## MVP Recommendation

Ship the core six-module track first, keep the high-friction modules as optional add-ons, and use the sample courseware format to keep the PDF content consistent and concise.