import unittest

from tracker.date import format

class DateFormatTest(unittest.TestCase):

  def test_convert_datetime(self):
    expected = '05/18/2018 09:08:40'

    given_datetime = '2018-05-18T13:08:40+0000'
    given_format = '%Y-%m-%dT%H:%M:%S%z'
    result = format.convert_datetime(given_datetime, given_format)

    self.assertEqual(expected, result)

  def test_convert_datetime_invalid_datetime(self):
    expected = ''

    given_datetime = '2018-05-18T13:08:40+000'
    given_format = '%Y-%m-%dT%H:%M:%S%z'
    result = format.convert_datetime(given_datetime, given_format)

    self.assertEqual(expected, result)

  def test_convert_datetime_invalid_format(self):
    expected = ''

    given_datetime = '2018-05-18T13:08:40+0000'
    given_format = '%Y-%m-%dT%H:%M:%S%a'
    result = format.convert_datetime(given_datetime, given_format)

    self.assertEqual(expected, result)
