# Lab 06: Containerization with Docker

## Module
Module 06 - Containerization with Docker

## Tier
Core MVP Lab

## Goal
Containerize the app and verify local runtime behavior.

## Prerequisites

- Repository available: `course/repos/eShopOnWeb`
- Docker or Podman installed
- .NET SDK installed

## Azure Ubuntu VM Fallback (sdm-2026-aug10)

Use this path if local Docker is unavailable or unstable.

- VM: `vm-ubuntu-sdm-2026-aug10`
- User: `labadmin`
- Docker Engine, Buildx, and Compose are preinstalled

```bash
# new SSH session recommended so docker group membership is active
ssh -i <path-to-private-key> labadmin@<vm-public-ip-or-dns>

docker version
docker compose version
docker ps
```

If `docker` requires sudo in an old session, reconnect SSH (or use `newgrp docker`).

## Steps

1. Create or update a multi-stage Dockerfile.
2. Build image locally.
3. Run container and test health endpoint.
4. Add or verify compose configuration if needed.
5. Tag image for pipeline or registry use.

### VM fallback execution

Run the same lab steps on the VM:

```bash
docker build -t sdm-web:lab06 .
docker run --rm -d -p 8080:8080 --name sdm-web sdm-web:lab06
curl http://localhost:8080/health
docker images | grep sdm-web
```

## Validation

- Image builds successfully.
- Container runs and responds to health checks.

## Evidence

- Build output
- Container run output
- Image tag list
- VM proof (SSH prompt + `docker ps` / `curl` health output)
