from typing import Dict, Callable, Any, Tuple


class Rule:
    def __init__(
        self,
        name: str,
        condition: Callable[[Dict[str, Any]], bool],
        action: Callable[[Dict[str, Any]], Tuple[str, Any, Any]],
    ):
        self.name = name
        self.condition = condition
        self.action = action

    def apply(self, option_data: Dict[str, Any]) -> str:
        if self.condition(option_data):
            recommendation, threshold, encountered_value = self.action(option_data)
            return f"{recommendation} (Threshold: {threshold}, Encountered: {encountered_value})"
        return None
