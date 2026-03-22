[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$apiDir = Join-Path $repoRoot "apps\api"
$webDir = Join-Path $repoRoot "apps\web"
$venvDir = Join-Path $apiDir ".venv"
$activateScript = Join-Path $venvDir "Scripts\Activate.ps1"
$pythonExe = Join-Path $venvDir "Scripts\python.exe"

function Copy-EnvIfMissing {
  param(
    [Parameter(Mandatory = $true)]
    [string]$Directory
  )

  $examplePath = Join-Path $Directory ".env.example"
  $envPath = Join-Path $Directory ".env"

  if ((Test-Path $examplePath) -and (-not (Test-Path $envPath))) {
    Copy-Item $examplePath $envPath
    Write-Host "Created $envPath from .env.example"
  }
}

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
  throw "Python was not found on PATH. Install Python 3.11+ and re-run .\scripts\setup.ps1."
}

$pnpm = Get-Command pnpm -ErrorAction SilentlyContinue
if (-not $pnpm) {
  throw "pnpm was not found on PATH. Install pnpm and re-run .\scripts\setup.ps1."
}

if (-not (Test-Path $venvDir)) {
  Write-Host "Creating API virtual environment..."
  Push-Location $apiDir
  python -m venv .venv
  Pop-Location
}

if (-not (Test-Path $activateScript)) {
  throw "Virtual environment activation script not found at $activateScript."
}

Write-Host "Activating API virtual environment..."
. $activateScript

Write-Host "Installing API dependencies..."
& $pythonExe -m pip install --upgrade pip
& $pythonExe -m pip install -r (Join-Path $apiDir "requirements.txt")

Write-Host "Installing web dependencies with pnpm..."
Push-Location $webDir
pnpm install
Pop-Location

Copy-EnvIfMissing -Directory $apiDir
Copy-EnvIfMissing -Directory $webDir

Write-Host "Setup complete."
