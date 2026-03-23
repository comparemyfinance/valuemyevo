[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$apiDir = Join-Path $repoRoot "apps\api"
$pythonExe = Join-Path $apiDir ".venv\Scripts\python.exe"
$apiEnvPath = Join-Path $apiDir ".env"

function Get-EnvFileValue {
  param(
    [Parameter(Mandatory = $true)]
    [string]$FilePath,
    [Parameter(Mandatory = $true)]
    [string]$VariableName
  )

  if (-not (Test-Path $FilePath)) {
    return $null
  }

  foreach ($line in Get-Content $FilePath) {
    if ($line -match "^\s*$VariableName=(.+)$") {
      return $matches[1].Trim()
    }
  }

  return $null
}

if (-not (Test-Path $pythonExe)) {
  throw "API virtual environment not found. Run .\scripts\setup.ps1 first."
}

$npm = Get-Command npm -ErrorAction SilentlyContinue
if (-not $npm) {
  throw "npm was not found on PATH. Install Node.js 20+ and re-run .\scripts\dev.ps1."
}

$apiPort = Get-EnvFileValue -FilePath $apiEnvPath -VariableName "APP_PORT"
if (-not $apiPort) {
  $apiPort = "8000"
}

$apiCommand = "& `"$pythonExe`" -m uvicorn app.main:app --reload --host 0.0.0.0 --port $apiPort"
$webCommand = "npm run dev:web -- --port 3000"

Start-Process powershell -WorkingDirectory $apiDir -ArgumentList @(
  "-NoExit",
  "-ExecutionPolicy", "Bypass",
  "-Command", $apiCommand
)

Start-Process powershell -WorkingDirectory $repoRoot -ArgumentList @(
  "-NoExit",
  "-ExecutionPolicy", "Bypass",
  "-Command", $webCommand
)

Write-Host "Started API on http://localhost:$apiPort and web on http://localhost:3000"
