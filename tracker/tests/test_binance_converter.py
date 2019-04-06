import unittest

from converter.binance import BinanceConverter
from model.entry import Entry

class BinanceConverterTest(unittest.TestCase):
  def setUp(self):
    self.converter = BinanceConverter()

  def test_no_data(self):
    expected = Entry()

    self._assert_convert(expected, {})

  def _assert_convert(self, expected, data):
    result = self.converter.convert(data)

    self.assertEqual(expected, result)
