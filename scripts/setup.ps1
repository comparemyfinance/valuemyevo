[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$apiDir = Join-Path $repoRoot "apps\api"
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

function Get-PythonBootstrapCommand {
  $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
  if ($pythonCommand) {
    return @{
      Executable = $pythonCommand.Source
      Arguments = @()
    }
  }

  $pyLauncher = Get-Command py -ErrorAction SilentlyContinue
  if ($pyLauncher) {
    return @{
      Executable = $pyLauncher.Source
      Arguments = @("-3")
    }
  }

  throw "Python was not found on PATH. Install Python 3.11+ and re-run .\scripts\setup.ps1."
}

$npm = Get-Command npm -ErrorAction SilentlyContinue
if (-not $npm) {
  throw "npm was not found on PATH. Install Node.js 20+ and re-run .\scripts\setup.ps1."
}

$pythonBootstrap = Get-PythonBootstrapCommand

if (-not (Test-Path $venvDir)) {
  Write-Host "Creating API virtual environment..."
  Push-Location $apiDir
  & $pythonBootstrap.Executable @($pythonBootstrap.Arguments + @("-m", "venv", ".venv"))
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

Write-Host "Installing repo dependencies with npm..."
Push-Location $repoRoot
npm install
Pop-Location

Copy-EnvIfMissing -Directory $apiDir
Copy-EnvIfMissing -Directory (Join-Path $repoRoot "apps\web")

Write-Host "Setup complete."
