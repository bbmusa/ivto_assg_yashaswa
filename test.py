# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 19:57:18 2023

@author: yswav
"""
import unittest
import pandas as pd
from database import data_dloader as dd
import pandas as pd

df = dd.download(stock='HINDALCO')

class TestDataFrames(unittest.TestCase):
    def test_valid_decimal_values(self):
        # Check if Open, High, Low, and Close columns in df are decimal values
        for col in ['open', 'high', 'low', 'close']:
            self.assertTrue(df[col].dtype == 'float64', f"Invalid data type for column {col}")

    def test_valid_integer_volume(self):
        # Check if Volume column in df is an integer
        self.assertTrue(df['volume'].dtype == 'int64', "Invalid data type for column Volume")

    def test_valid_datetime(self):
        # Check if datetime column in df is datetime type
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(df['datetime']),
                        "Invalid data type for column datetime")

if __name__ == '__main__':
    unittest.main()
