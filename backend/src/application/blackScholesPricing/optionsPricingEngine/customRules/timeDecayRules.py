from src.application.blackScholesPricing.optionsPricingEngine.recommendation.rule import Rule

rules = [
    Rule(
        name="High Time Decay for Near Expiry (BlackScholes & GarmanKohlhagen)",
        condition=lambda data: data["timeToExpirationYr"] < 0.08
        and data["modelName"] in ["BlackScholes", "GarmanKohlhagen"],
        action=lambda data: (
            f"[{data['modelName']}] The option is nearing its expiration date with only {data['timeToExpirationYr']*365} days left. "
            f"Expect a rapid time decay. Consider selling if holding, or be cautious when buying.",
            0.08,
            data["timeToExpirationYr"],
        ),
    ),
    Rule(
        name="High Time Decay for Near Expiry (Black76)",
        condition=lambda data: data["timeToExpirationYr"] < 0.08
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[Black76] The futures option is nearing its expiration date with only {data['timeToExpirationYr']*365} days left. "
            f"Expect a rapid time decay. Consider selling if holding, or be cautious when buying.",
            0.08,
            data["timeToExpirationYr"],
        ),
    ),
    Rule(
        name="Moderate Time Decay for Medium Term (BlackScholes & GarmanKohlhagen)",
        condition=lambda data: 0.08 <= data["timeToExpirationYr"] < 0.25
        and data["modelName"] in ["BlackScholes", "GarmanKohlhagen"],
        action=lambda data: (
            f"[{data['modelName']}] The option has a moderate time to expiration with {data['timeToExpirationYr']*365} days left. "
            f"Time decay will be noticeable but not as rapid. Monitor closely.",
            0.25,
            data["timeToExpirationYr"],
        ),
    ),
    Rule(
        name="Moderate Time Decay for Medium Term (Black76)",
        condition=lambda data: 0.08 <= data["timeToExpirationYr"] < 0.25
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[Black76] The futures option has a moderate time to expiration with {data['timeToExpirationYr']*365} days left. "
            f"Time decay will be noticeable but not as rapid. Monitor closely.",
            0.25,
            data["timeToExpirationYr"],
        ),
    ),
    Rule(
        name="Low Time Decay for Long Term (BlackScholes & GarmanKohlhagen)",
        condition=lambda data: data["timeToExpirationYr"] >= 0.25
        and data["modelName"] in ["BlackScholes", "GarmanKohlhagen"],
        action=lambda data: (
            f"[{data['modelName']}] The option has a longer time to expiration with {data['timeToExpirationYr']*365} days left. "
            f"Time decay is slower. This offers more time to make decisions based on other factors.",
            0.25,
            data["timeToExpirationYr"],
        ),
    ),
    Rule(
        name="Low Time Decay for Long Term (Black76)",
        condition=lambda data: data["timeToExpirationYr"] >= 0.25
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[Black76] The futures option has a longer time to expiration with {data['timeToExpirationYr']*365} days left. "
            f"Time decay is slower. This offers more time to make decisions based on other factors.",
            0.25,
            data["timeToExpirationYr"],
        ),
    ),
]
