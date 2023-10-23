from src.application.blackScholesPricing.optionsPricingEngine.bsv.pricingBase import OptionPricingBase
import numpy as np
from scipy.stats import norm
from typing import Dict


class BlackScholes(OptionPricingBase):
    """
    A class to calculate option prices and Greeks using the Black-Scholes formula.
    Derived from the OptionPricingBase class.
    """

    def __init__(
        self,
        stockPrice: float,
        strikePrice: float,
        timeToExpirationYr: float,
        riskFreeRate: float,
        volatility: float,
        optionType: str,
        dividendYield: float = 0.0,
    ):
        """
        Initialize the parameters for the Black-Scholes model.

        :param stockPrice: Current stock price.
        :param strikePrice: Option strike price.
        :param timeToExpirationYr: Time to expiration in years.
        :param riskFreeRate: Annual risk-free rate.
        :param volatility: Annual volatility of the stock.
        :param dividendYield: Continuous dividend yield (default is 0.0 for no dividends).
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
        Calculate the call option price using the Black-Scholes formula.

        :return: Call option price.
        """
        return self.stockPrice * np.exp(
            -self.dividendYield * self.timeToExpirationYr
        ) * norm.cdf(self._d1()) - self.strikePrice * np.exp(
            -self.riskFreeRate * self.timeToExpirationYr
        ) * norm.cdf(
            self._d2()
        )

    def put_price(self) -> float:
        """
        Calculate the put option price using the Black-Scholes formula.

        :return: Put option price.
        """
        return self.strikePrice * np.exp(
            -self.riskFreeRate * self.timeToExpirationYr
        ) * norm.cdf(-self._d2()) - self.stockPrice * np.exp(
            -self.dividendYield * self.timeToExpirationYr
        ) * norm.cdf(
            -self._d1()
        )

    def greeks(self) -> Dict[str, float]:
        """
        Calculate the option Greeks: Delta, Gamma, Vega, Theta, Rho.

        :return: Dictionary containing Delta, Gamma, Vega, Theta, Rho.
        """
        delta = np.exp(-self.dividendYield * self.timeToExpirationYr) * norm.cdf(
            self._d1()
        )
        gamma = (
            np.exp(-self.dividendYield * self.timeToExpirationYr)
            * norm.pdf(self._d1())
            / (self.stockPrice * self.volatility * np.sqrt(self.timeToExpirationYr))
        )
        vega = (
            self.stockPrice
            * np.exp(-self.dividendYield * self.timeToExpirationYr)
            * norm.pdf(self._d1())
            * np.sqrt(self.timeToExpirationYr)
        )
        theta = (
            (
                -self.stockPrice
                * self.volatility
                * np.exp(-self.dividendYield * self.timeToExpirationYr)
                * norm.pdf(self._d1())
                / (2 * np.sqrt(self.timeToExpirationYr))
            )
            - (
                self.riskFreeRate
                * self.strikePrice
                * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * norm.cdf(self._d2())
            )
            + (
                self.dividendYield
                * self.stockPrice
                * np.exp(-self.dividendYield * self.timeToExpirationYr)
                * norm.cdf(self._d1())
            )
        )
        rho = (
            self.strikePrice
            * self.timeToExpirationYr
            * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
            * norm.cdf(self._d2())
        )

        return {
            "delta": delta,
            "gamma": gamma,
            "vega": vega,
            "theta": theta,
            "rho": rho,
        }
