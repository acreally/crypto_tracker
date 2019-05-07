import unittest

from util import amount


class AmountUtilTest(unittest.TestCase):

    def test_format_amount_whole_number_has_one_zero_decimal(self):
        expected = '123.0'

        self._assert_format_amount(expected, '123')

    def test_format_amount_float_with_one_zero_decimal_digit_is_not_changed(self):
        expected = '123.0'

        self._assert_format_amount(expected, '123.0')

    def test_format_amount_float_with_only_trailing_zero_decimal_digits_is_truncated(self):
        expected = '123.0'

        self._assert_format_amount(expected, '123.000000')

    def test_format_amount_float_with_non_zero_decimal_with_no_trailing_zeros_is_not_changed(self):
        expected = '123.456'

        self._assert_format_amount(expected, '123.456')

    def test_format_amount_float_with_non_zero_decimal_with_trailing_zeros_is_truncated(self):
        expected = '123.456'

        self._assert_format_amount(expected, '123.4560000')

    def test_format_amount_zero_in_middle_of_decimal_is_not_truncated(self):
        expected = '123.406'

        self._assert_format_amount(expected, '123.406')

    def test_format_amount_zero_at_start_of_decimal_is_not_truncated(self):
        expected = '123.05678'

        self._assert_format_amount(expected, '123.05678')

    def _assert_format_amount(self, expected, request_value):
        result = amount.format_amount(request_value)

        self.assertEqual(expected, result)
