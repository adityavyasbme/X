import numpy as np
from scipy.stats import norm


class OptionPricingBase:
    """A base class to validate and store common inputs for various option pricing models."""

    def __init__(
        self,
        stockPrice: float,
        strikePrice: float,
        timeToExpirationYr: float,
        riskFreeRate: float,
        volatility: float,
        dividendYield: float = 0.0,
    ):
        """
        Initialize and validate the common parameters for option pricing models.

        :param stockPrice: Current stock price or futures price.
        :param strikePrice: Option strike price.
        :param timeToExpirationYr: Time to expiration in years.
        :param riskFreeRate: Annual risk-free rate.
        :param volatility: Annual volatility of the stock or futures.
        :param dividendYield: Continuous dividend yield (default is 0.0 for no dividends).
        """

        # Validate each parameter
        self.validate_positive(stockPrice, "stockPrice")
        self.validate_positive(strikePrice, "strikePrice")
        self.validate_positive(timeToExpirationYr, "timeToExpirationYr")
        self.validate_rate(riskFreeRate, "riskFreeRate")
        self.validate_rate(volatility, "volatility")
        self.validate_rate(dividendYield, "dividendYield")

        # Assign each parameter
        self.stockPrice = stockPrice
        self.strikePrice = strikePrice
        self.timeToExpirationYr = timeToExpirationYr
        self.riskFreeRate = riskFreeRate
        self.volatility = volatility
        self.dividendYield = dividendYield

    def validate_positive(self, value: float, name: str) -> None:
        """
        Validate that the given value is positive.

        :param value: The value to validate.
        :param name: The name of the parameter (for error messaging).
        """
        if value <= 0:
            raise ValueError(f"{name} must be positive.")

    def validate_rate(self, value: float, name: str) -> None:
        """
        Validate that the given value is between 0 and 1 (inclusive).

        :param value: The rate to validate.
        :param name: The name of the parameter (for error messaging).
        """
        if value < 0 or value > 1:
            raise ValueError(f"{name} must be between 0 and 1 (inclusive).")

    def _d1(self) -> float:
        """
        Calculate the d1 value used in the Black-Scholes formula and its variations.

        :return: Value of d1.
        """
        return (
            np.log(self.stockPrice / self.strikePrice)
            + (self.riskFreeRate - self.dividendYield + 0.5 * self.volatility**2)
            * self.timeToExpirationYr
        ) / (self.volatility * np.sqrt(self.timeToExpirationYr))

    def _d2(self) -> float:
        """
        Calculate the d2 value used in the Black-Scholes formula and its variations.

        :return: Value of d2.
        """
        return self._d1() - self.volatility * np.sqrt(self.timeToExpirationYr)
