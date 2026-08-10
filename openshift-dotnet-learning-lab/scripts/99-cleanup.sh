#!/usr/bin/env bash
set -euo pipefail

PROJECT_NAME="dotnet-learning-lab"

echo "==> Deleting project: ${PROJECT_NAME}"
oc delete project "${PROJECT_NAME}"
