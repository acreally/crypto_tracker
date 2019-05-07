from abc import ABCMeta, abstractmethod


class BaseStrategy(metaclass=ABCMeta):

    def __init__(self, name=None):
        if name:
            self.name = name

    @abstractmethod
    def convert_data(self, filename):
        pass
