#!/usr/bin/env bash
set -euo pipefail

APP_NAME="s2i-dotnetcore-ex"

echo "==> Starting rebuild"
oc start-build "${APP_NAME}"

LATEST_BUILD_NAME="$(oc get builds -o name | tail -n1 | cut -d/ -f2)"
if [[ -n "${LATEST_BUILD_NAME}" ]]; then
  oc logs -f "build/${LATEST_BUILD_NAME}"
fi
