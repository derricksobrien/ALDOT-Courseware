Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

. "$PSScriptRoot\_shared.ps1"

Write-Section "Lab 02 validation"

$repoRoot = Resolve-Path "$PSScriptRoot\..\..\.."
$labFile = Join-Path $repoRoot "course\mvp-delivery\labs\lab-02-ado-work-tracking.md"
$moduleFile = Join-Path $repoRoot "course\mvp-delivery\modules\module-02-ado-work-tracking.md"

Assert-PathExists -Path $labFile -Label "Lab file"
Assert-PathExists -Path $moduleFile -Label "Module file"
Assert-CommandAvailable -Command "git"

Assert-TextInFile -Path $labFile -Pattern "ADO organization/project access" -Description "ADO prerequisite"
Assert-TextInFile -Path $labFile -Pattern "Link work items to commits or pull requests" -Description "traceability step"

Write-Host "[INFO] External validation required: confirm ADO tenant/project access manually." -ForegroundColor Yellow
Finish-Success -LabName "Lab 02"
