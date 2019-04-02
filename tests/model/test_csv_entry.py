import unittest

from tracker.model.csvEntry import CsvEntry

class CsvEntryTest(unittest.TestCase):

  def test_repr_no_fields_set(self):
    expected = ',,0,0,,0,,,0,,0,0,,,,'

    entry = CsvEntry()

    self.assertEqual(expected, repr(entry))

  def test_repr_all_fields_set(self):
    expected = 'A,B,1,2,C,3,D,E,4,F,5,6,G,H,I,J'

    entry = CsvEntry()
    entry.currency = 'A'
    entry.date = 'B'
    entry.rate = 1
    entry.deposit = 2
    entry.cost = 'C'
    entry.withdrawl = 3
    entry.proceeds = 'D'
    entry.average_cost_basis = 'E'
    entry.fee = 4
    entry.fee_cost = 'F'
    entry.sell_fee = 5
    entry.network_fee = 6
    entry.running_deposits = 'G'
    entry.running_total_cost = 'H'
    entry.running_average_cost = 'I'
    entry.note = 'J'

    self.assertEqual(expected, repr(entry))
