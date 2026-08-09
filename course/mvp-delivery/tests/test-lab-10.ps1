Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

. "$PSScriptRoot\_shared.ps1"

Write-Section "Lab 10 validation"

$repoRoot = Resolve-Path "$PSScriptRoot\..\..\.."
$labFile = Join-Path $repoRoot "course\mvp-delivery\labs\lab-10-capstone-end-to-end.md"
$moduleFile = Join-Path $repoRoot "course\mvp-delivery\modules\module-10-capstone.md"

Assert-PathExists -Path $labFile -Label "Lab file"
Assert-PathExists -Path $moduleFile -Label "Module file"

Assert-TextInFile -Path $labFile -Pattern "core modules 1, 3, 4, 6, 7, and 8 completed" -Description "capstone entry gate"
Assert-TextInFile -Path $labFile -Pattern "published MVP artifacts" -Description "artifact fallback"
Assert-TextInFile -Path $labFile -Pattern "final capstone package" -Description "checkpoint packaging step"
Assert-TextInFile -Path $labFile -Pattern "Pipeline and deployment evidence are complete" -Description "capstone exit gate"

Finish-Success -LabName "Lab 10"
