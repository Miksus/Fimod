
from .stock import beta


def treynor_ratio(Rp, Rf, b):
    """Treynor's ratio
    
    Arguments:
        Rp {[type]} -- Portfolio return
        Rf {[type]} -- Risk-free return
        b {[type]} -- Portfolio beta
    """
    return (Rp - Rf) / b


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

