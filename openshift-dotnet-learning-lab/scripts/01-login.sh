#!/usr/bin/env bash
set -euo pipefail

echo "==> OpenShift Login"
echo "If already logged in, this will simply confirm identity."
oc whoami || {
  echo "Not logged in. Run: oc login https://api.<cluster>:6443"
  exit 1
}
oc whoami
oc projects
