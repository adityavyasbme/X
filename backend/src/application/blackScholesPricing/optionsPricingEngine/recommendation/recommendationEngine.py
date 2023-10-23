from typing import List, Dict, Any
from src.application.blackScholesPricing.optionsPricingEngine.recommendation.rule import Rule


# Define the RecommendationEngine class
class RecommendationEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules

    def recommend(self, option_data: Dict[str, Any]) -> str:
        recommendations = []
        for rule in self.rules:
            recommendation = rule.apply(option_data)
            if recommendation:
                recommendations.append(recommendation)

        if not recommendations:
            return "No recommendation available."

        return " \n\n".join(recommendations)
