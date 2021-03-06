# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:43:26 2019

@author: Matt Macarty
"""
import smtplib
from pw import pw

login  = pw()
USER = login.user
MY_PASSWORD = login.password

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
    # connect to gmail simple mail transfer protocol
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    print(smtp_obj.ehlo()) # -> enhanced handshake with server
    print(smtp_obj.starttls()) # -> encrypt commands  (transport layer security)
    print(smtp_obj.login(email, password))
    return smtp_obj

def create_message(name):
    f = open("message.txt", 'r')
    msg = f.read()
    personalized = msg.replace(msg[msg.find("<"):msg.find(">>")+2], name)
    return personalized

def send_mail(user,pw):
    contacts = read_contacts("contacts.txt")
    smtp_obj = email_login(user,pw)
    for contact in contacts:        
        try:
            msg = create_message(contact[0])
            smtp_obj.sendmail("matt.macarty@gmail.com", "mmacarty@bentley.edu", 
                  "Subject: test 1-2-3 \n" + msg)
            print("Message sent")
        except:
            raise Exception("An error occurred for: " + contact[0])
    smtp_obj.quit()

def add_contact(file_name):
    print("Enter contact name: ")
    name = input()
    print("Enter contact email: ")
    email = input()
    print("Enter flag: ")
    flag = input()
    contact = name +"|"+ email + "|" + flag + "\n"
    f = open("contacts.txt", 'a')
    f.write(contact)
    f.close()
    print("{} added".format(contact))
    
    
# function to permanently delete a name from the external file
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
        print("username: ")
        user = input()
        print("password: ")
        pw = input()
        send_mail(user, pw)
    elif choice == 2:
        add_contact('contacts.txt')
    elif choice == 3:
        # assumes you are working with a file named contacts.txt
        # setting variable allows you to immediately work with revised list
        contacts = delete_contact('contacts.txt')
    elif choice == 4:
        run_program = False