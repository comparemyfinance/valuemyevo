[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$apiDir = Join-Path $repoRoot "apps\api"
$webDir = Join-Path $repoRoot "apps\web"
$pythonExe = Join-Path $apiDir ".venv\Scripts\python.exe"

if (-not (Test-Path $pythonExe)) {
  throw "API virtual environment not found. Run .\scripts\setup.ps1 first."
}

$apiCommand = "& `"$pythonExe`" -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
$webCommand = "pnpm dev -- --port 3000"

Start-Process powershell -WorkingDirectory $apiDir -ArgumentList @(
  "-NoExit",
  "-ExecutionPolicy", "Bypass",
  "-Command", $apiCommand
)

Start-Process powershell -WorkingDirectory $webDir -ArgumentList @(
  "-NoExit",
  "-ExecutionPolicy", "Bypass",
  "-Command", $webCommand
)

Write-Host "Started API on http://localhost:8000 and web on http://localhost:3000"
