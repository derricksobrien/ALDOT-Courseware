# MVP Delta Outline

This document describes what changes from the full course plan to the MVP course so the team can work quickly without losing the course story.

## What Stays the Same

- The course still covers modernization from planning to delivery.
- The same reference app family is used across the course.
- The same lab-first structure is preserved.
- The same sample courseware tone is used: short narrative, then hands-on steps.
- The web app still exposes the course content and lab pages.

## What Changes for MVP

### Content Scope Changes

| Full Course Item | MVP Change | Reason |
|---|---|---|
| Module 2 - Azure DevOps work tracking | Reduce to optional/instructor-led | Too much tenant and template setup for the first release |
| Module 5 - Tosca automation | Reduce to optional/demo-only | Licensing and runner setup are high-risk |
| Module 9 - Azure deployment and operations | Move to advanced track | Cloud quota and service dependencies slow delivery |
| Module 10 - Capstone | Defer | Depends on the modules we are simplifying first |
| Heavy courseware theory | Shorten | Keep the PDF readable and actionable |
| Multiple infrastructure paths | Standardize | Reduce learner confusion and support load |

### Lab Design Changes

| Full Course Lab Pattern | MVP Pattern | Result |
|---|---|---|
| Many tool-specific branches | One standard branch per core module | Easier reset and support |
| Multiple deployment targets in the same lab | One primary target plus one fallback | Lower friction on delivery day |
| Mixed local/cloud setup in the same lab | Local first, cloud optional for advanced steps | Faster learner progress |
| Broad lab instructions | Tighter step-by-step action blocks | Less room for ambiguity |
| Dense background theory inside labs | Move theory to courseware PDF | Cleaner lab execution |

### Repository Usage Changes

| Repo | Full Course Use | MVP Use |
|---|---|---|
| `eShopOnWeb` | Main reference app | Primary MVP source for Modules 1, 3, 4, 6, 8 |
| `eShop` | Optional advanced/microservices path | Keep as stretch material |
| `samples` | Reference snippets and examples | Source for .NET patterns and starter code |
| `s2i-dotnetcore-ex` | OpenShift workshop baseline | Primary fallback for Module 7 |

## Delta by Module

### Module 1

- Keep the full modernization overview.
- Trim any extra strategy theory that is not needed for lab execution.
- Add a direct reference to the shared baseline repo.

### Module 2

- Convert from full hands-on ADO implementation to optional planning content.
- If ADO is not ready, replace the lab with a local backlog template exercise.

### Module 3

- Keep the Copilot refactor and testing story.
- Narrow the code target so every learner can complete the same path.

### Module 4

- Keep the REST and data-access lab.
- Simplify the data layer for MVP if Azure SQL is not ready.

### Module 5

- Keep the concept section.
- Replace or defer the Tosca hands-on path unless the licensing and infrastructure are already proven.

### Module 6

- Keep the Docker lab.
- Standardize on one runtime and one image path.

### Module 7

- Keep the Kubernetes/OpenShift lab.
- Use one cluster path and one fallback sample repo.

### Module 8

- Keep the GitHub Actions pipeline lab.
- Reduce the workflow to build, test, containerize, and deploy.

### Module 9

- Convert to optional advanced material.
- Keep the Azure observability story for the next release.

### Module 10

- Defer the full capstone.
- Reintroduce it only after the core modules pass e2e validation.

## Courseware Delta

The PDF courseware should change in these ways for MVP:

1. Shorter module introductions.
2. Fewer reference diagrams per module.
3. One primary lab entry point per module.
4. More explicit success criteria.
5. More visible callouts for what is optional or deferred.

## Delivery Delta

For MVP delivery day:

- Run the core six labs end to end in a clean environment.
- Treat Modules 2, 5, 9, and 10 as optional if access exists.
- Keep one instructor recovery path per core lab.
- Require a final smoke test before every session starts.

## Summary of the MVP Shift

The full course becomes a phase-1 MVP by focusing on the parts that are most reliable to execute and easiest to validate:

- Modernization overview
- Copilot-assisted C# changes
- .NET API and data access
- Docker/containerization
- Kubernetes/OpenShift deployment
- GitHub Actions automation

Everything else remains valuable, but it moves to a second release or an optional track so the first version can ship quickly and cleanly.