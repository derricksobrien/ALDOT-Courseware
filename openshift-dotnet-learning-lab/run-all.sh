#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="${ROOT_DIR}/scripts"

echo "==> OpenShift .NET Learning Lab Runner"
echo "This will execute the core setup flow in order."

declare -a STEPS=(
  "01-login.sh"
  "02-create-project.sh"
  "03-import-imagestreams.sh"
  "04-create-app.sh"
  "05-watch-build-and-rollout.sh"
  "06-expose-route.sh"
  "07-test-route.sh"
  "08-set-runtime-resources.sh"
  "09-set-build-resources.sh"
  "10-check-metrics.sh"
)

for step in "${STEPS[@]}"; do
  echo
  echo "=============================="
  echo "Running ${step}"
  echo "=============================="
  bash "${SCRIPTS_DIR}/${step}"
done

echo
echo "==> Applying HPA"
oc apply -f "${ROOT_DIR}/hpa.yaml"
oc get hpa s2i-dotnetcore-ex

echo
echo "Lab bootstrap complete."
echo "Next:"
echo "  1) Run load test:   ./scripts/11-loadgen.sh"
echo "  2) In another shell: oc get hpa s2i-dotnetcore-ex -w && oc get pods -w"
echo "  3) Trigger rebuild: ./scripts/12-start-rebuild.sh"
echo "  4) Cleanup:         ./scripts/99-cleanup.sh"
