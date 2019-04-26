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

# this function was defined in section 3_2 --> copy and paste
def read_contacts(file_name):
    f = open(file_name, 'r')
    data = f.read().split('\n')
    contacts = []
    for contact in data:
        if len(contact) > 0:
            contacts.append(contact.split('|'))
    return contacts

def email_login(email,password):
    pass

def send_mail():
    pass

def add_contact():
    pass

def delete_contact(file_name):
    contacts = read_contacts(file_name)
    enum_contacts = {}
    for i in range(1, len(contacts) + 1):
        enum_contacts[i] = contacts[i-1]
    print("Select contact to delete:")
    for key in enum_contacts:
        print("{} - {}".format(key, enum_contacts[key]))
    choice = int(input())
    deleted = contacts.pop(choice-1)
    print("{} removed".format(deleted))
    f = open('contacts.txt', 'w')
    for contact in contacts:
        f.write(contact[0] + '|' + contact[1] + '|' + contact[2] + '\n')
    f.close()
    return contacts    


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
        # assumes you are working with a file named contacts.txt
        delete_contact('contacts.txt')
    elif choice == 4:
        run_program = False