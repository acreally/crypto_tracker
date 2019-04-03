import unittest

from converter.shakepay import ShakepayConverter

class ShakepayConverterTest(unittest.TestCase):
  def setUp(self):
    self.converter = ShakepayConverter()

  def test_no_data(self):
    data = {}
    result = self.converter.convert(data)

    self.assertEqual('', result.currency)
    self.assertEqual('', result.date)
    self.assertEqual(0, result.rate)
    self.assertEqual(0, result.deposit)
    self.assertEqual('', result.cost)

  def test_with_data(self):
    data = {'Date': '2018-05-18T13:08:40+0000',
            'Amount Debited': '111.22',
            'Amount Credited': '0.123',
            'Credit Currency': 'BTC',
            'Exchange Rate': '1234.56'
           }
    result = self.converter.convert(data)

    self.assertEqual('BTC', result.currency)
    self.assertEqual('05/18/2018 09:08:40', result.date)
    self.assertEqual(1234.56, result.rate)
    self.assertEqual(0.123, result.deposit)
    self.assertEqual('111.22', result.cost)
