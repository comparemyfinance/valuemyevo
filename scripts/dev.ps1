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
$apiEnvFile = Join-Path $apiDir ".env"

function Get-EnvironmentValue {
  param(
    [Parameter(Mandatory = $true)]
    [string]$FilePath,
    [Parameter(Mandatory = $true)]
    [string]$Key
  )

  if (-not (Test-Path $FilePath)) {
    return $null
  }

  $matchingLine = Get-Content $FilePath |
    Where-Object { $_ -match "^\s*$Key=" } |
    Select-Object -First 1

  if (-not $matchingLine) {
    return $null
  }

  return ($matchingLine -split "=", 2)[1].Trim()
}

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

    $apiPort = Get-EnvironmentValue -FilePath $apiEnvFile -Key "APP_PORT"
    if (-not $apiPort) {
      $apiPort = "8000"
    }

    Push-Location $apiDir
    & $pythonExe -m uvicorn app.main:app --reload --host 0.0.0.0 --port $apiPort
    Pop-Location
  }
}

