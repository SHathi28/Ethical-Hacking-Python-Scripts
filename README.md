# Ethical Hacking Python Scripts

### Scanner Scripts
---
1. **advancedPortScanner.py:** An upgraded portScan.py script. This program will allow the user to specify either a host name or IP address and multiple ports to scan. The script will resolve any host name provided to an IP address and print to the console if the ports specified by the user are open or closed.

2. **portScan.py:** A simple port scanner coded in Python that asks to specify an IP address. With this IP address, the script will scan the first 1000 ports and print out which ports are open and which ports are closed.

3. **retrieveBanner.py: A python script that scans through the first 100 ports of a host the user inputs and attempts to retrieve the banners from the ports and prints the first 1024 bits of the banner to the console if it exists.

4. **vulnerabilityScanner.py:** An expansion of the retrieveBanner.py. This script will scan multiple hosts rather than a single on and will check some of the most common ports (20/21 - FTP, 22 - SSH/SFTP/SCP, 25 - SMTP, 443 - HTTPS, 3389 - RDP) and retrieve the banners of those ports from each host.

### SSH / FTP Scripts
---
1. **sshBrute.py:** An upgraded sshLogin.py script. This script is designed to all the user to input a host and username and attempts to SSH into the host and guess the username's password by reading passwords from a file. This file could be used to contain some of the most common password or default password used in systems. If the script is able to SSH into the host, it will attempt to print out all the encrypted passwords in the /etc/shadow file.

2. **sshLogin.py:** This script attempts to SSH into the user inputted host and login in using the user inputted username and password. The script is able to skip the "Are you sure you want to continue connecting" prompt when logging into a new host. If the SSH connection is successful, the script will attempt to print out target's root user's encrypted password from the target's /etc/shadow file.

3. **ftpBrute.py:** Reads through the specified username:password file in an attempt to brute force FTP login to the specified host. The username:password file could be used to contain some of the most common passwords or default passwords and after finding a misconfigured target that has FTP (port 20/21) enabled, it would read through the password file and try to connect to the host. If the script fine the correct username:password pair, it'll print the results to the console.
