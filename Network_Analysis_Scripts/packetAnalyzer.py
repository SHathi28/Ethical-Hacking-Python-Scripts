#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/20/2021

import socket
import os,sys
import struct
import binascii

socketCreated = False
socketSniffer = 0

def analyzeIP(dataRecv):
    ipHeader = struct.unpack('!6H4s4s', dataRecv[:20])
    version = ipHeader[0] >> 12
    ihl = (ipHeader[0] >> 8) & 0x0f
    tos = ipHeader[0] & 0x00ff
    totalLength = ipHeader[1]
    ipID = ipHeader[2]
    flags = ipHeader[3] >> 13
    fragOffset = ipHeader[3] & 0x1fff
    ipTTL = ipHeader[4] >> 8
    ipProtocol = ipHeader[4] & 0x00ff
    checksum = ipHeader[5]
    srcAddr = socket.inet_ntoa(ipHeader[6])
    dstAddr = socket.inet_ntoa(ipHeader[7])
    data = dataRecv[20:]
    print('---------- IP HEADER ----------')
    print('Version: %hu' % version)
    print('IHL: %hu' % ihl)
    print('TOS: %hu' % tos)
    print('Length: %hu' % totalLength)
    print('ID: %hu' % ipID)
    print('Offset: %hu' % fragOffset)
    print('TTL: %hu' % ipTTL)
    print('Protocol: %hu' % ipProtocol)
    print('Checksum: %hu' % checksum)
    print('Source IP: %s' % srcAddr)
    print('Destination IP: %s\n' % dstAddr)

    if ipProtocol == 6:
        tcp_udp = "TCP"
    elif ipProtocol == 17:
        tcp_udp = "UDP"
    else:
        tcp_udp = "Other"

    return data, tcp_udp


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

    if ipBool:
        dataRecv, tcp_udp = analyzeIP(dataRecv)
    else:
        return

while True:
    main()

