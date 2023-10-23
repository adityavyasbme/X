from src.application.blackScholesPricing.optionsPricingEngine.recommendation.rule import Rule

rules = [
    Rule(
        name="Positive Rho Sensitivity for Call Options (Black-Scholes)",
        condition=lambda data: data["optionType"] == "call"
        and data["modelName"] == "BlackScholes",
        action=lambda data: (
            f"[{data['modelName']}] A rise in the risk-free rate can increase the call option's price. "
            f"With a current risk-free rate of {data['riskFreeRate']*100}%, consider the potential impact on the option price if rates rise.",
            data["riskFreeRate"],
            data["riskFreeRate"],
        ),
    ),
    Rule(
        name="Negative Rho Sensitivity for Put Options (Black-Scholes)",
        condition=lambda data: data["optionType"] == "put"
        and data["modelName"] == "BlackScholes",
        action=lambda data: (
            f"[{data['modelName']}] An increase in the risk-free rate can decrease the put option's price. "
            f"With a current risk-free rate of {data['riskFreeRate']*100}%, consider the potential impact on the option price if rates increase.",
            data["riskFreeRate"],
            data["riskFreeRate"],
        ),
    ),
    Rule(
        name="Positive Rho Sensitivity for Call Options (Black76)",
        condition=lambda data: data["optionType"] == "call"
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[{data['modelName']}] A rise in the risk-free rate can increase the call option's price in futures. "
            f"With a current risk-free rate of {data['riskFreeRate']*100}%, consider the potential impact on the option price if rates rise.",
            data["riskFreeRate"],
            data["riskFreeRate"],
        ),
    ),
    Rule(
        name="Negative Rho Sensitivity for Put Options (Black76)",
        condition=lambda data: data["optionType"] == "put"
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[{data['modelName']}] An increase in the risk-free rate can decrease the put option's price in futures. "
            f"With a current risk-free rate of {data['riskFreeRate']*100}%, consider the potential impact on the option price if rates rise.",
            data["riskFreeRate"],
            data["riskFreeRate"],
        ),
    ),
    Rule(
        name="Positive Rho Sensitivity for Call Options (GarmanKohlhagen)",
        condition=lambda data: data["optionType"] == "call"
        and data["modelName"] == "GarmanKohlhagen",
        action=lambda data: (
            f"[{data['modelName']}] The call option's price will increase as the domestic interest rate rises. "
            f"Consider this if you anticipate an increase in the domestic interest rate.",
            data["riskFreeRate"],
            data["rho"],  # assuming rho value is present in data
        ),
    ),
    Rule(
        name="Negative Rho Sensitivity for Put Options (GarmanKohlhagen)",
        condition=lambda data: data["optionType"] == "put"
        and data["modelName"] == "GarmanKohlhagen",
        action=lambda data: (
            f"[{data['modelName']}] The put option's price will decrease as the domestic interest rate rises. "
            f"Consider this if you anticipate an increase in the domestic interest rate.",
            data["riskFreeRate"],
            data["rho"],  # assuming rho value is present in data
        ),
    ),
    Rule(
        name="Dual Rho Sensitivity for Call Options (GarmanKohlhagen)",
        condition=lambda data: data["optionType"] == "call"
        and data["modelName"] == "GarmanKohlhagen",
        action=lambda data: (
            f"[{data['modelName']}] The call option's price is affected by both domestic and foreign interest rates. "
            f"Consider the interplay between the two when making decisions.",
            data["riskFreeRate"]
            - data["foreignRiskFreeRate"],  # difference as threshold
            data["rho"],  # assuming rho value is present in data
        ),
    ),
    Rule(
        name="Dual Rho Sensitivity for Put Options (GarmanKohlhagen)",
        condition=lambda data: data["optionType"] == "put"
        and data["modelName"] == "GarmanKohlhagen",
        action=lambda data: (
            f"[{data['modelName']}] The put option's price is affected by both domestic and foreign interest rates. "
            f"Consider the interplay between the two when making decisions.",
            data["riskFreeRate"]
            - data["foreignRiskFreeRate"],  # difference as threshold
            data["rho"],  # assuming rho value is present in data
        ),
    ),
]
