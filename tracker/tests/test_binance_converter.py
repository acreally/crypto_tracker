import unittest

from datetime import datetime
from decimal import Decimal
from pytz import timezone

from converter.binance import BinanceConverter
from model.entry import Entry
from model.types import TransactionTypes


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
    expected.date = datetime.fromtimestamp(1516467599, timezone('US/Eastern'))
    expected.transaction_type = TransactionTypes.BUY
    expected.amount = Decimal('123.0')
    expected.fee = Decimal('0.123')

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
    expected.date = datetime.fromtimestamp(1516467599, timezone('US/Eastern'))
    expected.transaction_type = TransactionTypes.SELL
    expected.amount = Decimal('0.01518435')

    data = {'Date(UTC)': '2018-01-20 16:59:59',
            'Currency': 'ETH',
            'Type': 'SELL',
            'Amount': '0.01518435',
            'Fee': '0'
            }

    self._assert_convert(expected, data)

  def test_convert_fee_only(self):
    expected = Entry()
    expected.currency = 'BNB'
    expected.date = datetime.fromtimestamp(1529081999, timezone('US/Eastern'))
    expected.transaction_type = TransactionTypes.BUY
    expected.amount = Decimal('0.0')
    expected.fee = Decimal('1.234')

    data = {'Date(UTC)': '2018-06-15 16:59:59',
            'Currency': 'BNB',
            'Type': 'BUY',
            'Amount': '0',
            'Fee': '1.234'
            }

    self._assert_convert(expected, data)

  def _assert_convert(self, expected, data):
    result = self.converter.convert(data)

    self.assertEqual(expected, result)
