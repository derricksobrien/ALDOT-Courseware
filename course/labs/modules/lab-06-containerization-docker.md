# Lab 06: Containerization with Docker

## Module Alignment
Module 6: Containerization with Docker

## Timebox
90 minutes

## Objectives
- Create production-ready Dockerfiles for .NET workloads.
- Run multi-container local environments.
- Push images to Azure Container Registry.

## Prerequisites
- Docker Desktop or Podman.
- Azure subscription and ACR access.

## Step-by-Step
1. Create or refine a multi-stage Dockerfile for the API.
2. Build image locally and run containerized app.
3. Add health endpoint and verify container health.
4. Build a `docker-compose.yml` for app plus SQL dependencies.
5. Authenticate to Azure and create or reuse ACR.
6. Tag and push image to ACR.
7. Run image scanning and record findings.

## Validation Checks
- Application responds correctly in container mode.
- Compose stack starts and dependencies resolve.
- Image is available in ACR and tagged correctly.

## Deliverables
- Dockerfile and compose file updates.
- ACR push log.
- Image scan summary.

## Stretch Goals
- Publish SBOM and signed image metadata.
