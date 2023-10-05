import sys
sys.path.insert(0, 'src')  #noqa

import unittest
import my_utils
import numpy as np
import random
import os


class TestMyUtils(unittest.TestCase):
       
    def setUp(self):
        print()
        print()
        self.country = random.choice(['Australia', 'Brazil', 'China', 'Greece', 'Japan', 'United States of America'])
        self.forest_fires_results = my_utils.get_column('src/Agrofood_co2_emission.csv', 1, self.country, 4)
        self.mean_result = np.mean(self.forest_fires_results)
        self.median_result = np.median(self.forest_fires_results)
        self.sd_result = np.std(self.forest_fires_results)
        
        print(self.country)
        #print('=======================')
        #print()
    
    def test_get_column_success(self):
        print('test_get_column_success')
        print()
        self.assertEqual(my_utils.get_column('src/Agrofood_co2_emission.csv', 1, self.country, 4), self.forest_fires_results)    
        self.assertEqual(my_utils.get_column('src/Agrofood_co2_emission.csv', 1, self.country), self.forest_fires_results)    

    def test_get_column_no_such_file_failure(self):
        print('test_get_column_no_such_file_failure')
        print()
        self.assertEqual(my_utils.get_column('src/Agrofood_co2_emissions.csv', 1, self.country, 4), [])
           
    def test_get_column_index_failure(self):
        print('test_get_column_index_failure')
        print()
        self.assertEqual(my_utils.get_column('src/Agrofood_co2_emission.csv', 1, self.country, 400), [])
        self.assertEqual(my_utils.get_column('src/Agrofood_co2_emission.csv', 400, self.country, 4), [])

    def test_get_column_can_not_convert_to_int_failure(self):
        print('test_get_column_can_not_convert_to_int_failure')
        print()
        self.assertEqual(my_utils.get_column('src/Agrofood_co2_emission.csv', 1, self.country, 1), [])
        
    def test_mean(self):
        print('test_mean')
        print()
        self.assertEqual(my_utils.mean(self.forest_fires_results), self.mean_result)
    
    def test_median(self):
        print('test_median')
        print()
        self.assertEqual(my_utils.median(self.forest_fires_results), self.median_result)
        
    def test_standard_deviation(self):
        print('test_standard_deviation')
        print()
        self.assertEqual(my_utils.standard_deviation(self.forest_fires_results),self.sd_result)
    
    
if __name__ == '__main__':
    unittest.main()