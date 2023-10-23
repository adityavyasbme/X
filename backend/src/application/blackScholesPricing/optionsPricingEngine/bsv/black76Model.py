from src.application.blackScholesPricing.optionsPricingEngine.bsv.pricingBase import OptionPricingBase
import numpy as np
from scipy.stats import norm
from typing import Dict


class Black76(OptionPricingBase):
    """
    A class to calculate option prices using the Black '76 model for European options on futures.
    Derived from the OptionPricingBase class.
    """

    def __init__(
        self,
        futurePrice: float,
        strikePrice: float,
        timeToExpirationYr: float,
        riskFreeRate: float,
        volatility: float,
        optionType: str,
    ):
        """
        Initialize the parameters for the Black '76 model.

        :param futurePrice: Current futures price.
        :param strikePrice: Option strike price.
        :param timeToExpirationYr: Time to expiration in years.
        :param riskFreeRate: Annual risk-free rate.
        :param volatility: Annual volatility of the futures.
        :param optionType: Type of the option ('call' or 'put').
        """
        super().__init__(
            futurePrice, strikePrice, timeToExpirationYr, riskFreeRate, volatility
        )
        if optionType not in ["call", "put"]:
            raise ValueError("optionType must be either 'call' or 'put'")
        self.optionType = optionType

    def call_price(self) -> float:
        """
        Calculate the call option price using the Black '76 model.

        :return: Call option price.
        """
        return np.exp(-self.riskFreeRate * self.timeToExpirationYr) * (
            self.stockPrice * norm.cdf(self._d1())
            - self.strikePrice * norm.cdf(self._d2())
        )

    def put_price(self) -> float:
        """
        Calculate the put option price using the Black '76 model.

        :return: Put option price.
        """
        return np.exp(-self.riskFreeRate * self.timeToExpirationYr) * (
            self.strikePrice * norm.cdf(-self._d2())
            - self.stockPrice * norm.cdf(-self._d1())
        )

    def greeks(self) -> Dict[str, float]:
        """
        Calculate the option Greeks: Delta, Gamma, Vega, Theta, Rho.

        :return: Dictionary containing Delta, Gamma, Vega, Theta, Rho.
        """
        if self.optionType == "call":
            delta = np.exp(-self.riskFreeRate * self.timeToExpirationYr) * norm.cdf(
                self._d1()
            )
            rho = (
                self.timeToExpirationYr
                * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * (
                    self.stockPrice * norm.cdf(self._d1())
                    - self.strikePrice * norm.cdf(self._d2())
                )
            )
        else:
            delta = np.exp(-self.riskFreeRate * self.timeToExpirationYr) * (
                norm.cdf(self._d1()) - 1
            )
            rho = (
                self.timeToExpirationYr
                * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * (
                    self.strikePrice * norm.cdf(-self._d2())
                    - self.stockPrice * norm.cdf(-self._d1())
                )
            )

        gamma = (
            np.exp(-self.riskFreeRate * self.timeToExpirationYr)
            * norm.pdf(self._d1())
            / (self.stockPrice * self.volatility * np.sqrt(self.timeToExpirationYr))
        )
        vega = (
            self.stockPrice
            * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
            * norm.pdf(self._d1())
            * np.sqrt(self.timeToExpirationYr)
        )
        theta = (
            -self.stockPrice
            * self.volatility
            * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
            * norm.pdf(self._d1())
            / (2 * np.sqrt(self.timeToExpirationYr))
        )

        return {
            "delta": delta,
            "gamma": gamma,
            "vega": vega,
            "theta": theta,
            "rho": rho,
        }
