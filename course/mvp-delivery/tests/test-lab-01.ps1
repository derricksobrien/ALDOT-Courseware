Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

. "$PSScriptRoot\_shared.ps1"

Write-Section "Lab 01 validation"

$repoRoot = Resolve-Path "$PSScriptRoot\..\..\.."
$labFile = Join-Path $repoRoot "course\mvp-delivery\labs\lab-01-modernization-discovery.md"
$moduleFile = Join-Path $repoRoot "course\mvp-delivery\modules\module-01-modernization-overview.md"
$appRepo = Join-Path $repoRoot "course\repos\eShopOnWeb"

Assert-PathExists -Path $labFile -Label "Lab file"
Assert-PathExists -Path $moduleFile -Label "Module file"
Assert-PathExists -Path $appRepo -Label "Reference repository"

Assert-CommandAvailable -Command "git"
Assert-CommandAvailable -Command "dotnet"

Assert-TextInFile -Path $labFile -Pattern "modernization-candidate-matrix.md" -Description "required evidence artifact"
Assert-TextInFile -Path $labFile -Pattern "rehost, refactor, rearchitect, or rebuild" -Description "strategy classification step"

Finish-Success -LabName "Lab 01"
