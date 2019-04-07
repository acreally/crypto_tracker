import unittest

from converter.binance import BinanceConverter
from model.entry import Entry


class BinanceConverterTest(unittest.TestCase):

  def setUp(self):
    self.converter = BinanceConverter()

  def test_convert_no_data(self):
    expected = Entry()

    self._assert_convert(expected, {})

  def test_convert_buy_with_same_fee_currency(self):
    # Date(UTC),Market,Type,Price,Amount,Total,Fee,Fee Coin
    # 2018-01-20 16:59:59,XLMETH,BUY,0.00012345,123,0.01518435,0.123,XLM
    expected = Entry()
    expected.currency = 'XLM'
    expected.date = '01/20/2018 11:59:59'
    expected.deposit = '123.0'
    expected.fee = '0.123'

    data = {'Date(UTC)': '2018-01-20 16:59:59',
            'Currency': 'XLM',
            'Type': 'BUY',
            'Amount': '123',
            'Fee': '0.123'
            }

    self._assert_convert(expected, data)

  def test_convert_sell_with_same_fee_currency(self):
    # Date(UTC),Market,Type,Price,Amount,Total,Fee,Fee Coin
    # 2018-01-20 16:59:59,XLMETH,BUY,0.00012345,123,0.01518435,0.123,XLM
    expected = Entry()
    expected.currency = 'ETH'
    expected.date = '01/20/2018 11:59:59'
    expected.withdrawl = '0.01518435'

    data = {'Date(UTC)': '2018-01-20 16:59:59',
            'Currency': 'ETH',
            'Type': 'SELL',
            'Amount': '0.01518435',
            'Fee': '0'
            }

    self._assert_convert(expected, data)

  def _assert_convert(self, expected, data):
    result = self.converter.convert(data)

    self.assertEqual(expected, result)
