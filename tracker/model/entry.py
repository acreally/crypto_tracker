from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from date.format import convert_datetime_to_local_timezone


@dataclass
class Entry:
    date: datetime = None
    credit_currency: str = ''
    debit_currency: str = ''
    price: Decimal = Decimal(0.0)
    credit_amount: Decimal = Decimal(0.0)
    debit_amount: Decimal = Decimal(0.0)
    fee: Decimal = Decimal(0.0)
    note: str = ''

    def set_date(self, date_value: str, datetime_format: str) -> None:
        self.date = convert_datetime_to_local_timezone(
            date_value, datetime_format)

    def set_price(self, new_price: str) -> None:
        self.price = Decimal(new_price)

    def set_credit_amount(self, new_credit_amount: str) -> None:
        self.credit_amount = Decimal(new_credit_amount)

    def set_debit_amount(self, new_debit_amount: str) -> None:
        self.debit_amount = Decimal(new_debit_amount)

    def set_fee(self, new_fee: str) -> None:
        self.fee = Decimal(new_fee)
