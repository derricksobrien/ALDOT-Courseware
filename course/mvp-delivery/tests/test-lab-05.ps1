Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

. "$PSScriptRoot\_shared.ps1"

Write-Section "Lab 05 validation"

$repoRoot = Resolve-Path "$PSScriptRoot\..\..\.."
$labFile = Join-Path $repoRoot "course\mvp-delivery\labs\lab-05-test-automation-quality-gates.md"
$moduleFile = Join-Path $repoRoot "course\mvp-delivery\modules\module-05-test-automation-tosca.md"
$toscaSecrets = Join-Path $repoRoot "tosca-secrets.md"

Assert-PathExists -Path $labFile -Label "Lab file"
Assert-PathExists -Path $moduleFile -Label "Module file"
Assert-PathExists -Path $toscaSecrets -Label "Tosca secrets file"

Assert-TextInFile -Path $labFile -Pattern "Tosca installed and licensed" -Description "tool prerequisite"
Assert-TextInFile -Path $labFile -Pattern "tosca-secrets.md" -Description "Tosca credential reference"
Assert-TextInFile -Path $labFile -Pattern "quality gate" -Description "quality gate focus"

Write-Host "[INFO] Manual check required: Tosca runtime, license, and tenant access availability." -ForegroundColor Yellow
Finish-Success -LabName "Lab 05"
