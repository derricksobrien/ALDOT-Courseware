Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Write-Section {
    param([string]$Message)
    Write-Host "`n=== $Message ===" -ForegroundColor Cyan
}

function Assert-PathExists {
    param(
        [string]$Path,
        [string]$Label
    )

    if (-not (Test-Path -Path $Path)) {
        throw "Missing required $Label at path: $Path"
    }
    Write-Host "[OK] Found ${Label}: $Path" -ForegroundColor Green
}

function Assert-CommandAvailable {
    param([string]$Command)

    $cmd = Get-Command $Command -ErrorAction SilentlyContinue
    if (-not $cmd) {
        throw "Missing required command: $Command"
    }
    Write-Host "[OK] Command available: $Command" -ForegroundColor Green
}

function Assert-TextInFile {
    param(
        [string]$Path,
        [string]$Pattern,
        [string]$Description
    )

    $match = Select-String -Path $Path -Pattern $Pattern -SimpleMatch -ErrorAction SilentlyContinue
    if (-not $match) {
        throw "Missing expected text for '$Description' in file: $Path"
    }
    Write-Host "[OK] Found expected text for $Description" -ForegroundColor Green
}

function Finish-Success {
    param([string]$LabName)
    Write-Host "`nPASS: $LabName checks completed." -ForegroundColor Green
}
