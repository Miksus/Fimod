from .instrument import Instrument
from ...formulas.stock import sharpe, alpha

class Stock(Instrument):

    # Dynamic values
    price = None
    volatility = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def payoff(self):
        spot_price = self.price
        if self.position == "long":
            return spot_price - self.buying_price
        elif self.position == "short":
            return self.selling_price - spot_price
        else:
            raise TypeError
    
    @property
    def sharpe(self):
        return 

    def calc_alpha(self, riskfree_rate, ):
        pass
    
    @property
    def buying_price(self):
        if self.position == "long":
            return self.trade_price
        else:
            raise AttributeError(f"No buying price for {self.position} position")
    
    @property
    def selling_price(self):
        if self.position == "short":
            return self.trade_price
        else:
            raise AttributeError(f"No selling price for {self.position} position")
            
    def __str__(self):
        if self.ticker:
            return f'{self.ticker} stock {self.position}'
        else:
            return f'Stock {self.position}'