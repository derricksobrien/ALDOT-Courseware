# Lab 07: Kubernetes and OpenShift Deployment

## Module Alignment
Module 7: Kubernetes and OpenShift

## Timebox
90 minutes

## Objectives
- Deploy containerized .NET workloads to Kubernetes or OpenShift.
- Configure environment, secrets, probes, and autoscaling.
- Validate reliability through rolling updates.

## Prerequisites
- Access to OpenShift cluster (ARO or sandbox) or AKS for fallback.
- Container image available in registry.
- Optional baseline sample in `course/repos/s2i-dotnetcore-ex`.

## Step-by-Step
1. Create namespace and RBAC bindings for the team.
2. Apply deployment and service manifests.
3. Configure ConfigMaps and Secrets for app settings.
4. Add readiness and liveness probes.
5. Expose service with OpenShift Route or Kubernetes Ingress.
6. Configure HPA based on CPU or request rate.
7. Perform rolling update and observe zero-downtime behavior.

## Validation Checks
- Pod health checks pass.
- External route/ingress serves traffic.
- Autoscaling triggers under load test.

## Deliverables
- Manifest or helm/kustomize package.
- Cluster validation screenshots.
- Deployment runbook notes.

## Stretch Goals
- Add PodDisruptionBudget and anti-affinity policies.

## Note on Source Repo
If the original `aro-eshop-workshop` repository URL has changed, use `s2i-dotnetcore-ex` or another maintained OpenShift .NET sample and adapt the manifest structure to keep objectives unchanged.
