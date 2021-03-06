
import numpy as np
import matplotlib.pyplot as plt

def plot_payoff(*investments, pricerange=None, invline_kwds={}, portfline_kwds={}, title="Payoff"):

    for investment in investments:
        investment.underlying.price = pricerange

    total = np.sum([investment.payoff() for investment in investments], axis=0)
    
    for investment in investments:
        plt.plot(pricerange, investment.payoff(), label=str(investment), **invline_kwds)
        
    plt.plot(pricerange, total, label="Portfolio", **portfline_kwds)
    
    plt.axhline(0, linestyle="-", alpha=0.5, color="k", zorder=-1)
    plt.axis('equal')

    plt.xlabel("Price of Underlying")
    plt.ylabel("Payoff")
    
    plt.legend()
    plt.title(title)