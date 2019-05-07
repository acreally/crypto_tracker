import re

from decimal import Decimal


def format_amount(value):
    formatted_decimal_number = '{:.20f}'.format(Decimal(value))

    if formatted_decimal_number == '0.00000000000000000000':
        return '0.0'

    matcher = re.search(r'([0-9]+\.([0-9]*[1-9]+|0))(0*)', formatted_decimal_number)

    return matcher.group(1)
