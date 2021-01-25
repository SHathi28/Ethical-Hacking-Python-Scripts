# Ethical Hacking Python Scripts

## Scanner Scripts
1. **advancedPortScanner.py:** An upgraded portScan.py script. This program will allow the user to specify either a host name or IP address and multiple ports to scan. The script will resolve any host name provided to an IP address and print to the console if the ports specified by the user are open or closed.\
![advancedPortScanner Screenshot](README_Screenshots/advancedPortScanner_Screenshot.png)

2. **portScan.py:** A simple port scanner coded in Python that asks to specify an IP address. With this IP address, the script will scan the first 1000 ports and print out which ports are open and which ports are closed.\
![portScan Screenshot](README_Screenshots/portScan_Screenshot.png)

3. **retrieveBanner.py:** A python script that scans through the first 100 ports of a host the user inputs and attempts to retrieve the banners from the ports and prints the first 1024 bits of the banner to the console if it exists.\
![retrieveBanner Screenshot](README_Screenshots/retrieveBanner_Screenshot.png)

4. **vulnerabilityScanner.py:** An expansion of the retrieveBanner.py. This script will scan multiple hosts rather than a single on and will check some of the most common ports (20/21 - FTP, 22 - SSH/SFTP/SCP, 25 - SMTP, 443 - HTTPS, 3389 - RDP) and retrieve the banners of those ports from each host if the port contains a vulnerability.\
![vulnerabilityScanner Screenshot](README_Screenshots/vulnerabilityScanner_Screenshot.png)

## SSH / FTP Scripts
1. **anonymousLogin.py:** This script is designed to attempt an FTP Anonymous Login Attack. This script attempt to anonymously FTP login to the user supplied host. If the target host allows anonymous FTP login, the script print a success message to the console.\
![anonymousLogin Screenshot](README_Screenshots/anonymousLogin_Screenshot.png)

2. **sshBrute.py:** An upgraded sshLogin.py script. This script is designed to all the user to input a host and username and attempts to SSH into the host and guess the username's password by reading passwords from a file. This file could be used to contain some of the most common password or default password used in systems. If the script is able to SSH into the host, it will attempt to print out all the encrypted passwords in the /etc/shadow file.\
![sshBrute Screenshot](README_Screenshots/sshBrute_Screenshot.png)

3. **sshLogin.py:** This script attempts to SSH into the user inputted host and login in using the user inputted username and password. The script is able to skip the "Are you sure you want to continue connecting" prompt when logging into a new host. If the SSH connection is successful, the script will attempt to print out target's root user's encrypted password from the target's /etc/shadow file.\
![sshLogin Screenshot](README_Screenshots/sshLogin_Screenshot.png)

4. **ftpBrute.py:** Reads through the specified username:password file in an attempt to brute force FTP login to the specified host. The username:password file could be used to contain some of the most common passwords or default passwords and after finding a misconfigured target that has FTP (port 20/21) enabled, it would read through the password file and try to connect to the host. If the script finds the correct username:password pair, it'll print the results to the console.\
![ftpBrute Screenshot](README_Screenshots/ftpBrute_Screenshot.png)

## Password Cracking Scripts
1. **cryptForce.py**: This script attempts to mimic a dictionary attack against salted password. The script starts with grabbing the salt used by the passwords. By using a dictionary text file containing the most commonly used password, the script encrypts the dictionary passwords with the salt and compares them to passwords file which contain the user's pre-computed  salted password. If the computer encrypted password matches the user's password, it prints the result to the console.\
![cryptForce Screenshot](README_Screenshots/cryptForce_Screenshot.png)

2. **hasher.py**: Simple script that prints out the MD5, SHA1, SHA224. SHA256, and SHA512 hashes of the user specified phrase.\
![hasher Screenshot](README_Screenshots/hasher_Screenshot.png)

3. **md5Brute.py**: This script will ask the user to input a pre-computed MD5 hash. It will compare the input to the MD5 hashes from the user specified file. If the password is a match, the script will print the un-hashed password to the console.\
![md5Brute Password](README_Screenshots/md5Brute_Screenshot.png)

4. **sha1Hash.py**: The script will ask the user to input a pre-computed SHA1 hash. It will calculate the SHA1 hashes of the 10,000 more common passwords and compare them to the user inputted hash. If the hashes  match, the script will print the un-hashed password to the console.\
![sha1Hash Password](README_Screenshots/sha1hash_Screenshot.png)

## Flooder, Sniffer, and Spoofer Scripts
1. **arpSpoofer.py**: This Python script attempts to spoof ARP packets. The script will get the MAC address of the target IP address and attempt to send a packet from the local machine spoofed as the spoofed IP address. If the user interrupts the program while it is executing, the script will restore the ARP tables back to their original state.

2. **ftpSniffer.py**: This Python script is designed to sniff the host machine for any FTP attempts. When a user attempts to FTP onto a server, the script will print to the console the username, password, and IP used for the FTP connection.\
![ftpSniffer Screenshot](README_Screenshots/ftpSniffer_Screenshot.png)

3. **httpSniffer.py**: This Python script is designed to sniff the host machine for any HTTP packet in an attempt to grab a packet that contains a user's username and password they used to log into a website. The script will print out the captured packet's URL for the site logged into and payload that contains the username and password. The below images show what the script will print to console when I attempt to log on to http://demo.testfire.net/login.jsp with the username and password of admin / admin.\
![httpSniffer Screenshot 1](README_Screenshots/httpSniffer_Screenshot1.png)
![httpSniffer Screenshot 2](README_Screenshots/httpSniffer_Screenshot2.png)

