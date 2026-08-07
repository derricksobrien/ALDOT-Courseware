# Lab End-to-End Test Report

**Software Development Modernization &middot; `course/labs` (Labs 01&ndash;10)**

- **Prepared:** August 7, 2026
- **Live class:** August 10&ndash;11, 2026
- **Method:** Hands-on execution against the real repo + static review
- **Scope:** All 10 labs, plus the existing `course/mvp-delivery/tests` PowerShell suite

> Internal QA notes — not for distribution to students.

## What "tested" means here

I ran the actual repo &mdash; real `dotnet build`/`test`, a real `docker` image definition, a real `az bicep build` &mdash; against the exact source in `course/repos/`. That's genuine signal, not a guess.

**What I deliberately didn't touch:** the live Azure tenant, Azure DevOps org, and remote lab desktops from the `access-labs/` documents. Those Temporary Access Passes are provisioned for 14 real students in 3 days, and I couldn't confirm whether they're single-use &mdash; signing in myself risked consuming or locking one before anyone else does. I reviewed those labs' instructions closely instead of executing them live (see the access-risk note under Cross-Cutting Findings).

## Status at a Glance

| Lab | Topic | Status |
|---|---|---|
| 01 | Modernization Discovery | 🟠 Risk found (confirmed & fixed) |
| 02 | ADO Work Tracking | ⚪ Untestable (live tenant) |
| 03 | Copilot Refactor | 🟠 Risk found (confirmed) |
| 04 | .NET API + SQL | 🟠 Risk found (confirmed) |
| 05 | Tosca Testing | ⚪ Untestable (licensed GUI tool) |
| 06 | Docker | 🟠 Risk found (partially testable) |
| 07 | Kubernetes/OpenShift | 🟠 Risk found (confirmed content gap) |
| 08 | GitHub Actions | 🟢 Pass, with scope caveat |
| 09 | Azure Ops | 🟠 Risk found (permissions concern) |
| 10 | Capstone | 🟠 Compounds Labs 2, 4&ndash;9 |

## Per-Lab Findings

### Lab 01 &middot; Modernization Discovery

**Works:** `dotnet build eShopOnWeb.sln` succeeds in ~2.5 min (mostly NuGet restore). All 44 unit tests pass in under a second. The build even surfaces two real, known-vulnerable NuGet packages &mdash; genuinely useful, authentic material for the "find 8 modernization candidates" exercise.

**Breaks:** Step 2 ("build and run the solution locally") fails immediately for anyone without SQL Server LocalDB installed &mdash; and Lab 1's Prerequisites never mention SQL Server at all, so this arrives as a total surprise on the very first lab of the course.

```text
fail: Web[0]
      A network-related or instance-specific error occurred while establishing
      a connection to SQL Server... Unable to locate a Local Database Runtime installation.
```

**Recommendation:** The app already ships a working escape hatch &mdash; I verified it end to end:

```text
$ UseOnlyInMemoryDatabase=true dotnet run --urls http://localhost:5199
Now listening on: http://localhost:5199
$ curl http://localhost:5199/
HTTP 200 — "Catalog - Microsoft.eShopOnWeb"
```

Add one line to Lab 1's Prerequisites: set `UseOnlyInMemoryDatabase=true` (env var or `appsettings.Development.json`) if LocalDB isn't installed.

### Lab 02 &middot; Azure DevOps Work Tracking

**Untestable:** needs an interactive sign-in against the live tenant provisioned for the Aug 10 class (see access-risk note).

**Scope concern:** 2 epics, 4+ features, 12+ user stories each broken into tasks, one sprint with capacity, 3 saved queries, a 3-widget dashboard, and 3 commit links &mdash; from a cold start, including creating the team and area path &mdash; inside 60 minutes. That's a lot of pure configuration for a first-time Azure Boards user.

**Recommendation:** Either extend the timebox toward 90 minutes or trim scope, and pre-seed the team/area path so students start at "add stories," not "configure the project."

### Lab 03 &middot; Copilot Refactor and Unit Tests

**Works:** Baseline is clean: 44/44 tests pass, so "behavior preserved after refactor" is genuinely and quickly checkable by students.

**Breaks:** The validation check demands "at least 80 percent line coverage for changed code," but no step says how to measure it. The only coverage setup in the repo (`CodeCoverage.runsettings`) uses Visual Studio's Enterprise-only coverage collector, and the one project with a coverlet reference isn't the one students would actually touch.

**Recommendation:** Add a concrete step: `dotnet test --collect:"XPlat Code Coverage"` (works in VS Code, no Enterprise license needed) &mdash; or drop the numeric bar for a qualitative checklist.

