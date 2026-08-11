# Lab 07: Kubernetes and OpenShift Deployment — Visual Walkthrough

**Course:** Software Development Modernization  
**Module:** 07 — Kubernetes and OpenShift  
**Cluster path shown:** Red Hat Developer Sandbox (OpenShift) with AKS/Azure fallback notes  
**Screenshots taken:** 2026-08-10/11 across live course site, Red Hat, GitHub, Kubernetes docs, and Azure  
**Audience:** Students using this as a step-by-step guide or instructor reference  
**Tier:** Core MVP Lab

---

> **How to use this document**  
> This walkthrough follows the same pattern as Labs 05 and 06: each key screen is paired with what to do, what to look for, and why it matters in modernization delivery.  
> Use the command blocks exactly as shown, then capture your own evidence for validation.

---

## Why This Lab Matters — App Modernization Context

Lab 06 produced a deployable container image. Lab 07 is where you prove that image runs reliably in real cluster operations.

This matters for three reasons:

1. **Cluster deployment is the operational handoff point.** Your app moves from developer runtime to platform runtime (OpenShift/Kubernetes).
2. **Health probes and config objects make services resilient.** Liveness/readiness checks, ConfigMaps, and Secrets are core reliability controls.
3. **Autoscaling validates cloud-native behavior.** The app should scale with load rather than requiring manual infrastructure intervention.

> **Key concept:** Containerization alone is not modernization completion. Cluster runtime validation (health, routing, scaling) is required for production-readiness.

---

## What You Will Build

By the end of this lab you will have:

| Artifact | What it is | Where it lives |
|---|---|---|
| Cluster deployment | Running app deployment in OpenShift/Kubernetes | Namespace/project |
| Route or ingress | External endpoint for the app | OpenShift Route / K8s Ingress |
| ConfigMap + Secret wiring | Runtime config and secret separation | Cluster objects |
| Probe-enabled workload | Readiness/liveness health checks | Deployment manifest |
| HPA policy | CPU-driven autoscaling | HorizontalPodAutoscaler |
| Evidence package | Route output, pod health, HPA status | Lab submission |

---

## Prerequisites

| Item | How to verify |
|---|---|
| Image from Lab 06 | Container image reference is available |
| Cluster access | `oc whoami` or `kubectl auth can-i get pods` works |
| CLI installed | `oc version` or `kubectl version --client` |
| Starter source/manifests | Access to `redhat-developer/s2i-dotnetcore-ex` |

---

## Part 1 — Confirm Lab 07 Scope in the Course Site

![Course labs index showing Lab 07: Kubernetes and OpenShift Deployment card](lab-07-screenshots/ss01-course-labs-lab7-card.png)

**What you are looking at:**  
The course labs index with the Lab 07 card and objective summary. This aligns lab tasks to the modernization sequence.

**Lab outcome focus:**
- Deploy containerized workload
- Configure health and runtime settings
- Expose and validate endpoint
- Prove autoscaling behavior

---

## Part 2 — Access OpenShift / Sandbox Login Path

![Red Hat IDP login page used for OpenShift Developer Sandbox authentication](lab-07-screenshots/ss02-redhat-idp-login.png)

**What you are looking at:**  
The Red Hat identity provider sign-in flow used by the OpenShift Developer Sandbox.

**Why this matters:**  
For cohorts without a pre-provisioned enterprise cluster, the sandbox is the fastest zero-cost path to complete all core Lab 07 outcomes.

> ⚠️ **Snag — Account approval delay:** New Red Hat accounts may require manual approval. Have students activate sandbox access at least 24 hours before lab day.

---

## Part 3 — Verify Sandbox Entry Point and Capacity Expectations

![Red Hat Developer Sandbox landing page](lab-07-screenshots/ss03-redhat-developer-sandbox.png)

**What you are looking at:**  
The Developer Sandbox landing page where students initiate OpenShift access.

**Operational expectation for students:**
- One personal namespace/project
- Shared cluster behavior (occasional latency)
- Full support for Routes, ConfigMaps, Secrets, and HPA in namespace scope

---

