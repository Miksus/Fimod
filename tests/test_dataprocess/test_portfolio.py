
import pytest
import fimod
import numpy as np
import pandas as pd

def test_volatility_three_assets_with_cov_matrix():
    # Source: https://zerodha.com/varsity/chapter/risk-part-4-correlation-matrix-portfolio-variance/
    weights = np.array([7.00, 16.00, 25.00, 30.00, 22.00]) / 100
    cov_matrix = np.array([
        [0.0002194912630240880,	0.0000534668270279167,	0.0000334568709919831,	0.0000405389162821580,	0.0000633272461418023],
        [0.0000534668270279167,	0.0011089816927407000,	0.0000390975916989801,	0.0000227229941956951,	0.0000373731713775074],
        [0.0000334568709919831,	0.0000390975916989801,	0.0002405251746814680,	0.0000393614648047395,	0.0000276645081495045],
        [0.0000405389162821580,	0.0000227229941956951,	0.0000393614648047395,	0.0004022457937988150,	0.0000265795579238825],
        [0.0000633272461418023,	0.0000373731713775074,	0.0000276645081495045,	0.0000265795579238825,	0.0003393321844739220],
    ])
    expected = 1.11149415424894 / 100

    actual = finmod.datatools.portfolio.volatility(weights, cov_matrix=cov_matrix)
    assert round(expected, 5) == round(actual, 5)

def test_volatility_three_assets_with_returns():
    df_test = pd.read_excel("tests/test_data.xlsx", sheet_name="portfolio")
    cov_matrix = df_test.pct_change().cov()
    weights = np.array([7.00, 16.00, 25.00, 30.00, 22.00]) / 100
    expected = 1.11149415424894 / 100

    actual = finmod.datatools.portfolio.volatility(weights, cov_matrix) 
    assert round(expected, 3) == round(actual, 3)

def test_volatility_own_data():
    cov_matrix = np.array([
        [0.000320422528410904,	0.000031658195109736,	0.000041599619200370,	0.000051398375340468],
        [0.000031658195109736,	0.000174238616891167,	0.000051953158800973,	0.000039699413624074],
        [0.000041599619200370,	0.000051953158800973,	0.000208217667181106,	0.000047074983745919],
        [0.000051398375340468,	0.000039699413624074,	0.000047074983745919,	0.000133178222336378],
    ])
    weights = [0.423441648886495, 0.000000000000000, 0.248890082028500, 0.327668265348697]
    expected = 0.00537320225852404
    actual = finmod.datatools.portfolio.volatility(weights, cov_matrix=cov_matrix) * np.sqrt(252)
    assert round(expected, 5) == round(actual, 5)
