import os
import unittest

from model.entry import Entry
from strategy.shakepay import ShakepayStrategy

class ShakepayStrategyTest(unittest.TestCase):
  def setUp(self):
    self.strategy = ShakepayStrategy()

  def test_convert_data_empty_file(self):
    expected = []

    self.assert_convert_data(expected, 'empty.csv')

  def test_convert_data_headers_only(self):
    expected = []

    self.assert_convert_data(expected, 'headers_only.csv')

  def test_convert_data(self):
    entry_0 = Entry()
    entry_0.currency = 'BTC'
    entry_0.date = '05/18/2018 09:08:40'
    entry_0.rate = '10343.0693'
    entry_0.deposit = '0.0000001'
    entry_0.cost = '100.0'
    entry_0.withdrawl = ''
    entry_0.proceeds = ''
    entry_0.average_cost_basis = ''
    entry_0.fee = ''
    entry_0.fee_cost = ''
    entry_0.sell_fee = ''
    entry_0.network_fee = ''
    entry_0.running_deposits = ''
    entry_0.running_total_cost = ''
    entry_0.running_average_cost = ''
    entry_0.note = ''

    entry_1 = Entry()
    entry_1.currency = 'ABC'
    entry_1.date = '06/02/2018 00:32:20'
    entry_1.rate = '9663.5397'
    entry_1.deposit = '123.456'
    entry_1.cost = '400.0'
    entry_1.withdrawl = ''
    entry_1.proceeds = ''
    entry_1.average_cost_basis = ''
    entry_1.fee = ''
    entry_1.fee_cost = ''
    entry_1.sell_fee = ''
    entry_1.network_fee = ''
    entry_1.running_deposits = ''
    entry_1.running_total_cost = ''
    entry_1.running_average_cost = ''
    entry_1.note = ''

    entry_2 = Entry()
    entry_2.currency = 'ETH'
    entry_2.date = '07/04/2018 23:25:08'
    entry_2.rate = '8552.2188'
    entry_2.deposit = '0.01987'
    entry_2.cost = '125.0'
    entry_2.withdrawl = ''
    entry_2.proceeds = ''
    entry_2.average_cost_basis = ''
    entry_2.fee = ''
    entry_2.fee_cost = ''
    entry_2.sell_fee = ''
    entry_2.network_fee = ''
    entry_2.running_deposits = ''
    entry_2.running_total_cost = ''
    entry_2.running_average_cost = ''
    entry_2.note = ''

    expected = [entry_0, entry_1, entry_2]

    self.assert_convert_data(expected, 'sample_data.csv')

  def assert_convert_data(self, expected, filename):
    result = self.strategy.convert_data(self.build_filename_with_path(filename))

    self.assertEqual(expected, result)

  def build_filename_with_path(self, filename):
    return os.path.join(os.path.dirname(__file__), 'resources', 'shakepay', filename)