## Part 4 — Use the S2I .NET Sample as a Deployment Baseline

![GitHub repository redhat-developer/s2i-dotnetcore-ex on dotnet-8.0 branch with deploy commands](lab-07-screenshots/ss04-s2i-dotnetcore-repo.png)

**What you are looking at:**  
The sample repository used in the course resource guide, including OpenShift deployment commands.

**Reference command pattern:**

```bash
oc new-app dotnet:8.0-ubi8~https://github.com/redhat-developer/s2i-dotnetcore-ex.git#dotnet-8.0 \
  --name=dotnet-ex --context-dir=app

oc expose service/dotnet-ex
oc get route dotnet-ex
```

**Why this matters:**  
This gives students a known-good build/deploy path before applying the same cluster patterns to their Lab 06 image.

---

## Part 5 — Add Health Probes (Readiness/Liveness)

![Kubernetes documentation page for liveness, readiness, and startup probes](lab-07-screenshots/ss05-kubernetes-probes-doc.png)

**What you are looking at:**  
Official Kubernetes guidance for readiness, liveness, and startup probes.

**Probe pattern to apply:**

```yaml
readinessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 10

livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 15
```

**Why this matters:**  
Without probes, unhealthy containers can receive traffic or stay stuck in failed states. Probes convert runtime health into orchestration decisions.

---

## Part 6 — Cluster Fallback Path (Azure-backed Option)

![Azure portal create web app view with signed-in student subscription context](lab-07-screenshots/ss06-azure-portal-create-webapp.png)

**What you are looking at:**  
Live Azure subscription context (`iis-student-az-10`) confirming a cloud fallback exists if OpenShift access is delayed.

**Use this only as fallback for Lab 07:**  
Primary learning target remains Kubernetes/OpenShift runtime concepts. Azure path is acceptable for continuity when cluster access is blocked.

---

## Part 7 — Capture Team/Delivery Evidence Context

![Azure DevOps team dashboard overview for Software_Dev_Mod project](lab-07-screenshots/ss07-ado-dashboard-overview.png)

**What you are looking at:**  
The live project dashboard where teams can track Lab 07 deployment tasks and velocity signals.

**Evidence linkage suggestion:**
- Work item for deployment
- Work item for probes/config
- Work item for autoscaling validation
- Attach route and HPA outputs to completion comments

---

## Part 8 — Install and Validate `oc` CLI

![OpenShift client download index showing latest oc client artifacts](lab-07-screenshots/ss08-openshift-oc-download-index.png)

**What you are looking at:**  
The OpenShift client distribution index used to install `oc`.

**Windows quick-start:**

```powershell
Invoke-WebRequest -Uri 'https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/openshift-client-windows.zip' -OutFile oc.zip
Expand-Archive oc.zip -DestinationPath $env:USERPROFILE\bin
oc version
```

**Post-login verification:**

```bash
oc whoami
oc get pods
oc get route
oc get hpa
```

---

## Validation Checklist (Student Submission)

- [ ] Deployment/pod health is green (`oc get pods`, `oc get deploy`)
- [ ] Route or ingress responds successfully (`oc get route` + browser/curl proof)
- [ ] ConfigMap and Secret are attached to workload
- [ ] Readiness and liveness probes are configured and observed
- [ ] HPA exists and targets expected min/max replicas

---

## Common Snags and Fixes

| Snag | Symptom | Fix |
|---|---|---|
| Sandbox approval pending | Cannot access OpenShift project | Register at least 24h early; keep Docker Desktop/AKS fallback ready |
| Route not created | `oc get route` empty | Ensure service exists and run `oc expose service/<name>` |
| Pod restart loop | CrashLoopBackOff | Check container logs and probe path/port alignment |
| HPA not scaling | Replicas stay at 1 | Generate load and verify CPU requests are set in deployment |
| Missing CLI | `oc` command not found | Install from OpenShift mirror and add to PATH |

---

## Summary

Lab 07 proves the modernization package from Lab 06 is **operationally deployable**: health-managed, externally reachable, and horizontally scalable in a cluster runtime. This is the critical bridge from build artifact to cloud platform operations.

