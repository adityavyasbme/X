from src.application.blackScholesPricing.optionsPricingEngine.bsv.pricingBase import OptionPricingBase
import numpy as np
from scipy.stats import norm
from typing import Dict


class BinaryOption(OptionPricingBase):
    """
    A class to calculate prices for European binary (digital) options using the Black-Scholes formula.
    Derived from the OptionPricingBase class.
    """

    def __init__(
        self,
        stockPrice: float,
        strikePrice: float,
        timeToExpirationYr: float,
        riskFreeRate: float,
        volatility: float,
        dividendYield: float = 0.0,
        optionType: str = "call",
    ):
        """
        Initialize the parameters for the BinaryOption model.

        :param stockPrice: Current stock price.
        :param strikePrice: Option strike price.
        :param timeToExpirationYr: Time to expiration in years.
        :param riskFreeRate: Annual risk-free rate.
        :param volatility: Annual volatility of the stock.
        :param dividendYield: Continuous dividend yield (default is 0.0 for no dividends).
        :param optionType: Type of the option ("call" or "put").
        """
        super().__init__(
            stockPrice,
            strikePrice,
            timeToExpirationYr,
            riskFreeRate,
            volatility,
            dividendYield,
        )

        if optionType not in ["call", "put"]:
            raise ValueError("optionType must be either 'call' or 'put'")

        self.optionType = optionType

    def call_price(self) -> float:
        """
        Calculate the binary call option price using the Black-Scholes formula.

        :return: Binary call option price.
        """
        return np.exp(-self.riskFreeRate * self.timeToExpirationYr) * norm.cdf(
            self._d2()
        )

    def put_price(self) -> float:
        """
        Calculate the binary put option price using the Black-Scholes formula.

        :return: Binary put option price.
        """
        return np.exp(-self.riskFreeRate * self.timeToExpirationYr) * norm.cdf(
            -self._d2()
        )

    def greeks(self) -> Dict[str, float]:
        """
        Calculate the option Greeks for the BinaryOption model.

        :return: A dictionary containing Delta, Gamma, Vega, Theta, and Rho.
        """
        d1 = self._d1()
        d2 = self._d2()

        if self.optionType == "call":
            delta = (
                np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * norm.pdf(d2)
                / (self.stockPrice * self.volatility * np.sqrt(self.timeToExpirationYr))
            )
            rho = (
                -self.timeToExpirationYr
                * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * norm.cdf(d2)
            )
            theta = -(
                self.stockPrice
                * self.volatility
                * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * norm.pdf(d2)
                / (2 * np.sqrt(self.timeToExpirationYr))
            ) + (
                self.riskFreeRate
                * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * norm.cdf(d2)
            )
        else:  # put
            delta = (
                -np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * norm.pdf(d2)
                / (self.stockPrice * self.volatility * np.sqrt(self.timeToExpirationYr))
            )
            rho = (
                self.timeToExpirationYr
                * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * norm.cdf(-d2)
            )
            theta = -(
                self.stockPrice
                * self.volatility
                * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * norm.pdf(d2)
                / (2 * np.sqrt(self.timeToExpirationYr))
            ) - (
                self.riskFreeRate
                * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * norm.cdf(-d2)
            )

        gamma = (
            np.exp(-self.riskFreeRate * self.timeToExpirationYr)
            * norm.pdf(d2)
            / (self.stockPrice**2 * self.volatility**2 * self.timeToExpirationYr)
        )
        vega = (
            np.exp(-self.riskFreeRate * self.timeToExpirationYr)
            * norm.pdf(d2)
            * np.sqrt(self.timeToExpirationYr)
        )

        return {
            "delta": delta,
            "gamma": gamma,
            "vega": vega,
            "theta": theta,
            "rho": rho,
        }
