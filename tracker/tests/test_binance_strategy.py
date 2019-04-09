import os
import unittest

from model.entry import Entry
from strategy.binance import BinanceStrategy

from tests import helpers


SHAKEPAY_RESOURCES_PATH = helpers.TEST_RESOURCES_PATH + ['binance']


class BinanceStrategyTest(unittest.TestCase):

  def setUp(self):
    self.strategy = BinanceStrategy()

  def test_convert_data_empty_file(self):
    expected = []

    self._assert_convert_data(expected, 'empty.csv', helpers.TEST_RESOURCES_PATH)

  def test_convert_data_headers_only(self):
    expected = []

    self._assert_convert_data(expected, 'headers_only.csv', SHAKEPAY_RESOURCES_PATH)

  def _assert_convert_data(self, expected, filename, file_path):
    result = self.strategy.convert_data(helpers.get_absolute_file_path(filename, *file_path))

    self.assertEqual(expected, result)

  def test_split_transaction_buy_with_same_fee_currency_returns_only_buy_transaction(self):
    # Date(UTC),Market,Type,Price,Amount,Total,Fee,Fee Coin
    # 2018-01-20 16:59:59,XLMETH,BUY,0.00012345,123,0.01518435,0.123,XLM
    expected_buy = {'Date(UTC)': '2018-01-20 16:59:59',
                    'Currency': 'XLM',
                    'Type': 'BUY',
                    'Amount': '123',
                    'Fee': '0.123'
                    }
    expected = [expected_buy]

    transaction = {'Date(UTC)': '2018-01-20 16:59:59',
                   'Market': 'XLMETH',
                   'Type': 'BUY',
                   'Price': '0.00012345',
                   'Amount': '123',
                   'Total': '0.01518435',
                   'Fee': '0.123',
                   'Fee Coin': 'XLM'
                   }

    self._assert_split_transaction(expected, transaction)

  def test_split_transaction_buy_with_different_fee_currency_returns_buy_and_fee_transactions(self):
    # Date(UTC),Market,Type,Price,Amount,Total,Fee,Fee Coin
    # 2018-05-11 21:42:11,ZILBTC,BUY,0.00001111,999,0.01109889,0.00077777,BNB
    expected_fee = {'Date(UTC)': '2018-05-11 21:42:11',
                    'Currency': 'BNB',
                    'Type': 'BUY',
                    'Amount': '0',
                    'Fee': '0.00077777'
                    }
    expected_buy = {'Date(UTC)': '2018-05-11 21:42:11',
                    'Currency': 'ZIL',
                    'Type': 'BUY',
                    'Amount': '999',
                    'Fee': '0'
                    }
    expected = [expected_fee, expected_buy]

    transaction = {'Date(UTC)': '2018-05-11 21:42:11',
                   'Market': 'ZILBTC',
                   'Type': 'BUY',
                   'Price': '0.00001111',
                   'Amount': '999',
                   'Total': '0.01518435',
                   'Fee': '0.00077777',
                   'Fee Coin': 'BNB'
                   }

    self._assert_split_transaction(expected, transaction)

  def _assert_split_transaction(self, expected, transaction):
    result = self.strategy._split_transaction(transaction)

    self.assertEqual(expected, result)
