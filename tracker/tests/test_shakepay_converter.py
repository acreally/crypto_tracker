import unittest

from datetime import datetime
from decimal import Decimal
from pytz import timezone

from converter.shakepay import ShakepayConverter
from model.entry import Entry


class ShakepayConverterTest(unittest.TestCase):

  def setUp(self):
    self.converter = ShakepayConverter()

  def test_no_data(self):
    expected = Entry()

    self._assert_convert(expected, {})

  def test_with_data(self):
    expected = Entry()
    expected.currency = 'BTC'
    expected.date = datetime.fromtimestamp(1526648920, timezone('US/Eastern'))
    expected.rate = Decimal('1234.56')
    expected.deposit = Decimal('0.123')
    expected.cost = Decimal('111.22')

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
