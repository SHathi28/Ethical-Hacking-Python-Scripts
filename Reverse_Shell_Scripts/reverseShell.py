#/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/22/2021

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.7.125", 54321))
sock.close()
