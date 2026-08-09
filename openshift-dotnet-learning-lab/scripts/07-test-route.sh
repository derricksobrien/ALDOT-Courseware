#!/usr/bin/env bash
set -euo pipefail

APP_NAME="s2i-dotnetcore-ex"
HOST="$(oc get route "${APP_NAME}" -o jsonpath='{.spec.host}')"
APP_URL="http://${HOST}"

echo "==> App URL: ${APP_URL}"
echo "==> Testing route"
curl -I "${APP_URL}"
