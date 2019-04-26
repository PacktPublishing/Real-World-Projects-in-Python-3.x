#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7
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

def show_default(symbols):
    symbols.sort()
    return symbols

def add_to_default(symbols):
    print("Enter symbol to add: ")
    symbol = input()
    while symbol != '':
        symbols.append(symbol)
        symbol = input("Enter symbol to add: Hit enter to quit").upper()
    
    return symbols.sort()    

def edit_default(symbols):
    print("Select symbol to delete:")
    for i in range(1,len(symbols) + 1):
        print("{} - {}".format(i, symbols[i-1]))
    remove = symbols.pop(int(input()) - 1)    
    print("{} removed".format(remove))

# final function defined
# add new list --> prompt for symbols until empty string 
def add_list():
    new_list = []
    print("Enter symbol to add: ")
    symbol = input().upper()
    while symbol != '':
        new_list.append(symbol)
        symbol = input("Enter symbol to add, or enter to quit: ")
        symbol = symbol.upper()
    return new_list

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
        
        if choice == 1:
            print("Getting quotes")
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
            edit_default(symbols)
        # final function implemented and quotes fetched
		elif choice == 5:
            new_list = add_list()
            print("Getting quotes")
            while True:
                print(get_prices(new_list))
                print("CNTL + C to quit")
                sleep(5)
        elif choice == 6:
            run_program = False
            


if __name__ == "__main__":
    main()    