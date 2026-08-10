#!/usr/bin/env bash
set -euo pipefail

APP_NAME="s2i-dotnetcore-ex"

echo "==> Setting runtime resources on deployment"
oc set resources deploy/"${APP_NAME}" \
  --requests=cpu=100m,memory=256Mi \
  --limits=cpu=500m,memory=512Mi

echo "==> Verifying"
oc get deploy "${APP_NAME}" -o jsonpath='{.spec.template.spec.containers[0].resources}{"\n"}'
