#!/usr/bin/env bash
set -euo pipefail

APP_NAME="s2i-dotnetcore-ex"

echo "==> Creating app from Git source using dotnet:10.0 builder"
oc new-app dotnet:10.0~https://github.com/redhat-developer/s2i-dotnetcore-ex#dotnet-10.0 --context-dir app --name "${APP_NAME}" || true

echo "==> Current resources"
oc get bc,is,deploy,svc,pods
