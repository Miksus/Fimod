
# !STATE: UNTESTED

import pandas as pd
import numpy as np
from scipy import stats

from typing import Union
import functools


def regression_beta(security_returns:pd.Series, market_returns:pd.Series, significance_level=0.05) -> dict:
    "Calculate regression and then betas, alphas, intercepts ect."
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(market_returns.values, security_returns.values)

    probability = 1-significance_level/2 #two tailed
    z_score = stats.norm.ppf(probability)

    return {
        "Company":security_returns.name, 
        "Beta":slope, 
        "Lower bound (beta)": slope-z_score*std_err, 
        "Upper bound (beta)": slope+z_score*std_err, 
        "Alpha": intercept,
        "P-value": p_value
    }
    

def beta(r_security:pd.Series, r_market:pd.Series) -> float:
    "Cov(rs, rm)/var(rm)"
    if hasattr(r_market, "cov") and hasattr(r_market, "var"):
        return r_security.cov(r_market) / r_market.var()
    else:
        raise NotImplementedError(f"Beta not implemented for {type(r_security)} and {type(r_market)}")

def value_at_risk(r_security, extrapolate_periods=1, significance_level=0.05):
    """Value at Risk (VaR)
    
    Arguments:
        r_security {[type]} -- [description]
    
    Keyword Arguments:
        extrapolate_periods {int} -- [description] (default: {1})
        significance_level {float} -- [description] (default: {0.05})
    
    Raises:
        NotImplementedError -- [description]
    
    VaR = r - z_score*std_dev
    VaR(n) = VaR(1)*sqrt(n)

    See also
    https://www.investopedia.com/articles/04/101304.asp
    """


    probability = 1-significance_level # one tailed probability
    z_score = stats.norm.ppf(probability)

    if all(hasattr(r_security, attr) for attr in ("std", "mean")):
        std_dev = r_security.std()
        mean_return = r_security.mean()
        var = mean_return - z_score*std_dev
    else:
        raise NotImplementedError(f"Beta not implemented for {type(r_security)} and {type(r_market)}")
    
    return var*np.sqrt(extrapolate_periods)


def std(returns:Union[pd.Series, pd.DataFrame]) -> Union[float, pd.Series]:
    return returns.std(ddof=0)



