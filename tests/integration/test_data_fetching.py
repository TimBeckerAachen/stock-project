import unittest
from stock_project.data_fetching import get_stock_data


class TestFetchStockData(unittest.TestCase):

    def test_single_ticker_few_days(self):
        tickers = ['AAPL']
        num_days = 5
        data = get_stock_data(tickers, num_days)
        self.assertIn('AAPL', data)
        self.assertEqual(len(data['AAPL']), num_days)
        self.assertFalse(data['AAPL'].isnull().values.any())

    def test_multiple_tickers(self):
        tickers = ['AAPL', 'MSFT', 'GOOGL']
        num_days = 10
        data = get_stock_data(tickers, num_days)
        for ticker in tickers:
            self.assertIn(ticker, data)
            self.assertEqual(len(data[ticker]), num_days)
            self.assertFalse(data[ticker].isnull().values.any())

    def test_zero_days(self):
        tickers = ['AAPL']
        num_days = 0
        data = get_stock_data(tickers, num_days)
        self.assertEqual(len(data['AAPL']), 0)

    def test_invalid_ticker(self):
        tickers = ['INVALID']
        num_days = 5
        data = get_stock_data(tickers, num_days)
        self.assertIn('INVALID', data)
        self.assertEqual(len(data['INVALID']), 0)

    def test_value_error_for_too_many_days(self):
        tickers = ['AAPL']
        num_days = 190

        with self.assertRaises(ValueError) as context:
            get_stock_data(tickers, num_days)

        self.assertEqual(
            str(context.exception),
            f"Fetching that {num_days} days is not supported! Reduce the number of days"
        )
