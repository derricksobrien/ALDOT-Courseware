---
layout: default
title: "Lab 07 Cluster Options and Sandbox Guide"
parent: Resources
nav_order: 2
---

# Lab 07 Cluster Options — OpenShift Sandbox, Docker Desktop, and Azure

- Created: 2026-08-09T17:38:00-06:00
- Scope: Comparison of runtime options for Lab 07 and a full guide to using the Red Hat Developer Sandbox as the recommended zero-cost fallback.

---

## Option comparison

| Capability | OpenShift Cluster | Docker Desktop (Kubernetes) | Azure (AKS / ACA) |
|---|---|---|---|
| Cost | Shared org cluster (free) or Red Hat Developer Sandbox (free, 30-day) | Free on the student machine | Pay-per-use — requires Azure subscription |
| Setup complexity | Low if pre-provisioned; medium if students provision their own | Very low — enable in Docker Desktop settings | Medium — AKS requires CLI, resource group, and cluster creation |
| Realism to enterprise | Highest — matches what many government and regulated orgs run | Low — local only, no real cluster concepts | High — widely used in enterprise, different from OpenShift |
| OpenShift-specific features | Full — Routes, SCC, oc CLI, built-in registry | None — plain Kubernetes only | None — AKS uses standard Kubernetes |
| Works offline | No — requires network access | Yes — runs completely locally | No — requires internet and Azure |
| Student machine requirements | Light — just oc or kubectl CLI | Heavy — 8–16 GB RAM minimum | Light — just Azure CLI |
| Persistent across class days | Yes if shared cluster; ephemeral for sandbox | Yes — local state persists | Yes — resources persist until deleted |
| Routes and ingress | Native Route object via oc expose | Requires ingress controller (extra step) | AKS needs ingress controller; ACA has built-in HTTPS |
| Autoscaling (HPA) | Supported | Supported but no real load target | Supported on AKS; ACA scales automatically |
| Registry integration | Built-in OpenShift internal registry | Uses local Docker daemon | ACR — images must be pushed there first |
| Instructor reset path | Delete namespace, recreate | Docker Desktop reset | Delete resource group, recreate |
| Risk of cost overrun | None | None | Real risk if students forget to delete resources |

---

## Recommended decision tree

```
Do students have access to an OpenShift cluster or Red Hat Developer Sandbox?
  YES → Use OpenShift. Highest realism, covers oc, Routes, SCC.
  NO  → Do student machines have 16 GB RAM and Docker Desktop installed?
          YES → Use Docker Desktop Kubernetes. Zero cost, works offline.
          NO  → Does the class already have Azure subscriptions active?
                  YES → Use AKS or ACA. Ties naturally into Lab 09.
                  NO  → Use Red Hat Developer Sandbox (free 30-day account).
```

---

## Red Hat Developer Sandbox — Full Guide

### What it is

The Red Hat Developer Sandbox is a free, 30-day, shared OpenShift cluster that any developer can access with a Red Hat account. It gives each student a personal namespace on a real OpenShift cluster hosted by Red Hat — no infrastructure setup, no credit card required.

### What students get

| Resource | Limit |
|---|---|
| Duration | 30 days (can be renewed) |
| Namespace | 1 personal namespace per account |
| CPU | ~7 cores shared |
| Memory | ~14 GB shared |
| Persistent storage | Available but limited |
| OpenShift Web Console | Full access |
| oc CLI | Full access |
| kubectl | Also works |
| Internal image registry | Available |
| Routes | Available — real HTTPS URL per deployed app |
| OpenShift Pipelines | Available |
| OpenShift Dev Spaces | Available (browser-based VS Code) |
| Admin / cluster-admin | Not available — namespace-scoped only |

### How students sign up

1. Go to https://developers.redhat.com/developer-sandbox
2. Click **Start your sandbox for free**
3. Sign in with a free Red Hat account (or create one — email only, no credit card)
4. Navigate to https://sandbox.redhat.com and click **Try it** next to **OpenShift**
5. The cluster provisions — either automatically (under 2 minutes) or after manual approval

> ⚠️ **Manual approval notice (observed 2026-08-10 during live test):** New Red Hat accounts may receive the message *"Your account needs manual approval from the Developer Sandbox administrators."* This appears to apply to newly created accounts. Approval typically completes within a few hours. **Students must sign up at least 24 hours before Lab 07** to ensure access is available.

6. Once approved, the OpenShift Web Console opens from the sandbox dashboard
7. The console URL looks like: `https://console-openshift-console.apps.rm2.thpm.p1.openshiftapps.com`
   - **Live-tested cluster (2026-08-10):** `https://console-openshift-console.apps.rm2.thpm.p1.openshiftapps.com`
   - API endpoint: `https://api.rm2.thpm.p1.openshiftapps.com:6443`
   - Namespace: `<username>-dev`

Each student needs their own Red Hat account. One sandbox per account.

### How to connect from the command line

After signing in to the web console:

1. Click the username in the top-right corner → **Copy login command**
2. Click **Display token**
3. Copy the `oc login` command — it looks like:

