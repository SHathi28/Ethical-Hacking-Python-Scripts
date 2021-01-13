#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/07/2021

import socket

def returnBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return str(banner)
    except:
        return

def main():
    ip = raw_input("[*] Enter Target IP to Scan: ")
    for port in range(1,100):
        banner = returnBanner(ip, port)
        if banner:
            print "[*]" + ip + ":" + str(port) + " - " + banner.string('/n')

main()


