
# !STATE: UNTESTED

import pandas as pd
import numpy as np
import datetime

from typing import Union


from .periodical import group_day, group_week, group_month, group_year, group_period

from risk import beta as calc_beta


def expected_rate_of_return(r_security, r_market, r_riskfree, beta=None):
    """Calculate Expected Return (Capital Asset Pricing Model)
    CAPM = Rf + b(Rm - Rf) 
    """

    if beta is None:
        beta = calc_beta(r_security, r_market)
    

    return riskfree_returns + beta*(r_market - r_riskfree)



# TODO
# Put expected_rate_of_return elsewhere (ACCEPT RETURNS AND NOT PRICES)

def _to_period(series, period):
    if period is None:
        return series

    funcs = {
        "day": group_day,
        "week": group_week,
        "month": group_month,
        "year": group_year
    }
    if period not in funcs:
        grouped = group_period(series, period)
    else:
        func = funcs[period]
        grouped = func(series)
    return grouped.last()



def absolute_return(prices: pd.Series, period="day"):
    "Calculate absolute returns"
    
    return _to_period(prices, period).diff()


def cumulative_absolute_return(prices: pd.Series, period="day"):
    "Calculate cumulative absolute returns"
    
    abs_returns = absolute_return(prices, period)
    return abs_returns.cumsum()


def rate_of_return(prices: Union[pd.Series, pd.DataFrame], period="day") -> Union[pd.Series, pd.DataFrame]:
    """Calculate rate of return
    """
    return _to_period(prices, period).pct_change(fill_method=None)


def cumulative_rate_of_return(prices:pd.Series, **kwargs):
    "Calculate cumulative rate of returns"
    returns = rate_of_return(prices, **kwargs)

    return (returns+1).cumprod()-1





# Short hands (To returns)
def daily_return(security_returns:pd.Series, **kwargs):
    return _to_period(security_returns, "day").pct_change(fill_method=None)

def weekly_return(security_returns:pd.Series, **kwargs):
    return _to_period(security_returns, "week").pct_change(fill_method=None)

def monthly_returns(security_returns:pd.Series, **kwargs):
    return _to_period(security_returns, "month").pct_change(fill_method=None)

def annual_returns(security_returns:pd.Series, **kwargs):
    return _to_period(security_returns, "year").pct_change(fill_method=None)


