Here is the master list of pre-existing materials followed by detailed breakdown tables for each module in the 2-day **Software Development and Modernization** curriculum.

---

## 🛠️ Master List of Pre-Existing Materials

1. **`eShopOnWeb` Reference Application** (Microsoft Official GitHub Repo)
2. **`eShopOnContainers` / `eShop` Microservices Application** (Microsoft Official GitHub Repo)
3. **`aro-eshop-workshop`** (Microsoft & Red Hat OpenShift Azure Reference)
4. **Azure DevOps Demo Generator** (`Parts Unlimited` & `eShopOnWeb` templates)
5. **GitHub Copilot Upgrade Agent / Workshop Repositories**
6. **Red Hat Developer Sandbox for OpenShift**
7. **Tricentis Tosca Marketplace Extension for GitHub Actions**
8. **Microsoft Learn Labs** (Docker, AKS, Application Insights, Azure Bicep)

---

## 📅 Day 1 — Modern Development Foundations & AI-Assisted Coding

### Module 1: Software Modernization Overview

| Resource Type | Pre-Existing Material / Source Link | Application in Course Lab |
| --- | --- | --- |
| **Reference Code** | `dotnet-architecture/eShopOnWeb` | Baseline monolithic application to inspect for modernization candidates.

 |
| **Documentation** | Microsoft Azure Architecture Center: *.NET Application Architecture Guides* | Slide material explaining Rehost, Refactor, Rearchitect, and Rebuild strategies.

 |
| **AI Tooling** | GitHub Copilot Upgrade Agent / Extension

 | Used to assess the legacy solution and generate modernization plans.

 |

---

### Module 2: Azure DevOps (ADO) – Work Item Tracking

| Resource Type | Pre-Existing Material / Source Link | Application in Course Lab |
| --- | --- | --- |
| **Lab Provisioning** | Azure DevOps Demo Generator (`azuredevopsdemogenerator.azurewebsites.net`) | Auto-populates ADO with pre-configured Epics, User Stories, and Sprints.

 |
| **Template** | *Parts Unlimited* or *eShopOnWeb* Demo Project Template | Board configuration, backlog management, and sprint backlog tracking lab.

 |
| **Documentation** | Azure Boards Documentation (*Agile Planning and Portfolio Management*) | Reference guide for team velocity tracking and dashboard queries.

 |

---

### Module 3: GitHub Copilot – AI-Assisted C# Development

| Resource Type | Pre-Existing Material / Source Link | Application in Course Lab |
| --- | --- | --- |
| **Workshop Repo** | `microsoft/copilot-labs` or `microsoft/copilot-csharp-workshop` | Practice prompting strategies, unit test generation (MSTest/xUnit), and refactoring.

 |
| **Learning Path** | Microsoft Learn: *Develop with AI-powered code suggestions using GitHub Copilot* | Source material for prompt engineering and governance best practices.

 |
| **IDE Plugins** | GitHub Copilot for Visual Studio / VS Code

 | Developer desktop integration for writing unit tests and XML documentation.

 |

---

### Module 4: C# and .NET in the Modern Stack

| Resource Type | Pre-Existing Material / Source Link | Application in Course Lab |
| --- | --- | --- |
| **Sample Code** | `.NET 8 / .NET 9 Web API Reference Samples` (`dotnet/samples`) | Template for Minimal APIs, Dependency Injection, and Async/Await.

 |
| **ORM / Database** | Entity Framework Core & Dapper Docs / Code Snippets

 | Adding REST endpoints backed by Azure SQL / SQL Server LocalDB.

 |
| **Security Guides** | Azure Key Vault references for ASP.NET Core (`Microsoft.Extensions.Configuration.AzureKeyVault`)

 | Secrets management lab exercise.

 |

---

### Module 5: Test Automation with Tricentis Tosca

