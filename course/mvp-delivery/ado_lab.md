lab generation.. Markdown


# TASK: Generate a Student Lab Manual & Repository Specs for "App Modernization with Azure DevOps"

## Context & Learning Objectives
Act as an Enterprise DevOps Architect and Technical Course Author. Generate a complete, production-ready lab manual in Markdown format (`lab-app-modernization-ado.md`) for students learning Azure DevOps (ADO).

The lab focuses on decomposing a monolithic architecture into a modern containerized application using **eShopOnWeb** as the reference application.

---

## Lab Architecture & Workflow

### 1. Project Provisioning (Azure DevOps Demo Generator)
* **Template Source:** `eShopOnWeb` (via `azuredevopsdemogenerator.azurewebsites.net`)
* **Process Template:** Agile / Scrum
* **Target Repositories:** `eShopOnWeb` ASP.NET Core Monolith and modern Microservices (`Catalog.API`).

### 2. Module Objectives & Student Tasks
Generate detailed, step-by-step instructions for the following 4 exercises:

#### Exercise 1: Agile Planning for Monolith Modernization
* **Task 1.1:** Create an Agile Hierarchy:
  * **Epic:** *Monolith Decomposition to Microservices*
  * **Features:** *Extract Catalog Microservice*, *Containerize Web UI*, *Implement CI/CD Traceability*.
* **Task 1.2:** Map user stories and sprint tasks under the *Catalog Microservice* feature.
* **Task 1.3:** Configure Area Paths (*Legacy-Monolith*, *Modern-CatalogAPI*) and Iteration Schedules (*Sprint 1: Refactoring*, *Sprint 2: Containerization*).

#### Exercise 2: Code Refactoring & Branching Strategy
* **Task 2.1:** Create a feature branch `feature/catalog-api-container` from `main` in Azure Repos.
* **Task 2.2:** Add a multi-stage `Dockerfile` to containerize the decoupled API module.
* **Task 2.3:** Link the local branch and commit directly to the Azure Boards Task ID using `#<work-item-id>` notation in commit messages.

#### Exercise 3: CI/CD Pipeline & Automated Traceability
* **Task 3.1:** Author an `azure-pipelines.yml` file featuring:
  * Multi-stage build (Build & Test, Containerize to Azure Container Registry).
  * Automated work item linking and state transition on successful main branch merge.
* **Task 3.2:** Open a Pull Request in Azure Repos, assign work item links, and complete the merge.

#### Exercise 4: Verification & Dashboard Analytics
* **Task 4.1:** Verify work item status transition and traceability from the Development Pane.
* **Task 4.2:** Build a custom ADO Dashboard containing:
  * Burndown Chart for Sprint 1.
  * Query Tile showing open Modernization Bugs vs. Completed Stories.
  * Pipeline status widget for `eShopOnWeb-CI`.

---

## Formatting & Output Requirements
1. **Student Lab Manual (`lab-app-modernization-ado.md`):**
   * Clear prerequisites (Azure DevOps Org, Azure Subscription).
   * Exact navigation steps (e.g., `Boards -> Backlogs -> + New Work Item`).
   * Code blocks for `azure-pipelines.yml` and `Dockerfile`.
   * Validation checkpoints at the end of each exercise.

2. **Instructor Guide & Verification Script:**
   * A checklist for instructors to quickly grade student boards and pipelines.