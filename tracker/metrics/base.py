from abc import ABCMeta, abstractmethod
from datetime import datetime


class BaseMetricsClient(metaclass=ABCMeta):

  def __init__(self, name=None):
    if name:
      self.name = name

  @abstractmethod
  def get_historical_price(self, from_symbol: str, to_symbol: str, timestamp: datetime):
    pass
