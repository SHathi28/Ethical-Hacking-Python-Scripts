#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/20/2021

import socket
import os,sys
import struct
import binascii

socketCreated = False
socketSniffer = 0

def analyzeEtherHeader(dataRecv):
    ipBool = False
    etherHeader = struct.unpack('!6s6sH',dataRecv[:14])
    dstMac = binascii.hexlify(etherHeader[0]).decode()
    srcMac = binascii.hexlify(etherHeader[1]).decode()
    protocol = etherHeader[2] >> 8
    data = dataRecv[14:]

    print('---------- ETHERNET HEADER -----------')
    print('Destination MAC: %s:%s:%s:%s:%s:%s' % (dstMac[0:2], dstMac[2:4], dstMac[4:6], dstMac[6:8], dstMac[8:10], dstMac[10:12]))
    print('Source MAC: %s:%s:%s:%s:%s:%s' % (srcMac[0:2], srcMac[2:4], srcMac[4:6], srcMac[6:8], srcMac[8:10], srcMac[10:12]))
    print('Protocol: %hu\n' % protocol)

    if protocol == 0x08:
        ipBool = True

    return data, ipBool

def main():
    global socketCreated
    global socketSniffer

    if socketCreated == False:
        socketSniffer = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
        socketCreated = True;

    dataRecv = socketSniffer.recv(2048)
    os.system('clear')

    dataRecv, ipBool = analyzeEtherHeader(dataRecv)

while True:
    main()

