from decimal import Decimal


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
    entry.set_date(data.get(self.DATE, '') + '00', self.DATETIME_FORMAT)
    entry.set_rate(data.get(self.EXCHANGE_RATE, '0.0'))
    entry.set_deposit(data.get(self.AMOUNT_CREDITED, '0.0'))
    entry.set_cost(data.get(self.AMOUNT_DEBITED, '0.0'))

    return entry
