from pydantic import BaseModel, Field, validator
from typing import Literal


class OptionCalculatorModel(BaseModel):
    modelName: str = Field(...,
                           description="Name of the option pricing model, e.g., BlackScholes")
    stockPrice: float = Field(..., gt=0,
                              description="Current stock or futures price.")
    strikePrice: float = Field(..., gt=0, description="Option strike price.")
    timeToExpirationYr: float = Field(..., gt=0,
                                      description="Time to expiration in years.")
    riskFreeRate: float = Field(..., ge=0, le=1,
                                description="Annual domestic risk-free rate.")
    volatility: float = Field(..., ge=0, le=1,
                              description="Annual volatility of the stock or futures.")
    dividendYield: float = Field(
        0.0, ge=0, le=1, description="Continuous dividend yield.")
    foreignRiskFreeRate: float = Field(
        0.0, ge=0, le=1, description="Annual foreign risk-free rate.")
    optionType: Literal["call",
                        "put"] = Field(..., description="Type of the option.")

    @validator("foreignRiskFreeRate", pre=True, always=True)
    def validate_foreignRiskFreeRate(cls, value, values):
        modelName = values.get('modelName')
        if modelName == "GarmanKohlhagen":
            if value is None:
                raise ValueError(
                    "foreignRiskFreeRate must be provided for GarmanKohlhagen model.")
        return value
