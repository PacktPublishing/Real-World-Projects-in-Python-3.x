#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6
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
        symbol = input("Enter symbol to add: Hit enter to quit")
    #symbols.sort()
    return symbols.sort()    

# function code added
# read each symbol and output in numbered list indexed from 1
# take user input to delete a number from list 	
def edit_default(symbols):
    print("Select symbol to delete:")
    for i in range(1,len(symbols) + 1):
        print("{} - {}".format(i, symbols[i-1]))
    remove = symbols.pop(int(input()) - 1)    
    print("{} removed".format(remove))

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
        # contine to implement defined functions 
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
			# new addition
            edit_default(symbols)
        elif choice == 5:
            add_list()
        elif choice == 6:
            run_program = False
            


if __name__ == "__main__":
    main()    