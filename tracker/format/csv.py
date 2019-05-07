from decimal import Decimal

from date.format import format_datetime
from format.base import BaseFormatter
from model.types import TransactionTypes


class CsvFormatter(BaseFormatter):

    def format(self, data):
        if data is None:
            return []

        data.sort(key=lambda e: (e.currency))
        formatted_data = []

        for datum in data:
            deposit = Decimal(0.0)
            withdrawl = Decimal(0.0)
            proceeds = Decimal(0.0)
            average_cost_basis = Decimal(0.0)
            sell_fee = Decimal(0.0)
            network_fee = Decimal(0.0)
            running_deposits = Decimal(0.0)
            running_total_cost = Decimal(0.0)
            running_average_cost = Decimal(0.0)

            if datum.transaction_type is TransactionTypes.BUY:
                deposit = datum.amount
            elif datum.transaction_type is TransactionTypes.SELL:
                withdrawl = datum.amount
                proceeds = datum.amount * datum.cost

            field_values = [datum.currency, format_datetime(datum.date), datum.rate, deposit, datum.cost,
                            withdrawl, proceeds, average_cost_basis, datum.fee, datum.fee_cost, sell_fee, network_fee,
                            running_deposits, running_total_cost, running_average_cost, datum.note]
            fields_csv = ','.join([str(field_value) for field_value in field_values])
            formatted_data.append(fields_csv)

        return formatted_data
