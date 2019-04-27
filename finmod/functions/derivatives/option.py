
# !State: NOT TESTED

import numpy as np
from scipy import stats

# Black and Scholes
def european_call_price(S, K, T, r, sigma, q=0):
    """
    S = Underlying's spot
    K = Strike
    T = time to maturity
    r = riskless rate
    sigma = volatility of underlying
    q = dividend rate
    """
    d1_ = d1(S, K, T, r, sigma)
    d2_ = d2(S, K, T, r, sigma)
    if q == 0:
        return (S * stats.norm.cdf(d1_) - K * np.exp(-r * T) * stats.norm.cdf(d2_))
    else:
        return (S * np.exp(-q*T) * stats.norm.cdf(d1_) - K * np.exp(-r * T) * stats.norm.cdf(d2_))

def european_put_price(S, K, T, r, sigma, q=0):
    """
    Arguments:
        S -- Underlying's spot
        K -- Strike
        T -- Time to Maturity
        r -- Riskless Rate
        sigma -- Volatility of Underlying
        q -- Dividend rate (default: no dividend)
    """
    d1_ = d1(S, K, T, r, sigma)
    d2_ = d2(S, K, T, r, sigma)
    if q == 0:
        return K * np.exp(-r * T) * stats.norm.cdf(-d2_) - S * stats.norm.cdf(-d1_)
    else:
        return K * np.exp(-r * T) * stats.norm.cdf(-d2_) - S * np.exp(-q * T) * stats.norm.cdf(-d1_)

def d1(S, K, T, r, sigma):
    """Calculate d1 in B&S
    
    Arguments:
        S -- Underlying's spot
        K -- Strike
        T -- Time to Maturity
        r -- Riskless Rate
        sigma -- Volatility of Underlying
    """
    return (np.log(S / K) + (r + (sigma ** 2 / 2)) * T) / (sigma * np.sqrt(T))

def d2(S, K, T, r, sigma):
    """Calculate d2 in B&S
    
    Arguments:
        S -- Underlying's spot
        K -- Strike
        T -- Time to Maturity
        r -- Riskless Rate
        sigma -- Volatility of Underlying
    """
    return (np.log(S / K) + (r - (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))


# Greeks
def delta_call(S, K, T, r, sigma, q=0):
    "NOTE: European"
    d1_ = d1(S, K, T, r, sigma)
    if q == 0:
        return stats.norm.cdf(d1_)
    else:
        return np.exp(-q*T) * stats.norm.cdf(d1_)

def delta_put(S, K, T, r, sigma, q=0):
    "NOTE: European"
    d1_ = d1(S, K, T, r, sigma)
    if q == 0:
        return stats.norm.cdf(d1_) - 1
    else:
        return np.exp(-q*T) * stats.norm.cdf(d1_) - 1

# To be implemented Greeks
#   Gamma
#   Vega
