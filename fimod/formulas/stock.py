
import numpy as np

def sharpe(R, Rf, sigma):
    """Sharpe ratio
    
    Arguments:
        R {[type]} -- Asset return
        Rf {[type]} -- Risk-free return
        sigma {[type]} -- Asset Standard Deviation
    """
    return (R - Rf) / sigma

def alpha(R, Rm, b, Rf):
    """Jensen's Alpha
    
    Arguments:
        R {[type]} -- Asset return
        Rm {[type]} -- Market return
        b {[type]} -- Asset beta
        Rf {[type]} -- Risk-free return
    
    Returns:
        [type] -- [description]
    """
    return R - (Rf + b*(Rm - Rf))

def beta(R, Rf):
    """Beta
    
    Arguments:
        R {[type]} -- Asset return
        Rf {[type]} -- Risk-free return
    
    """
    cov = np.cov(R, Rf)
    var = np.var(R)
    return cov / var

def value_at_risk(R, sigma, alpha=0.05):
    """VaR (Method: Variance-Covariance Method)
    
    Arguments:
        R {[type]} -- Asset return
        sigma {[type]} -- Asset standard deviation
        alpha {float} -- Significance level (default: {0.05})
    """
    p = 1-alpha # one tailed probability
    Z = stats.norm.ppf(p) # Z score

    return R - Z * sigma

def expected_return(Rm, b, Rf):
    """CAPM (Capital Asset Pricing Model)
    
    Arguments:
        Rm {[type]} -- Market return
        b {[type]} -- Asset beta
        Rf {[type]} -- Risk-free return
    """
    return Rf + b*(Rm - Rf)