Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$scripts = @(
    "test-lab-01.ps1",
    "test-lab-02.ps1",
    "test-lab-03.ps1",
    "test-lab-04.ps1",
    "test-lab-05.ps1",
    "test-lab-06.ps1",
    "test-lab-07.ps1",
    "test-lab-08.ps1",
    "test-lab-09.ps1",
    "test-lab-10.ps1"
)

$results = @()

foreach ($script in $scripts) {
    Write-Host "`nRunning $script" -ForegroundColor Cyan
    try {
        & (Join-Path $PSScriptRoot $script)
        $results += [PSCustomObject]@{
            Script = $script
            Status = "PASS"
            Message = ""
        }
    }
    catch {
        $results += [PSCustomObject]@{
            Script = $script
            Status = "FAIL"
            Message = $_.Exception.Message
        }
        Write-Host "[FAIL] $script - $($_.Exception.Message)" -ForegroundColor Red
    }
}

$passCount = @($results | Where-Object { $_.Status -eq "PASS" }).Count
$failCount = @($results | Where-Object { $_.Status -eq "FAIL" }).Count

Write-Host "`nLab check summary" -ForegroundColor Cyan
$results | Format-Table -AutoSize

if ($failCount -gt 0) {
    throw "Lab checks completed with failures. Passed: $passCount, Failed: $failCount"
}

Write-Host "`nAll lab checks completed successfully. Passed: $passCount" -ForegroundColor Green
