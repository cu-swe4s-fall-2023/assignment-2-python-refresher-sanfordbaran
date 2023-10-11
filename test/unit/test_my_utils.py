import sys
import unittest
import numpy as np
import random
import os

sys.path.insert(0, '../../src')  #noqa
import my_utils


class TestMyUtils(unittest.TestCase):

    def setUp(self):
        print()
        print()
        self.country = random.choice(['Australia', 'Brazil', 'China',
                                      'Greece', 'Japan',
                                      'United States of America'])
        self.filename = '../data/Agrofood_co2_emission_ft.csv'
        self.ff_results = my_utils.get_column(self.filename, 1,
                                              self.country, 4)
        self.bad_filename = '../../src/Agrofood_co2_emissions.csv'

        self.mean_result = np.mean(self.ff_results)
        self.median_result = np.median(self.ff_results)
        self.sd_result = np.std(self.ff_results)

        print(self.country)

    def test_get_column_success(self):
        print('test_get_column_success')
        print()
        self.assertEqual(my_utils.get_column(self.filename, 1,
                                             self.country, 4),
                         self.ff_results)
        self.assertEqual(my_utils.get_column(self.filename, 1, self.country),
                         self.ff_results)

    def test_get_column_no_such_file_failure(self):
        print('test_get_column_no_such_file_failure')
        print()
        self.assertEqual(my_utils.get_column(self.bad_filename, 1,
                                             self.country, 4),
                         [])

    def test_get_column_index_failure(self):
        print('test_get_column_index_failure')
        print()
        self.assertEqual(my_utils.get_column(self.filename, 1,
                                             self.country, 400),
                         [])
        self.assertEqual(my_utils.get_column(self.filename, 400,
                                             self.country, 4),
                         [])

    def test_get_column_can_not_convert_to_int_failure(self):
        print('test_get_column_can_not_convert_to_int_failure')
        print()
        self.assertEqual(my_utils.get_column(self.filename, 1,
                                             self.country, 1),
                         [])

    def test_mean(self):
        print('test_mean')
        print()
        self.assertEqual(my_utils.mean(self.ff_results),
                         self.mean_result)

    def test_median(self):
        print('test_median')
        print()
        self.assertEqual(my_utils.median(self.ff_results),
                         self.median_result)

    def test_standard_deviation(self):
        print('test_standard_deviation')
        print()
        self.assertEqual(my_utils.standard_deviation(self.ff_results),
                         self.sd_result)


if __name__ == '__main__':
    unittest.main()
