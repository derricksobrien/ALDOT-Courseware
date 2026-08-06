Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

. "$PSScriptRoot\_shared.ps1"

Write-Section "Lab 04 validation"

$repoRoot = Resolve-Path "$PSScriptRoot\..\..\.."
$labFile = Join-Path $repoRoot "course\mvp-delivery\labs\lab-04-modern-dotnet-api-sql.md"
$moduleFile = Join-Path $repoRoot "course\mvp-delivery\modules\module-04-modern-dotnet-api.md"
$appRepo = Join-Path $repoRoot "course\repos\eShopOnWeb"

Assert-PathExists -Path $labFile -Label "Lab file"
Assert-PathExists -Path $moduleFile -Label "Module file"
Assert-PathExists -Path $appRepo -Label "Reference repository"

Assert-CommandAvailable -Command "dotnet"

Assert-TextInFile -Path $labFile -Pattern "Add a new API endpoint" -Description "API development step"
Assert-TextInFile -Path $labFile -Pattern "integration tests" -Description "integration requirement"

Write-Host "[INFO] SQL reachability should be validated in delivery environment." -ForegroundColor Yellow
Finish-Success -LabName "Lab 04"
