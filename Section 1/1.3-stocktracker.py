#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3
Created on Mon Mar 18 14:20:27 2019

@author: mjmacarty
"""
import pandas as pd
import pandas_datareader as pdr

from time import sleep

# get prices from default list
symbols = ['AMZN', 'GOOG', 'NFLX', 'FB', 'GLD', 'SPY']

# create list to store menu options for app
options = " Track Default List, Show Default List, \
Add to Default, Edit Default List, Add New List, Quit".split(",")


# placeholder functions for most menu options`
def show_default():
    pass

def add_to_default():
    pass

def edit_default():
    pass

def add_list():
    pass

def get_prices(symbols):
    symbols.sort()
    return pdr.get_quote_yahoo(symbols)['price']
# replace True with variable to be used later and display menu  
def main():
    run_program = True
    while run_program:
        print("Choose option:")
        for i in range(1, len(options)+1):
            print("{:} - {}".format(i,options[i-1]))
        
        print(get_prices(symbols))
        print("CNTL + C to quit")
        sleep(5)


if __name__ == "__main__":
    main()    