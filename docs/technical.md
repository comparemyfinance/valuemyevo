# EvoWorth Technical Notes

## Monorepo layout

- `apps/web`: Next.js frontend using the App Router and TypeScript
- `apps/api`: FastAPI backend with routers, services, adapters, schemas, utils, and tests
- `docs`: Product and technical documentation
- `scripts`: Windows-first setup and development scripts

## Current architecture

- The web app is a thin landing page shell.
- The API exposes root, health, and evo valuation endpoints.
- Environment variables are app-local and documented with `.env.example` files.
- The API keeps HTTP wiring in routers, business flow in services, data normalization in adapters, typed contracts in schemas, and shared parsing and median helpers in utils.
- The valuation API contract is `POST /valuation/evo`, built around `EvoCardInput`, `SourcePrice`, `ComparableCard`, and `ValuationResponse`.

## Next recommended steps

- Add API versioning and settings management
- Add frontend data-fetching boundary for API integration
- Expand Python coverage beyond the baseline utility and response-shape tests

