# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:02:37 2019

@author: Matt Macarty
"""

from tkinter import *
import numpy as np

class LoanCalculator:

    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        
        Label(window, text="Loan Amount").grid(row=1, column=1, sticky=W)
        Label(window, text="Interest rate").grid(row=2, column=1, sticky=W)
        Label(window, text="Term (years)").grid(row=3, column=1, sticky=W)
        Label(window, text=None).grid(row=4,column=1) # space between inputs and outputs
		
		
        Label(window, text="Payment:").grid(row=5, column=1, sticky=W)
        Label(window, text="Total Payments:").grid(row=6, column=1, sticky=W)
        
        # variables to store inputs
        self.pv = StringVar()
        self.interest_rate = StringVar()
        self.term = StringVar()

		# variables for outputs
        self.pmt = StringVar()
        self.total = StringVar() 
		
		# text boxes to hold inputs and outputs
        Entry(window, textvariable = self.pv,
              justify=RIGHT).grid(row=1,column=2, padx=(0,5))
        Entry(window, textvariable = self.interest_rate, 
              justify=RIGHT).grid(row=2,column=2)
        Entry(window, textvariable = self.term, 
              justify=RIGHT).grid(row=3,column=2)
        Label(window, textvariable = self.pmt, 
			font="Helvetica 12 bold", 
            justify=RIGHT).grid(row=5,column=2,sticky= E )
        Label(window, textvariable = self.total, 
			font="Helvetica 12 bold", 
            justify=RIGHT).grid(row=6,column=2, sticky= E)

        window.mainloop()


LoanCalculator()
