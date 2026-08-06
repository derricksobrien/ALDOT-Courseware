Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

. "$PSScriptRoot\_shared.ps1"

Write-Section "Lab 06 validation"

$repoRoot = Resolve-Path "$PSScriptRoot\..\..\.."
$labFile = Join-Path $repoRoot "course\mvp-delivery\labs\lab-06-containerization-docker.md"
$moduleFile = Join-Path $repoRoot "course\mvp-delivery\modules\module-06-containerization.md"
$appRepo = Join-Path $repoRoot "course\repos\eShopOnWeb"

Assert-PathExists -Path $labFile -Label "Lab file"
Assert-PathExists -Path $moduleFile -Label "Module file"
Assert-PathExists -Path $appRepo -Label "Reference repository"

Assert-CommandAvailable -Command "dotnet"

# Accept either Docker or Podman.
$docker = Get-Command docker -ErrorAction SilentlyContinue
$podman = Get-Command podman -ErrorAction SilentlyContinue
if (-not $docker -and -not $podman) {
    throw "Missing container runtime command. Install Docker or Podman."
}
Write-Host "[OK] Container runtime detected." -ForegroundColor Green

Assert-TextInFile -Path $labFile -Pattern "multi-stage Dockerfile" -Description "container build step"
Assert-TextInFile -Path $labFile -Pattern "health endpoint" -Description "health validation step"

Finish-Success -LabName "Lab 06"
