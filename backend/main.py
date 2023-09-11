from fastapi import FastAPI
from src.infrastructure import healthcheck

app = FastAPI(
    title="Backend For X",
    description="""This is just a test api""",
    version="0.1.0",
)

app.include_router(healthcheck.router)
