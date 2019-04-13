from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from date.format import convert_datetime_to_local_timezone


@dataclass
class Entry:
  currency: str = ''
  date: datetime = None
  rate: Decimal = Decimal(0.0)
  deposit: Decimal = Decimal(0.0)
  cost: Decimal = Decimal(0.0)
  withdrawl: Decimal = Decimal(0.0)
  proceeds: Decimal = Decimal(0.0)
  average_cost_basis: Decimal = Decimal(0.0)
  fee: Decimal = Decimal(0.0)
  fee_cost: Decimal = Decimal(0.0)
  sell_fee: Decimal = Decimal(0.0)
  network_fee: Decimal = Decimal(0.0)
  running_deposits: Decimal = Decimal(0.0)
  running_total_cost: Decimal = Decimal(0.0)
  running_average_cost: Decimal = Decimal(0.0)
  note: str = ''

  def set_date(self, date_value: str, datetime_format: str) -> None:
    self.date = convert_datetime_to_local_timezone(date_value, datetime_format)

  def set_rate(self, new_rate: str) -> None:
    self.rate = Decimal(new_rate)

  def set_deposit(self, new_deposit: str) -> None:
    self.deposit = Decimal(new_deposit)

  def set_cost(self, new_cost: str) -> None:
    self.cost = Decimal(new_cost)
