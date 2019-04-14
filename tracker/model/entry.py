from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from date.format import convert_datetime_to_local_timezone
from model.types import TransactionTypes


@dataclass
class Entry:
  currency: str = ''
  transaction_type: TransactionTypes = TransactionTypes.UNKNOWN
  date: datetime = None
  rate: Decimal = Decimal(0.0)
  amount: Decimal = Decimal(0.0)
  cost: Decimal = Decimal(0.0)
  fee: Decimal = Decimal(0.0)
  fee_cost: Decimal = Decimal(0.0)
  note: str = ''

  def set_date(self, date_value: str, datetime_format: str) -> None:
    self.date = convert_datetime_to_local_timezone(date_value, datetime_format)

  def set_rate(self, new_rate: str) -> None:
    self.rate = Decimal(new_rate)

  def set_amount(self, new_amount: str) -> None:
    self.amount = Decimal(new_amount)

  def set_cost(self, new_cost: str) -> None:
    self.cost = Decimal(new_cost)

  def set_withdrawl(self, new_withdrawl: str) -> None:
    self.withdrawl = Decimal(new_withdrawl)

  def set_fee(self, new_fee: str) -> None:
    self.fee = Decimal(new_fee)
