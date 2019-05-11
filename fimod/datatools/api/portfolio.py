
import pandas as pd
from .. import portfolio, price

import numpy as np

class Portfolio:

    days_in_year = 252

    def __init__(self, *asset_prices:pd.Series, weights, name=None):
        self.prices = asset_prices
        self.weights = weights
        self.portfolio_name = name
        
    def to_frame(self):
        return pd.concat(self.prices, axis=1, how="outer")

    @property
    def daily_returns(self):
        ret_matrix = self.to_frame().pct_change()

        portf_returns = portfolio.returns(ret_matrix.values, self.weights)

        return pd.Series(portf_returns, index=ret_matrix.index, name=self.portfolio_name)

    @property
    def annual_returns(self):
        return price.convert_to_returns(self.to_frame(), freq="BA")

    @property
    def daily_volatility(self):
        returns = price.convert_to_returns(self.to_frame(), freq="D")
        cov_matrix = returns.cov()
        return portfolio.volatility(weights, cov_matrix) 

    @property
    def annual_volatility(self):
        return self.daily_volatility * np.sqrt(self.days_in_year)
