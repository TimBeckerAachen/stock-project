import yfinance as yf
import pandas as pd


def get_stock_data(tickers: list[str], num_days: int) -> dict[str, pd.DataFrame]:
    """
    Fetches the latest num_days of stock data for the given tickers from Yahoo Finance.

    :param tickers: A list of stock tickers (e.g., ['AAPL', 'MSFT', 'GOOGL'])
    :param num_days: Number of latest data points (trading days) to fetch.
    :return: A dictionary where each key is a ticker and the value is a DataFrame with the stock data.
    """
    stock_data = {}
    approximate_days = num_days * 2

    if approximate_days <= 5:
        period = "5d"
    elif approximate_days <= 30:
        period = "1mo"
    elif approximate_days <= 90:
        period = "3mo"
    elif approximate_days <= 180:
        period = "6mo"
    elif approximate_days <= 360:
        period = "1y"
    else:
        raise ValueError(f"Fetching that {num_days} days is not supported! Reduce the number of days")

    for ticker in tickers:
        df = yf.download(ticker, period=period, interval="1d", progress=False)
        stock_data[ticker] = df.tail(num_days)

    return stock_data

