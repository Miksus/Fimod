

from ..instrument import Instrument
from ....formulas.derivatives.option import (
    european_call_price as calc_european_call, 
    european_put_price as calc_european_put, 
    d1 as calc_d1, 
    d2 as calc_d2
)
from ..stock import Stock

class _Option(Instrument):

    # Dynamic values
    current_date = None

    def __init__(self, strike, underlying=None, expiration_date=None, riskfree_rate=None, premium=None, style="european", **kwargs):
        """
        premium: price of which the instrument was bought/sold
        strike
        exercise_date
        type: [call, put]
        style: [american, european]
        """
        self.strike_price = strike
        self.expiration_date = expiration_date

        self.underlying = Stock() if underlying is None else underlying

        self.riskfree_rate = riskfree_rate
        self.premium = premium
        
        self.style = style
        super().__init__(**kwargs)

    @property
    def spot_price(self):
        return self.underlying.price
    
    @property
    def underlying_volatility(self):
        return self.underlying.volatility

    def payoff(self):
        intrinsic = self.intrinsic_value
        premium = self.premium
        
        if self.position == "long":
            return intrinsic - premium
        elif self.position == "short":
            return premium - intrinsic
        else:
            raise TypeError(f"Invalid option position: {self.position}")

    @property
    def time_to_maturity(self):
        return self.expiration_date - self.current_date

    @property
    def price(self):
        if self.style == "european":
            return self.get_european_price(
                spot_price=self.spot_price, 
                strike_price=self.strike_price, 
                time_to_maturity=self.time_to_maturity,
                riskfree_rate=self.riskfree_rate,
                underlying_volatility=self.underlying_volatility
            )
        else:
            raise NotImplementedError(f"Price formula for {self.style} not implemented")
            
    @staticmethod
    def get_d1(spot_price, strike_price, time_to_maturity, riskfree_rate, underlying_volatility):
        return calc_d1(
            S=spot_price, 
            K=strike_price, 
            sigma=underlying_volatility, 
            T=time_to_maturity, 
            r=riskfree_rate
        )
    
    @staticmethod
    def get_d2(spot_price, strike_price, time_to_maturity, riskfree_rate, underlying_volatility):
        return calc_d2(
            S=spot_price, 
            K=strike_price, 
            sigma=underlying_volatility, 
            T=time_to_maturity, 
            r=riskfree_rate
        ) 
        
        
    def implied_volatility(self):
        pass
    
# Greeks

    def gamma(self):
        """Delta change of
        one unit change in underlying price
        """
        
    def vega(self):
        """ν=Sϕ(d1)t√
        """
    
# Decorators
    def __str__(self):
        return f'{self.type_} {self.position} option'


class PutOption(_Option):

    type_ = "Put"

    @property
    def intrinsic_value(self):
        strike = self.strike_price
        underlying = self.underlying.price
        intrinsic = strike - underlying
        intrinsic[intrinsic < 0] = 0
        return intrinsic
    
    @staticmethod
    def get_european_price(spot_price, strike_price, time_to_maturity, riskfree_rate, underlying_volatility):
        price = calc_european_put(
            S=spot_price, 
            K=strike_price, 
            sigma=underlying_volatility, 
            T=time_to_maturity, 
            r=riskfree_rate
        )
        return price


class CallOption(_Option):

    type_ = "Call"

    @property
    def intrinsic_value(self):
        strike = self.strike_price
        underlying = self.underlying.price
        intrinsic = underlying - strike

        intrinsic[intrinsic < 0] = 0
        return intrinsic

    @staticmethod
    def get_european_price(spot_price, strike_price, time_to_maturity, riskfree_rate, underlying_volatility):
        price = calc_european_call(
            S=spot_price, 
            K=strike_price, 
            sigma=underlying_volatility, 
            T=time_to_maturity, 
            r=riskfree_rate
        )
        return price