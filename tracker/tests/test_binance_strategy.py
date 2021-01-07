import unittest

from datetime import datetime
from decimal import Decimal
from pytz import timezone

from model.entry import Entry
from model.types import TransactionTypes
from strategy.binance import BinanceStrategy
from tests import helpers

BINANCE_RESOURCES_PATH = helpers.TEST_RESOURCES_PATH + ['binance']


class BinanceStrategyTest(unittest.TestCase):

    def setUp(self):
        self.strategy = BinanceStrategy()

    def test_convert_data_empty_file(self):
        expected = []

        self._assert_convert_data(expected, 'empty.csv', helpers.TEST_RESOURCES_PATH)

    def test_convert_data_headers_only(self):
        expected = []

        self._assert_convert_data(expected, 'headers_only.csv', BINANCE_RESOURCES_PATH)

    def test_convert_data_buy_same_fee_coin(self):
        expected_trade = self._build_entry('XLM', 'ETH', '0.00012345', '123', '0.01518435', '0.123')
        expected = [expected_trade]

        self._assert_convert_data(expected, 'buy_same_fee_coin.csv', BINANCE_RESOURCES_PATH)

    def test_convert_data_buy_different_fee_coin(self):
        expected_fee = self._build_buy_entry('BNB', '0.0', '0.00054321')
        expected_buy = self._build_buy_entry('XLM', '123.0', '0.0')
        expected_sell = self._build_sell_entry('ETH', '0.01518435')
        expected = [expected_fee, expected_buy, expected_sell]

        self._assert_convert_data(expected, 'buy_diff_fee_coin.csv', BINANCE_RESOURCES_PATH)

    def test_convert_data_sell_same_fee_coin(self):
        expected_buy = self._build_buy_entry('ETH', '0.01518435', '0.00007592175')
        expected_sell = self._build_sell_entry('XLM', '123.0')
        expected = [expected_buy, expected_sell]

        self._assert_convert_data(expected, 'sell_same_fee_coin.csv', BINANCE_RESOURCES_PATH)

    def test_convert_data_sell_different_fee_coin(self):
        expected_fee = self._build_buy_entry('BNB', '0.0', '0.00151515')
        expected_buy = self._build_buy_entry('ETH', '0.01518435', '0.0')
        expected_sell = self._build_sell_entry('XLM', '123.0')
        expected = [expected_fee, expected_buy, expected_sell]

        self._assert_convert_data(expected, 'sell_diff_fee_coin.csv', BINANCE_RESOURCES_PATH)

    def _build_entry(self, credit_currency, debit_currency, price, credit_amount, debit_amount, fee='0'):
        entry = Entry()
        entry.date = datetime.fromtimestamp(1516467599, timezone('US/Eastern'))
        entry.credit_currency = credit_currency
        entry.debit_currency = debit_currency
        entry.price = price
        entry.credit_amount = credit_amount
        entry.debit_amount = debit_amount
        entry.fee = fee
        return entry

    def _assert_convert_data(self, expected, filename, file_path):
        result = self.strategy.convert_data(helpers.get_absolute_file_path(filename, *file_path))

        self.assertEqual(expected, result)
