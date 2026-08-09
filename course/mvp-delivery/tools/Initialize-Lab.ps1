[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^\d{2}$')]
    [string]$LabNumber,

    [string]$TargetPath,

    [switch]$OpenInExplorer
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$labFiles = @{
    '01' = @{ Title = 'Modernization Discovery'; LabFile = 'course\mvp-delivery\labs\lab-01-modernization-discovery.md'; ModuleFile = 'course\mvp-delivery\modules\module-01-modernization-overview.md' }
    '02' = @{ Title = 'ADO Work Tracking'; LabFile = 'course\mvp-delivery\labs\lab-02-ado-work-tracking.md'; ModuleFile = 'course\mvp-delivery\modules\module-02-ado-work-tracking.md' }
    '03' = @{ Title = 'Copilot Refactor and Tests'; LabFile = 'course\mvp-delivery\labs\lab-03-copilot-refactor-and-tests.md'; ModuleFile = 'course\mvp-delivery\modules\module-03-copilot-csharp.md' }
    '04' = @{ Title = 'Modern .NET API and SQL'; LabFile = 'course\mvp-delivery\labs\lab-04-modern-dotnet-api-sql.md'; ModuleFile = 'course\mvp-delivery\modules\module-04-modern-dotnet-api.md' }
    '05' = @{ Title = 'Test Automation Quality Gates'; LabFile = 'course\mvp-delivery\labs\lab-05-test-automation-quality-gates.md'; ModuleFile = 'course\mvp-delivery\modules\module-05-test-automation-tosca.md' }
    '06' = @{ Title = 'Containerization with Docker'; LabFile = 'course\mvp-delivery\labs\lab-06-containerization-docker.md'; ModuleFile = 'course\mvp-delivery\modules\module-06-containerization.md' }
    '07' = @{ Title = 'Kubernetes and OpenShift'; LabFile = 'course\mvp-delivery\labs\lab-07-kubernetes-openshift.md'; ModuleFile = 'course\mvp-delivery\modules\module-07-kubernetes-openshift.md' }
    '08' = @{ Title = 'CI/CD with GitHub Actions'; LabFile = 'course\mvp-delivery\labs\lab-08-cicd-github-actions.md'; ModuleFile = 'course\mvp-delivery\modules\module-08-cicd-github-actions.md' }
    '09' = @{ Title = 'Azure Deployment Operations'; LabFile = 'course\mvp-delivery\labs\lab-09-azure-deployment-operations.md'; ModuleFile = 'course\mvp-delivery\modules\module-09-azure-operations.md' }
    '10' = @{ Title = 'Capstone End-to-End Modernization'; LabFile = 'course\mvp-delivery\labs\lab-10-capstone-end-to-end.md'; ModuleFile = 'course\mvp-delivery\modules\module-10-capstone.md' }
}

if (-not $labFiles.ContainsKey($LabNumber)) {
    throw "Unsupported lab number '$LabNumber'. Expected 01-10."
}

$labInfo = $labFiles[$LabNumber]
if ([string]::IsNullOrWhiteSpace($TargetPath)) {
    $TargetPath = Join-Path $repoRoot "course\mvp-delivery\student-work\lab-$LabNumber"
}

$resolvedTarget = [System.IO.Path]::GetFullPath($TargetPath)
New-Item -ItemType Directory -Path $resolvedTarget -Force | Out-Null

$labGuidePath = Join-Path $repoRoot $labInfo.LabFile
$modulePath = Join-Path $repoRoot $labInfo.ModuleFile

if (-not (Test-Path $labGuidePath)) {
    throw "Lab guide not found: $labGuidePath"
}
if (-not (Test-Path $modulePath)) {
    throw "Module file not found: $modulePath"
}

$readmeContent = @"
# Lab $LabNumber Workspace

Lab: $($labInfo.Title)

This folder was created to give you a consistent starting point for the lab.

## References
- Lab guide: $labGuidePath
- Module: $modulePath

## Suggested next steps
1. Review the lab guide and module content.
2. Confirm the required prerequisites and tools are available.
3. Create or update any starter files required by the lab.
4. Run the assessment script after completing the work.

## Notes
Use this file for your working notes, screenshots, commands, and evidence.
"@

$readmePath = Join-Path $resolvedTarget 'README.md'
Set-Content -Path $readmePath -Value $readmeContent -Encoding UTF8

$notesPath = Join-Path $resolvedTarget 'lab-notes.md'
Set-Content -Path $notesPath -Value "# Lab $LabNumber Notes

Capture your commands, observations, and evidence here.
" -Encoding UTF8

$statePath = Join-Path $resolvedTarget 'lab-state.json'
$state = [ordered]@{
    labNumber = $LabNumber
    title = $labInfo.Title
    createdAtUtc = [DateTime]::UtcNow.ToString('o')
    labGuide = $labGuidePath
    moduleFile = $modulePath
    workspacePath = $resolvedTarget
}
$state | ConvertTo-Json | Set-Content -Path $statePath -Encoding UTF8

Write-Host "Prepared lab workspace for Lab $LabNumber" -ForegroundColor Green
Write-Host "Workspace: $resolvedTarget" -ForegroundColor Green
Write-Host "README: $readmePath" -ForegroundColor Green

if ($OpenInExplorer) {
    Invoke-Item $resolvedTarget
}
