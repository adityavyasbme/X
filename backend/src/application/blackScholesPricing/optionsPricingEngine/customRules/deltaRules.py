from src.application.blackScholesPricing.optionsPricingEngine.recommendation.rule import Rule

rules = [
    Rule(
        name="High Positive Delta (BlackScholes)",
        condition=lambda data: data["delta"] >= 0.8
        and data["optionType"] == "call"
        and data["modelName"] == "BlackScholes",
        action=lambda data: (
            f"[BlackScholes] The call option is deeply in-the-money with a delta of {data['delta']}. "
            f"There's a strong likelihood the stock will finish in-the-money, making this option a potential buying opportunity.",
            0.8,
            data["delta"],
        ),
    ),
    Rule(
        name="Low Positive Delta (BlackScholes)",
        condition=lambda data: 0.5 <= data["delta"] < 0.8
        and data["optionType"] == "call"
        and data["modelName"] == "BlackScholes",
        action=lambda data: (
            f"[BlackScholes] The call option is slightly in-the-money or at-the-money with a delta of {data['delta']}. "
            f"There's a moderate chance the stock will finish in-the-money. Exercise caution and consider other factors before making a decision.",
            0.5,
            data["delta"],
        ),
    ),
    Rule(
        name="High Negative Delta (BlackScholes)",
        condition=lambda data: data["delta"] <= -0.8
        and data["optionType"] == "put"
        and data["modelName"] == "BlackScholes",
        action=lambda data: (
            f"[BlackScholes] The put option is deeply in-the-money with a delta of {data['delta']}. "
            f"There's a strong likelihood the stock will finish in-the-money, suggesting this might be a good buying opportunity.",
            -0.8,
            data["delta"],
        ),
    ),
    Rule(
        name="Low Negative Delta (BlackScholes)",
        condition=lambda data: -0.8 < data["delta"] <= -0.5
        and data["optionType"] == "put"
        and data["modelName"] == "BlackScholes",
        action=lambda data: (
            f"[BlackScholes] The put option is slightly in-the-money or at-the-money with a delta of {data['delta']}. "
            f"There's a moderate chance the stock will finish in-the-money. Exercise caution and consider other factors before deciding.",
            -0.5,
            data["delta"],
        ),
    ),
    Rule(
        name="High Positive Delta (Black76)",
        condition=lambda data: data["delta"] > 0.7
        and data["optionType"] == "call"
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[Black76] The futures call option has a delta of {data['delta']}, indicating it's deeply in-the-money. "
            f"There's a strong chance that the futures contract will finish in-the-money. This option might be a good buy if you anticipate further upward movement in the futures price.",
            0.7,
            data["delta"],
        ),
    ),
    Rule(
        name="Low Positive Delta (Black76)",
        condition=lambda data: 0.4 <= data["delta"] <= 0.6
        and data["optionType"] == "call"
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[Black76] The futures call option has a delta of {data['delta']}, suggesting it's slightly in-the-money or at-the-money. "
            f"There's a moderate chance that the futures contract will finish in-the-money. Consider your market view and other factors before making a decision.",
            0.5,  # Average of the range for threshold
            data["delta"],
        ),
    ),
    Rule(
        name="High Negative Delta (Black76)",
        condition=lambda data: data["delta"] < -0.7
        and data["optionType"] == "put"
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[Black76] The futures put option has a delta of {data['delta']}, indicating it's deeply in-the-money. "
            f"There's a strong chance that the futures contract will finish in-the-money. This option might be a good buy if you anticipate further downward movement in the futures price.",
            -0.7,
            data["delta"],
        ),
    ),
    Rule(
        name="Low Negative Delta (Black76)",
        condition=lambda data: -0.6 <= data["delta"] <= -0.4
        and data["optionType"] == "put"
        and data["modelName"] == "Black76",
        action=lambda data: (
            f"[Black76] The futures put option has a delta of {data['delta']}, suggesting it's slightly in-the-money or at-the-money. "
            f"There's a moderate chance that the futures contract will finish in-the-money. Consider your market view and other factors before making a decision.",
            -0.5,  # Average of the range for threshold
            data["delta"],
        ),
    ),
    Rule(
        name="High Positive Delta (GarmanKohlhagen)",
        condition=lambda data: data["delta"] > 0.7
        and data["optionType"] == "call"
        and data["modelName"] == "GarmanKohlhagen",
        action=lambda data: (
            f"[{data['modelName']}] The foreign exchange call option has a high delta of {data['delta']}, indicating it's deeply in-the-money. "
            f"There's a strong likelihood the currency pair will finish in-the-money. This can be a promising buy for investors bullish on the currency pair.",
            0.7,
            data["delta"],
        ),
    ),
    Rule(
        name="Low Positive Delta (GarmanKohlhagen)",
        condition=lambda data: 0.3 <= data["delta"] <= 0.5
        and data["optionType"] == "call"
        and data["modelName"] == "GarmanKohlhagen",
        action=lambda data: (
            f"[{data['modelName']}] The foreign exchange call option has a delta of {data['delta']}, suggesting it's slightly in-the-money or at-the-money. "
            f"There's a moderate chance the currency pair will finish in-the-money. This option can be considered for speculative purposes or hedging.",
            0.5,
            data["delta"],
        ),
    ),
    Rule(
        name="High Negative Delta (GarmanKohlhagen)",
        condition=lambda data: data["delta"] < -0.7
        and data["optionType"] == "put"
        and data["modelName"] == "GarmanKohlhagen",
        action=lambda data: (
            f"[{data['modelName']}] The foreign exchange put option has a high negative delta of {data['delta']}, indicating it's deeply in-the-money. "
            f"There's a strong likelihood the currency pair will finish in-the-money. This can be a promising buy for investors bearish on the currency pair.",
            -0.7,
            data["delta"],
        ),
    ),
    Rule(
        name="Low Negative Delta (GarmanKohlhagen)",
        condition=lambda data: -0.5 <= data["delta"] <= -0.3
        and data["optionType"] == "put"
        and data["modelName"] == "GarmanKohlhagen",
        action=lambda data: (
            f"[{data['modelName']}] The foreign exchange put option has a delta of {data['delta']}, suggesting it's slightly in-the-money or at-the-money. "
            f"There's a moderate chance the currency pair will finish in-the-money. This option can be considered for speculative purposes or hedging.",
            -0.5,
            data["delta"],
        ),
    ),
]
