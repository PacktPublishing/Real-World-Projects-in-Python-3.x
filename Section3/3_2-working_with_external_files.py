# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:58:48 2019

@author: Matt Macarty
"""

# working with external files

# writing to a text file

# create a file handle with Python function 
f = open("contacts.txt", 'w')

# write a contact to the file
f.write("Mickey Mouse|mickey.mouse@disney.com|Y\n")

f.close()

#adding another contact
f = open("contacts.txt", 'a')
f.write("Donald Duck|donald.duck@disney.com|N\n")

f.close()

#reading from a file
f = open("contacts.txt", 'r')
contacts = f.read()

# create a function to process a contact file
def read_contacts(file_name):
    f = open(file_name, 'r')
    data = f.read().split('\n')
    contacts = []
    for contact in data:
        if len(contact) > 0:
            contacts.append(contact.split('|'))
    return contacts    













