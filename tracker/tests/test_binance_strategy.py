import os
import unittest

from datetime import datetime
from decimal import Decimal
from pytz import timezone

from model.entry import Entry
from model.types import TransactionTypes
from strategy.binance import BinanceStrategy
from tests import helpers

SHAKEPAY_RESOURCES_PATH = helpers.TEST_RESOURCES_PATH + ['binance']


class BinanceStrategyTest(unittest.TestCase):

  def setUp(self):
    self.strategy = BinanceStrategy()

  def test_split_transaction_buy_with_same_fee_currency_returns_buy_and_sell_transactions(self):
    # Date(UTC),Market,Type,Price,Amount,Total,Fee,Fee Coin
    # 2018-01-20 16:59:59,XLMETH,BUY,0.00012345,123,0.01518435,0.123,XLM
    expected_buy = {'Date(UTC)': '2018-01-20 16:59:59',
                    'Currency': 'XLM',
                    'Type': 'BUY',
                    'Amount': '123',
                    'Fee': '0.123'
                    }
    expected_sell = {'Date(UTC)': '2018-01-20 16:59:59',
                     'Currency': 'ETH',
                     'Type': 'SELL',
                     'Amount': '0.01518435',
                     'Fee': '0'
                     }
    expected = [expected_buy, expected_sell]

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

  def test_split_transaction_buy_with_different_fee_currency_returns_buy_and_fee_and_sell_transactions(self):
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
    expected_sell = {'Date(UTC)': '2018-05-11 21:42:11',
                     'Currency': 'BTC',
                     'Type': 'SELL',
                     'Amount': '0.01109889',
                     'Fee': '0'
                     }
    expected = [expected_fee, expected_buy, expected_sell]

    transaction = {'Date(UTC)': '2018-05-11 21:42:11',
                   'Market': 'ZILBTC',
                   'Type': 'BUY',
                   'Price': '0.00001111',
                   'Amount': '999',
                   'Total': '0.01109889',
                   'Fee': '0.00077777',
                   'Fee Coin': 'BNB'
                   }

    self._assert_split_transaction(expected, transaction)

  def test_split_transaction_sell_with_same_fee_currency_returns_buy_and_sell_transactions(self):
    # Date(UTC),Market,Type,Price,Amount,Total,Fee,Fee Coin
    # 2018-11-01 23:23:23,LTCBTC,SELL,0.015151,0.75,0.01136325,0.00005682,BTC
    expected_buy = {'Date(UTC)': '2018-11-01 23:23:23',
                    'Currency': 'BTC',
                    'Type': 'BUY',
                    'Amount': '0.01136325',
                    'Fee': '0.00005682'
                    }
    expected_sell = {'Date(UTC)': '2018-11-01 23:23:23',
                     'Currency': 'LTC',
                     'Type': 'SELL',
                     'Amount': '0.75',
                     'Fee': '0'
                     }
    expected = [expected_buy, expected_sell]

    transaction = {'Date(UTC)': '2018-11-01 23:23:23',
                   'Market': 'LTCBTC',
                   'Type': 'SELL',
                   'Price': '0.015151',
                   'Amount': '0.75',
                   'Total': '0.01136325',
                   'Fee': '0.00005682',
                   'Fee Coin': 'BTC'
                   }

    self._assert_split_transaction(expected, transaction)

  def test_split_transaction_sell_with_different_fee_currency_returns_buy_and_fee_and_sell_transactions(self):
    # Date(UTC),Market,Type,Price,Amount,Total,Fee,Fee Coin
    # 2018-11-01 23:23:23,LTCBTC,SELL,0.015151,0.75,0.01136325,0.00123456,BNB
    expected_fee = {'Date(UTC)': '2018-11-01 23:23:23',
                    'Currency': 'BNB',
                    'Type': 'BUY',
                    'Amount': '0',
                    'Fee': '0.00123456'
                    }
    expected_buy = {'Date(UTC)': '2018-11-01 23:23:23',
                    'Currency': 'BTC',
                    'Type': 'BUY',
                    'Amount': '0.01136325',
                    'Fee': '0'
                    }
    expected_sell = {'Date(UTC)': '2018-11-01 23:23:23',
                     'Currency': 'LTC',
                     'Type': 'SELL',
                     'Amount': '0.75',
                     'Fee': '0'
                     }
    expected = [expected_fee, expected_buy, expected_sell]

    transaction = {'Date(UTC)': '2018-11-01 23:23:23',
                   'Market': 'LTCBTC',
                   'Type': 'SELL',
                   'Price': '0.015151',
                   'Amount': '0.75',
                   'Total': '0.01136325',
                   'Fee': '0.00123456',
                   'Fee Coin': 'BNB'
                   }

    self._assert_split_transaction(expected, transaction)

  def _assert_split_transaction(self, expected, transaction):
    result = self.strategy._split_transaction(transaction)

    self.assertEqual(expected, result)

  def test_convert_data_empty_file(self):
    expected = []

    self._assert_convert_data(expected, 'empty.csv', helpers.TEST_RESOURCES_PATH)

  def test_convert_data_headers_only(self):
    expected = []

    self._assert_convert_data(expected, 'headers_only.csv', SHAKEPAY_RESOURCES_PATH)

  def test_convert_data_buy_same_fee_coin(self):
    expected_buy = self._build_buy_entry('XLM', '123.0', '0.123')
    expected_sell = self._build_sell_entry('ETH', '0.01518435')
    expected = [expected_buy, expected_sell]

    self._assert_convert_data(expected, 'buy_same_fee_coin.csv', SHAKEPAY_RESOURCES_PATH)

  def test_convert_data_buy_different_fee_coin(self):
    expected_fee = self._build_buy_entry('BNB', '0.0', '0.00054321')
    expected_buy = self._build_buy_entry('XLM', '123.0', '0.0')
    expected_sell = self._build_sell_entry('ETH', '0.01518435')
    expected = [expected_fee, expected_buy, expected_sell]

    self._assert_convert_data(expected, 'buy_diff_fee_coin.csv', SHAKEPAY_RESOURCES_PATH)

  def test_convert_data_sell_same_fee_coin(self):
    expected_buy = self._build_buy_entry('ETH', '0.01518435', '0.00007592175')
    expected_sell = self._build_sell_entry('XLM', '123.0')
    expected = [expected_buy, expected_sell]

    self._assert_convert_data(expected, 'sell_same_fee_coin.csv', SHAKEPAY_RESOURCES_PATH)

  def test_convert_data_sell_different_fee_coin(self):
    expected_fee = self._build_buy_entry('BNB', '0.0', '0.00151515')
    expected_buy = self._build_buy_entry('ETH', '0.01518435', '0.0')
    expected_sell = self._build_sell_entry('XLM', '123.0')
    expected = [expected_fee, expected_buy, expected_sell]

    self._assert_convert_data(expected, 'sell_diff_fee_coin.csv', SHAKEPAY_RESOURCES_PATH)

  def _build_buy_entry(self, currency, deposit, fee):
    entry = self._build_entry(currency)
    entry.transaction_type = TransactionTypes.BUY
    entry.amount = Decimal(deposit)
    entry.fee = Decimal(fee)
    return entry

  def _build_sell_entry(self, currency, withdrawl):
    entry = self._build_entry(currency)
    entry.transaction_type = TransactionTypes.SELL
    entry.amount = Decimal(withdrawl)
    return entry

  def _build_entry(self, currency):
    entry = Entry()
    entry.currency = currency
    entry.date = datetime.fromtimestamp(1516467599, timezone('US/Eastern'))
    return entry

  def _assert_convert_data(self, expected, filename, file_path):
    result = self.strategy.convert_data(helpers.get_absolute_file_path(filename, *file_path))

    self.assertEqual(expected, result)
