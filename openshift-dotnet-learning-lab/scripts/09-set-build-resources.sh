#!/usr/bin/env bash
set -euo pipefail

APP_NAME="s2i-dotnetcore-ex"

echo "==> Patching BuildConfig resources"
oc patch bc/"${APP_NAME}" --type merge -p '{
  "spec": {
    "resources": {
      "requests": {
        "cpu": "500m",
        "memory": "1Gi",
        "ephemeral-storage": "2Gi"
      },
      "limits": {
        "cpu": "2",
        "memory": "3Gi",
        "ephemeral-storage": "6Gi"
      }
    }
  }
}'

echo "==> Verifying"
oc get bc "${APP_NAME}" -o jsonpath='{.spec.resources}{"\n"}'
