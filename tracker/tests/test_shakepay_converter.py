import unittest

from converter.shakepay import ShakepayConverter
from model.entry import Entry


class ShakepayConverterTest(unittest.TestCase):

  def setUp(self):
    self.converter = ShakepayConverter()

  def test_no_data(self):
    expected = Entry()
    expected.rate = '0.0'
    expected.deposit = '0.0'
    expected.cost = '0.0'

    self._assert_convert(expected, {})

  def test_with_data(self):
    expected = Entry()
    expected.currency = 'BTC'
    expected.date = '05/18/2018 09:08:40'
    expected.rate = '1234.56'
    expected.deposit = '0.123'
    expected.cost = '111.22'

    data = {'Date': '2018-05-18T13:08:40+00',
            'Amount Debited': '111.22',
            'Amount Credited': '0.123',
            'Credit Currency': 'BTC',
            'Exchange Rate': '1234.56'
            }

    self._assert_convert(expected, data)

  def _assert_convert(self, expected, data):
    result = self.converter.convert(data)

    self.assertEqual(expected, result)
