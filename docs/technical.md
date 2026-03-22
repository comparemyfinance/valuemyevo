# EvoWorth Technical Notes

## Monorepo layout

- `apps/web`: Next.js frontend using the App Router and TypeScript
- `apps/api`: FastAPI backend with a minimal ASGI entrypoint
- `docs`: Product and technical documentation
- `scripts`: Windows-first setup and development scripts

## Current architecture

- The web app is a thin landing page shell.
- The API exposes root and health endpoints for service checks.
- Environment variables are app-local and documented with `.env.example` files.

## Next recommended steps

- Add API versioning and settings management
- Add frontend data-fetching boundary for API integration
- Add testing and linting for the Python service

