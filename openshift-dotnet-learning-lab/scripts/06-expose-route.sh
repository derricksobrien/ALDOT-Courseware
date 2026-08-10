#!/usr/bin/env bash
set -euo pipefail

APP_NAME="s2i-dotnetcore-ex"

echo "==> Exposing service"
oc expose service "${APP_NAME}" || true

echo "==> Route"
oc get route "${APP_NAME}"
