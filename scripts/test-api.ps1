[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$apiDir = Join-Path $repoRoot "apps\api"
$pythonExe = Join-Path $apiDir ".venv\Scripts\python.exe"

if (-not (Test-Path $pythonExe)) {
  throw "API virtual environment not found. Run .\scripts\setup.ps1 first."
}

Push-Location $apiDir
try {
  & $pythonExe -m pytest
}
finally {
  Pop-Location
}
