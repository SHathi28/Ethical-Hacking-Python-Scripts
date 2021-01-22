#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/22/2021

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("192.168.7.125", 54321))
sock.listen(5)

print(colored("[!] Listening For Incoming Connections", "yellow"))

target, ip = sock.accept()

print(colored("[+] Connection Established From : %s" % str(ip), "green"))

sock.close()