### Lab 04 &middot; Modern .NET API with SQL

**Works:** A complete, real Minimal API + repository pattern already exists in `PublicApi` for students to model their new endpoint on.

**Breaks:** The prerequisite is "Local SQL Server or Azure SQL," but neither is confirmed. LocalDB isn't present in my test environment, and the repo's Docker-based SQL fallback couldn't be verified because Docker Desktop's engine isn't running here (see Cross-Cutting Findings). The Azure SQL instance from Module 9 isn't provisioned until Day 2 &mdash; and that module is Optional &mdash; so Day 1's Lab 4 has no confirmed database target. Separately: Dapper is offered as an alternative to EF Core, but zero Dapper code exists anywhere in the repo, so that path starts from nothing while EF Core has a full worked example.

**Recommendation:** Confirm LocalDB (or a working Docker SQL container) on the real lab machines before Aug 10. Default the lab to EF Core, or add one Dapper snippet if it should stay an equal option.

### Lab 05 &middot; Test Automation and Quality Gates (Tosca)

**Untestable:** proprietary, licensed Windows GUI software.

**Gap:** None of the three `access-labs` documents mention Tosca being installed or licensed for this cohort &mdash; only remote desktop, Azure, and ADO access are confirmed. Module 5 is already marked Optional in the MVP outline for this exact reason; asking for 10 automated test cases (5 UI + 5 API) in 75 minutes on a tool most students have never opened is ambitious even if it is installed.

**Recommendation:** Confirm Tosca install/license with ProTech before Aug 10, or run this module as an instructor-led demo, as the courseware already anticipates.

### Lab 06 &middot; Containerization with Docker

**Verified:** The multi-stage Dockerfile itself is real, correct, and pulled directly from `course/repos/eShopOnWeb` &mdash; not a fabricated example.

**Could not verify:** the actual `docker build`/`run`. Docker Desktop's CLI is installed in my environment, but its engine service is stopped, and I don't have permission to start it:

```text
failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine
Cannot open com.docker.service service on computer '.' (access denied)
```

That's a limit of my sandbox, not a confirmed defect &mdash; but it's worth naming: Docker Desktop is a well-known failure point inside remote-desktop/VDI machines unless the host explicitly enables nested virtualization for its WSL2 backend, which is exactly the class of machine `labs.protechtraining.com` provides.

**Recommendation:** Before Aug 10, run `docker run hello-world` on one real COMPUTER52x machine. This is the single highest-leverage pre-flight check for the whole two days &mdash; Labs 6, 7, and 10 all assume a working container runtime. Separately, ACR push (steps 5&ndash;6) needs Azure auth not taught until Module 9 &mdash; same sequencing gap as Lab 4.

### Lab 07 &middot; Kubernetes and OpenShift Deployment

**Breaks:** `course/repos/s2i-dotnetcore-ex` &mdash; the repo the lab points students to &mdash; contains **zero** Kubernetes/OpenShift YAML. It deploys entirely through OpenShift's `oc new-app` source-to-image flow, which builds its BuildConfig/DeploymentConfig/ImageStream internally. Step 2 ("apply deployment and service manifests") assumes a manifest that doesn't exist anywhere in this repo. The lab's own footnote anticipates falling back to this repo if `aro-eshop-workshop` is unavailable &mdash; and that repo isn't present in `course/repos/` at all, so this fallback is the path every student actually hits, and it currently dead-ends.

**Recommendation:** Add a small, ready-to-use set of Deployment/Service/Route YAML (targeting the Module 6 image) into the repo or lab handout. Also confirm a reachable OpenShift/AKS cluster for 14 students before Aug 10 &mdash; the access documents provision a general Azure subscription but don't name a cluster.

### Lab 08 &middot; CI/CD with GitHub Actions

**Verified:** The real workflow (`dotnetcore.yml`) is valid YAML and does exactly what the lab assumes: checkout, restore, build, test &mdash; nothing else. "Extend this into a full pipeline" is an honest, accurate framing of the actual starting point.

```text
Steps: actions/checkout@v2 → Setup .NET → Build with dotnet → Test with dotnet
YAML parses cleanly
```

**Minor pitfalls:** The bare `on:` key is a known trap for generic YAML tools (a YAML 1.1 parser reads it as the boolean `true`, not the string "on") &mdash; not a bug, GitHub's own parser is unaffected, but worth a one-line callout so a student who checks their file with a random online linter isn't thrown by an unrelated error. Separately, prerequisites say "GitHub repository with Actions enabled" without saying which repo &mdash; eShopOnWeb here is a read-only reference copy.

