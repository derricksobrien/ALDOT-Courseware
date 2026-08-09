<#
.SYNOPSIS
    Sets up the reference repositories required for the MVP modernization course labs.

.DESCRIPTION
    This script initialises the git submodules (eShopOnWeb and s2i-dotnetcore-ex)
    and verifies that the required tools are available. Run this script once at the
    start of the course before opening any lab.

.PARAMETER SkipSubmodules
    Skip the git submodule initialisation step (useful if repos are already present).

.PARAMETER SkipToolCheck
    Skip the tool availability check.

.EXAMPLE
    .\Setup-LabRepos.ps1

.EXAMPLE
    .\Setup-LabRepos.ps1 -SkipToolCheck
#>
[CmdletBinding()]
param(
    [switch]$SkipSubmodules,
    [switch]$SkipToolCheck
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path

function Write-Step {
    param([string]$Message)
    Write-Host "`n==> $Message" -ForegroundColor Cyan
}

function Write-OK {
    param([string]$Message)
    Write-Host "[OK] $Message" -ForegroundColor Green
}

function Write-Warn {
    param([string]$Message)
    Write-Host "[WARN] $Message" -ForegroundColor Yellow
}

function Write-Fail {
    param([string]$Message)
    Write-Host "[FAIL] $Message" -ForegroundColor Red
}

# ── Tool check ────────────────────────────────────────────────────────────────

if (-not $SkipToolCheck) {
    Write-Step "Checking required tools"

    $required = @(
        @{ Command = 'git';    Label = 'Git' },
        @{ Command = 'dotnet'; Label = '.NET SDK' },
        @{ Command = 'docker'; Label = 'Docker (optional)' }
    )

    foreach ($tool in $required) {
        $cmd = Get-Command $tool.Command -ErrorAction SilentlyContinue
        if ($cmd) {
            Write-OK "$($tool.Label) found at $($cmd.Source)"
        } else {
            if ($tool.Command -eq 'docker') {
                Write-Warn "$($tool.Label) not found — required for Lab 06 onwards"
            } else {
                Write-Fail "$($tool.Label) not found — please install before continuing"
                throw "Missing required tool: $($tool.Command)"
            }
        }
    }
}

# ── Submodule initialisation ──────────────────────────────────────────────────

if (-not $SkipSubmodules) {
    Write-Step "Initialising git submodules (eShopOnWeb and s2i-dotnetcore-ex)"

    $gitModulesPath = Join-Path $repoRoot '.gitmodules'
    if (-not (Test-Path $gitModulesPath)) {
        Write-Warn ".gitmodules not found at repo root. Falling back to manual clone."
        $fallback = $true
    } else {
        try {
            Push-Location $repoRoot
            git submodule update --init --recursive 2>&1 | ForEach-Object { Write-Host $_ }
            Pop-Location
            Write-OK "Submodules initialised"
            $fallback = $false
        } catch {
            Write-Warn "Submodule init failed: $($_.Exception.Message). Falling back to manual clone."
            $fallback = $true
        }
    }

    if ($fallback) {
        Write-Step "Falling back to manual clone of reference repositories"

        $repos = @(
            @{
                Url    = 'https://github.com/dotnet-architecture/eShopOnWeb.git'
                Target = Join-Path $repoRoot 'course\repos\eShopOnWeb'
                Label  = 'eShopOnWeb'
            },
            @{
                Url    = 'https://github.com/redhat-developer/s2i-dotnetcore-ex.git'
                Target = Join-Path $repoRoot 'course\repos\s2i-dotnetcore-ex'
                Label  = 's2i-dotnetcore-ex'
            }
        )

        foreach ($repo in $repos) {
            if (Test-Path (Join-Path $repo.Target '.git')) {
                Write-OK "$($repo.Label) already cloned at $($repo.Target)"
            } else {
                New-Item -ItemType Directory -Path $repo.Target -Force | Out-Null
                git clone $repo.Url $repo.Target 2>&1 | ForEach-Object { Write-Host $_ }
                Write-OK "Cloned $($repo.Label) to $($repo.Target)"
            }
        }
    }
}

# ── Verify repo content ───────────────────────────────────────────────────────

Write-Step "Verifying reference repositories"

$checks = @(
    @{ Path = Join-Path $repoRoot 'course\repos\eShopOnWeb\eShopOnWeb.sln'; Label = 'eShopOnWeb solution file' },
    @{ Path = Join-Path $repoRoot 'course\repos\s2i-dotnetcore-ex\README.md'; Label = 's2i-dotnetcore-ex README' }
)

$allGood = $true
foreach ($check in $checks) {
    if (Test-Path $check.Path) {
        Write-OK "$($check.Label) found"
    } else {
        Write-Warn "$($check.Label) not found at $($check.Path)"
        $allGood = $false
    }
}

# ── Summary ───────────────────────────────────────────────────────────────────

Write-Host ""
if ($allGood) {
    Write-Host "Lab environment ready. You can now open any lab guide and begin." -ForegroundColor Green
} else {
    Write-Host "Setup completed with warnings. Check the output above before starting labs." -ForegroundColor Yellow
}
