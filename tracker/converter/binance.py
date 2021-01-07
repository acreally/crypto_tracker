import re

from model.entry import Entry


class BinanceConverter:
    DATE = 'Date(UTC)'
    MARKET = 'Market'
    TYPE = 'Type'
    PRICE = 'Price'
    AMOUNT = 'Amount'
    TOTAL = 'Total'
    FEE = 'Fee'
    FEE_COIN = 'Fee Coin'

    TRANSACTION_TYPE_BUY = 'BUY'
    TRANSACTION_TYPE_SELL = 'SELL'

    BASE_MARKET_CURRENCIES = ['BTC', 'ETH', 'BNB']

    DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S%z'

    '''
  Each entry will be 2 or 3 transactions:
  1) buy transaction for one crypto asset
  2) sell transaction for one crypto asset
  3) optional, fees paid in a separate crypto asset
  Fees made be paid in the currency of the acquiring asset
  Markets are either BTC, ETH, or BNB based
  2 transactions example entry:
  2018-01-20 16:59:59,XLMETH,BUY,0.00012345,123,0.01518435,0.123,XLM
  3 transactions example entry
  2018-11-01 23:23:23,LTCBTC,SELL,0.015151,0.75,0.01136325,0.00151515,BNB
  '''

    def convert(self, data):
        if data is None or type(data) != dict or len(data) == 0:
            return []

        entry = Entry()
        entries = [entry]

        transaction_date = data.get(self.DATE, '') + '+0000'

        credit_currency, debit_currency = self._split_currencies(data.get(self.MARKET), data.get(self.TYPE))
        credit_amount, debit_amount = self._split_amounts(data.get(self.AMOUNT, '0.0'), data.get(self.TOTAL, '0.0'), data.get(self.TYPE))

        fee_currency = data.get(self.FEE_COIN)
        fee = data.get(self.FEE, '0.0')

        entry.set_date(transaction_date, self.DATETIME_FORMAT)
        entry.credit_currency = credit_currency
        entry.debit_currency = debit_currency
        entry.set_price(data.get(self.PRICE))
        entry.set_credit_amount(credit_amount)
        entry.set_debit_amount(debit_amount)

        if fee_currency == credit_currency:
            entry.set_fee(fee)
        else:
            entries.append(self._build_fee_entry(transaction_date, fee_currency, fee))

        return entries

    def _split_currencies(self, market, type):
        pattern = '(.*)({})'.format('|'.join(self.BASE_MARKET_CURRENCIES))
        currencies = re.findall(pattern, market)[0]

        if type == self.TRANSACTION_TYPE_BUY:
            return currencies[0], currencies[1]
        elif type == self.TRANSACTION_TYPE_SELL:
            return currencies[1], currencies[0]

    def _split_amounts(self, amount, total, type):
        if type == self.TRANSACTION_TYPE_BUY:
            return amount, total
        elif type == self.TRANSACTION_TYPE_SELL:
            return total, amount

    def _build_fee_entry(self, transaction_date, fee_coin, fee):
        entry = Entry()

        entry.set_date(transaction_date, self.DATETIME_FORMAT)
        entry.debit_currency = fee_coin
        entry.set_fee(fee)

        return entry
