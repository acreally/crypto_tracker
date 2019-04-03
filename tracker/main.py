from factory import get_instance

from strategy.base import BaseStrategy

def generate_report(filename, exchange):
  strategy_class = exchange.capitalize() + 'Strategy'
  conversion_strategy = get_instance('strategy.' + exchange, strategy_class, BaseStrategy)
  converted_data = conversion_strategy.convert_data(filename)
  print(converted_data)
