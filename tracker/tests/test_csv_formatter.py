import os
import unittest

from datetime import datetime
from decimal import Decimal

from model.entry import Entry
from model.types import TransactionTypes
from format.csv import CsvFormatter


class CsvFormatterTest(unittest.TestCase):

  def setUp(self):
    self.formatter = CsvFormatter()

  def test_format_no_data(self):
    expected = []

    self._assert_format(expected, None)

  def test_format_empty_data(self):
    expected = []

    self._assert_format(expected, [])

  def test_format_one_buy_entry(self):
    expected = [self._build_expected_buy_formatted_data('1')]

    entry = self._build_entry('1', TransactionTypes.BUY)

    self._assert_format(expected, [entry])

  def test_format_one_sell_entry(self):
    expected = [self._build_expected_sell_formatted_data('1')]

    entry = self._build_entry('1', TransactionTypes.SELL)

    self._assert_format(expected, [entry])

  def _assert_format(self, expected, data):
    result = self.formatter.format(data)

    self.assertEqual(expected, result)

  def _build_entry(self, id, transaction_type):
    entry = Entry()
    entry.currency = 'A' + id
    entry.date = datetime.fromtimestamp(1526634520)
    entry.transaction_type = transaction_type
    entry.rate = Decimal(1)
    entry.amount = Decimal(2)
    entry.cost = Decimal(3)
    entry.fee = Decimal(4)
    entry.fee_cost = Decimal(5)
    entry.note = 'C' + id

    return entry

  def _build_expected_buy_formatted_data(self, id):
    return 'A' + id + ',05/18/2018 05:08:40' + ',1,2,3,0,0,0,4,5,0,0,0,0,0,C' + id

  def _build_expected_sell_formatted_data(self, id):
    return 'A' + id + ',05/18/2018 05:08:40' + ',1,0,3,2,6,0,4,5,0,0,0,0,0,C' + id
