import re

from decimal import Decimal

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
    entry.date = convert_datetime(data.get(self.DATE, '') + '00', self.DATETIME_FORMAT)
    entry.rate = self._format_amount(data, self.EXCHANGE_RATE)
    entry.deposit = self._format_amount(data, self.AMOUNT_CREDITED)
    entry.cost = self._format_amount(data, self.AMOUNT_DEBITED)

    return entry

  def _format_amount(self, data, field):
    formatted_decimal_number = '{:.20f}'.format(Decimal(data.get(field, 0.0)))

    if formatted_decimal_number == '0.00000000000000000000':
      return '0.0'

    matcher = re.search(r'([0-9]+\.([0-9]*[1-9]+|0))(0*)', formatted_decimal_number)

    return matcher.group(1)