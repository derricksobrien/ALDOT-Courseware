Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

. "$PSScriptRoot\_shared.ps1"

Write-Section "Lab 08 validation"

$repoRoot = Resolve-Path "$PSScriptRoot\..\..\.."
$labFile = Join-Path $repoRoot "course\mvp-delivery\labs\lab-08-cicd-github-actions.md"
$moduleFile = Join-Path $repoRoot "course\mvp-delivery\modules\module-08-cicd-github-actions.md"

Assert-PathExists -Path $labFile -Label "Lab file"
Assert-PathExists -Path $moduleFile -Label "Module file"
Assert-CommandAvailable -Command "git"

Assert-TextInFile -Path $labFile -Pattern "workflow triggers for push and pull request" -Description "CI trigger configuration"
Assert-TextInFile -Path $labFile -Pattern "quality gates" -Description "quality gate requirement"

Write-Host "[INFO] Manual check: verify GitHub secrets and Actions permissions." -ForegroundColor Yellow
Finish-Success -LabName "Lab 08"
