[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$apiDir = Join-Path $repoRoot "apps\api"
$webDir = Join-Path $repoRoot "apps\web"
$venvDir = Join-Path $apiDir ".venv"
$pythonExe = Join-Path $venvDir "Scripts\python.exe"

Write-Host "Installing web dependencies..."
Push-Location $repoRoot
npm install
Pop-Location

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
  Write-Warning "Python was not found. Web setup completed, but API setup was skipped."
  Write-Warning "Install Python 3.11+ and re-run .\scripts\setup.ps1 to prepare the API environment."
  exit 0
}

if (-not (Test-Path $venvDir)) {
  Write-Host "Creating API virtual environment..."
  Push-Location $apiDir
  python -m venv .venv
  Pop-Location
}

Write-Host "Installing API dependencies..."
& $pythonExe -m pip install --upgrade pip
& $pythonExe -m pip install -r (Join-Path $apiDir "requirements.txt")

Write-Host "Setup complete."

