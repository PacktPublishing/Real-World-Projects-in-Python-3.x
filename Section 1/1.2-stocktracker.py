#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 2
Created on Mon Mar 18 14:20:27 2019

@author: mjmacarty
"""
import pandas as pd
import pandas_datareader as pdr

from time import sleep
# get prices from many symbols

symbols = ['AMZN', 'GOOG', 'NFLX', 'FB', 'GLD', 'SPY']


# sort list, get prices
def get_prices(symbols):
	symbols.sort()
    return pdr.get_quote_yahoo(symbols)['price']

# program entry point --> gets prices every 5 seconds until broken	
def main():
    while True:
        
        print(get_prices(symbols))
        print("CNTL + C to quit")
        sleep(5)


		
if __name__ == "__main__":
    main()    