from src.application.blackScholesPricing.optionsPricingEngine.recommendation.rule import Rule

vega_threshold_high = 0.2  # Example threshold value for high vega sensitivity
vega_threshold_low = 0.05  # Example threshold value for low vega sensitivity

rules = [
    Rule(
        name="High Vega Sensitivity (BlackScholes) - Call Option",
        condition=lambda data: data["vega"] > vega_threshold_high
        and data["optionType"] == "call"
        and data["modelName"] == "BlackScholes",
        action=lambda data: (
            f"[{data['modelName']}] The call option has a high Vega sensitivity of {data['vega']}. "
            f"This indicates that for every 1% increase in implied volatility, the option's price will increase by approximately ${data['vega']}. "
            f"Consider this sensitivity when anticipating future volatility changes.",
            vega_threshold_high,
            data["vega"],
        ),
    ),
    Rule(
        name="High Vega Sensitivity (BlackScholes) - Put Option",
        condition=lambda data: data["vega"] > vega_threshold_high
        and data["optionType"] == "put"
        and data["modelName"] == "BlackScholes",
        action=lambda data: (
            f"[{data['modelName']}] The put option has a high Vega sensitivity of {data['vega']}. "
            f"This indicates that for every 1% increase in implied volatility, the option's price will increase by approximately ${data['vega']}. "
            f"Consider this sensitivity when anticipating future volatility changes.",
            vega_threshold_high,
            data["vega"],
        ),
    ),
    Rule(
        name="Low Vega Sensitivity (BlackScholes) - Call Option",
        condition=lambda data: data["vega"] < vega_threshold_low
        and data["optionType"] == "call"
        and data["modelName"] == "BlackScholes",
        action=lambda data: (
            f"[{data['modelName']}] The call option has a low Vega sensitivity of {data['vega']}. "
            f"This suggests that changes in implied volatility will have a minor effect on the option's price. "
            f"Other factors may play a more dominant role in the option's pricing.",
            vega_threshold_low,
            data["vega"],
        ),
    ),
    Rule(
        name="Low Vega Sensitivity (BlackScholes) - Put Option",
        condition=lambda data: data["vega"] < vega_threshold_low
        and data["optionType"] == "put"
        and data["modelName"] == "BlackScholes",
        action=lambda data: (
            f"[{data['modelName']}] The put option has a low Vega sensitivity of {data['vega']}. "
            f"This suggests that changes in implied volatility will have a minor effect on the option's price. "
            f"Other factors may play a more dominant role in the option's pricing.",
            vega_threshold_low,
            data["vega"],
        ),
    ),
    Rule(
        name="High Vega Sensitivity (Black76) - Call Option",
        condition=lambda data: data["vega"] > 0.05
        and data["optionType"] == "call"
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[{data['modelName']}] The call option's price is highly sensitive to changes in implied volatility. "
            f"A slight increase in volatility can significantly increase the option's price. "
            f"Consider this if you expect volatility to rise.",
            0.05,
            data["vega"],
        ),
    ),
    Rule(
        name="High Vega Sensitivity (Black76) - Put Option",
        condition=lambda data: data["vega"] > 0.05
        and data["optionType"] == "put"
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[{data['modelName']}] The put option's price is highly sensitive to changes in implied volatility. "
            f"A slight increase in volatility can significantly increase the option's price. "
            f"Consider this if you expect volatility to rise.",
            0.05,
            data["vega"],
        ),
    ),
    Rule(
        name="Low Vega Sensitivity (Black76) - Call Option",
        condition=lambda data: data["vega"] <= 0.05
        and data["optionType"] == "call"
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[{data['modelName']}] The call option's price is less sensitive to changes in implied volatility. "
            f"Changes in volatility won't significantly impact the option's price. "
            f"This can be beneficial if you expect volatility to remain stable.",
            0.05,
            data["vega"],
        ),
    ),
    Rule(
        name="Low Vega Sensitivity (Black76) - Put Option",
        condition=lambda data: data["vega"] <= 0.05
        and data["optionType"] == "put"
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[{data['modelName']}] The put option's price is less sensitive to changes in implied volatility. "
            f"Changes in volatility won't significantly impact the option's price. "
            f"This can be beneficial if you expect volatility to remain stable.",
            0.05,
            data["vega"],
        ),
    ),
    Rule(
        name="High Vega Sensitivity (GarmanKohlhagen) - Call Option",
        condition=lambda data: data["vega"] > 0.05
        and data["modelName"] == "GarmanKohlhagen"
        and data["optionType"] == "call",
        action=lambda data: (
            f"[{data['modelName']}] The call option has high Vega sensitivity with a Vega of {data['vega']}. "
            f"This implies that for a 1% increase in implied volatility, the option's price will increase by approximately the Vega value. "
            f"Consider this sensitivity when expecting volatility changes in the underlying asset.",
            0.05,
            data["vega"],
        ),
    ),
    Rule(
        name="High Vega Sensitivity (GarmanKohlhagen) - Put Option",
        condition=lambda data: data["vega"] > 0.05
        and data["modelName"] == "GarmanKohlhagen"
        and data["optionType"] == "put",
        action=lambda data: (
            f"[{data['modelName']}] The put option has high Vega sensitivity with a Vega of {data['vega']}. "
            f"This implies that for a 1% increase in implied volatility, the option's price will increase by approximately the Vega value. "
            f"Consider this sensitivity when expecting volatility changes in the underlying asset.",
            0.05,
            data["vega"],
        ),
    ),
    Rule(
        name="Low Vega Sensitivity (GarmanKohlhagen) - Call Option",
        condition=lambda data: data["vega"] <= 0.05
        and data["modelName"] == "GarmanKohlhagen"
        and data["optionType"] == "call",
        action=lambda data: (
            f"[{data['modelName']}] The call option has low Vega sensitivity with a Vega of {data['vega']}. "
            f"This implies that changes in implied volatility will have a lesser impact on the option's price. "
            f"Consider this when not expecting significant volatility changes in the underlying asset.",
            0.05,
            data["vega"],
        ),
    ),
    Rule(
        name="Low Vega Sensitivity (GarmanKohlhagen) - Put Option",
        condition=lambda data: data["vega"] <= 0.05
        and data["modelName"] == "GarmanKohlhagen"
        and data["optionType"] == "put",
        action=lambda data: (
            f"[{data['modelName']}] The put option has low Vega sensitivity with a Vega of {data['vega']}. "
            f"This implies that changes in implied volatility will have a lesser impact on the option's price. "
            f"Consider this when not expecting significant volatility changes in the underlying asset.",
            0.05,
            data["vega"],
        ),
    ),
]
