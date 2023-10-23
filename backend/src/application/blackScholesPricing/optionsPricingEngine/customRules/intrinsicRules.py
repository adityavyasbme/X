from src.application.blackScholesPricing.optionsPricingEngine.recommendation.rule import Rule

rules = [
    Rule(
        name="Call Option Intrinsic Value",
        condition=lambda data: data["stockPrice"] > data["strikePrice"]
        and data["optionType"] == "call",
        action=lambda data: (
            f"Call option has an intrinsic value of ${data['stockPrice'] - data['strikePrice']}. "
            f"Exercising now would lead to a profit of ${data['stockPrice'] - data['strikePrice']} per option. "
            f"Consider buying if you anticipate the stock price will continue to rise.",
            data["strikePrice"],
            data["stockPrice"],
        ),
    ),
    Rule(
        name="Put Option Intrinsic Value",
        condition=lambda data: data["stockPrice"] < data["strikePrice"]
        and data["optionType"] == "put",
        action=lambda data: (
            f"Put option has an intrinsic value of ${data['strikePrice'] - data['stockPrice']}. "
            f"Exercising now would lead to a profit of ${data['strikePrice'] - data['stockPrice']} per option. "
            f"Consider buying if you anticipate the stock price will continue to fall.",
            data["strikePrice"],
            data["stockPrice"],
        ),
    ),
    Rule(
        name="No Intrinsic Value",
        condition=lambda data: (
            data["stockPrice"] <= data["strikePrice"] and data["optionType"] == "call"
        )
        or (data["stockPrice"] >= data["strikePrice"] and data["optionType"] == "put"),
        action=lambda data: (
            "The option currently has no intrinsic value. "
            "It's not profitable to exercise the option at the current stock price. "
            "Consider other factors like time value before buying.",
            data["strikePrice"],
            data["stockPrice"],
        ),
    ),
]
