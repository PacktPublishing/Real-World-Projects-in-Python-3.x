#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
5
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

# define functions to show current list and add symbols to default
def show_default(symbols):
    symbols.sort()
    return symbols

# this will only be valid until program is reloaded	
# to make changes permanent would be an improvement --> requires data to be read
# from database (this can be a simple text file
# function prompts for new symbol until an empty string is input
def add_to_default(symbols):
    print("Enter symbol to add: ")
    symbol = input()
    while symbol != '':
        symbols.append(symbol)
        symbol = input("Enter symbol to add: Hit enter to quit")
    #symbols.sort()
    return symbols.sort()    

def edit_default():
    pass

def add_list():
    pass


def get_prices(symbols):
    symbols.sort()
    return pdr.get_quote_yahoo(symbols)['price']

def main():
   
    run_program = True
    while run_program:
        print("Choose option:")
        for i in range(1, len(options)+1):
            print("{:} - {}".format(i,options[i-1]))
        choice = int(input())    
        # implement functions here, passing in variables as needed
	
        if choice == 1:
            while True:
                print(get_prices(symbols))
                print("CNTL + C to quit")
                sleep(5)
        elif choice == 2:
            print("Current default list:")
            print(show_default(symbols))
            print()
        elif choice == 3:
            add_to_default(symbols)
        elif choice == 4:
            edit_default()
        elif choice == 5:
            add_list()
        elif choice == 6:
            run_program = False
            


if __name__ == "__main__":
    main()    