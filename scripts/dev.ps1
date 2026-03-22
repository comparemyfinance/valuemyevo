[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)]
  [ValidateSet("web", "api")]
  [string]$Target
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$apiDir = Join-Path $repoRoot "apps\api"
$webDir = Join-Path $repoRoot "apps\web"
$pythonExe = Join-Path $apiDir ".venv\Scripts\python.exe"

switch ($Target) {
  "web" {
    Push-Location $repoRoot
    npm --workspace @evoworth/web run dev
    Pop-Location
  }
  "api" {
    if (-not (Test-Path $pythonExe)) {
      throw "API virtual environment not found. Run .\scripts\setup.ps1 first."
    }

    Push-Location $apiDir
    & $pythonExe -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    Pop-Location
  }
}

