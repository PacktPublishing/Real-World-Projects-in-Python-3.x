#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 1
Created on Mon Mar 18 12:17:42 2019

@author: mjmacarty
"""

# open a command line window (terminal) and enter the following:
# pip install pandas-datareader

import pandas as pd
import pandas_datareader as pdr

# read data from one of the APIs

# i.e. pdr.get_data_yahoo('SPY') --> returns dataframe of historical quotes for symbol SPY

pdr.get_data_yahoo("SPY")

# many data sources and variations on data sets, we are interested in a current price:
# get_quote downloads "live" data from the API
print(pdr.get_quote_yahoo('AAPL'))
print(pdr.get_quote_yahoo('AAPL')['price'])



     