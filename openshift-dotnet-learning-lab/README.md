# .NET Core Sample App for OpenShift — Learning Lab

This lab walks you end-to-end through creating a .NET app build/deploy workflow on OpenShift using S2I, then adding resource controls and autoscaling.

## What you'll learn

1. Create an OpenShift project
2. Import .NET ImageStreams
3. Create app from Git with S2I
4. Expose app route
5. Set runtime and build resource requests/limits
6. Configure HPA autoscaling
7. Generate load and observe scaling
8. Clean up

---

## Prerequisites

- OpenShift cluster access
- `oc` CLI installed
- Permissions to create projects/resources
- Cluster monitoring/metrics enabled (for HPA)

---

## Repository layout

- `hpa.yaml` — starter HPA configuration
- `scripts/` — step-by-step lab scripts
- `run-all.sh` — convenience runner (interactive)

---

## Quick start

```bash
cd openshift-dotnet-learning-lab
chmod +x run-all.sh scripts/*.sh
./run-all.sh
```

Or run scripts one-by-one in order.

---

## Manual walkthrough

### 1) Login and create project

```bash
./scripts/01-login.sh
./scripts/02-create-project.sh
```

### 2) Import .NET ImageStreams

```bash
./scripts/03-import-imagestreams.sh
```

### 3) Create app from Git (S2I)

```bash
./scripts/04-create-app.sh
./scripts/05-watch-build-and-rollout.sh
```

### 4) Expose route and test

```bash
./scripts/06-expose-route.sh
./scripts/07-test-route.sh
```

### 5) Apply starter resources

```bash
./scripts/08-set-runtime-resources.sh
./scripts/09-set-build-resources.sh
```

### 6) Configure HPA

```bash
oc apply -f hpa.yaml
oc get hpa s2i-dotnetcore-ex
./scripts/10-check-metrics.sh
```

### 7) Generate load and observe autoscaling

```bash
./scripts/11-loadgen.sh
```

In a second terminal:

```bash
oc get hpa s2i-dotnetcore-ex -w
oc get pods -w
```

### 8) Trigger rebuild

```bash
./scripts/12-start-rebuild.sh
```

### 9) Cleanup

```bash
./scripts/99-cleanup.sh
```

---

## Starter resource sizing used

### Build pod (BuildConfig/S2I)

- requests: `cpu=500m`, `memory=1Gi`, `ephemeral-storage=2Gi`
- limits: `cpu=2`, `memory=3Gi`, `ephemeral-storage=6Gi`

### Runtime app pod

- requests: `cpu=100m`, `memory=256Mi`
- limits: `cpu=500m`, `memory=512Mi`

If your app receives heavier traffic, a safer runtime baseline is:
- requests: `cpu=250m`, `memory=512Mi`
- limits: `cpu=1`, `memory=1Gi`

---

## Troubleshooting

- `oc top pods` fails: metrics not available; HPA won't function until cluster metrics are enabled.
- Build image pull errors: check egress/proxy and pull secret configuration.
- Route unreachable: verify ingress/router and DNS.
- Runtime OOMKilled: increase runtime memory limit to `1Gi`.

---

## Notes

- Scripts are designed for learning and clarity over production hardening.
- You can safely rerun most scripts; they are mostly idempotent where practical.
