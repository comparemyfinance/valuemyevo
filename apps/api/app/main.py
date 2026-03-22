from fastapi import FastAPI


app = FastAPI(
    title="EvoWorth API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/", tags=["meta"])
def read_root() -> dict[str, str]:
    return {
        "name": "EvoWorth API",
        "status": "ok",
    }


@app.get("/health", tags=["meta"])
def health() -> dict[str, str]:
    return {
        "status": "ok",
    }


@app.get("/health/live", tags=["meta"])
def liveness() -> dict[str, str]:
    return {
        "status": "ok",
    }


@app.get("/health/ready", tags=["meta"])
def readiness() -> dict[str, str]:
    return {
        "status": "ok",
    }
