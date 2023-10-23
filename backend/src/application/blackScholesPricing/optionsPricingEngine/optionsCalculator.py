from src.application.blackScholesPricing.optionsPricingEngine.bsv.bachelierModel import BachelierModel
from src.application.blackScholesPricing.optionsPricingEngine.bsv.binaryModel import BinaryOption
from src.application.blackScholesPricing.optionsPricingEngine.bsv.black76Model import Black76
from src.application.blackScholesPricing.optionsPricingEngine.bsv.blackScholes import BlackScholes
from src.application.blackScholesPricing.optionsPricingEngine.bsv.garmanKohlhagen import GarmanKohlhagen
from typing import Dict, Union


class OptionCalculator:
    """
    A wrapper class to interact with various option pricing models.
    """

    def __init__(self):
        self.model = None
        self.modelName = None
        self.modelResults = {}
        self.modelParams = {}

    def select_model(
        self,
        modelName: str,
        stockPrice: float,
        strikePrice: float,
        timeToExpirationYr: float,
        riskFreeRate: float,
        volatility: float,
        dividendYield: float = 0.0,
        foreignRiskFreeRate: float = None,
        optionType: str = "call",
    ):
        """
        Select and initialize the desired option pricing model.

        :param modelName: Name of the option pricing model (e.g., "BlackScholes", "Black76", etc.)
        :param stockPrice: Current stock or futures price.
        :param strikePrice: Option strike price.
        :param timeToExpirationYr: Time to expiration in years.
        :param riskFreeRate: Annual domestic risk-free rate.
        :param volatility: Annual volatility of the stock or futures.
        :param dividendYield: Continuous dividend yield (default is 0.0 for no dividends).
        :param foreignRiskFreeRate: Annual foreign risk-free rate (only for GarmanKohlhagen model).
        :param optionType: Type of the option ("call" or "put").
        """
        if modelName == "BlackScholes":
            self.model = BlackScholes(
                stockPrice,
                strikePrice,
                timeToExpirationYr,
                riskFreeRate,
                volatility,
                optionType,
                dividendYield,
            )

        elif modelName == "Black76":
            self.model = Black76(
                stockPrice,
                strikePrice,
                timeToExpirationYr,
                riskFreeRate,
                volatility,
                optionType,
            )

        elif modelName == "GarmanKohlhagen":
            if foreignRiskFreeRate is None:
                raise ValueError(
                    "foreignRiskFreeRate is required for GarmanKohlhagen model."
                )
            self.model = GarmanKohlhagen(
                stockPrice,
                strikePrice,
                timeToExpirationYr,
                riskFreeRate,
                foreignRiskFreeRate,
                volatility,
                optionType,
            )

        elif modelName == "BachelierModel":
            self.model = BachelierModel(
                stockPrice,
                strikePrice,
                timeToExpirationYr,
                riskFreeRate,
                volatility,
                optionType,
            )

        elif modelName == "BinaryOption":
            self.model = BinaryOption(
                stockPrice,
                strikePrice,
                timeToExpirationYr,
                riskFreeRate,
                volatility,
                dividendYield,
                optionType,
            )

        else:
            raise ValueError(f"Invalid model name: {modelName}")

        self.modelName = modelName
        self.modelParams["stockPrice"] = stockPrice
        self.modelParams["strikePrice"] = strikePrice
        self.modelParams["timeToExpirationYr"] = timeToExpirationYr
        self.modelParams["riskFreeRate"] = riskFreeRate
        self.modelParams["volatility"] = volatility
        self.modelParams["dividendYield"] = dividendYield
        self.modelParams["foreignRiskFreeRate"] = foreignRiskFreeRate
        self.modelParams["optionType"] = optionType
        self.modelParams["modelName"] = modelName

    def calculate_price(self):
        """
        Calculate the option price based on the selected model and its type (call/put).

        :return: Option price.
        """
        if self.model.optionType == "call":
            cp = self.model.call_price()
            self.modelResults["price"] = cp
            return cp
        else:
            pp = self.model.put_price()
            self.modelResults["price"] = pp
            return pp

    def calculate_greeks(self) -> Dict[str, float]:
        """
        Calculate the option Greeks based on the selected model.

        :return: Dictionary containing the option Greeks.
        """
        res = self.model.greeks()
        self.modelResults.update(res)
        self.modelParams.update(res)
        return res

    def calculate_price_and_greeks(self) -> Dict[str, Union[float, Dict[str, float]]]:
        """
        Calculate both the option price and its Greeks based on the selected model.

        :return: Dictionary containing the option price and its Greeks.
        """
        option_price = self.calculate_price()
        greeks = self.calculate_greeks()
        return self.modelResults
