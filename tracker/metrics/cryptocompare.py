import requests

from datetime import datetime
from decimal import Decimal

from metrics.base import BaseMetricsClient

URL = 'https://min-api.cryptocompare.com/data/dayAvg'

class CryptoCompareClient(BaseMetricsClient):

  def get_historical_price(self, from_symbol: str, to_symbol: str, timestamp: datetime) -> Decimal:
    params = {'fsym': from_symbol,
              'tsym': to_symbol,
              'toTs': str(int(timestamp.timestamp()))
              }
    response = requests.get(URL, params=params)

    if response.status_code == 200:
      return Decimal(response.json().get(to_symbol))
