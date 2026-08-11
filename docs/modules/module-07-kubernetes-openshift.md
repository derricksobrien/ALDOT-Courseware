---
layout: default
title: "Module 07 — Kubernetes and OpenShift"
parent: Modules
nav_order: 7
---

# Module 07 Courseware: Kubernetes and OpenShift

## Tier
Core MVP Module

## Learning Objectives

- Deploy workloads to Kubernetes or OpenShift.
- Configure health probes, configuration objects, and scaling policy.
- Verify deployment health through route or ingress checks.

## Narrative

This module operationalizes the container image by deploying it into a managed cluster context and validating reliability behavior.

## Supporting Assets

- OpenShift sample: `course/repos/s2i-dotnetcore-ex`
- Container image from Module 6

## Lab Alignment

- Matching lab: `mvp-delivery/labs/lab-07-kubernetes-openshift.md`
- Required output: deployment status, route URL, scaling evidence

## Success Criteria

- Workload is reachable and healthy, and can scale under load.

## Further Reading

- [Liveness, Readiness, and Startup Probes — Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/probes/)
