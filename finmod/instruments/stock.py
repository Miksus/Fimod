from .instrument import Instrument

class Stock(Instrument):
    
    def __init__(self, price, ticker=None, **kwargs):
        
        self.trade_price = price
        
        self.ticker = ticker
        
        super().__init__(**kwargs)
    
    def payoff(self, spot_price):
        if self.position == "long":
            return spot_price - self.buying_price
        elif self.position == "short":
            return self.selling_price - spot_price
        else:
            raise TypeError
    
    
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