import os
import unittest

from datetime import datetime
from decimal import Decimal
from pytz import timezone

from model.entry import Entry
from model.types import TransactionTypes
from strategy.shakepay import ShakepayStrategy
from tests import helpers


SHAKEPAY_RESOURCES_PATH = helpers.TEST_RESOURCES_PATH + ['shakepay']


class ShakepayStrategyTest(unittest.TestCase):

  def setUp(self):
    self.strategy = ShakepayStrategy()

  def test_convert_data_empty_file(self):
    expected = []

    self._assert_convert_data(expected, 'empty.csv', helpers.TEST_RESOURCES_PATH)

  def test_convert_data_headers_only(self):
    expected = []

    self._assert_convert_data(expected, 'headers_only.csv', SHAKEPAY_RESOURCES_PATH)

  def test_convert_data(self):
    entry_0 = Entry()
    entry_0.currency = 'BTC'
    entry_0.date = datetime.fromtimestamp(1526648920, timezone('US/Eastern'))
    entry_0.transaction_type = TransactionTypes.BUY
    entry_0.rate = Decimal('10343.0693')
    entry_0.amount = Decimal('0.0000001')
    entry_0.cost = Decimal('100')

    entry_1 = Entry()
    entry_1.currency = 'ABC'
    entry_1.date = datetime.fromtimestamp(1527913940, timezone('US/Eastern'))
    entry_1.transaction_type = TransactionTypes.BUY
    entry_1.rate = Decimal('9663.5397')
    entry_1.amount = Decimal('123.456')
    entry_1.cost = Decimal('400')

    entry_2 = Entry()
    entry_2.currency = 'ETH'
    entry_2.date = datetime.fromtimestamp(1530761108, timezone('US/Eastern'))
    entry_2.transaction_type = TransactionTypes.BUY
    entry_2.rate = Decimal('8552.2188')
    entry_2.amount = Decimal('0.01987')
    entry_2.cost = Decimal('125')

    expected = [entry_0, entry_1, entry_2]

    self._assert_convert_data(expected, 'sample_data.csv', SHAKEPAY_RESOURCES_PATH)

  def _assert_convert_data(self, expected, filename, file_path):
    result = self.strategy.convert_data(helpers.get_absolute_file_path(filename, *file_path))

    self.assertEqual(expected, result)
