import csv
import re

from strategy.base import BaseStrategy
from converter.binance import BinanceConverter


BASE_MARKET_CURRENCIES = ['BTC', 'ETH', 'BNB']


class BinanceStrategy(BaseStrategy):
  DATE = 'Date(UTC)'
  MARKET = 'Market'
  TYPE = 'Type'
  PRICE = 'Price'
  AMOUNT = 'Amount'
  TOTAL = 'Total'
  FEE = 'Fee'
  FEE_COIN = 'Fee Coin'

  CURRENCY = 'Currency'

  TRANSACTION_TYPE_BUY = 'BUY'
  TRANSACTION_TYPE_SELL = 'SELL'

  def __init__(self):
    self.converter = BinanceConverter()

  def convert_data(self, filename):
    converted_data = []

    with open(filename) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        transactions = self._split_transaction(row)
        for transaction in transactions:
          converted_data.append(self.converter.convert(transaction))

    return converted_data

  def _split_transaction(self, transaction):
    date = transaction.get(self.DATE)
    market = transaction.get(self.MARKET)
    transaciton_type = transaction.get(self.TYPE)
    price = transaction.get(self.PRICE)
    amount = transaction.get(self.AMOUNT)
    total = transaction.get(self.TOTAL)
    fee = transaction.get(self.FEE)
    fee_currency = transaction.get(self.FEE_COIN)

    pattern = '(.*)({})'.format('|'.join(BASE_MARKET_CURRENCIES))
    currencies = re.findall(pattern, market)

    transactions = []
    if transaciton_type == self.TRANSACTION_TYPE_BUY:
      transactions += self._split_buy_transaction(date, currencies[0][0], amount, fee, fee_currency)
      transactions.append(self._build_sell_transaction(date, currencies[0][1], total))
    else:
      transactions += self._split_buy_transaction(date, currencies[0][1], total, fee, fee_currency)
      transactions.append(self._build_sell_transaction(date, currencies[0][0], amount))

    return transactions

  def _split_buy_transaction(self, date, currency, amount, fee, fee_currency):
    transactions = []

    buy_transaction = {self.DATE: date,
                       self.CURRENCY: currency,
                       self.TYPE: self.TRANSACTION_TYPE_BUY,
                       self.AMOUNT: amount
                       }

    if fee_currency == currency:
      buy_transaction[self.FEE] = fee
    else:
      buy_transaction[self.FEE] = '0'
      transactions.append(self._build_fee_transaction(date, fee, fee_currency))

    transactions.append(buy_transaction)

    return transactions

  def _build_fee_transaction(self, date, fee, fee_currency):
    return {self.DATE: date,
            self.CURRENCY: fee_currency,
            self.TYPE: self.TRANSACTION_TYPE_BUY,
            self.AMOUNT: '0',
            self.FEE: fee
            }

  def _build_sell_transaction(self, date, currency, amount):
    return {self.DATE: date,
            self.CURRENCY: currency,
            self.TYPE: self.TRANSACTION_TYPE_SELL,
            self.AMOUNT: amount,
            self.FEE: '0'
            }
