# Port and Vulnerability Scanning Scripts

portScan.py: A simple port scanner coded in Python that asks to specify an IP address. With this IP address, the script will scan the first 1000 ports and print out which ports are open and which ports are closed.

advancedPortScanner.py: An upgraded portScan.py script. This program will allow the user to specify either a host name or IP address and multiple ports to scan. The script will resolve any host name provided to an IP address and print to the console if the ports specified by the user are open or closed.

retrieveBanner.py: A python script that scans through the first 100 ports of a host the user inputs and attempts to retrieve the banners from the ports and prints the first 1024 bits of the banner to the console if it exists.

vulnerabilityScanner.py: An expansion of the retrieveBanner.py. This script will scan multiple hosts rather than a single on and will check some of the most common ports (20/21 - FTP, , 22 - SSH/SFTP/SCP, 25 - SMTP, 443 - HTTPS, 3389 - RDP) and retrieve the banners of those ports from each host.
