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
        expected = []

        self._assert_convert(expected, {})

    def test_convert_buy_with_same_fee_currency(self):
        # Date(UTC),Market,Type,Price,Amount,Total,Fee,Fee Coin
        # 2018-01-20 16:59:59,XLMETH,BUY,0.00012345,123,0.01518435,0.123,XLM
        expected_entry = Entry()
        expected_entry.date = datetime.fromtimestamp(1516467599, timezone('US/Eastern'))
        expected_entry.credit_currency = 'XLM'
        expected_entry.debit_currency = 'ETH'
        expected_entry.price = Decimal('0.00012345')
        expected_entry.credit_amount = Decimal('123')
        expected_entry.debit_amount = Decimal('0.01518435')
        expected_entry.fee = Decimal('0.123')

        expected = [expected_entry]

        data = {'Date(UTC)': '2018-01-20 16:59:59',
                'Market': 'XLMETH',
                'Type': 'BUY',
                'Price': '0.00012345',
                'Amount': '123',
                'Total': '0.01518435',
                'Fee': '0.123',
                'Fee Coin': 'XLM'
                }

        self._assert_convert(expected, data)

    def test_convert_buy_with_different_fee_currency(self):
        # Date(UTC),Market,Type,Price,Amount,Total,Fee,Fee Coin
        # 2018-01-20 16:59:59,XLMETH,BUY,0.00012345,123,0.01518435,0.00045678,BNB
        expected_trade_entry = Entry()
        expected_trade_entry.date = datetime.fromtimestamp(1516467599, timezone('US/Eastern'))
        expected_trade_entry.credit_currency = 'XLM'
        expected_trade_entry.debit_currency = 'ETH'
        expected_trade_entry.price = Decimal('0.00012345')
        expected_trade_entry.credit_amount = Decimal('123')
        expected_trade_entry.debit_amount = Decimal('0.01518435')

        expected_fee_entry = Entry()
        expected_fee_entry.date = datetime.fromtimestamp(1516467599, timezone('US/Eastern'))
        expected_fee_entry.debit_currency = 'BNB'
        expected_fee_entry.fee = Decimal('0.00045678')

        expected = [expected_trade_entry, expected_fee_entry]

        data = {'Date(UTC)': '2018-01-20 16:59:59',
                'Market': 'XLMETH',
                'Type': 'BUY',
                'Price': '0.00012345',
                'Amount': '123',
                'Total': '0.01518435',
                'Fee': '0.00045678',
                'Fee Coin': 'BNB'
                }

        self._assert_convert(expected, data)

    def test_convert_sell_with_same_fee_currency(self):
        # Date(UTC),Market,Type,Price,Amount,Total,Fee,Fee Coin
        # 2018-01-20 16:59:59,XLMETH,SELL,8100.445524503847711624,123,0.01518435,0.00001518435,ETH
        expected_entry = Entry()
        expected_entry.date = datetime.fromtimestamp(1516467599, timezone('US/Eastern'))
        expected_entry.credit_currency = 'ETH'
        expected_entry.debit_currency = 'XLM'
        expected_entry.price = Decimal('8100.445524503847711624')
        expected_entry.credit_amount = Decimal('0.01518435')
        expected_entry.debit_amount = Decimal('123')
        expected_entry.fee = Decimal('0.00001518435')

        expected = [expected_entry]

        data = {'Date(UTC)': '2018-01-20 16:59:59',
                'Market': 'XLMETH',
                'Type': 'SELL',
                'Price': '8100.445524503847711624',
                'Amount': '123',
                'Total': '0.01518435',
                'Fee': '0.00001518435',
                'Fee Coin': 'ETH'
                }

        self._assert_convert(expected, data)

    def test_convert_sell_with_different_fee_currency(self):
        # Date(UTC),Market,Type,Price,Amount,Total,Fee,Fee Coin
        # 2018-01-20 16:59:59,XLMETH,SELL,8100.445524503847711624,123,0.01518435,0.00045678,BNB
        expected_trade_entry = Entry()
        expected_trade_entry.date = datetime.fromtimestamp(1516467599, timezone('US/Eastern'))
        expected_trade_entry.credit_currency = 'ETH'
        expected_trade_entry.debit_currency = 'XLM'
        expected_trade_entry.price = Decimal('8100.445524503847711624')
        expected_trade_entry.credit_amount = Decimal('0.01518435')
        expected_trade_entry.debit_amount = Decimal('123')

        expected_fee_entry = Entry()
        expected_fee_entry.date = datetime.fromtimestamp(1516467599, timezone('US/Eastern'))
        expected_fee_entry.debit_currency = 'BNB'
        expected_fee_entry.fee = Decimal('0.00045678')

        expected = [expected_trade_entry, expected_fee_entry]

        data = {'Date(UTC)': '2018-01-20 16:59:59',
                'Market': 'XLMETH',
                'Type': 'SELL',
                'Price': '8100.445524503847711624',
                'Amount': '123',
                'Total': '0.01518435',
                'Fee': '0.00045678',
                'Fee Coin': 'BNB'
                }

        self._assert_convert(expected, data)

    def _assert_convert(self, expected, data):
        result = self.converter.convert(data)

        self.assertEqual(expected, result)
