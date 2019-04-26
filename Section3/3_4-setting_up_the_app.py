# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:43:26 2019

@author: Matt Macarty
"""

# Setting up the application

# create a menu of options for email system
mail_options = {1:"Send Message", 2 :"Add Contact",
                3:"Delete Contact", 4: "Quit"}

# primary application functions

def read_contacts(file_name):
    pass

def email_login(email,password):
    pass

def send_mail():
    pass

def add_contact():
    pass

def delete_contact():
    pass


run_program =True
# main loop for program
while run_program:
    print("Please select a item number from the menu:")
    for k,v in mail_options.items():
        print("{} - {}".format(k,v))
    choice = int(input())
    # control structer for menu choices
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        run_program = False