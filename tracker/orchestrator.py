from factory import get_instance

from format.base import BaseFormatter
from strategy.base import BaseStrategy

def generate_report(filename, exchange, output_format):
  converted_data = convert_data(filename, exchange)
  formatted_data = format_data(converted_data, output_format)
  return formatted_data

def convert_data(filename, exchange):
  strategy_class = exchange.capitalize() + 'Strategy'
  conversion_strategy = get_instance('strategy.' + exchange, strategy_class, BaseStrategy)
  return conversion_strategy.convert_data(filename)

def format_data(converted_data, output_format):
  formatter_class = output_format.capitalize() + 'Formatter'
  data_formatter = get_instance('format.' + output_format, formatter_class, BaseFormatter)
  return data_formatter.format(converted_data)
