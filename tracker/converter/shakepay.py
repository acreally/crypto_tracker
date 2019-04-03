from date.format import convert_datetime
from model.entry import Entry

class ShakepayConverter:
  DATE = 'Date'
  AMOUNT_DEBITED = 'Amount Debited'
  AMOUNT_CREDITED = 'Amount Credited'
  CREDIT_CURRENCY = 'Credit Currency'
  EXCHANGE_RATE = 'Exchange Rate'

  DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S%z'


  def convert(self, data):
    entry = Entry()

    entry.currency = data.get(self.CREDIT_CURRENCY, '')
    entry.date = convert_datetime(data.get(self.DATE, ''), self.DATETIME_FORMAT)
    entry.rate = float(data.get(self.EXCHANGE_RATE, 0.0))
    entry.deposit = float(data.get(self.AMOUNT_CREDITED, 0.0))
    entry.cost = data.get(self.AMOUNT_DEBITED, '')

    return entry