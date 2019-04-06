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

  def _assert_convert_data(self, expected, filename, file_path):
    result = self.strategy.convert_data(helpers.get_absolute_file_path(filename, *file_path))

    self.assertEqual(expected, result)
