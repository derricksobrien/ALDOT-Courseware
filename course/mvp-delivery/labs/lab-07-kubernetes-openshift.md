# Lab 07: Kubernetes and OpenShift Deployment

## Module
Module 07 - Kubernetes and OpenShift

## Tier
Core MVP Lab

## Goal
Deploy the containerized app to cluster infrastructure and validate reliability.

## Prerequisites

- Cluster access available (OpenShift or AKS fallback)
- Image from Lab 06 available
- `kubectl` or `oc` installed

## Steps

1. Create namespace and apply baseline manifests.
2. Configure ConfigMaps and Secrets.
3. Add readiness and liveness probes.
4. Expose service via route or ingress.
5. Configure and test autoscaling.

## Validation

- Pod and deployment health are green.
- Route/ingress is reachable.
- Autoscaling responds to load.

## Evidence

- Deployment status output
- Route URL response proof
- HPA status output
