from format.base import BaseFormatter


class CsvFormatter(BaseFormatter):

  def format(self, data):
    if data is None:
      return []

    formated_data = []

    for datum in data:
      field_values = [datum.currency, datum.date, datum.rate, datum.deposit, datum.cost, datum.withdrawl, datum.proceeds, datum.average_cost_basis, datum.fee, datum.fee_cost, datum.sell_fee, datum.network_fee, datum.running_deposits, datum.running_total_cost, datum.running_average_cost, datum.note]
      fields_csv = ','.join([str(field_value) for field_value in field_values])
      formated_data.append(fields_csv)

    return formated_data