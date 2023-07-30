# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 19:34:25 2023

@author: yswav
"""

from database import data_dloader as dd
import pandas as pd

print(dd.stocks_ticker())
df = dd.download(stock='HINDALCO')
df.head()
df.info()
