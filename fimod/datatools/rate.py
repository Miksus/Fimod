
DAYS_IN_YEAR = 365

DAY_MAPPING = {
    "annual": DAYS_IN_YEAR,
    "semi annual": DAYS_IN_YEAR / 2,
    "quartal": 90,
    "monthly": 30,
    "weekly": 7,
    "daily": 1,
}


def convert(rate, from_freq, as_freq="daily", effective_rate=True):

    origin_in_days = DAY_MAPPING[from_freq]
    out_in_days = DAY_MAPPING[as_freq]

    if effective_rate:
        daily_rate = (1 + rate) ** (1 / origin_in_days) - 1
        return (1 + daily_rate) ** out_in_days - 1
    else:
        daily_rate = rate / origin_in_days
        return daily_rate * out_in_days
