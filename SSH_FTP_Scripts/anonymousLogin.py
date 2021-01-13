#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/12/2021

import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        print('[+] ' + hostname + ' FTP Anonymous Login Successfull')
        ftp.quit()
        return True
    except:
        print('[-] ' + hostname + ' FTP Anonymous Login Failed')
        return False

host = input("Enter IP Address to Target: ")
anonLogin(host)
