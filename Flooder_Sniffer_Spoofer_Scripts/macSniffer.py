#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/19/2020

import socket
from struct import *

def ethAddress(addr):
    ret = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (addr[0], addr[1], addr[2], addr[3], addr[4], addr[5])
    return ret

try:
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except:
    print('[-] Error Creating Socket Object')
    exit(1)

while True:
    packet = s.recvfrom(65535)
    packet = packet[0]

    ethLength = 14
    ethHeader = packet[:ethLength]
    
    ether = unpack('!6s6sH', ethHeader)
    ethProtocol = socket.ntohs(ether[2])
    print('[+} Destination MAC: ' + ethAddress(packet[0:6]) + ' | Source MAC: ' + ethAddress(packet[6:12]) + ' | Protocol: ' + str(ethProtocol))



