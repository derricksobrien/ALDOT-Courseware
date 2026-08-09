Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

. "$PSScriptRoot\_shared.ps1"

Write-Section "Lab 09 validation"

$repoRoot = Resolve-Path "$PSScriptRoot\..\..\.."
$labFile = Join-Path $repoRoot "course\mvp-delivery\labs\lab-09-azure-deployment-operations.md"
$moduleFile = Join-Path $repoRoot "course\mvp-delivery\modules\module-09-azure-operations.md"

Assert-PathExists -Path $labFile -Label "Lab file"
Assert-PathExists -Path $moduleFile -Label "Module file"

$az = Get-Command az -ErrorAction SilentlyContinue
if (-not $az) {
    Write-Host "[WARN] Azure CLI not detected. Install Azure CLI to run this lab end to end." -ForegroundColor Yellow
} else {
    Write-Host "[OK] Azure CLI detected." -ForegroundColor Green
}

Assert-TextInFile -Path $labFile -Pattern "Contributor or Owner access" -Description "RBAC prerequisite"
Assert-TextInFile -Path $labFile -Pattern "Select a target hosting model" -Description "hosting model step"
Assert-TextInFile -Path $labFile -Pattern "Application Insights and Log Analytics" -Description "observability step"
Assert-TextInFile -Path $labFile -Pattern "SLOs" -Description "SLO requirement"
Assert-TextInFile -Path $labFile -Pattern "Azure subscription and quota" -Description "cloud prerequisite"

Finish-Success -LabName "Lab 09"
