import strategy


def generate_report(filename, exchange):
  conversion_strategy = strategy.factory(filename)
  converted_data = conversion_strategy.convert_data(filename)
  print(convert_data)
