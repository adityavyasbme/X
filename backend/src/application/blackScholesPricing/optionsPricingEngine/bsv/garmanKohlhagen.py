from src.application.blackScholesPricing.optionsPricingEngine.bsv.pricingBase import OptionPricingBase
import numpy as np
from scipy.stats import norm
from typing import Dict


class GarmanKohlhagen(OptionPricingBase):
    """
    A class to calculate option prices using the Garman-Kohlhagen model for foreign currency options.
    Derived from the OptionPricingBase class.
    """

    def __init__(
        self,
        stockPrice: float,
        strikePrice: float,
        timeToExpirationYr: float,
        riskFreeRate: float,
        foreignRiskFreeRate: float,
        volatility: float,
        optionType: str,
    ):
        """
        Initialize the parameters for the Garman-Kohlhagen model.

        :param stockPrice: Current foreign currency price.
        :param strikePrice: Option strike price.
        :param timeToExpirationYr: Time to expiration in years.
        :param riskFreeRate: Annual domestic risk-free rate.
        :param foreignRiskFreeRate: Annual foreign risk-free rate.
        :param volatility: Annual volatility of the foreign currency.
        :param optionType: Type of the option ('call' or 'put').
        """
        super().__init__(
            stockPrice, strikePrice, timeToExpirationYr, riskFreeRate, volatility
        )
        self.foreignRiskFreeRate = foreignRiskFreeRate
        if optionType not in ["call", "put"]:
            raise ValueError("optionType must be either 'call' or 'put'")
        self.optionType = optionType

    def _d1(self) -> float:
        """Overridden d1 calculation for the Garman-Kohlhagen model."""
        return (
            np.log(self.stockPrice / self.strikePrice)
            + (
                self.riskFreeRate
                - self.foreignRiskFreeRate
                + 0.5 * self.volatility**2
            )
            * self.timeToExpirationYr
        ) / (self.volatility * np.sqrt(self.timeToExpirationYr))

    def call_price(self) -> float:
        """
        Calculate the call option price using the Garman-Kohlhagen model.

        :return: Call option price.
        """
        return self.stockPrice * np.exp(
            -self.foreignRiskFreeRate * self.timeToExpirationYr
        ) * norm.cdf(self._d1()) - self.strikePrice * np.exp(
            -self.riskFreeRate * self.timeToExpirationYr
        ) * norm.cdf(
            self._d2()
        )

    def put_price(self) -> float:
        """
        Calculate the put option price using the Garman-Kohlhagen model.

        :return: Put option price.
        """
        return self.strikePrice * np.exp(
            -self.riskFreeRate * self.timeToExpirationYr
        ) * norm.cdf(-self._d2()) - self.stockPrice * np.exp(
            -self.foreignRiskFreeRate * self.timeToExpirationYr
        ) * norm.cdf(
            -self._d1()
        )

    def greeks(self) -> Dict[str, float]:
        """
        Calculate the option Greeks for the Garman-Kohlhagen model: Delta, Gamma, Vega, Theta, Rho.

        :return: Dictionary containing the Greeks: Delta, Gamma, Vega, Theta, and Rho.
        """
        if self.optionType == "call":
            delta = np.exp(
                -self.foreignRiskFreeRate * self.timeToExpirationYr
            ) * norm.cdf(self._d1())
            rho = (
                self.strikePrice
                * self.timeToExpirationYr
                * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * norm.cdf(self._d2())
            )
            theta = (
                (
                    -self.stockPrice
                    * np.exp(-self.foreignRiskFreeRate * self.timeToExpirationYr)
                    * self.volatility
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
                    self.foreignRiskFreeRate
                    * self.stockPrice
                    * np.exp(-self.foreignRiskFreeRate * self.timeToExpirationYr)
                    * norm.cdf(self._d1())
                )
            )
        else:  # put
            delta = -np.exp(
                -self.foreignRiskFreeRate * self.timeToExpirationYr
            ) * norm.cdf(-self._d1())
            rho = (
                -self.strikePrice
                * self.timeToExpirationYr
                * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                * norm.cdf(-self._d2())
            )
            theta = (
                (
                    -self.stockPrice
                    * np.exp(-self.foreignRiskFreeRate * self.timeToExpirationYr)
                    * self.volatility
                    * norm.pdf(self._d1())
                    / (2 * np.sqrt(self.timeToExpirationYr))
                )
                + (
                    self.riskFreeRate
                    * self.strikePrice
                    * np.exp(-self.riskFreeRate * self.timeToExpirationYr)
                    * norm.cdf(-self._d2())
                )
                - (
                    self.foreignRiskFreeRate
                    * self.stockPrice
                    * np.exp(-self.foreignRiskFreeRate * self.timeToExpirationYr)
                    * norm.cdf(-self._d1())
                )
            )

        gamma = (
            np.exp(-self.foreignRiskFreeRate * self.timeToExpirationYr)
            * norm.pdf(self._d1())
            / (self.stockPrice * self.volatility * np.sqrt(self.timeToExpirationYr))
        )
        vega = (
            self.stockPrice
            * np.exp(-self.foreignRiskFreeRate * self.timeToExpirationYr)
            * norm.pdf(self._d1())
            * np.sqrt(self.timeToExpirationYr)
        )

        return {
            "delta": delta,
            "gamma": gamma,
            "vega": vega,
            "theta": theta,
            "rho": rho,
        }
