from src.application.blackScholesPricing.optionsPricingEngine.recommendation.rule import Rule

rules = [
    Rule(
        name="High Gamma for BlackScholes Model",
        condition=lambda data: data["gamma"] > 0.05
        and data["modelName"] == "BlackScholes",
        action=lambda data: (
            f"[BlackScholes] High gamma of {data['gamma']} indicates the option's delta is highly sensitive to price changes in the underlying asset. "
            f"This can be particularly relevant for short-term options, and can lead to rapid profits or losses.",
            0.05,
            data["gamma"],
        ),
    ),
    Rule(
        name="Low Gamma for BlackScholes Model",
        condition=lambda data: data["gamma"] < 0.01
        and data["modelName"] == "BlackScholes",
        action=lambda data: (
            f"[BlackScholes] Low gamma of {data['gamma']} suggests the option's delta has low sensitivity to price changes. "
            f"This might mean less risk from rapid price movements, but also potentially slower profits.",
            0.01,
            data["gamma"],
        ),
    ),
    Rule(
        name="High Gamma for Black76 Model",
        condition=lambda data: data["gamma"] > 0.05 and data["modelName"] == "Black76",
        action=lambda data: (
            f"[Black76] High gamma of {data['gamma']} for this futures option indicates a high sensitivity to price changes in the underlying future. "
            f"Traders need to be cautious of rapid price changes, as this can lead to quick profits or losses.",
            0.05,
            data["gamma"],
        ),
    ),
    Rule(
        name="Low Gamma for Black76 Model",
        condition=lambda data: data["gamma"] < 0.01 and data["modelName"] == "Black76",
        action=lambda data: (
            f"[Black76] Low gamma of {data['gamma']} for this futures option suggests the delta is less affected by price changes in the underlying future. "
            f"This can offer more stability against rapid price movements.",
            0.01,
            data["gamma"],
        ),
    ),
    Rule(
        name="High Gamma for GarmanKohlhagen Model",
        condition=lambda data: data["gamma"] > 0.05
        and data["modelName"] == "GarmanKohlhagen",
        action=lambda data: (
            f"[GarmanKohlhagen] High gamma of {data['gamma']} indicates the currency option's delta is highly sensitive to changes in the currency pair. "
            f"Such options can be affected rapidly by market movements, leading to potential quick gains or losses.",
            0.05,
            data["gamma"],
        ),
    ),
    Rule(
        name="Low Gamma for GarmanKohlhagen Model",
        condition=lambda data: data["gamma"] < 0.01
        and data["modelName"] == "GarmanKohlhagen",
        action=lambda data: (
            f"[GarmanKohlhagen] Low gamma of {data['gamma']} for this currency option suggests its delta is less sensitive to movements in the currency pair. "
            f"This can provide a buffer against rapid market fluctuations, potentially offering more stability.",
            0.01,
            data["gamma"],
        ),
    ),
]
