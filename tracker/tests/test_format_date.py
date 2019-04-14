import unittest

from datetime import datetime
from pytz import timezone

from date import format


class DateFormatTest(unittest.TestCase):

  def test_format_datetime(self):
    expected = '05/18/2018 05:08:40'

    given_datetime = datetime.fromtimestamp(1526634520)
    result = format.format_datetime(given_datetime)

    self.assertEqual(expected, result)

  def test_convert_datetime_to_local_timezone(self):
    expected = datetime.fromtimestamp(1526648920, timezone('US/Eastern'))

    given_datetime = '2018-05-18T13:08:40+0000'
    given_format = '%Y-%m-%dT%H:%M:%S%z'
    result = format.convert_datetime_to_local_timezone(given_datetime, given_format)

    self.assertEqual(expected, result)

  def test_convert_datetime_to_local_timezone_invalid_datetime(self):
    expected = None

    given_datetime = '2018-05-18T13:08:40+000'
    given_format = '%Y-%m-%dT%H:%M:%S%z'
    result = format.convert_datetime_to_local_timezone(given_datetime, given_format)

    self.assertEqual(expected, result)

  def test_convert_datetime_invalid_format(self):
    expected = None

    given_datetime = '2018-05-18T13:08:40+0000'
    given_format = '%Y-%m-%dT%H:%M:%S%a'
    result = format.convert_datetime_to_local_timezone(given_datetime, given_format)

    self.assertEqual(expected, result)