```bash
oc login --token=sha256~xxxx --server=https://api.sandbox-m3.1530.p1.openshiftapps.com:6443
```

4. Paste it into a terminal on the lab machine
5. Verify access:

```bash
oc whoami
oc project   # shows your assigned namespace
```

### How to deploy the containerized app from Lab 06

```bash
# Deploy from the image built in Lab 06
oc new-app --name=eshop <your-image>

# Or apply the starter manifests from the s2i-dotnetcore-ex repo
oc apply -f course/repos/s2i-dotnetcore-ex/k8s/

# Expose the service as an HTTPS route
oc expose svc/eshop
oc get route eshop   # shows the public HTTPS URL
```

For the dotnet S2I path (build from source directly in the cluster — **live-tested 2026-08-10, working**):

```bash
# Deploy and build directly from source using S2I
oc new-app dotnet:8.0-ubi8~https://github.com/redhat-developer/s2i-dotnetcore-ex.git#dotnet-8.0 \
  --name=dotnet-ex --context-dir=app

# Follow the build log
oc logs -f buildconfig/dotnet-ex

# Expose the service as a route (HTTP)
oc expose service/dotnet-ex
oc get route dotnet-ex   # shows public URL

# Add a ConfigMap for app configuration
oc create configmap dotnet-ex-config --from-literal=APP_ENV=sandbox

# Enable autoscaling
oc autoscale deployment/dotnet-ex --min=1 --max=3 --cpu-percent=70
```

**Live test result (2026-08-10):**
- Build: ✅ Complete (55s — .NET 8 S2I build)
- Pod: ✅ Running (`1/1`)
- Route: `dotnet-ex-derricksobrien-dev.apps.rm2.thpm.p1.openshiftapps.com`
- HTTP 200: ✅ App serving ASP.NET Core MVC home page
- ConfigMap: ✅ Created
- HPA: ✅ Created (1–3 replicas, 70% CPU target)

### Constraints and impact on Lab 07

| Constraint | Impact on Lab 07 |
|---|---|
| No cluster-admin | Cannot create ClusterRoles or modify SCCs — no impact on core lab steps |
| Single namespace | All work stays in one namespace — no issue for this lab |
| 30-day expiry | Students must sign up before class; content is deleted after 30 days |
| Shared cluster | Occasional slowdowns under heavy load |
| No persistent volumes by default | Stateful apps need explicit PVC configuration |
| Image pull from external registries | Works — may need imagePullSecrets for private registries |

### What works fine for Lab 07

- Routes work fully — students get real HTTPS URLs immediately
- HPA (autoscaling) works within namespace quota
- ConfigMaps and Secrets work fully
- Readiness and liveness probes work fully
- The `oc` CLI connects directly from the student's lab machine
- The web console gives a visual view of pods, routes, logs, and events

### Installing the oc CLI

Download from: https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/

Windows (PowerShell):

```powershell
# Download and extract oc.exe
Invoke-WebRequest -Uri 'https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/openshift-client-windows.zip' -OutFile oc.zip
Expand-Archive oc.zip -DestinationPath $env:USERPROFILE\bin
# Add $env:USERPROFILE\bin to PATH if not already present
oc version
```

### Instructor preparation checklist

- [ ] **Sign students up for Red Hat accounts at least 24 hours before Lab 07** — new accounts require manual approval by Red Hat administrators
- [ ] Confirm sandbox sign-up works 1 week before class and that the OpenShift tile shows "Try it" (not a provisioning spinner)
- [ ] Test the `oc login --token` flow on a clean machine
- [ ] Confirm the s2i-dotnetcore-ex manifests apply cleanly in a sandbox namespace
- [ ] Prepare a fallback plan (Docker Desktop or AKS) for students whose sandbox is still pending approval
- [ ] Remind students the sandbox expires after 30 days and to not store course evidence exclusively there

### Recommended student pre-class setup steps

1. Create a free Red Hat account at https://developers.redhat.com **(do this at least 24 hours before Lab 07)**
2. Activate the sandbox at https://sandbox.redhat.com → click **Try it** next to OpenShift
3. Wait for approval email (new accounts may require manual review — typical wait: a few hours)
4. Install the `oc` CLI from https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/
5. Run `oc version` to confirm installation
6. Log in using the token from the web console
7. Run `oc whoami` and `oc get pods` to confirm access

---

## Recommendation for the MVP course

Use the following priority order for Lab 07:

1. **Shared org OpenShift cluster** — if your organization has one provisioned for the course
2. **Red Hat Developer Sandbox** — best zero-cost fallback, real OpenShift experience, HTTPS routes included
3. **Docker Desktop Kubernetes** — for offline or resource-constrained environments
4. **AKS or ACA** — if the class already has Azure subscriptions active for Lab 09

The lab guide and validation script should detect which CLI is available (`oc` vs `kubectl`) and adjust evidence instructions accordingly. The sandbox path is fully supported for all core Lab 07 outcomes.

