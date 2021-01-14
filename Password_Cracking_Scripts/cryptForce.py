#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/13/2021

import crypt
from colorama import Fore

def crackPassword(username, password):
    salt = password[0:2]
    dictionary = open('crypt_dictionary.txt', 'r')
    for word in dictionary:
        word = word.strip('\n')
        cryptPassword = crypt.crypt(word, salt)
        if password == cryptPassword:
            print(Fore.GREEN + '[+] Found Password\t\t\t' + username + ' : ' + word)
            return
    print(Fore.RED + '[-] Unable to Crack Password For:\t' + username)
    
def main():
    try:
        passwordFile = open('crypt_passwords.txt', 'r')
    except:
        print('[-] File Not Found')
        quit()
    for line in passwordFile.readlines():
        username = line.split(':')[0]    
        password = line.split(':')[1].strip('\n')
        #print(Fore.RED + '[*] Cracking Password For: ' + username)
        crackPassword(username, password)
    

main()
