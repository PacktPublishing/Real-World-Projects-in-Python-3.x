#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:03:59 2019

@author: mjmacarty
"""

import smtplib
from pw import pw

# this method of creating a class with my password was used to protect privacy
# you should replace MY_PASSWORD with your email password  
pw = pw()
USER = pw.user
MY_PASSWORD = pw.password

# connect to gmail simple mail transfer protocol
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)

print(smtp_obj.ehlo()) # -> enhanced handshake with server

print(smtp_obj.starttls()) # -> encrypt commands  (transport layer security)


# if using google you will need to change security setting to allow access --> see link
print(smtp_obj.login(USER, MY_PASSWORD))


smtp_obj.sendmail("matt.macarty@gmail.com", "mmacarty@bentley.edu", 
                  "Subject: test 1-2-3 \n Hello dear friend. I just emailed to say hello. You need lots more email I know. Thank you.")

print(smtp_obj.quit())

