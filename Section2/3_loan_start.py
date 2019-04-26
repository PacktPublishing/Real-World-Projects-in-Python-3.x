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

        window.mainloop()


LoanCalculator()
