#!/usr/bin/env bash
set -euo pipefail

APP_NAME="s2i-dotnetcore-ex"
HOST="$(oc get route "${APP_NAME}" -o jsonpath='{.spec.host}')"
APP_URL="http://${HOST}"

echo "==> Starting ephemeral load generator pod"
oc run -i --tty loadgen --rm --restart=Never --image=registry.access.redhat.com/ubi9/ubi-minimal -- bash -lc "\
  microdnf install -y curl >/dev/null 2>&1; \
  echo Load target: ${APP_URL}; \
  while true; do \
    for i in \\$(seq 1 200); do curl -s ${APP_URL} > /dev/null & done; \
    wait; \
    echo burst sent; \
    sleep 2; \
  done\
"
