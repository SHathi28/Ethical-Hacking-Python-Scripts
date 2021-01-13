#!/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/13/2021

from colorama import Fore
import hashlib

def openFile(wordList):
    try:    
        file = open(wordList, 'r')
        return file
    except:
        print("[-] File Not Found")
        quit()

passwordHash = input('Enter MD5 Hash Value: ')
wordList = input('Enter Path to Password File: ')
file = openFile(wordList)

for word in file:
    print(Fore.YELLOW + '[*] Trying: ' + word.strip('\n'))
    encodeWord = word.encode('UTF-8')
    md5Hash = hashlib.md5(encodeWord.strip()).hexdigest()

    if md5Hash == passwordHash:
        print(Fore.GREEN + '[+] Password Found: ' + word)
        exit(0)
    else:
        pass

print('[-] Password Not in List')

