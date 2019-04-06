from date.format import convert_datetime
from model.entry import Entry
from util.amount import format_amount

class BinanceConverter:
  DATE = 'Date(UTC)'
  MARKET = 'Market'
  TYPE = 'Type'
  PRICE = 'Price'
  AMOUNT = 'Amount'
  FEE = 'Fee'
  FEE_COIN = 'Fee Coin'

  DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


  def convert(self, data):
    entry = Entry()

    return entry
