#/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/22/2021

import socket

def shell():
    command = sock.recv(1024)
    message = "Hello, World!"
    sock.send(message.encode())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.7.125", 54321))
shell()
sock.close()
