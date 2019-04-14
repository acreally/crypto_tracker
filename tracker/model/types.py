from enum import Enum, unique


@unique
class TransactionTypes(Enum):
  BUY = 'BUY'
  SELL = 'SELL'
  UNKNOWN = 'UNKNOWN'
