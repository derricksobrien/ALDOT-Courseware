[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^\d{2}$')]
    [string]$LabNumber,

    [string]$StudentPath,

    [string]$OutputPath,

    [switch]$SkipAi
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$labTestScript = Join-Path $repoRoot "course\mvp-delivery\tests\test-lab-$LabNumber.ps1"

if (-not (Test-Path $labTestScript)) {
    throw "No matching validation script found: $labTestScript"
}

if ([string]::IsNullOrWhiteSpace($StudentPath)) {
    $StudentPath = Join-Path $repoRoot "course\mvp-delivery\student-work\lab-$LabNumber"
}

$resolvedStudentPath = [System.IO.Path]::GetFullPath($StudentPath)
if (-not (Test-Path $resolvedStudentPath)) {
    New-Item -ItemType Directory -Path $resolvedStudentPath -Force | Out-Null
}

if ([string]::IsNullOrWhiteSpace($OutputPath)) {
    $OutputPath = Join-Path $resolvedStudentPath 'assessment-report.md'
}

$resolvedOutputPath = [System.IO.Path]::GetFullPath($OutputPath)
$reportDir = Split-Path $resolvedOutputPath -Parent
New-Item -ItemType Directory -Path $reportDir -Force | Out-Null

$validationSummary = ''
$validationStatus = 'passed'

try {
    $validationOutput = & $labTestScript 2>&1 | Out-String
    $validationSummary = $validationOutput.Trim()
}
catch {
    $validationStatus = 'failed'
    $validationSummary = $_.Exception.Message
}

$artifacts = @()
if (Test-Path $resolvedStudentPath) {
    $artifacts = @(Get-ChildItem -Path $resolvedStudentPath -Recurse -File | Select-Object -ExpandProperty FullName)
}

$artifactSummary = if ($artifacts.Count -gt 0) {
    $artifacts | ForEach-Object { "- $_" } | Out-String
} else {
    '- No workspace artifacts found.'
}

function Invoke-AiAssessment {
    param(
        [string]$LabNumber,
        [string]$ValidationStatus,
        [string]$ValidationSummary,
        [string]$ArtifactSummary
    )

    $openAiKey = $env:OPENAI_API_KEY
    $azureEndpoint = $env:AZURE_OPENAI_ENDPOINT
    $azureKey = $env:AZURE_OPENAI_API_KEY
    $azureDeployment = $env:AZURE_OPENAI_DEPLOYMENT

    if (-not [string]::IsNullOrWhiteSpace($openAiKey)) {
        $payload = [ordered]@{
            model = 'gpt-4o-mini'
            messages = @(
                [ordered]@{ role = 'system'; content = 'You are a supportive lab coach. Evaluate the learner work briefly and provide 3 bullet points: strengths, gaps, and next steps.' },
                [ordered]@{ role = 'user'; content = "Lab number: $LabNumber`nValidation status: $ValidationStatus`nValidation summary: $ValidationSummary`nArtifacts:`n$ArtifactSummary" }
            )
            temperature = 0.2
        }

        try {
            $headers = @{ Authorization = "Bearer $openAiKey" }
            $response = Invoke-RestMethod -Method Post -Uri 'https://api.openai.com/v1/chat/completions' -Headers $headers -ContentType 'application/json' -Body ($payload | ConvertTo-Json -Depth 10)
            return $response.choices[0].message.content
        }
        catch {
            return "AI evaluation requested but failed: $($_.Exception.Message)"
        }
    }

    if (-not [string]::IsNullOrWhiteSpace($azureEndpoint) -and -not [string]::IsNullOrWhiteSpace($azureKey) -and -not [string]::IsNullOrWhiteSpace($azureDeployment)) {
        $uri = "$azureEndpoint/openai/deployments/$azureDeployment/chat/completions?api-version=2024-02-01"
        $payload = [ordered]@{
            messages = @(
                [ordered]@{ role = 'system'; content = 'You are a supportive lab coach. Evaluate the learner work briefly and provide 3 bullet points: strengths, gaps, and next steps.' },
                [ordered]@{ role = 'user'; content = "Lab number: $LabNumber`nValidation status: $ValidationStatus`nValidation summary: $ValidationSummary`nArtifacts:`n$ArtifactSummary" }
            )
            temperature = 0.2
        }

        try {
            $headers = @{ 'api-key' = $azureKey }
            $response = Invoke-RestMethod -Method Post -Uri $uri -Headers $headers -ContentType 'application/json' -Body ($payload | ConvertTo-Json -Depth 10)
            return $response.choices[0].message.content
        }
        catch {
            return "Azure OpenAI evaluation requested but failed: $($_.Exception.Message)"
        }
    }

    return 'AI evaluation skipped. Set OPENAI_API_KEY or AZURE_OPENAI_ENDPOINT/AZURE_OPENAI_API_KEY/AZURE_OPENAI_DEPLOYMENT to enable it.'
}

$aiEvaluation = ''
if (-not $SkipAi) {
    $aiEvaluation = Invoke-AiAssessment -LabNumber $LabNumber -ValidationStatus $validationStatus -ValidationSummary $validationSummary -ArtifactSummary $artifactSummary
}
else {
    $aiEvaluation = 'AI evaluation skipped. Re-run with -SkipAi:$false after configuring an AI provider.'
}

$recommendations = @()
if ($validationStatus -eq 'passed') {
    $recommendations += '- Validation checks passed. Capture evidence and share the report with the instructor.'
}
else {
    $recommendations += '- Review the validation output and address the failed checks before submission.'
    $recommendations += '- Compare the generated artifacts with the lab guide and add any missing evidence.'
}

$reportContent = @"
# Lab $LabNumber Assessment Report

- Generated: $(Get-Date -Format o)
- Workspace: $resolvedStudentPath
- Validation status: $validationStatus

## Validation output

```text
$validationSummary
```

## Workspace artifacts

$artifactSummary

## AI evaluation

$aiEvaluation

## Recommended next steps

$($recommendations -join [Environment]::NewLine)
"@

Set-Content -Path $resolvedOutputPath -Value $reportContent -Encoding UTF8

$summaryPath = Join-Path $resolvedStudentPath 'assessment-summary.json'
$summaryObject = [ordered]@{
    labNumber = $LabNumber
    workspacePath = $resolvedStudentPath
    validationStatus = $validationStatus
    validationScript = $labTestScript
    reportPath = $resolvedOutputPath
    generatedAtUtc = [DateTime]::UtcNow.ToString('o')
}
$summaryObject | ConvertTo-Json | Set-Content -Path $summaryPath -Encoding UTF8

Write-Host "Assessment report written to $resolvedOutputPath" -ForegroundColor Green
Write-Host "Summary written to $summaryPath" -ForegroundColor Green
