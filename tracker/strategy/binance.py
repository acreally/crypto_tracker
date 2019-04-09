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
        converted_data.append(self.converter.convert(row))

    return converted_data

  def _split_transaction(self, transaction):
    transactions = []
    market = transaction.get(self.MARKET)

    pattern = '(.*)({})'.format('|'.join(BASE_MARKET_CURRENCIES))
    currencies = re.findall(pattern, market)

    transaciton_type = transaction.get(self.TYPE)

    if transaciton_type == self.TRANSACTION_TYPE_BUY:
      transactions += self._split_buy_transaction(transaction, currencies[0][0], transaction.get(self.AMOUNT))

    return transactions

  def _split_buy_transaction(self, transaction, currency, amount):
    date = transaction.get(self.DATE)
    fee = transaction.get(self.FEE)
    fee_currency = transaction.get(self.FEE_COIN)
    transactions = []

    buy_transaction = {self.DATE: date,
                       self.CURRENCY: currency,
                       self.TYPE: self.TRANSACTION_TYPE_BUY,
                       self.AMOUNT: amount
                       }

    if transaction.get(self.FEE_COIN) == currency:
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
