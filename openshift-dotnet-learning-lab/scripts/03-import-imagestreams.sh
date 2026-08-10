#!/usr/bin/env bash
set -euo pipefail

echo "==> Importing .NET ImageStreams"
oc apply -f https://raw.githubusercontent.com/redhat-developer/s2i-dotnetcore/main/dotnet_imagestreams.json

echo "==> Available ImageStreams"
oc get is | grep dotnet || true
