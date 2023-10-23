from fastapi import FastAPI
from src.infrastructure import healthCheck
from src.application.coverLetterCreator import coverLetter
from src.application.carValuationApp import carValuation
from src.application.stockPricePrediction import microsoftStock
from src.application.blackScholesPricing import blackScholesPricing

app = FastAPI(
    title="Backend APIs For X",
    description="""This is just a test api""",
    version="0.1.0",
    # docs_url=None,
    openapi_url="/api/openapi.json"
)

app.include_router(healthCheck.router)
app.include_router(coverLetter.router)
app.include_router(carValuation.router)
app.include_router(microsoftStock.router)
app.include_router(blackScholesPricing.router)
