import csv

from converter.binance import BinanceConverter
from strategy.base import BaseStrategy


class BinanceStrategy(BaseStrategy):

    def __init__(self):
        self.converter = BinanceConverter()

    def convert_data(self, filename):
        converted_data = []

        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                converted_data.extend(self.converter.convert(row))

        return converted_data
