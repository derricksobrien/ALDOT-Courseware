# -*- coding: utf-8 -*-
"""Enhanced content for all 10 modules + the build loop.

Content is grounded in three places:
  1. This repo's actual module/lab/design/outline files.
  2. Real code pulled from course/repos/eShopOnWeb and course/repos/s2i-dotnetcore-ex.
  3. Authoritative external docs (Microsoft Learn, Docker Docs, Kubernetes.io,
     GitHub Docs, Tricentis) fetched and cited per module.
"""
import os
from reportlab.pdfgen import canvas

from build_module_pdfs import (
    PAGE_W, PAGE_H, OUT_DIR, img,
    title_slide, section_slide, bullet_slide, cards_slide, quiz_slide,
    diagram_slide, code_slide, sources_slide,
    icon_rocket, icon_gear, icon_grid, icon_cycle,
    icon_chart_up, icon_document, icon_person, icon_check,
)

MODULES = [
    # ================================================================ M1
    dict(
        file="module-01-modernization-overview",
        day="Day 1", tier="Core MVP Module", kicker="Module 01",
        title="Software Modernization Overview",
        theme=["legacy code on computer screen close up",
               "software architecture diagram on whiteboard",
               "developer reviewing old codebase",
               "modern vs legacy technology concept"],
        objectives=[
            "Explain modernization outcomes in business and technical terms.",
            "Distinguish rehost, refactor, rearchitect, and rebuild.",
            "Identify modernization candidates in a legacy .NET application.",
        ],
        narrative=["This module establishes the course baseline and shared vocabulary.",
                   "Learners review a real .NET application and classify modernization "
                   "opportunities by strategy and risk."],
        focus=["Why modernization matters",
               "Rehost, refactor, rearchitect, rebuild",
               "How the reference app anchors the course"],
        diagram=dict(
            caption="Microsoft's Cloud Adoption Framework: four of the core migration strategies, in order of increasing change.",
            steps=[
                ("REHOST", "Lift-and-shift; minimal code change"),
                ("REFACTOR", "Improve code structure; cut tech debt"),
                ("REARCHITECT", "Redesign for scale — e.g. monolith to microservices"),
                ("REBUILD", "Full redevelopment on cloud-native tech"),
            ],
            icons=[icon_cycle, icon_gear, icon_grid, icon_rocket],
        ),
        field_facts=dict(
            title="From the Docs: The Full Migration Framework",
            bullets=[
                "Microsoft's Cloud Adoption Framework actually defines 8 strategies: Retire, Retain, Rehost, Replatform, Refactor, Rearchitect, Rebuild, Replace.",
                "Rehost = like-for-like migration, e.g. on-prem servers moved directly to Azure VMs.",
                "Microsoft's own warning: don't rehost a problematic workload as-is — it just carries the technical debt into the cloud.",
                "Rearchitect example Microsoft gives: breaking a monolith into microservices for scale and agility.",
                "Rebuild is reserved for systems too outdated or inflexible to modernize any other way.",
            ],
            source=("Select your cloud migration strategies — Cloud Adoption Framework",
                    "https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/plan/select-cloud-migration-strategy"),
        ),
        real_example=dict(
            kind="quote",
            slide_title="The Reference App, In Its Own Words",
            bullets=[
                "eShopOnWeb describes itself as a “sample ASP.NET Core reference application… demonstrating a single-process (monolithic) application architecture.”",
                "Its own README points to eShopOnContainers/eShop as the sibling app that “focuses on a microservices/containers-based application architecture.”",
                "Same product line, two strategies: eShopOnWeb is the rehost/refactor target; eShop is what a rearchitect looks like.",
            ],
            source_note="Source: course/repos/eShopOnWeb/README.md",
        ),
        resources=[
            ("Reference Code", "dotnet-architecture/eShopOnWeb",
             "Baseline monolithic application to inspect for modernization candidates."),
            ("Documentation", "Microsoft Azure Architecture Center: .NET Application Architecture Guides",
             "Slide material explaining Rehost, Refactor, Rearchitect, and Rebuild strategies."),
            ("AI Tooling", "GitHub Copilot Upgrade Agent / Extension",
             "Used to assess the legacy solution and generate modernization plans."),
        ],
        assets=["Reference app: course/repos/eShopOnWeb", "Design anchor: course/design.md"],
        lab_name="Lab 01: Modernization Discovery",
        lab_goal="Identify and prioritize modernization candidates in the baseline app.",
        lab_env="Tools: Git, .NET SDK, VS Code · No cloud dependency required.",
        lab_steps=[
            "Step 1 — Open eShopOnWeb and run a local build.",
            "Step 2 — Identify major architecture boundaries and high-risk areas.",
            "Step 3 — Record at least 8 modernization candidates.",
            "Step 4 — Tag each item as rehost, refactor, rearchitect, or rebuild.",
            "Step 5 — Prioritize the list by impact and implementation effort.",
        ],
        lab_validation="Validation: baseline app builds successfully, and the candidate matrix contains classification plus priority.",
        quiz=dict(
            q="Which modernization strategy moves an application to new infrastructure with minimal changes to the underlying code?",
            options=["Rebuild", "Rehost", "Refactor", "Rearchitect"],
            answer=1,
        ),
        quiz2=dict(
            q="According to Microsoft's Cloud Adoption Framework, how many total migration strategies (“R's”) does it define?",
            options=["4", "5", "6", "8"],
            answer=3,
        ),
        sources=dict(
            citations=[("Select your cloud migration strategies — Cloud Adoption Framework",
                        "https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/plan/select-cloud-migration-strategy")],
            local_paths=["course/repos/eShopOnWeb/README.md", "course/design.md",
                         "course/mvp-delivery/modules/module-01-modernization-overview.md"],
        ),
        success="Learner completes candidate matrix with at least 8 candidate changes and strategy labels.",
    ),
    # ================================================================ M2
    dict(
        file="module-02-ado-work-tracking",
        day="Day 1", tier="Optional MVP Module", kicker="Module 02",
        title="Azure DevOps Work Tracking",
        theme=["kanban board with sticky notes",
               "agile sprint planning meeting",
               "project management dashboard on screen",
               "team standup meeting in office"],
        objectives=[
            "Model modernization work in an Agile hierarchy.",
            "Configure board, backlog, and sprint views.",
            "Connect work items to commits and pull requests.",
        ],
        narrative=["This module is useful for enterprise workflow alignment.",
                   "It is optional for MVP delivery where tenant or project provisioning "
                   "is not guaranteed."],
        focus=["ADO concepts", "Work item hierarchy", "Sprint flow"],
        diagram=dict(
            caption="The Agile process template's work item hierarchy, per Azure Boards documentation — each level rolls up into the one above it.",
            steps=[
                ("EPIC", "Large business scenario (portfolio-level)"),
                ("FEATURE", "Deliverable that supports the epic"),
                ("USER STORY", "Customer-valued requirement"),
                ("TASK", "Sprint-level unit of work"),
            ],
            icons=[icon_chart_up, icon_document, icon_person, icon_check],
        ),
        field_facts=dict(
            title="From the Docs: How Work Items Really Link",
            bullets=[
                "Agile hierarchy, top to bottom: Epic > Feature > User Story > Task, joined by parent-child links.",
                "Epics and Features are portfolio-level — they group work, they aren't used to track daily tasks.",
                "A Bug can be configured to live at the User Story level or the Task level, per team.",
                "Every work item's Development pane shows linked branches, commits, pull requests, and builds.",
                "Boards show Kanban-style status; Backlogs prioritize work; Sprints time-box it into iterations.",
            ],
            source=("About work items and work item types — Azure Boards",
                    "https://learn.microsoft.com/en-us/azure/devops/boards/work-items/about-work-items?view=azure-devops"),
        ),
        real_example=None,
        resources=[
            ("Lab Provisioning", "Azure DevOps Demo Generator (azuredevopsdemogenerator.azurewebsites.net)",
             "Auto-populates ADO with pre-configured Epics, User Stories, and Sprints."),
            ("Template", "Parts Unlimited or eShopOnWeb Demo Project Template",
             "Board configuration, backlog management, and sprint backlog tracking lab."),
            ("Documentation", "Azure Boards Documentation: Agile Planning and Portfolio Management",
             "Reference guide for team velocity tracking and dashboard queries."),
        ],
        assets=["ADO project template (if available)", "Reference context: course/repos/eShopOnWeb"],
        lab_name="Lab 02: ADO Work Tracking",
        lab_goal="Create the modernization board, backlog, and sprint traceability.",
        lab_env="Tools: browser · Requires an Azure DevOps org/project and assigned team members.",
        lab_steps=[
            "Step 1 — Create epics and features aligned to modernization goals.",
            "Step 2 — Add user stories, tasks, and bugs.",
            "Step 3 — Plan one sprint with capacity.",
            "Step 4 — Create dashboard queries and status widgets.",
            "Step 5 — Link work items to commits or pull requests.",
        ],
        lab_validation="Validation: the board hierarchy is complete, and queries/dashboards render live data.",
        quiz=dict(
            q="In Azure Boards' Agile work item hierarchy, which item type groups related user stories into a larger initiative?",
            options=["Sprint", "Epic", "Pull Request", "Backlog"],
            answer=1,
        ),
        quiz2=dict(
            q="Per Microsoft's own Azure Boards documentation, what does a work item's Development pane show?",
            options=["Only its due date", "Linked branches, commits, pull requests, and builds",
                     "A team velocity chart", "A sprint burndown chart"],
            answer=1,
        ),
        sources=dict(
            citations=[("About work items and work item types — Azure Boards",
                        "https://learn.microsoft.com/en-us/azure/devops/boards/work-items/about-work-items?view=azure-devops")],
            local_paths=["course/mvp-delivery/labs/lab-02-ado-work-tracking.md",
                         "course/design.md"],
        ),
        success="Work item hierarchy is complete and linked to source-control activity.",
    ),
    # ================================================================ M3
    dict(
        file="module-03-copilot-csharp",
        day="Day 1", tier="Core MVP Module", kicker="Module 03",
        title="Copilot-Assisted C# Development",
        theme=["developer using an AI code assistant",
               "GitHub Copilot code suggestion on screen",
               "programmer pair programming with AI",
               "C# code editor close up"],
        objectives=[
            "Use prompt patterns for targeted refactoring and test generation.",
            "Review AI-generated code for quality and security.",
            "Improve maintainability of a legacy C# component.",
        ],
        narrative=["This module converts theory into productivity by using Copilot against "
                   "a controlled code surface.",
                   "The focus is safe acceleration, not blind generation."],
        focus=["Prompting patterns", "Refactoring legacy code",
               "Generating tests and documentation", "Governance and safe usage"],
        diagram=dict(
            caption="The safe-acceleration loop this module teaches — Copilot proposes, a human always validates.",
            steps=[
                ("PROMPT", "Specific, scoped instruction with context"),
                ("SUGGESTION", "Copilot generates code inline or in chat"),
                ("HUMAN REVIEW", "Check correctness, security, readability"),
                ("ACCEPT / REVISE", "Merge only after validation"),
            ],
        ),
        field_facts=dict(
            title="From the Docs: GitHub's Own Best Practices",
            bullets=[
                "GitHub: break complex tasks into smaller, specific prompts for better suggestions.",
                "GitHub: be specific — provide example inputs, outputs, and implementations in the prompt.",
                "GitHub's own advice: ask Copilot Chat to explain a suggestion before you implement it.",
                "GitHub calls for manual review of AI code for functionality, security, readability, and maintainability.",
                "GitHub names writing tests and repetitive code as a core strength of Copilot suggestions.",
            ],
            source=("Best practices for using GitHub Copilot",
                    "https://docs.github.com/en/copilot/get-started/best-practices"),
        ),
        real_example=None,
        resources=[
            ("Workshop Repo", "microsoft/copilot-labs or microsoft/copilot-csharp-workshop",
             "Practice prompting strategies, unit test generation (MSTest/xUnit), and refactoring."),
            ("Learning Path", "Microsoft Learn: Develop with AI-powered code suggestions using GitHub Copilot",
             "Source material for prompt engineering and governance best practices."),
            ("IDE Plugins", "GitHub Copilot for Visual Studio / VS Code",
             "Developer desktop integration for writing unit tests and XML documentation."),
        ],
        assets=["Code target: course/repos/eShopOnWeb", "Optional examples: course/repos/samples"],
        lab_name="Lab 03: Copilot Refactor and Tests",
        lab_goal="Refactor one legacy component and generate useful tests with Copilot.",
        lab_env="Tools: VS Code or Visual Studio, .NET SDK, GitHub Copilot (license + sign-in required).",
        lab_steps=[
            "Step 1 — Select one target class with known complexity issues.",
            "Step 2 — Prompt Copilot for a refactor plan.",
            "Step 3 — Apply the refactor incrementally.",
            "Step 4 — Generate unit tests for happy-path and failure-path behavior.",
            "Step 5 — Run the tests and review generated code for quality and security.",
        ],
        lab_validation="Validation: the project compiles after refactor, and tests pass for the changed behavior.",
        quiz=dict(
            q="What is the recommended practice after GitHub Copilot generates a refactor or test?",
            options=["Merge immediately to save time",
                     "Review the output for correctness, security, and maintainability before accepting",
                     "Disable code review since AI output is always correct",
                     "Delete the original code without comparison"],
            answer=1,
        ),
        quiz2=dict(
            q="Per GitHub's own best practices, what should you do before implementing a Copilot suggestion you don't fully recognize?",
            options=["Merge it immediately", "Ask Copilot Chat to explain it and understand it first",
                     "Disable all linting", "Delete your original code"],
            answer=1,
        ),
        sources=dict(
            citations=[("Best practices for using GitHub Copilot",
                        "https://docs.github.com/en/copilot/get-started/best-practices")],
            local_paths=["course/mvp-delivery/labs/lab-03-copilot-refactor-and-tests.md",
                         "course/repos/eShopOnWeb"],
        ),
        success="Refactored code compiles, tests pass, and learner can explain the decisions made.",
    ),
    # ================================================================ M4
    dict(
        file="module-04-modern-dotnet-api",
        day="Day 1", tier="Core MVP Module", kicker="Module 04",
        title="Modern .NET API and Data Access",
        theme=["REST API code on a monitor",
               "database server room",
               "developer building a web API",
               "software architecture data flow diagram"],
        objectives=[
            "Build a modern API endpoint using current .NET patterns.",
            "Integrate data access through EF Core or Dapper.",
            "Implement robust validation and configuration handling.",
        ],
        narrative=["This module creates the first meaningful modernization increment.",
                   "It delivers a production-relevant API capability with data persistence "
                   "and test coverage."],
        focus=["Minimal APIs", "Dependency injection", "Configuration",
               "Async/await", "Data access"],
        diagram=dict(
            caption="The exact request path a Minimal API endpoint follows in eShopOnWeb's PublicApi project.",
            steps=[
                ("HTTP REQUEST", "GET /api/catalog-items/{id}"),
                ("MINIMAL API", "app.MapGet route handler"),
                ("REPOSITORY + EF CORE", "IRepository<CatalogItem> queries the DbContext"),
                ("SQL DATABASE", "Azure SQL / SQL Server LocalDB"),
                ("JSON RESPONSE", "Results.Ok(dto) or Results.NotFound()"),
            ],
        ),
        field_facts=dict(
            title="From the Docs: Why Minimal APIs",
            bullets=[
                "Microsoft recommends Minimal APIs over controller-based APIs for new ASP.NET Core projects.",
                "Minimal APIs build working REST endpoints with minimal code — no controller classes or scaffolding.",
                "Endpoints are defined with app.MapGet(), MapPost(), MapPut(), MapDelete() on the WebApplication instance.",
                "Route handlers can request services directly — ASP.NET Core resolves them from DI automatically.",
                "Dapper is a lightweight object mapper for raw SQL; EF Core is a full ORM with change tracking and migrations.",
            ],
            source=("APIs overview — ASP.NET Core",
                    "https://learn.microsoft.com/en-us/aspnet/core/fundamentals/apis"),
        ),
        real_example=dict(
            kind="code",
            slide_title="Real Endpoint — eShopOnWeb PublicApi",
            source_label="src/PublicApi/CatalogItemEndpoints/CatalogItemGetByIdEndpoint.cs",
            code_lines=[
                "public class CatalogItemGetByIdEndpoint",
                "    : IEndpoint<IResult, GetByIdCatalogItemRequest, IRepository<CatalogItem>>",
                "{",
                "    public void AddRoute(IEndpointRouteBuilder app)",
                "    {",
                "        app.MapGet(\"api/catalog-items/{catalogItemId}\",",
                "            async (int catalogItemId, IRepository<CatalogItem> itemRepository) =>",
                "            {",
                "                return await HandleAsync(",
                "                    new GetByIdCatalogItemRequest(catalogItemId), itemRepository);",
                "            })",
                "            .Produces<GetByIdCatalogItemResponse>()",
                "            .WithTags(\"CatalogItemEndpoints\");",
                "    }",
                "",
                "    // HandleAsync queries the repository, then returns",
                "    // Results.NotFound() or Results.Ok(response)",
                "}",
            ],
            note="This is the exact Minimal API + repository pattern Lab 04 extends with a new endpoint.",
        ),
        resources=[
            ("Sample Code", ".NET 8 / .NET 9 Web API Reference Samples (dotnet/samples)",
             "Template for Minimal APIs, Dependency Injection, and Async/Await."),
            ("ORM / Database", "Entity Framework Core & Dapper docs and code snippets",
             "Adding REST endpoints backed by Azure SQL / SQL Server LocalDB."),
            ("Security Guides", "Azure Key Vault references for ASP.NET Core",
             "Secrets management lab exercise."),
        ],
        assets=["App baseline: course/repos/eShopOnWeb", "Pattern references: course/repos/samples"],
        lab_name="Lab 04: Modern .NET API + SQL",
        lab_goal="Add a SQL-backed API endpoint and validate it end to end.",
        lab_env="Tools: .NET SDK, SQL tooling · Cloud: optional Azure SQL, otherwise local SQL.",
        lab_steps=[
            "Step 1 — Add a new API endpoint for a domain entity.",
            "Step 2 — Register services via dependency injection.",
            "Step 3 — Add EF Core or Dapper data access logic.",
            "Step 4 — Add configuration and secure secret handling.",
            "Step 5 — Add and run integration tests.",
        ],
        lab_validation="Validation: the endpoint returns expected codes/schema, and integration tests pass.",
        quiz=dict(
            q="Which two data-access approaches are named for connecting a modern .NET "
              "API to a database in this module?",
            options=["EF Core and Dapper", "jQuery and AJAX", "XML and SOAP", "FTP and SCP"],
            answer=0,
        ),
        quiz2=dict(
            q="Per Microsoft's own ASP.NET Core docs, which API style is now recommended for new projects?",
            options=["SOAP services", "Minimal APIs", "WCF", "Controller-based APIs only"],
            answer=1,
        ),
        sources=dict(
            citations=[("APIs overview — ASP.NET Core",
                        "https://learn.microsoft.com/en-us/aspnet/core/fundamentals/apis")],
            local_paths=["course/repos/eShopOnWeb/src/PublicApi/CatalogItemEndpoints/CatalogItemGetByIdEndpoint.cs",
                         "course/mvp-delivery/labs/lab-04-modern-dotnet-api-sql.md"],
        ),
        success="Endpoint passes functional and integration checks and follows secure config handling.",
    ),
    # ================================================================ M5
    dict(
        file="module-05-test-automation-tosca",
        day="Day 2", tier="Optional MVP Module", kicker="Module 05",
        title="Test Automation with Tosca",
        theme=["automated software testing dashboard",
               "QA tester reviewing test results",
               "software test automation concept",
               "quality assurance checklist on screen"],
        objectives=[
            "Understand model-based testing for API and UI validation.",
            "Organize execution lists and quality gates.",
            "Publish automated test results into delivery workflows.",
        ],
        narrative=["This module can be delivered as an optional hands-on track once Tosca "
                   "provisioning is complete.",
                   "Otherwise it runs as an instructor-led demo in MVP phase one."],
        focus=["Model-based testing", "Execution lists", "CI integration"],
        diagram=dict(
            caption="How a Tosca model-based test run actually moves from the app to a pipeline gate.",
            steps=[
                ("SCAN APP", "Tosca scans UI/API to build objects"),
                ("MODULES & TESTCASES", "Reusable Modules assembled into TestCases"),
                ("EXECUTION LIST", "Ordered list of TestCases to run"),
                ("CI/CD QUALITY GATE", "Pass/fail published back to the pipeline"),
            ],
        ),
        field_facts=dict(
            title="From the Docs: What Model-Based Testing Actually Means",
            bullets=[
                "Tosca scans an app's UI/API to build a codeless, business-readable automation model — not hand-written scripts.",
                "Tricentis's own framing: traditional scripted tools are technical and brittle; MBT decouples test logic from the model.",
                "Modules capture reusable app objects; updating one Module auto-syncs the change across every linked TestCase.",
                "TestCases are assembled from TestSteps (actions) and TestStepValues (data/verification points).",
                "Tosca Cloud connects to CI/CD tools like Jenkins via API to automate execution end to end.",
            ],
            source=("Tosca — Model-Based Test Automation",
                    "https://www.tricentis.com/products/automate-continuous-testing-tosca/model-based-test-automation"),
        ),
        real_example=None,
        resources=[
            ("Official Docs", "Tricentis Tosca Documentation: Model-Based Testing and ADO Integration",
             "Theoretical basis for MBT (Modules, TestCase Design, Execution Lists)."),
            ("CI/CD Plugin", "Tricentis Tosca Execution Task for Azure DevOps / GitHub Actions",
             "Integrating automated UI/API test runs directly into pipelines."),
            ("Target App", "Modernized REST API built in Module 4",
             "Live endpoint target for scanning UI and executing API test suites."),
        ],
        assets=["Target app from Module 4", "Tosca runtime and integration connectors"],
        lab_name="Lab 05: Test Automation Quality Gates",
        lab_goal="Build and run automation suites and define release quality gates.",
        lab_env="Tools: Tosca (installed and licensed) · Target app is the Lab 04 API.",
        lab_steps=[
            "Step 1 — Scan the target UI and API endpoints.",
            "Step 2 — Build smoke and regression suites.",
            "Step 3 — Execute test lists and capture results.",
            "Step 4 — Publish results to the pipeline or work tracking.",
            "Step 5 — Define pass/fail quality gate thresholds.",
        ],
        lab_validation="Validation: the automated suite executes successfully, and gate criteria are documented.",
        quiz=dict(
            q="What does model-based testing primarily rely on to design test cases?",
            options=["Random fuzzing of inputs",
                     "A model or representation of the application, rather than hand-scripted steps",
                     "Manual exploratory testing only",
                     "Production incident reports"],
            answer=1,
        ),
        quiz2=dict(
            q="In Tosca's model, what happens when you update one Module used across many TestCases?",
            options=["Nothing — each TestCase must be edited by hand",
                     "The change automatically syncs to every linked TestCase",
                     "All TestCases using it are deleted",
                     "Only the newest TestCase updates"],
            answer=1,
        ),
        sources=dict(
            citations=[("Tosca — Model-Based Test Automation",
                        "https://www.tricentis.com/products/automate-continuous-testing-tosca/model-based-test-automation")],
            local_paths=["course/mvp-delivery/labs/lab-05-test-automation-quality-gates.md"],
        ),
        success="Automated runs execute and publish actionable pass/fail results.",
    ),
    # ================================================================ M6
    dict(
        file="module-06-containerization",
        day="Day 2", tier="Core MVP Module", kicker="Module 06",
        title="Containerization with Docker",
        theme=["shipping containers stacked aerial view",
               "container ship at port concept",
               "server room technology concept",
               "developer building a container image in terminal"],
        objectives=[
            "Build and run .NET application images using multi-stage Dockerfiles.",
            "Validate health and runtime behavior in a containerized environment.",
            "Prepare images for registry and pipeline use.",
        ],
        narrative=["Containerization is the handoff boundary between development and "
                   "platform operations.",
                   "This module establishes that boundary using repeatable image build "
                   "practices."],
        focus=["Multi-stage builds", "Image management", "Local orchestration"],
        diagram=dict(
            caption="The exact two-stage build the eShopOnWeb Dockerfile uses to keep the shipped image small.",
            steps=[
                ("BUILD STAGE", "FROM dotnet/sdk:8.0 — full SDK"),
                ("DOTNET PUBLISH", "Compiles PublicApi.csproj to /app/publish"),
                ("COPY --from=publish", "Only the compiled output crosses over"),
                ("FINAL STAGE", "FROM dotnet/aspnet:8.0 — runtime only, no SDK"),
            ],
        ),
        field_facts=dict(
            title="From the Docs: Why Multi-Stage Builds",
            bullets=[
                "Docker's own goal for multi-stage builds: optimize image size while keeping Dockerfiles easy to read and maintain.",
                "Multi-stage builds selectively copy artifacts between stages, leaving build tools out of the final image.",
                "Docker's own description of the result: “a tiny production image with nothing but the binary inside.”",
                "Name a stage with FROM <image> AS <name>; pull from it later with COPY --from=<name>.",
                "COPY --from is reorder-safe — stages can be reordered later without breaking the copy.",
            ],
            source=("Multi-stage builds — Docker Docs",
                    "https://docs.docker.com/build/building/multi-stage/"),
        ),
        real_example=dict(
            kind="code",
            slide_title="Real Multi-Stage Dockerfile — eShopOnWeb",
            source_label="src/PublicApi/Dockerfile",
            code_lines=[
                "FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base",
                "WORKDIR /app",
                "EXPOSE 80",
                "EXPOSE 443",
                "",
                "FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build",
                "WORKDIR /app",
                "COPY . .",
                "WORKDIR \"/app/src/PublicApi\"",
                "RUN dotnet restore",
                "RUN dotnet build \"./PublicApi.csproj\" -c Release -o /app/build",
                "",
                "FROM build AS publish",
                "RUN dotnet publish \"./PublicApi.csproj\" -c Release -o /app/publish",
                "",
                "FROM base AS final",
                "WORKDIR /app",
                "COPY --from=publish /app/publish .",
                "ENTRYPOINT [\"dotnet\", \"PublicApi.dll\"]",
            ],
            note="Same FROM…AS / COPY --from pattern the Docker docs describe, in the app you'll containerize in Lab 06.",
        ),
        resources=[
            ("Official Repo", "dotnet/dotnet-docker (Official Microsoft .NET Docker Samples)",
             "Multi-stage Dockerfile templates for ASP.NET Core (Linux/Windows)."),
            ("Microsoft Learn", "Build and run a containerized web app with Docker and Azure Container Registry",
             "ACR registry setup, image building, tagging, and pushing."),
            ("Local Tooling", "Docker Desktop / Podman CLI & Docker Compose",
             "Multi-container local orchestration (App + SQL Server)."),
        ],
        assets=["App baseline: course/repos/eShopOnWeb", "Container examples: course/repos/samples"],
        lab_name="Lab 06: Containerization with Docker",
        lab_goal="Containerize the app and verify local runtime behavior.",
        lab_env="Tools: Docker or Podman, .NET SDK · Cloud: optional Azure Container Registry.",
        lab_steps=[
            "Step 1 — Create or update a multi-stage Dockerfile.",
            "Step 2 — Build the image locally.",
            "Step 3 — Run the container and test the health endpoint.",
            "Step 4 — Add or verify compose configuration if needed.",
            "Step 5 — Tag the image for pipeline or registry use.",
        ],
        lab_validation="Validation: the image builds successfully and the container responds to health checks.",
        quiz=dict(
            q="What is the main benefit of a multi-stage Dockerfile for a .NET application?",
            options=["It removes the need for a runtime environment",
                     "It builds the app in one stage and copies only the compiled output "
                     "into a smaller final runtime image",
                     "It automatically deploys the app to Kubernetes",
                     "It replaces the need for a database"],
            answer=1,
        ),
        quiz2=dict(
            q="In the eShopOnWeb Dockerfile, why does the final image use the aspnet:8.0 base instead of the sdk:8.0 image used to build it?",
            options=["aspnet is only faster to download", "The final stage only needs the runtime, not the full SDK, keeping the image smaller",
                     "sdk images can't run in containers", "There is no difference"],
            answer=1,
        ),
        sources=dict(
            citations=[("Multi-stage builds — Docker Docs",
                        "https://docs.docker.com/build/building/multi-stage/")],
            local_paths=["course/repos/eShopOnWeb/src/PublicApi/Dockerfile",
                         "course/repos/eShopOnWeb/docker-compose.yml"],
        ),
        success="Containerized app starts and serves expected responses.",
    ),
    # ================================================================ M7
    dict(
        file="module-07-kubernetes-openshift",
        day="Day 2", tier="Core MVP Module", kicker="Module 07",
        title="Kubernetes and OpenShift",
        theme=["cloud infrastructure network diagram",
               "data center server racks with blue light",
               "kubernetes cluster architecture concept",
               "engineer monitoring a cloud dashboard"],
        objectives=[
            "Deploy workloads to Kubernetes or OpenShift.",
            "Configure health probes, configuration objects, and scaling policy.",
            "Verify deployment health through route or ingress checks.",
        ],
        narrative=["This module operationalizes the container image by deploying it into "
                   "a managed cluster context.",
                   "Learners validate reliability behavior once the workload is running."],
        focus=["Kubernetes primitives", "OpenShift specifics", "Routes", "Probes", "Scaling"],
        diagram=dict(
            caption="What actually gates traffic to a newly deployed pod, per the Kubernetes docs.",
            steps=[
                ("DEPLOY POD", "Container scheduled onto the cluster"),
                ("READINESS PROBE", "Gates traffic until the app can serve it"),
                ("LIVENESS PROBE", "Restarts the container if it hangs"),
                ("ROUTE / INGRESS", "Exposes the healthy pod externally"),
                ("AUTOSCALE", "HPA adds/removes pods under load"),
            ],
        ),
        field_facts=dict(
            title="From the Docs: Probes, Precisely",
            bullets=[
                "Liveness probe: checks whether a container is still running correctly (e.g., not deadlocked).",
                "Liveness failure: once failures cross the threshold, the kubelet restarts the container.",
                "Readiness probe: checks whether a container is ready to accept traffic.",
                "Readiness failure: the Pod's IP is pulled from Service endpoints — traffic stops, container keeps running.",
                "OpenShift Routes add features plain Kubernetes Ingress lacks, e.g. TLS re-encryption and blue-green traffic splits.",
            ],
            source=("Liveness, Readiness, and Startup Probes — Kubernetes",
                    "https://kubernetes.io/docs/concepts/workloads/pods/probes/"),
        ),
        real_example=dict(
            kind="code",
            slide_title="Real Deploy Commands — s2i-dotnetcore-ex",
            source_label="README.adoc (Red Hat's official S2I .NET sample)",
            code_lines=[
                "$ oc new-project mydemo",
                "",
                "$ oc apply -f https://raw.githubusercontent.com/redhat-developer/",
                "     s2i-dotnetcore/main/dotnet_imagestreams.json",
                "",
                "$ oc new-app dotnet:10.0~https://github.com/redhat-developer/",
                "     s2i-dotnetcore-ex#dotnet-10.0 --context-dir app",
                "",
                "$ oc expose service s2i-dotnetcore-ex",
                "$ oc get route s2i-dotnetcore-ex",
            ],
            note="The exact source-to-image build-and-deploy flow Lab 07 follows against OpenShift.",
        ),
        resources=[
            ("Workshop Repo", "Azure-Samples/aro-eshop-workshop (Azure Red Hat OpenShift Workshop)",
             "Manifest files (.yaml), OpenShift Routes, DeploymentConfigs, and ImageStreams."),
            ("Sandbox Environment", "Red Hat Developer Sandbox for OpenShift",
             "Free 30-day cluster environment for students to deploy containerized workloads."),
            ("K8s Guides", "Kubernetes Documentation: ConfigMaps, Secrets, Probes, Autoscaling",
             "Configuring liveness/readiness probes, secrets, and autoscaling."),
        ],
        assets=["OpenShift sample: course/repos/s2i-dotnetcore-ex", "Container image from Module 6"],
        lab_name="Lab 07: Kubernetes and OpenShift",
        lab_goal="Deploy the containerized app to cluster infrastructure and validate reliability.",
        lab_env="Tools: kubectl or oc · Cluster: OpenShift, or AKS as a fallback.",
        lab_steps=[
            "Step 1 — Create a namespace and apply baseline manifests.",
            "Step 2 — Configure ConfigMaps and Secrets.",
            "Step 3 — Add readiness and liveness probes.",
            "Step 4 — Expose the service via route or ingress.",
            "Step 5 — Configure and test autoscaling.",
        ],
        lab_validation="Validation: pod/deployment health is green, the route is reachable, and autoscaling responds to load.",
        quiz=dict(
            q="What is the purpose of a Kubernetes readiness probe?",
            options=["To restart the container on a fixed schedule",
                     "To tell Kubernetes when a container is ready to accept traffic",
                     "To scan the container image for vulnerabilities",
                     "To assign the pod a static IP address"],
            answer=1,
        ),
        quiz2=dict(
            q="What happens specifically when a Kubernetes readiness probe fails?",
            options=["The container is immediately deleted",
                     "The pod's IP is removed from Service endpoints, but the container keeps running",
                     "The whole node is cordoned",
                     "Nothing happens"],
            answer=1,
        ),
        sources=dict(
            citations=[("Liveness, Readiness, and Startup Probes — Kubernetes",
                        "https://kubernetes.io/docs/concepts/workloads/pods/probes/")],
            local_paths=["course/repos/s2i-dotnetcore-ex/README.adoc",
                         "course/mvp-delivery/labs/lab-07-kubernetes-openshift.md"],
        ),
        success="Workload is reachable and healthy, and can scale under load.",
    ),
    # ================================================================ M8
    dict(
        file="module-08-cicd-github-actions",
        day="Day 2", tier="Core MVP Module", kicker="Module 08",
        title="CI/CD with GitHub Actions",
        theme=["CI CD pipeline automation concept",
               "GitHub Actions workflow on screen",
               "automated deployment pipeline diagram",
               "developer pushing code to a repository"],
        objectives=[
            "Build a workflow that compiles, tests, and packages the application.",
            "Enforce quality gates before deployment.",
            "Produce traceable CI/CD evidence from commit to deploy.",
        ],
        narrative=["This module connects all prior modules into a delivery pipeline.",
                   "Automated checks and deployment orchestration tie the toolchain together."],
        focus=["Workflow structure", "Test gates", "Container publish", "Deployment automation"],
        diagram=dict(
            caption="Where eShopOnWeb's real workflow stops today, and the two stages Lab 08 adds.",
            steps=[
                ("PUSH / PULL REQUEST", "on: push/pull_request triggers the workflow"),
                ("BUILD + TEST JOB", "setup-dotnet → dotnet build → dotnet test"),
                ("CONTAINER PUBLISH", "docker/build-push-action builds & pushes the image"),
                ("DEPLOY JOB", "Rolls the image out to the target environment"),
                ("QUALITY GATE", "Required status check blocks merge on failure"),
            ],
        ),
        field_facts=dict(
            title="From the Docs: What a Quality Gate Actually Is",
            bullets=[
                "Workflows group work into jobs, and each job runs an ordered sequence of steps.",
                "actions/setup-dotnet finds a .NET version in the runner's tool cache and adds it to PATH.",
                "GitHub calls setup-dotnet the recommended way to get consistent .NET behavior across runners.",
                "A typical .NET CI job: dotnet restore, dotnet build --no-restore, dotnet test --no-build.",
                "Required status checks must pass before collaborators can merge into a protected branch.",
            ],
            source=("Building and testing .NET — GitHub Docs",
                    "https://docs.github.com/actions/guides/building-and-testing-net"),
        ),
        real_example=dict(
            kind="code",
            slide_title="Real Workflow (Today) — eShopOnWeb",
            source_label=".github/workflows/dotnetcore.yml",
            code_lines=[
                "name: eShopOnWeb Build and Test",
                "",
                "on: [push, pull_request, workflow_dispatch]",
                "",
                "jobs:",
                "  build:",
                "    runs-on: ubuntu-latest",
                "    steps:",
                "    - uses: actions/checkout@v2",
                "    - name: Setup .NET",
                "      uses: actions/setup-dotnet@v1",
                "      with:",
                "        dotnet-version: '8.0.x'",
                "    - name: Build with dotnet",
                "      run: dotnet build ./eShopOnWeb.sln --configuration Release",
                "    - name: Test with dotnet",
                "      run: dotnet test ./eShopOnWeb.sln --configuration Release",
            ],
            note="Build+test only, today. Lab 08 extends this exact file with a container-publish and deploy job.",
        ),
        resources=[
            ("GitHub Actions", "dotnet/setup-dotnet, docker/build-push-action, redhat-actions/oc-login",
             "Modular pipeline steps for building, packaging, and deploying."),
            ("Lab Guide", "Microsoft Learn: AZ-400 Implement CI/CD with GitHub Actions and Azure",
             "Building end-to-end automation triggers and pipeline quality gates."),
            ("Sample Pipeline", ".github/workflows/deploy.yml from the eShopOnWeb repo",
             "Working reference workflow for container builds and deployment."),
        ],
        assets=["App repo from Modules 3 to 7", "Pipeline references from existing GitHub workflow patterns"],
        lab_name="Lab 08: CI/CD with GitHub Actions",
        lab_goal="Create a working build-test-deploy workflow with quality gates.",
        lab_env="Tools: Git, GitHub Actions · Requires GitHub secrets for registry/deploy targets.",
        lab_steps=[
            "Step 1 — Add workflow triggers for push and pull request.",
            "Step 2 — Add build and test jobs.",
            "Step 3 — Add a container build and publish stage.",
            "Step 4 — Add a deployment job and environment guardrails.",
            "Step 5 — Enforce test and coverage quality gates.",
        ],
        lab_validation="Validation: the workflow executes end to end, and failed tests block the deploy stage.",
        quiz=dict(
            q="In a CI/CD pipeline, what is a quality gate?",
            options=["A firewall rule",
                     "A required check, such as passing tests, that must succeed before code "
                     "proceeds to the next stage",
                     "A type of Docker base image",
                     "A GitHub repository naming setting"],
            answer=1,
        ),
        quiz2=dict(
            q="Per GitHub's own docs, what must happen before collaborators can merge into a protected branch?",
            options=["Nothing is required", "Required status checks must pass",
                     "The repo must be archived", "Actions must be disabled"],
            answer=1,
        ),
        sources=dict(
            citations=[("Building and testing .NET — GitHub Docs",
                        "https://docs.github.com/actions/guides/building-and-testing-net")],
            local_paths=["course/repos/eShopOnWeb/.github/workflows/dotnetcore.yml",
                         "course/mvp-delivery/labs/lab-08-cicd-github-actions.md"],
        ),
        success="Pipeline executes end to end and blocks failing quality checks.",
    ),
    # ================================================================ M9
    dict(
        file="module-09-azure-operations",
        day="Day 2", tier="Optional MVP Module", kicker="Module 09",
        title="Azure Deployment and Operations",
        theme=["Azure cloud dashboard on a monitor",
               "cloud computing data center",
               "IT operations monitoring wall of screens",
               "cloud security and identity concept"],
        objectives=[
            "Provision Azure resources with repeatable templates.",
            "Configure identity, monitoring, and alerting.",
            "Validate runtime telemetry and operational readiness.",
        ],
        narrative=["This module extends the core track into cloud operations.",
                   "It is optional for MVP delivery when quota or tenant constraints are present."],
        focus=["Azure hosting options", "Identity", "Observability", "Bicep", "Costs"],
        diagram=dict(
            caption="How eShopOnWeb's own infra/main.bicep turns into a running, observable environment.",
            steps=[
                ("BICEP (IaC)", "Declarative main.bicep defines the environment"),
                ("AZURE RESOURCES", "App Service, Key Vault, Azure SQL provisioned"),
                ("APPLICATION INSIGHTS", "Requests, dependencies, exceptions telemetry"),
                ("ALERTS", "Actionable signals on top of the telemetry"),
            ],
        ),
        field_facts=dict(
            title="From the Docs: Bicep, Precisely",
            bullets=[
                "Bicep is a declarative domain-specific language for deploying Azure resources.",
                "Bicep is a transparent abstraction over ARM JSON — the Bicep CLI transpiles it to ARM at deployment.",
                "Benefit Microsoft states: Bicep files are more concise and easier to read than the equivalent ARM JSON.",
                "Benefit Microsoft states: Bicep gets day-one support for new/preview Azure resource types.",
                "Benefit Microsoft states: no state files to manage — Azure itself stores deployment state.",
            ],
            source=("What is Bicep? — Azure Resource Manager",
                    "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview"),
        ),
        real_example=dict(
            kind="code",
            slide_title="Real IaC — eShopOnWeb infra/main.bicep",
            source_label="infra/main.bicep (excerpt)",
            code_lines=[
                "targetScope = 'subscription'",
                "",
                "param environmentName string",
                "param location string",
                "",
                "@secure()",
                "param sqlAdminPassword string",
                "",
                "resource rg 'Microsoft.Resources/resourceGroups@2021-04-01' = {",
                "  name: !empty(resourceGroupName) ? resourceGroupName",
                "    : '${abbrs.resourcesResourceGroups}${environmentName}'",
                "  location: location",
                "  tags: tags",
                "}",
                "",
                "module web './core/host/appservice.bicep' = {",
                "  name: 'web'",
                "  scope: rg",
                "  params: { runtimeName: 'dotnetcore', runtimeVersion: '8.0' }",
                "}",
            ],
            note="Provisions the App Service, Key Vault, and two Azure SQL databases this module's lab deploys.",
        ),
        resources=[
            ("IaC Templates", "Azure Quickstart Templates / Bicep files (Azure/azure-quickstart-templates)",
             "Infrastructure as Code deployment for App Service, AKS, and Azure SQL."),
            ("Monitoring Docs", "Microsoft Learn: Monitor application performance with Application Insights",
             "Telemetry, logging, and SLA dashboard setup."),
            ("Migration Guides", "Azure SQL Database Migration Guides (Data Migration Assistant / Azure Migrate)",
             "Database migration hands-on reference."),
        ],
        assets=["Azure templates and scripts from local references", "App artifacts from prior modules"],
        lab_name="Lab 09: Azure Deployment and Operations",
        lab_goal="Deploy to Azure and establish baseline observability.",
        lab_env="Tools: Azure CLI, Bicep · Requires an Azure subscription with quota.",
        lab_steps=[
            "Step 1 — Deploy core resources from templates.",
            "Step 2 — Deploy the app artifact.",
            "Step 3 — Configure identity and secret access.",
            "Step 4 — Enable logs, metrics, and alerts.",
            "Step 5 — Validate app and telemetry behavior.",
        ],
        lab_validation="Validation: deployment succeeds without manual rework, and monitoring/alerts show active signals.",
        quiz=dict(
            q="Which Azure capability is used to write infrastructure as repeatable, "
              "version-controlled templates?",
            options=["Azure Bicep", "Azure Front Door", "Azure DevTest Labs", "Azure Cost Management"],
            answer=0,
        ),
        quiz2=dict(
            q="Per Microsoft's own docs, what does the Bicep CLI do with a .bicep file at deployment time?",
            options=["Executes it directly as PowerShell", "Transpiles it into an ARM JSON template",
                     "Converts it to Terraform", "Nothing — no conversion happens"],
            answer=1,
        ),
        sources=dict(
            citations=[("What is Bicep? — Azure Resource Manager",
                        "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview")],
            local_paths=["course/repos/eShopOnWeb/infra/main.bicep",
                         "course/repos/eShopOnWeb/azure.yaml"],
        ),
        success="Workload is deployed and observable with actionable alerts.",
    ),
    # ================================================================ M10
    dict(
        file="module-10-capstone",
        day="Day 2", tier="Optional or Stretch for MVP", kicker="Module 10",
        title="Capstone: End-to-End Modernization",
        theme=["software development team celebrating success",
               "team high five in an office",
               "project completion presentation meeting",
               "diverse tech team collaborating around a laptop"],
        objectives=[
            "Execute a full modernization flow as a coordinated team.",
            "Demonstrate planning, coding, deployment, and operational validation.",
            "Produce a delivery narrative and lessons learned.",
        ],
        narrative=["The capstone is a synthesis module.",
                   "In MVP phase one, it should be used only once the core six modules "
                   "run cleanly with no unresolved provisioning issues."],
        focus=["Combine the full toolchain into a team delivery flow"],
        diagram=dict(
            caption="Every prior module converges into one traceable, deployed increment.",
            kind="converge",
            steps=["Plan\n(M1–M2)", "Build\n(M3–M4)", "Test\n(M5)",
                   "Containerize\n(M6)", "Deploy\n(M7, M9)", "Automate\n(M8)"],
            bottom=("CAPSTONE DELIVERY", "One traceable, tested, deployed modernization increment"),
        ),
        field_facts=dict(
            title="What Ties It Together",
            bullets=[
                "Rearchitect vs. rehost is the vocabulary the team's plan is judged against (Module 1, Microsoft CAF).",
                "The Epic → Feature → Story → Task hierarchy is how the team's slice gets scoped (Module 2, Azure Boards).",
                "Readiness probes gate live traffic to whatever the team deploys (Module 7, Kubernetes docs).",
                "A required status check is the safety net that blocks a broken build from shipping (Module 8, GitHub Docs).",
                "Bicep provisions the target environment the team's demo actually runs in (Module 9, Microsoft Learn).",
            ],
            source=("See Modules 1–9 for the full external source list", ""),
        ),
        real_example=dict(
            kind="quote",
            slide_title="What “Done” Looks Like",
            bullets=[
                "“The capstone is a synthesis module” — it doesn't teach new tools, it proves the prior nine work together.",
                "Combined artifacts required from Modules 1, 3, 4, 6, 7, and 8; optional artifacts from Modules 2, 5, and 9.",
                "MVP guidance: defer the capstone to release 2 until the core six modules run cleanly end to end.",
            ],
            source_note="Source: course/mvp-delivery/modules/module-10-capstone.md",
        ),
        resources=[
            ("Master Architecture", "dotnet-architecture/eShopOnWeb or dotnet/eShop",
             "Final repository for end-to-end modernized delivery."),
            ("Integrated Stack", "Combined Module 2 ADO board + GitHub Actions + Red Hat "
             "OpenShift + Azure App Insights",
             "Final student team challenge and debrief roadmap."),
        ],
        assets=["Combined artifacts from Modules 1, 3, 4, 6, 7, and 8",
                "Optional artifacts from Modules 2, 5, and 9"],
        lab_name="Lab 10: Capstone End-to-End",
        lab_goal="Execute a full modernization slice from planning through deployment verification.",
        lab_env="Requires: Modules 1, 3, 4, 6, 7, and 8 completed, with team roles assigned.",
        lab_steps=[
            "Step 1 — Define acceptance criteria and the sprint slice.",
            "Step 2 — Implement the selected modernization changes.",
            "Step 3 — Build and test through the CI pipeline.",
            "Step 4 — Deploy to the target environment.",
            "Step 5 — Validate operations and present outcomes.",
        ],
        lab_validation="Validation: acceptance criteria are met, with complete pipeline and deployment evidence.",
        quiz=dict(
            q="What is the primary goal of a capstone module in a technical training course?",
            options=["Introduce entirely new tools that were not covered before",
                     "Let learners apply and integrate everything they learned in an "
                     "end-to-end, team-based scenario",
                     "Replace all of the prior labs",
                     "Test typing speed"],
            answer=1,
        ),
        quiz2=dict(
            q="Which delivery mechanic from Module 8 acts as the safety net that blocks a broken capstone build from shipping?",
            options=["Manually emailing the team", "A required status check / quality gate in the CI/CD pipeline",
                     "Deleting the failing tests", "Skipping code review"],
            answer=1,
        ),
        sources=dict(
            citations=[("(Synthesis module — see Modules 1–9 for full external citations)", "")],
            local_paths=["course/mvp-delivery/modules/module-10-capstone.md",
                         "course/mvp-delivery/labs/lab-10-capstone-end-to-end.md"],
        ),
        success="Team demonstrates a traceable, tested, deployed modernization increment.",
    ),
]


