Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

. "$PSScriptRoot\_shared.ps1"

Write-Section "Lab 07 validation"

$repoRoot = Resolve-Path "$PSScriptRoot\..\..\.."
$labFile = Join-Path $repoRoot "course\mvp-delivery\labs\lab-07-kubernetes-openshift.md"
$moduleFile = Join-Path $repoRoot "course\mvp-delivery\modules\module-07-kubernetes-openshift.md"
$sampleRepo = Join-Path $repoRoot "course\repos\s2i-dotnetcore-ex"

Assert-PathExists -Path $labFile -Label "Lab file"
Assert-PathExists -Path $moduleFile -Label "Module file"
Assert-PathExists -Path $sampleRepo -Label "OpenShift sample repository"

$kubectl = Get-Command kubectl -ErrorAction SilentlyContinue
$oc = Get-Command oc -ErrorAction SilentlyContinue
if (-not $kubectl -and -not $oc) {
    throw "Missing cluster CLI. Install kubectl or oc."
}
Write-Host "[OK] Cluster CLI detected." -ForegroundColor Green

Assert-TextInFile -Path $labFile -Pattern "readiness and liveness probes" -Description "health probe requirement"
Assert-TextInFile -Path $labFile -Pattern "autoscaling" -Description "scale validation requirement"

Finish-Success -LabName "Lab 07"
