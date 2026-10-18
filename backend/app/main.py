"""FastAPI application entrypoint."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_PREFIX}/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["health"])
def health_check() -> dict:
    """Liveness/readiness probe used by docker-compose and CI."""
    return {"status": "ok", "environment": settings.ENVIRONMENT}


@app.get("/", tags=["health"])
def root() -> dict:
    return {"service": settings.PROJECT_NAME, "status": "running"}
