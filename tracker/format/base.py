from abc import ABCMeta, abstractmethod


class BaseFormatter(metaclass=ABCMeta):

  def __init__(self, name=None):
    if name:
      self.name = name

  @abstractmethod
  def format(self, data):
    pass
