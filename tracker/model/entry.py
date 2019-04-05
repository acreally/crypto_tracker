from dataclasses import dataclass


@dataclass
class Entry:
  currency: str = ''
  date: str = ''
  rate: str = ''
  deposit: str = ''
  cost: str = ''
  withdrawl: str = ''
  proceeds: str = ''
  average_cost_basis: str = ''
  fee: str = ''
  fee_cost: str = ''
  sell_fee: str = ''
  network_fee: str = ''
  running_deposits: str = ''
  running_total_cost: str = ''
  running_average_cost: str = ''
  note: str = ''
