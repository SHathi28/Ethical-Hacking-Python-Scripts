#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/18/2021

import subprocess

def changeMACAddress(interface, macAddr):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",macAddr])
    subprocess.call(["ifconfig",interface,"up"])

def main():
    interface = str(input('Enter Intreface to Change MAC Address of: '))
    newMACAddr = input('Enter MAC Address to Change to: ')

    before = subprocess.check_output(["ifconfig",interface])
    changeMACAddress(interface, newMACAddr)
    after = subprocess.check_output(["ifconfig",interface])

    if(before == after):
        print("[-] MAC Address Change Failed")
    else:
        print('[+] MAC Address Change Successfully')

main()
