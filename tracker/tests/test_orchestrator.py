import os
import unittest

import orchestrator


EXCHANGE_SHAKEPAY = 'shakepay'
OUTPUT_CSV = 'csv'

class OrchestratorTest(unittest.TestCase):

  def setUp(self):
    self.shakepay_file = os.path.join(os.path.dirname(__file__), 'resources', 'shakepay', 'sample_data.csv')

  def test_generate_shakepay_report_with_csv_output(self):
    expected_line_0 = 'BTC,05/18/2018 09:08:40,10343.0693,0.0000001,100.0,,,,,,,,,,,'
    expected_line_1 = 'ABC,06/02/2018 00:32:20,9663.5397,123.456,400.0,,,,,,,,,,,'
    expected_line_2 = 'ETH,07/04/2018 23:25:08,8552.2188,0.01987,125.0,,,,,,,,,,,'
    expected = [expected_line_0, expected_line_1, expected_line_2]

    result = orchestrator.generate_report(self.shakepay_file, EXCHANGE_SHAKEPAY, OUTPUT_CSV)

    self.assertEqual(expected, result)
