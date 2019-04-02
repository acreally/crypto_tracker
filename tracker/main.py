from strategy import factory


def generate_report(filename, exchange):
  conversion_strategy = factory(exchange)
  converted_data = conversion_strategy.convert_data(filename)
  print(convert_data)
