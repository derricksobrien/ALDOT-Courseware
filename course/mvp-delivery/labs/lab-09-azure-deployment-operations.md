# Lab 09: Azure Deployment and Operations

## Module
Module 09 - Azure Deployment and Operations

## Tier
Optional MVP Lab

## Goal
Deploy to Azure and establish baseline observability.

## Prerequisites

- Azure subscription and quota
- Contributor or Owner access that can create role assignments
- Deployment templates and parameter files ready
- App artifact available
- If the role only grants Contributor, skip any Key Vault role-assignment step and document the access gap

## VM Fallback Scope Clarification

The Ubuntu VM helps with runtime hosting fallback, but does not replace core Lab 09 Azure operations outcomes.

- Useful fallback: run app on `vm-ubuntu-sdm-2026-aug10` if App Service deployment blocks progress
- Still required: observability evidence, alerting design, and documented Azure operations workflow
- Document any deviation from App Service/ACA/AKS as a temporary MVP fallback
 
## Step-by-Step

1. Select a target hosting model: App Service, AKS, or Container Apps.
2. Deploy baseline Azure resources from Bicep templates.
3. Deploy the app artifact and configure environment settings.
4. Provision or migrate the database target and update connection settings.
5. Enable managed identity and role assignments; document any RBAC gap if role assignment creation is blocked.
6. Enable Application Insights and Log Analytics.
7. Create alerts for error rate, latency, and resource saturation.
8. Build an operations dashboard and define SLOs.

9. If using VM fallback, capture VM deployment evidence and map monitoring equivalents.

## Validation

- Infrastructure deployment completes without manual portal edits.
- Application and database connectivity is healthy.
- Monitoring and alerts show active signals.
- An SLO or alert policy is documented.

## Evidence

- Bicep parameter file or deployment output
- Dashboard screenshots
- Alert rule proof
- If VM fallback is used: SSH/deployment output plus fallback rationale note
