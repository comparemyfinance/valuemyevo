# EvoWorth

EvoWorth is an early-stage product for understanding and comparing the evolving value of financial opportunities. This repo is the foundation for that product: a public web app, a Python API, and a clean monorepo layout designed for further product development.

## What exists today

- `apps/web` is a Next.js App Router frontend with a simple landing page.
- `apps/api` is a FastAPI backend with health endpoints and sample valuation endpoints.
- `scripts/setup.ps1` installs dependencies and prepares local env files on Windows.
- `scripts/dev.ps1` starts both local apps in separate PowerShell windows.

## What is sample data vs not implemented yet

- Sample data:
  - The valuation endpoints return sample prices and comparables driven by environment variables.
- Implemented:
  - Web landing page
  - API root endpoint
  - API health, liveness, and readiness endpoints
  - API valuation endpoints at `/valuation` and `/valuation/evo`
  - Local Windows setup and dev scripts
- Not implemented yet:
  - Authentication
  - Scraping logic
  - Real valuation pipelines or persistent storage
  - Payments
  - Admin tooling
  - Docker

## Repo structure

```text
apps/
  api/
    app/
      adapters/   normalize outbound data
      config/     environment-backed settings
      routers/    HTTP route wiring only
      schemas/    typed response contracts
      services/   business flow
      utils/      parsing and median helpers
    tests/        baseline API tests
  web/
    app/          Next.js App Router pages and layout
    lib/          typed frontend config and content
docs/             product and technical notes
scripts/          Windows setup and local dev scripts
```

## Windows prerequisites

Install these before running any repo scripts:

- Node.js 20+
- Python 3.11+

Useful checks:

```powershell
node --version
npm --version
python --version
```

If PowerShell blocks local scripts, open PowerShell as your user and run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Setup on Windows

From the repo root, run:

```powershell
.\scripts\setup.ps1
```

Or:

```powershell
npm run setup:windows
```

`setup.ps1` does the following:

- creates `apps/api/.venv` if it does not already exist
- installs Python dependencies from `apps/api/requirements.txt`
- installs root and workspace Node dependencies with `npm`
- copies `apps/api/.env.example` to `apps/api/.env` if missing
- copies `apps/web/.env.example` to `apps/web/.env` if missing

After setup, review these files if you want to change local defaults:

- `apps/api/.env`
- `apps/web/.env`

## Start both apps locally

From the repo root, run:

```powershell
.\scripts\dev.ps1
```

Or:

```powershell
npm run dev
```

`dev.ps1` opens two PowerShell windows:

- API: FastAPI with Uvicorn on `http://localhost:8000` by default, or `APP_PORT` from `apps/api/.env`
- Web: Next.js dev server on `http://localhost:3000`

Local endpoints:

- Web: [http://localhost:3000](http://localhost:3000)
- API root: [http://localhost:8000](http://localhost:8000)
- API health: [http://localhost:8000/health](http://localhost:8000/health)
- API liveness: [http://localhost:8000/health/live](http://localhost:8000/health/live)
- API readiness: [http://localhost:8000/health/ready](http://localhost:8000/health/ready)
- API valuation: `POST /valuation`
- API valuation alias: `POST /valuation/evo`

## Run checks

From the repo root:

```powershell
npm run lint:web
npm run test:api
```

## Engineering conventions

- Use typed interfaces and typed response models.
- Keep files small and explicit.
- Keep business logic out of routers.
- Services call adapters.
- Adapters normalize data.
- Shared parsing and median helpers live under `utils`.
- Runtime config comes from environment variables.
- Keep naming stable and explicit.
