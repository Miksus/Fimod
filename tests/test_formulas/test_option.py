
import pytest
import sys
sys.path.append('..')

from fimod.formulas.derivatives import option

"""
Example Exercise:
    A 6-month call option with an exercise 
    price of $50 on a stock that is trading 
    at $52 costs $4.5. Determine whether you 
    should buy the option if the annual risk-free 
    rate is 5% and the annual standard deviation 
    of the stock returns is 12%.
        https://xplaind.com/793334/black-scholes
"""


def test_d1():
    precision = 4

    S = 52
    K = 50
    T = 0.5
    r = 0.05
    sigma = 0.12

    d1_expected = 0.7993
    d1_actual = option.d1(S=S, K=K, T=T, r=r, sigma=sigma)
    assert round(d1_expected, precision) == round(d1_actual, precision)

def test_d2():
    precision = 4
    S = 52
    K = 50
    T = 0.5
    r = 0.05
    sigma = 0.12

    d2_expected = 0.7144
    d2_actual = option.d2(S=S, K=K, T=T, r=r, sigma=sigma)
    assert round(d2_expected, precision) == round(d2_actual, precision)

def test_european_call_price():
    precision = 3 

    S = 52
    K = 50
    T = 0.5
    r = 0.05
    sigma = 0.12
    q = 0

    C_expected = 3.788 # Verified with: https://www.mystockoptions.com/black-scholes.cfm?ticker=&s=52&x=50&t=0.5&r=5%25&v=12%25&calculate=Calculate
    C_actual = option.european_call_price(S=S, K=K, T=T, r=r, sigma=sigma, q=q)
    assert round(C_expected, precision) == round(C_actual, precision)


def test_european_put_price():
    # Source: https://goodcalculators.com/black-scholes-calculator/
    precision = 2

    S = 52
    K = 50
    T = 0.5
    r = 0.05
    sigma = 0.12
    q = 0

    C_expected = 0.55
    C_actual = option.european_put_price(S=S, K=K, T=T, r=r, sigma=sigma, q=q)
    assert round(C_expected, precision) == round(C_actual, precision)

def test_european_call_price_with_q():
    # Source: https://goodcalculators.com/black-scholes-calculator/
    precision = 2

    S = 52
    K = 50
    T = 0.5
    r = 0.05
    sigma = 0.12
    q = 0.05

    C_expected = 2.83
    C_actual = option.european_call_price(S=S, K=K, T=T, r=r, sigma=sigma, q=q)
    assert round(C_expected, precision) == round(C_actual, precision)

def test_european_put_price_with_q():
    # Source: https://goodcalculators.com/black-scholes-calculator/
    precision = 2

    S = 52
    K = 50
    T = 0.5
    r = 0.05
    sigma = 0.12
    q = 0.05

    C_expected = 0.89
    C_actual = option.european_put_price(S=S, K=K, T=T, r=r, sigma=sigma, q=q)
    assert round(C_expected, precision) == round(C_actual, precision)
