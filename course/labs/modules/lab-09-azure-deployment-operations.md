# Lab 09: Azure Deployment and Operations

## Module Alignment
Module 9: Azure Cloud Deployment and Operations

## Timebox
90 minutes

## Objectives
- Provision cloud resources using Infrastructure as Code.
- Deploy app and database workloads to Azure.
- Enable monitoring and operational dashboards.

## Prerequisites
- Azure subscription with contributor or owner permissions that can create role assignments.
- Access to Bicep templates and deployment scripts.
- If the training role only grants Contributor access, skip the Key Vault role-assignment step and document the prerequisite gap.

## Step-by-Step
1. Select target hosting model (App Service, AKS, or Container Apps).
2. Deploy baseline resources using Bicep templates.
3. Deploy application image and configure environment settings.
4. Provision or migrate to Azure SQL and update connection settings.
5. Enable managed identity and role assignments; if role assignment creation is blocked by RBAC, document the gap and continue with the rest of the deployment.
6. Enable Application Insights and Log Analytics.
7. Create alerts for error rate, latency, and resource saturation.
8. Build an operations dashboard and define SLOs.

## Validation Checks
- Infrastructure deployment completes without manual portal edits.
- Application and database connectivity is healthy.
- Telemetry and alerts are firing as expected.

## Deliverables
- Bicep deployment parameter file.
- Operations dashboard screenshots.
- SLO and alert policy document.

## Stretch Goals
- Add cost controls with tags, budgets, and rightsizing recommendations.
