from src.application.blackScholesPricing.optionsPricingEngine.optionsCalculator import OptionCalculator
from src.application.blackScholesPricing.optionsPricingEngine.customRules.rules import rules
from src.application.blackScholesPricing.optionsPricingEngine.recommendation.recommendationEngine import RecommendationEngine
from src.application.blackScholesPricing.blackScholesPricingParams import OptionCalculatorModel

from fastapi import APIRouter

router = APIRouter()


@router.post("/api/optionPricingRecommendation")
def optionPricingRecommendation(oci: OptionCalculatorModel):
    ocip = oci.model_dump(mode='json')
    # Initialize the OptionCalculator
    calculator = OptionCalculator()
    # Select the desired option pricing model with its parameters
    # For this example, we'll use the Black-Scholes model for a call option
    calculator.select_model(
        modelName=ocip['modelName'],
        stockPrice=ocip["stockPrice"],               # Current stock price
        strikePrice=ocip["strikePrice"],              # Option strike price
        # Time to expiration in years
        timeToExpirationYr=ocip["timeToExpirationYr"],
        riskFreeRate=ocip["riskFreeRate"],            # Annual risk-free rate
        volatility=ocip["volatility"],               # Annual volatility
        # Continuous dividend yield
        dividendYield=ocip["dividendYield"],
        foreignRiskFreeRate=ocip["foreignRiskFreeRate"],
        # Option type (either "call" or "put")
        optionType=ocip["optionType"]
    )
    # Calculate both the option price and its Greeks in one go
    _ = calculator.calculate_price_and_greeks()
    engine = RecommendationEngine(rules=rules)
    data = calculator.modelResults
    data.update(calculator.modelParams)
    return engine.recommend(data)
