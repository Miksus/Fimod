
# !STATE: UNTESTED

import itertools
from typing import List, Dict, AnyStr

from .risk import beta


def sharpe(r_portfolio, r_riskfree, std_portfolio):
    """Calculate Sharpe of a portfolio
    
    Arguments:
        r_portfolio {pd.Series, float} -- Average return of portfolio
        r_riskfree {pd.Series, float} -- Risk-free rate of return
        std_portfolio {pd.Series, float} -- Standard deviation of portfolio returns (r_portfolio)
    
    """
    return (r_portfolio - r_riskfree) / std_portfolio


def alpha(r_portfolio, r_market,  r_riskfree, r_expected=None, **kwargs):
    """Calculate Alpha of a portfolio

    Arguments:
        r_portfolio {[type]} -- [description]
        r_market {[type]} -- Market returns
        r_riskfree {[type]} -- Risk-free returns
        r_expected {[type]} -- Expected returns

    alpha = r - e
    alpha = r - [r_f + b*(r_m - r_f)]
        Where
            e : expected return of the security
            r : return of the security
            r_f : risk-free rate
            r_m : market return
            b : beta
    """
    if r_expected is None:
        r_expected = (r_riskfree + beta*(r_market - r_riskfree))
        
    return r_portfolio - r_expected


def standard_deviation(std_assets:List[float], w_assets:List[float], cov_matrix:List[List]):
    """Calculate portfolio standard deviation

    Arguments:
        std_assets {List[float]} -- Standard deviations of assets
        w_assets {List[float]} -- Weights of assets
        cov_matrix {List[List]} -- Covariance matrix
    
    Example:
    >>> std_assets = []
    >>> w_assets = [.2, .4, .4]
    >>> cov_matrix = [[..., ..., ...], [..., ..., ], [..., ..., ...]]

    Theory:
        With 2 Assets:
            std = sqrt(w_i^2*std_i^2 + w_j^2*std_j^2 + 2*w_i*w_j*COV_ij)
    """
    # To index sets: [(i, j)]
    indexes = range(len(std_assets))

    weights = w_assets
    stds = std_assets
    COV = cov_matrix
    volatility = sum(

        weights[i]**2 + weights[j]**2 + stds[i]**2 + stds[j]**2
        + 2*weights[i]*weights[j]*COV[i][j]

        for i, j in itertools.combinations(indexes, 2)
    )
    return sqrt(volatility)


def returns(r_assets, w_assets):
    """Calculate portfolio returns
    
    Arguments:
        r_assets {[type]} -- [description]
        w_assets {[type]} -- [description]
    
    Returns:
        [type] -- [description]

    >>> returns(
        pd.DataFrame([[1,2,3, ...], [1,2,3, ...]], columns=["Asset A", "Asset B", "Asset C"]), 
        pd.Series([0.2, 0.5, 0.8], index=["Asset A", "Asset B", "Asset C"])
    )
    """
    
    try:
        # Try pandas
        portfolio_returns = (r_assets * w_assets).sum()
    except TypeError:
        portfolio_returns = sum(r*w for r, w in zip(r_asset, w_assets))

    return portfolio_returns