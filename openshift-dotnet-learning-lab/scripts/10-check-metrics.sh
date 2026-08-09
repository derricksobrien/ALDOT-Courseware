#!/usr/bin/env bash
set -euo pipefail

echo "==> Checking cluster metrics"
oc top pods
