from date.format import convert_datetime
from model.entry import Entry
from util.amount import format_amount

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
    entry.date = convert_datetime(data.get(self.DATE, '') + '00', self.DATETIME_FORMAT)
    entry.rate = format_amount(data.get(self.EXCHANGE_RATE, 0.0))
    entry.deposit = format_amount(data.get(self.AMOUNT_CREDITED, 0.0))
    entry.cost = format_amount(data.get(self.AMOUNT_DEBITED, 0.0))

    return entry
