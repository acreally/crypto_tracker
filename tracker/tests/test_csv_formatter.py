import os
import unittest

from model.entry import Entry
from format.csv import CsvFormatter

class ShakepayStrategyTest(unittest.TestCase):
  def setUp(self):
    self.formatter = CsvFormatter()

  def test_format_no_data(self):
    expected = []

    self.assert_format(expected, None)

  def test_format_empty_data(self):
    expected = []

    self.assert_format(expected, [])

  def test_format_one_entry(self):
    expected = [self.build_expected_formatted_data('1')]

    entry = self.build_entry('1')

    self.assert_format(expected, [entry])

  def assert_format(self, expected, data):
    result = self.formatter.format(data)

    self.assertEqual(expected, result)

  def build_entry(self, id):
    entry = Entry()
    entry.currency = 'A' + id
    entry.date = 'B' + id
    entry.rate = 1
    entry.deposit = 2
    entry.cost = 'C' + id
    entry.withdrawl = 3
    entry.proceeds = 'D' + id
    entry.average_cost_basis = 'E' + id
    entry.fee = 4
    entry.fee_cost = 'F' + id
    entry.sell_fee = 5
    entry.network_fee = 6
    entry.running_deposits = 'G' + id
    entry.running_total_cost = 'H' + id
    entry.running_average_cost = 'I' + id
    entry.note = 'J' + id

    return entry

  def build_expected_formatted_data(self, id):
    return 'A' + id +',B' + id + ',1,2' + ',C' + id + ',3,D' + id + ',E' + id +',4,F' + id + ',5,6,G' + id +',H' + id +',I' + id +',J' + id
