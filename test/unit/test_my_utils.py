import sys
sys.path.insert(0, 'src')  #noqa

import unittest
import my_utils
import numpy as np
import random
import os


class TestMyUtils(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.usa_result = [1999, 1999, 1999, 1999, 1999, 1999, 3286, 1553, 3099, 3578, 3687, 534, 1475, 1224, 1201, 915, 1086, 1558, 2068, 1093, 912, 1330, 1173, 1284, 1336, 2235, 1438, 2664, 2457, 1190, 5405]
        print('start')
        print('================')
    
    def test_get_column_success_1(self):
        self.assertEqual(my_utils.get_column('src/Agrofood_co2_emission.csv', 1, 'United States of America', 4), self.usa_result)    

    def test_get_column_success_2(self):
        self.assertEqual(my_utils.get_column('src/Agrofood_co2_emission.csv', 1, 'United States of America'), self.usa_result)    

    def test_get_column_no_such_file_failure(self):
        self.assertEqual(my_utils.get_column('src/Agrofood_co2_emissions.csv', 1, 'United States of America', 4), [])
           
    def test_get_column_index_failure_1(self):
        self.assertEqual(my_utils.get_column('src/Agrofood_co2_emission.csv', 1, 'United States of America', 400), [])
        
    def test_get_column_index_failure_2(self):
        self.assertEqual(my_utils.get_column('src/Agrofood_co2_emission.csv', 400, 'United States of America', 4), [])

    def test_get_column_can_not_convert_to_int_failure(self):
        self.assertEqual(my_utils.get_column('src/Agrofood_co2_emission.csv', 1, 'United States of America', 1), [])
        
    def test_mean(self):
        self.assertEqual(my_utils.mean(self.usa_result), np.mean(self.usa_result))
    
    def test_median(self):
        self.assertEqual(my_utils.median(self.usa_result), np.median(self.usa_result))
        
    def test_standard_deviation(self):
        self.assertEqual(my_utils.standard_deviation(self.usa_result),np.std(self.usa_result))
    
    
if __name__ == '__main__':
    unittest.main()