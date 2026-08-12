# Course Outline Comparison

**Date:** 2026-08-09  
**Source 1:** `Software Development Modernization.docx` (official course outline)  
**Source 2:** `course/mvp-delivery/revised-course-outline.md` (MVP delivery outline)

---

## Summary

The `.docx` outline is the authoritative customer-facing course description. The revised MVP outline is the instructor's delivery plan — it preserves the same 10-module structure but classifies modules as Core, Optional, or Stretch and trims scope to ensure a first-release delivery.

Both documents share the same 2-day, 10-module shape and the same reference application (eShopOnWeb / C#/.NET). Key differences are in **module status**, **lab scope**, and the **Tosca (Module 5)** and **ADO (Module 2)** treatment.

---

## Module-by-Module Comparison

| # | Module Title | .docx Status | MVP Status | Lab Topic (.docx) | Lab Topic (MVP) | Key Gaps / Differences |
|---|---|---|---|---|---|---|
| 1 | Software Modernization Overview | Full (Core) | Core | Explore reference app; identify modernization candidates | Same | None — fully aligned |
| 2 | Azure DevOps – Work Item Tracking | Full (Core) | **Optional / supporting** | Create and manage a sprint backlog | Instructor-led demo or guided tour when ADO access is available | MVP demotes to optional; .docx treats as a required Day 1 module |
| 3 | GitHub Copilot – AI-Assisted C# Development | Full (Core) | Core | Refactor legacy C# module; generate unit tests with Copilot | Same | None — fully aligned |
| 4 | C# and .NET in the Modern Stack | Full (Core) | Core | Add SQL Server-backed REST endpoint using Copilot | Add SQL-backed REST endpoint to reference app | Minor wording difference; scope aligned |
| 5 | Test Automation with Tricentis Tosca | Full (Core) | **Optional / phase-2** | Create and execute Tosca tests; publish results to ADO | Instructor demo or phase-2 enrichment when Tosca access is not ready | Largest gap — .docx shows Tosca as a required Day 2 module; MVP defers it due to tooling/access constraints |
| 6 | Containerization with Docker | Full (Core) | Core | Containerize ASP.NET Core app; push to Azure Container Registry | Containerize app; run locally with health checks; push to ACR | MVP adds explicit health-check step; otherwise aligned |
| 7 | Kubernetes and OpenShift | Full (Core) | Core | Deploy containerized app to OpenShift; configure autoscaling | Deploy to OpenShift or Kubernetes fallback; configure autoscaling | MVP adds explicit Kubernetes fallback path (Red Hat Developer Sandbox); otherwise aligned |
| 8 | CI/CD Pipelines with GitHub Actions | Full (Core) | Core | Build complete CI/CD pipeline: commit → build → test → OpenShift deploy | Create working build-test-deploy pipeline with quality gates | MVP emphasizes quality gates; .docx adds Tosca integration in pipeline — deferred in MVP |
| 9 | Azure Cloud Deployment and Operations | Full (Core) | **Optional / advanced** | Deploy full reference stack to Azure with App Insights monitoring | Advanced path when quotas and access are available | MVP demotes to optional; .docx treats as a required Day 2 module |
| 10 | Capstone – End-to-End Modernization | Full (Core) | **Stretch / synthesis** | Full delivery: ADO backlog → monitored Azure deployment | Package work completed across prior labs as capstone checkpoint | .docx capstone includes Azure monitoring and ADO reporting; MVP trims to core toolchain synthesis |

---

## Alignment Score

| Dimension | Aligned | Partially Aligned | Gap |
|---|---|---|---|
| Module count and sequence | ✅ | | |
| Day 1 / Day 2 split | ✅ | | |
| Core lab topics (1, 3, 4, 6, 7, 8) | ✅ | | |
| Module 2 ADO scope | | ⚠️ | |
| Module 5 Tosca scope | | | ❌ |
| Module 9 Azure Operations scope | | ⚠️ | |
| Module 10 Capstone depth | | ⚠️ | |
| Reference application (eShopOnWeb / C#) | ✅ | | |
| Target audience and prerequisites | ✅ | | |

---

## Key Recommendations

1. **Module 5 (Tosca)** is the most significant gap. The `.docx` positions it as a required Day 2 module with a full lab. The MVP plan defers it. Before course delivery, decide whether:
   - Tosca licenses and a test environment will be available, or
   - The module is explicitly reframed as "bring-your-own-tool" with an equivalent open-source demo.

2. **Module 2 (ADO)** is taught as required in the `.docx` but treated as optional in the MVP. Instructors who have ADO org access should deliver it as written. Document this as a prerequisite for the ADO org to be provisioned before class.

3. **Module 9 (Azure)** requires Azure quota and subscription access. The MVP correctly flags this as advanced. Add a note in the student guide so learners know what to provision before Day 2.

4. **Module 10 (Capstone)** in the `.docx` includes ADO reporting and Azure monitoring — both depend on Modules 2 and 9. The MVP capstone scope should be explicitly versioned: *MVP Capstone* vs *Full Capstone*.

5. **CI/CD pipeline (Module 8)** in the `.docx` includes Tosca test runs inside the pipeline. Since Tosca is deferred in the MVP, add a placeholder step that shows where Tosca would integrate, so the pipeline lab remains accurate relative to the `.docx`.

---

## Files Referenced

| File | Description |
|---|---|
| `Software Development Modernization.docx` | Official customer-facing course outline |
| `course/mvp-delivery/revised-course-outline.md` | MVP delivery plan and module classification |
| `course/mvp-delivery/labs/` | MVP lab markdown files (one per module) |
| `course/mvp-delivery/modules/` | MVP module content files (one per module) |
| `assess-labs/lab-e2e-test-report.md` | E2E test report for all 10 labs |