| Resource Type | Pre-Existing Material / Source Link | Application in Course Lab |
| --- | --- | --- |
| **Official Docs** | Tricentis Tosca Documentation (*Model-Based Testing and ADO Integration*)

 | Theoretical basis for MBT (Modules, TestCase Design, Execution Lists).

 |
| **CI/CD Plugin** | Visual Studio Marketplace: *Tricentis Tosca Execution Task for Azure DevOps / GitHub Actions*<br> | Integrating automated UI/API test runs directly into pipelines.

 |
| **Target App** | Modernized REST API built in Module 4

 | Live endpoint target for scanning UI and executing API test suits.

 |

---

## 📅 Day 2 — Containerization, Kubernetes, CI/CD, and Azure Deployment

### Module 6: Containerization with Docker & Podman

| Resource Type | Pre-Existing Material / Source Link | Application in Course Lab |
| --- | --- | --- |
| **Official Repo** | `dotnet/dotnet-docker` (Official Microsoft .NET Docker Samples) | Multi-stage `Dockerfile` templates for ASP.NET Core (Linux/Windows).

 |
| **Microsoft Learn** | *Build and run a containerized web app with Docker and Azure Container Registry*<br> | ACR registry setup, image building, tagging, and pushing.

 |
| **Local Tooling** | Docker Desktop / Podman CLI & Docker Compose

 | Multi-container local orchestration (App + SQL Server).

 |

---

### Module 7: Kubernetes and OpenShift

| Resource Type | Pre-Existing Material / Source Link | Application in Course Lab |
| --- | --- | --- |
| **Workshop Repo** | `Azure-Samples/aro-eshop-workshop` (Azure Red Hat OpenShift Workshop) | Manifest files (`.yaml`), OpenShift `Routes`, `DeploymentConfigs`, and `ImageStreams`.

 |
| **Sandbox Environment** | Red Hat Developer Sandbox for OpenShift | Free 30-day cluster environment for students to deploy containerized workloads.

 |
| **K8s Guides** | Kubernetes Documentation (*ConfigMaps, Secrets, Probes, Autoscaling*)

 | Configuring liveness/readiness probes, secrets, and autoscaling.

 |

---

### Module 8: CI/CD Pipelines with GitHub Actions

| Resource Type | Pre-Existing Material / Source Link | Application in Course Lab |
| --- | --- | --- |
| **GitHub Actions** | Official Marketplace Actions: `dotnet/setup-dotnet`, `docker/build-push-action`, `redhat-actions/oc-login` | Modular pipeline steps for building, packaging, and deploying.

 |
| **Lab Guide** | Microsoft Learn: *AZ-400 Implement CI/CD with GitHub Actions and Azure* | Building end-to-end automation triggers and pipeline quality gates.

 |
| **Sample Pipeline** | `.github/workflows/deploy.yml` from `eShopOnWeb` repo | Working reference workflow for container builds and deployment.

 |

---

### Module 9: Azure Cloud Deployment and Operations

| Resource Type | Pre-Existing Material / Source Link | Application in Course Lab |
| --- | --- | --- |
| **IaC Templates** | Azure Quickstart Templates / Bicep Files (`Azure/azure-quickstart-templates`) | Infrastructure as Code deployment for App Service, AKS, and Azure SQL.

 |
| **Monitoring Docs** | Microsoft Learn: *Monitor application performance with Application Insights*<br> | Telemetry, logging, and SLA dashboard setup.

 |
| **Migration Guides** | Azure SQL Database Migration Guides (Data Migration Assistant / Azure Migrate)

 | Database migration hands-on reference.

 |

---

### Module 10: Capstone – End-to-End Modernization

| Resource Type | Pre-Existing Material / Source Link | Application in Course Lab |
| --- | --- | --- |
| **Master Architecture** | `dotnet-architecture/eShopOnWeb` OR `dotnet/eShop` | Final repository for end-to-end modernized delivery.

 |
| **Integrated Stack** | Combined Module 2 ADO Board + GitHub Actions + Red Hat OpenShift + Azure App Insights

 | Final student team challenge and debrief roadmap.

 |