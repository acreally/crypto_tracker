import csv

from ..converter.shakepay import ShakepayConverter

class ShakepayStrategy:

  def __init__(self):
    self.converter = ShakepayConverter()

  def convert_data(self, filename):
    converted_data = []

    with open(filename) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          converted_data.append(self.converter.convert(row))

    return converted_data
