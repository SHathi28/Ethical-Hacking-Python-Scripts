#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/07/2021

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] Please Specify a Host to Scan: ")

def portscanner(port):
    if sock.connect_ex((host,port)):
        print(colored("[-] Port %d is closed" % (port), 'red'))
    else:
        print(colored("[+] Port %d is open" % (port), 'green'))

for port in range (1, 1000):
    portscanner(port);