4. **macChanger.py**: This Python script is designed to allow a user to change their MAC address of an interface of their choosing. The script will bring down the interface, change the MAC address, then bring the interface back up.\
![macChange Screenshot](README_Screenshots/macChanger_Screenshot.png)

5. **macSniffer.py**: This Python script is designed to mimic the sniffing capabilities of Wireshark. This script will sniff all packets sent and received by the host machine and will print to the console the packet's destination and source MAC address and protocol being used.\
![macSniffer Screenshot](README_Screenshots/macSniffer_Screenshot.png)

6. **synFlooder.py**: This Python script will attempt a SYN Flood attack. The script will consistently send packets to the destination IP address and port specified by the user, masquerading as an IP address different than the machine that is running the program. For example, this script can be used to block port 80 on the target, resulting in the target being unable to/slowly able to access the internet.\
![synFlooder Screenshot](README_Screenshots/synFlooder_Screenshot.png)

## Network Analysis Scripts
1. **packetAnalyzer.py**: This Python program will analyze each packet received by the host machine and print out the contents of its Ethernet, IP, and TCP/UDP headers to the console. The script will differentiate the packet's protocol as either TCP or UDP and print their respective headers to the console.\
![packetAnalyzer Screenshot 1](README_Screenshots/packetAnalyzer_Screenshot1.png)\
![packetAnalyzer Screenshot 2](README_Screenshots/packetAnalyzer_Screenshot2.png)

## Reverse Shell Scripts
1. **keylogger.py**: A simple keylogger that can be run on the target machine to record all the keystrokes the target types while using the target machine.

2. **reverseShell.py**: Works in conjunction with server.py. This script is designed to be placed on the target machine and establish a connection with the command system, waiting to receive commands to execute and send back.

3. **server.py v1.0**: A simple Python script designed to listen for incoming connections on the host machine.\
![reverseShell Screenshot 1](README_Screenshots/reverseShell_Screenshot1.png)

   **server.py v1.1**: Upgrade of the script. Allows the script to connect to a remote system (in this case it's the local machine) and send and receive messages between the two programs.\
![reverseShell Screenshot 2](README_Screenshots/reverseShell_Screenshot2.png)

   **server.py v1.2**: Allows the script to now continuously execute commands on the remote system and print the results to the console.\
![reverseShell Screenshot 3](README_Screenshots/reverseShell_Screenshot3.png)

   **server.py v1.3**: Increase the amount of data the server is able to receive and parse from the remote system by utilizing the JSON library. In this example, the script is able to receive the data from the command 'netstat -nr' which is above 1024 bytes and would have previously crashed the program.\
![reverseShell Screenshot 4](README_Screenshots/reverseShell_Screenshot4.png)

   **server.py v1.4**: Add directory traversal functionality to the script to allow the host to navigate through the target's file system.\
![reverseShell Screenshot 5](README_Screenshots/reverseShell_Screenshot5.png)

   **server.py v1.5**: Allow the server to upload (work in progress) and download (completed) files from the target machines. Pictured below is the download function.\
![reverseShell Screenshot 6](README_Screenshots/reverseShell_Screenshot6.png)

   **server.py v1.6**: Allow the reverseShell.py script have persistence storage on target and masquerade itself in the Registry when running.\
![reverseShell Screenshot 7](README_Screenshots/reverseShell_Screenshot7.png)

   **server.py v1.7**: Everytime it's  run, the reverse shell/backdoor program, will continuously try to establish a connection with the server. If it is unable to connect, it will wait 5 seconds before attempting to re-connect.\
![reverseShell Screenshot 8](README_Screenshots/reverseShell_Screenshot8.png)

   **server.py v2.0**: Implement multiple new functions. Added the ability to download files to that target PC, capture screeenshots of the target's monitor, check if the user has admin privileges on the target, allow the user to start programs on the target, and start and dump the contents of a keylogger. Below is an example of the newly added help section and the user checking if they have admin privileges./
![reverseShell Screenshot 9](README_Screenshots/reverseShell_Screenshot9.png)

4. **threaded.py**: An extension of the server.py file that acts as a Command and Control Center that can connect to multiple target machines and execute commands on them individually or execute commands on all the machines at once.\
![threaded Screenshot 1](README_Screenshots/threaded_Screenshot1.png)
![threaded Screenshot 1](README_Screenshots/threaded_Screenshot2.png)

## Web Penetration Testing Scripts
1. **bruteforcer.py**: Python script that attempts to bruteforce login into the the URL specified in the script. If the username and password combination is found, it will be printed to the console. This script can be used to attempt to login into different types of login pages.\
![bruteforcer Screenshot](README_Screenshots/bruteforcer_Screenshot.png)

2. **directoryDiscover.py**: Designed to look for hidden directories on a site specified by the user.\
![directoryDiscover Screenshot](README_Screenshots/directoryDiscover_Screenshot.png)

3. **gmailBruteforce.py**: A simple Python script that attempts to bruteforce login into the user specified Gmail account. The program will print to the console if the login attempt was successful or not.\
![gmailBruteforce Screenshot](README_Screenshots/gmailBruteforce_Screenshot.png)

4. **wifiStealer.py**: A simple Python script that attempts to retrieve the plaintext passwords of all Wi-Fi networks on the host. The script will then attempt to email the passwords to an email the user can specify and will save the output to a file.
