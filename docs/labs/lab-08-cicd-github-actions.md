---
layout: default
title: "Lab 08 — CI/CD with GitHub Actions"
parent: Labs
nav_order: 8
---

# Lab 08: CI/CD with GitHub Actions

## Module
Module 08 - CI/CD with GitHub Actions

## Tier
Core MVP Lab

## Goal
Create a working build-test-deploy workflow with quality gates.

## Prerequisites

- A fork of the app repository in your GitHub account with Actions enabled
- Required secrets configured
- App from prior modules committed

## Azure Ubuntu VM Fallback (Deployment Target)

If App Service or container platform deployment is blocked, use `vm-ubuntu-sdm-2026-aug10` as the deploy target while preserving CI quality gates.

Recommended GitHub secrets:

- `VM_HOST`
- `VM_USER` (for this cohort: `labadmin`)
- `VM_SSH_KEY`

## Steps

0. Fork the repository to your own GitHub account and use that fork as the workflow target.
1. Add workflow triggers for push and pull request.
2. Add build and test jobs.
3. Add container build and publish stage.
4. Add deployment job and environment guardrails.
5. Enforce test and coverage quality gates.
6. Add branch protection with required checks.

### VM fallback deployment job (optional)

Add a deploy job after build/test that SSHs to the VM and runs the image:

```yaml
deploy_vm:
  needs: [build, test]
  runs-on: ubuntu-latest
  steps:
    - name: Deploy on Ubuntu VM over SSH
      uses: appleboy/ssh-action@v1.2.0
      with:
        host: ${{ secrets.VM_HOST }}
        username: ${{ secrets.VM_USER }}
        key: ${{ secrets.VM_SSH_KEY }}
        script: |
          docker pull <image-ref>
          docker rm -f sdm-web || true
          docker run -d --name sdm-web -p 8080:8080 <image-ref>
          curl -f http://localhost:8080/health
```

## Validation

- Workflow executes end to end from the forked repository.
- Failed tests block the deploy stage.

## Evidence

- Workflow YAML file
- Branch protection or required-checks proof
- Successful run URL
- Failed run URL showing gate enforcement
- VM deployment proof (`docker ps` and health check from pipeline log or SSH output)
