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
    entry = Entry()

    return entry
