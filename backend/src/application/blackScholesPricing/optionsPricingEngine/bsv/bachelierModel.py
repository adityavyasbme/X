from src.application.blackScholesPricing.optionsPricingEngine.bsv.pricingBase import OptionPricingBase
import numpy as np
from scipy.stats import norm
from typing import Dict


class BachelierModel(OptionPricingBase):
    """
    Implements the Bachelier (Normal) model for option pricing.
    Derived from the OptionPricingBase class.
    """

    def __init__(
        self,
        stockPrice: float,
        strikePrice: float,
        timeToExpirationYr: float,
        riskFreeRate: float,
        volatility: float,
        optionType: str = "call",
    ):
        """
        Initialize the parameters for the Bachelier model.

        :param stockPrice: Current stock price.
        :param strikePrice: Option strike price.
        :param timeToExpirationYr: Time to expiration in years.
        :param riskFreeRate: Annual risk-free rate.
        :param volatility: Annual volatility of the stock.
        :param optionType: Type of the option ("call" or "put").
        """
        super().__init__(
            stockPrice, strikePrice, timeToExpirationYr, riskFreeRate, volatility
        )

        if optionType not in ["call", "put"]:
            raise ValueError("optionType must be either 'call' or 'put'")

        self.optionType = optionType

    def _d1(self) -> float:
        """
        Overridden d1 calculation for the Bachelier model.

        :return: Value of d1.
        """
        return (self.stockPrice - self.strikePrice) / (
            self.volatility * np.sqrt(self.timeToExpirationYr)
        )

    def call_price(self) -> float:
        """
        Calculate the call option price using the Bachelier model.

        :return: Call option price.
        """
        d1 = self._d1()
        return (self.stockPrice - self.strikePrice) * norm.cdf(
            d1
        ) + self.volatility * np.sqrt(self.timeToExpirationYr) * norm.pdf(d1)

    def put_price(self) -> float:
        """
        Calculate the put option price using the Bachelier model.

        :return: Put option price.
        """
        d1 = self._d1()
        return (self.strikePrice - self.stockPrice) * norm.cdf(
            -d1
        ) + self.volatility * np.sqrt(self.timeToExpirationYr) * norm.pdf(-d1)

    def greeks(self) -> Dict[str, float]:
        """
        Calculate the option Greeks for the Bachelier model.

        :return: A dictionary containing Delta, Gamma, Vega, Theta, and Rho.
        """
        d1 = self._d1()
        delta = norm.cdf(d1) if self.optionType == "call" else -norm.cdf(-d1)
        gamma = norm.pdf(d1) / (self.volatility *
                                np.sqrt(self.timeToExpirationYr))
        vega = np.sqrt(self.timeToExpirationYr) * norm.pdf(d1)

        # Theta and Rho for Bachelier Model are more complex than Black-Scholes and its variations.
        # As a simplification, we'll use an approximation here.
        theta = (
            -0.5
            * self.volatility**2
            * norm.pdf(d1)
            / (2 * np.sqrt(self.timeToExpirationYr))
        )
        rho = (
            self.timeToExpirationYr
            * (self.strikePrice - self.stockPrice)
            * norm.cdf(d1)
            if self.optionType == "call"
            else self.timeToExpirationYr
            * (self.stockPrice - self.strikePrice)
            * norm.cdf(-d1)
        )

        return {
            "delta": delta,
            "gamma": gamma,
            "vega": vega,
            "theta": theta,
            "rho": rho,
        }
