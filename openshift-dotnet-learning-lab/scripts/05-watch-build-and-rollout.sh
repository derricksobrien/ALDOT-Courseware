#!/usr/bin/env bash
set -euo pipefail

APP_NAME="s2i-dotnetcore-ex"

echo "==> Watching latest build logs"
LATEST_BUILD_NAME="$(oc get builds -o name | tail -n1 | cut -d/ -f2)"
if [[ -n "${LATEST_BUILD_NAME}" ]]; then
  oc logs -f "build/${LATEST_BUILD_NAME}" || true
fi

echo "==> Waiting for rollout"
oc rollout status "deploy/${APP_NAME}"

echo "==> Pods"
oc get pods
