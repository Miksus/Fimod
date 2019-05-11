


def convert_to_returns(price_frame, freq, closed="right", to_absolute=False, to_cumulative=False):
    """Convert prices to returns
    
    Arguments:
        price_frame {pd.Series, pd.DataFrame} -- [description]
        freq {[type]} -- [description]
    
    Keyword Arguments:
        to_absolute {bool} -- [description] (default: {False})
    
    Returns:
        [type] -- [description]
    """
    resampled = price_frame.resample(freq)

    if closed == "left":
        resampled = resampled.first
    elif closed == "right":
        resampled = resampled.last
    else:
        raise NotImplementedError

    if to_absolute:
        returns = resampled.diff()
        if to_cumulative:
            returns = returns.cumsum()
        return returns
    else:
        returns = resampled.pct_change(fill_method=None)
        if to_cumulative:
            returns = (returns + 1).cumprod() - 1
        return returns