
import numpy as np

def volatility(weights, cov_matrix):
    """Calculate portfolio standard deviation

    Arguments:
        weights {List[float]} -- Weights of assets
        cov_matrix {List[List]} -- Covariance matrix

    """
    weights = np.array(weights)
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))


def returns(returns, weights):
    """Calculate portfolio returns
    
    Arguments:
        returns {[type]} -- [description]
        weights {[type]} -- [description]
    
    """
    returns = np.array(returns)
    weights = np.array(weights)

    return np.sum(returns * weights)