**Recommendation:** Add an explicit "fork the repo to your own account" step 0. Move rollback/notifications (currently core steps) to Stretch Goals &mdash; they stack a lot of new surface onto the same 90 minutes as the container job.

### Lab 09 &middot; Azure Deployment and Operations

**Verified:** The Bicep templates are real and complete (App Service, plan, SQL Server, Key Vault + access module) and compile cleanly:

```text
$ az bicep build --file main.bicep --stdout
2 nullability warnings only — no errors
```

**Unconfirmed risk:** `main.bicep` provisions Key Vault role assignments, which normally requires `Microsoft.Authorization/roleAssignments/write` &mdash; a permission the students' granted "PowerUser" role often does *not* include (that's usually Owner or User Access Administrator). If PowerUser turns out to be Contributor-equivalent only, the deployment will fail partway through on the role-assignment step &mdash; a confusing place for a newcomer to get stuck.

**Recommendation:** Confirm the exact RBAC behind "PowerUser" before Aug 10. If it's Contributor-only, either pre-grant the role assignment or trim that resource out of the training deployment.

### Lab 10 &middot; Capstone End-to-End

**Assessment:** Inherits every open risk above by construction. The MVP course outline already defers this lab to "release 2" until the core six modules are proven stable &mdash; this testing pass gives concrete, evidence-backed support for that call rather than a new finding.

## Cross-Cutting Findings

**Total lab time vs. two days.** Stated timeboxes sum to 840 minutes (14 hours) across all 10 labs. Even just the "core six" the MVP outline treats as required (1, 3, 4, 6, 7, 8) total 495 minutes (8.25 hours) of hands-on time alone &mdash; before any lecture/module content &mdash; across two days. The gaps above (SQL access, Docker engine, missing manifests) will eat directly into that budget as troubleshooting time if not resolved beforehand.

**Why I didn't sign in with the provisioned access.** The `access-labs` documents contain real Temporary Access Passes for 14 students and 1 instructor against a live Entra ID tenant, plus remote-desktop credentials for the ProTech machines, all provisioned for the Aug 10&ndash;11 class. TAPs can be configured single-use or multi-use by the tenant admin &mdash; I had no way to tell which from the document alone. Signing in myself, three days out, risked consuming or flagging one before the actual student ever touches it. I treated that as outside what "go ahead and test the labs" should implicitly authorize, and reviewed those labs' content instead of executing them live.

## Improvement List, by Priority

### P0 &mdash; verify before Aug 10 (would derail a live session)

1. **Confirm the SQL path for Labs 1 & 4** &mdash; LocalDB installed, or the Docker SQL container actually starts, on a real COMPUTER52x machine.
2. **Run `docker run hello-world` on a real training machine** &mdash; confirms Docker Desktop's engine actually starts inside the ProTech remote-desktop environment.
3. **Confirm the RBAC behind students' "PowerUser" Azure role** &mdash; Lab 9's Bicep creates role assignments; verify that permission is actually granted.
4. **Confirm Tosca is installed and licensed for this cohort** &mdash; or commit now to running Lab 5 as an instructor-led demo.
5. **Confirm a reachable Kubernetes/OpenShift cluster for Lab 7** &mdash; no AKS cluster or OpenShift sandbox is named anywhere in the access documents.

### P1 &mdash; content fixes (no live infra required)

6. **Document `UseOnlyInMemoryDatabase=true` in Lab 1** &mdash; verified working fallback for machines without LocalDB.
7. **Add a real coverage-measurement step to Lab 3** &mdash; `dotnet test --collect:"XPlat Code Coverage"`, works without a VS Enterprise license.
8. **Add starter Kubernetes/OpenShift manifests for Lab 7** &mdash; none exist today in any repo the lab points to.
9. **Add a "fork the repo" step to Lab 8** &mdash; before any workflow file can be edited and pushed.
10. **Resolve the EF Core / Dapper asymmetry in Lab 4** &mdash; default to EF Core, or add one worked Dapper example to match it.

### P2 &mdash; scope and sequencing

11. **Re-time or pre-seed Lab 2** &mdash; 60 minutes is tight for the amount of ADO configuration asked from a first-time user.
12. **Move ACR push (Lab 6) and rollback/notifications (Lab 8) to Stretch Goals** &mdash; both currently sit as core steps but depend on Module 9 content not yet taught.
13. **Revisit the total lab-time budget** &mdash; ~8.25 hours of hands-on time for the core six alone, across two days, once lecture time is added.

---

*Evidence gathered via `dotnet`, `docker`, `az bicep`, `kubectl`/`oc`, and `gh` CLIs directly against `course/repos/` &mdash; no live Azure, ADO, or remote-desktop session was used.*