def mod_num(mod):
    return mod["file"].split("-")[1]


def slot_img(mod, slot):
    return img(f"m{mod_num(mod)}_{slot}")


def render_real_example(c, page, mod):
    ex = mod["real_example"]
    if ex["kind"] == "code":
        code_slide(c, page, ex["slide_title"], mod["kicker"], ex["source_label"],
                   ex["code_lines"], note=ex.get("note"))
    else:
        bullet_slide(c, page, ex["slide_title"], mod["kicker"], ex["bullets"],
                     slot_img(mod, "real"), source_note=ex.get("source_note"))


def build_module_pdf(mod):
    path = os.path.join(OUT_DIR, mod["file"] + ".pdf")
    c = canvas.Canvas(path, pagesize=(PAGE_W, PAGE_H))
    page = 1

    subtitle = f"{mod['day']} · {mod['tier']}"
    title_slide(c, page, mod["kicker"], mod["title"], subtitle, slot_img(mod, "title"))
    page += 1

    bullet_slide(c, page, "Learning Objectives", mod["kicker"], mod["objectives"],
                 slot_img(mod, "objectives"))
    page += 1

    bullet_slide(c, page, "Why This Module Matters", mod["kicker"], [],
                 slot_img(mod, "why"), intro=mod["narrative"])
    page += 1

    d = mod["diagram"]
    diagram_slide(c, page, "Concept Map", mod["kicker"], d["caption"], d["steps"],
                  kind=d.get("kind", "flow"), bottom=d.get("bottom"), icons=d.get("icons"))
    page += 1

    ff = mod["field_facts"]
    src_note = f"Source: {ff['source'][0]}" + (f" — {ff['source'][1]}" if ff['source'][1] else "")
    bullet_slide(c, page, ff["title"], mod["kicker"], ff["bullets"],
                 slot_img(mod, "facts"), source_note=src_note)
    page += 1

    bullet_slide(c, page, "Courseware Focus", mod["kicker"], mod["focus"],
                 slot_img(mod, "focus"))
    page += 1

    if mod.get("real_example"):
        render_real_example(c, page, mod)
        page += 1

    cards_slide(c, page, "Tools & Resources", mod["kicker"], mod["resources"])
    page += 1

    bullet_slide(c, page, "Supporting Assets", mod["kicker"], mod["assets"],
                 slot_img(mod, "assets"))
    page += 1

    section_slide(c, page, mod["kicker"], mod["lab_name"], slot_img(mod, "labdiv"))
    page += 1

    lab_bullets = list(mod["lab_steps"]) + [mod["lab_validation"]]
    bullet_slide(c, page, "Lab Steps", mod["kicker"], lab_bullets,
                 slot_img(mod, "labsteps"),
                 intro=[f"Goal: {mod['lab_goal']}", mod["lab_env"]])
    page += 1

    q1 = mod["quiz"]
    quiz_slide(c, page, mod["title"], q1["q"], q1["options"], slot_img(mod, "quiz1"))
    page += 1
    quiz_slide(c, page, mod["title"], q1["q"], q1["options"],
               slot_img(mod, "quiz1"), reveal_index=q1["answer"])
    page += 1

    q2 = mod["quiz2"]
    quiz_slide(c, page, mod["title"], q2["q"], q2["options"], slot_img(mod, "quiz2"))
    page += 1
    quiz_slide(c, page, mod["title"], q2["q"], q2["options"],
               slot_img(mod, "quiz2"), reveal_index=q2["answer"])
    page += 1

    src = mod["sources"]
    citations = [c2 for c2 in src["citations"] if c2[1]]
    sources_slide(c, page, "Sources & Further Reading", mod["kicker"], citations, src["local_paths"])
    page += 1

    bullet_slide(c, page, "Recap & Success Criteria", mod["kicker"],
                 [mod["success"], f"Tier: {mod['tier']}"],
                 slot_img(mod, "recap"))
    page += 1

    c.save()
    return path, page - 1


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    results = []
    for mod in MODULES:
        path, n = build_module_pdf(mod)
        results.append((path, n))
        print(f"Wrote {path} ({n} pages)")
    print(f"\nDone: {len(results)} PDFs, {sum(n for _, n in results)} total pages")
