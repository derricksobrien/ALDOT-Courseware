Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

. "$PSScriptRoot\_shared.ps1"

Write-Section "Lab 03 validation"

$repoRoot = Resolve-Path "$PSScriptRoot\..\..\.."
$labFile = Join-Path $repoRoot "course\mvp-delivery\labs\lab-03-copilot-refactor-and-tests.md"
$moduleFile = Join-Path $repoRoot "course\mvp-delivery\modules\module-03-copilot-csharp.md"
$appRepo = Join-Path $repoRoot "course\repos\eShopOnWeb"

Assert-PathExists -Path $labFile -Label "Lab file"
Assert-PathExists -Path $moduleFile -Label "Module file"
Assert-PathExists -Path $appRepo -Label "Reference repository"

Assert-CommandAvailable -Command "dotnet"
Assert-CommandAvailable -Command "git"

Assert-TextInFile -Path $labFile -Pattern "Prompt Copilot for a refactor plan" -Description "Copilot usage step"
Assert-TextInFile -Path $labFile -Pattern "Test run output" -Description "evidence requirement"

Write-Host "[INFO] Manual check: verify Copilot entitlement and sign-in in IDE." -ForegroundColor Yellow
Finish-Success -LabName "Lab 03"
