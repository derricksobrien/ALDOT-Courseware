#!/usr/bin/env bash
set -euo pipefail

PROJECT_NAME="dotnet-learning-lab"

echo "==> Creating/selecting project: ${PROJECT_NAME}"
if oc get project "${PROJECT_NAME}" >/dev/null 2>&1; then
  oc project "${PROJECT_NAME}"
else
  oc new-project "${PROJECT_NAME}"
fi

oc project "${PROJECT_NAME}"
