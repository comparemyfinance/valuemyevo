# EvoWorth

Minimal production-minded monorepo foundation for EvoWorth.

## Structure

```text
apps/
  api/   FastAPI backend with routers, services, adapters, schemas, utils, and tests
  web/   Next.js App Router frontend
docs/    Product and technical documentation
scripts/ Windows setup and development scripts
```

## Prerequisites

- Node.js 20+
- npm 10+
- Python 3.11+ for the API

## Setup

Run the Windows setup script:

```powershell
.\scripts\setup.ps1
```

This will:

- create `apps/api/.venv` if it does not exist
- install Python dependencies from `apps/api/requirements.txt`
- install web dependencies with `pnpm` in `apps/web`
- copy each app's `.env.example` to `.env` if missing

## Run locally

Start both services from the repo root:

```powershell
.\scripts\dev.ps1
```

Default local URLs:

- Web: [http://localhost:3000](http://localhost:3000)
- API: [http://localhost:8000](http://localhost:8000)
- API health: [http://localhost:8000/health](http://localhost:8000/health)
- API valuation summary: [http://localhost:8000/valuation/summary](http://localhost:8000/valuation/summary)

## Engineering conventions

- Use typed interfaces and response models.
- Keep files small and focused.
- Keep routers thin and free of business logic.
- Services call adapters.
- Adapters normalize data before it leaves the service boundary.
- Shared parsing and median helpers live under `utils`.
- Runtime configuration comes from environment variables.
- Keep naming stable and explicit.

## Notes

- Docker is intentionally not included yet.
- Auth is intentionally not included yet.
- Scraping logic is intentionally not included yet.
