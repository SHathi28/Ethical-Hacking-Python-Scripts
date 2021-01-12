#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connectionScan(targetHost, targetPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((targetHost,targetPort))
        print '[*] %d/tcp Open' % targetPort
    except:
        print '[-] %d/tcp Closed' % targetPort
    finally:
        sock.close()

def portScan(targetHost, targetPorts):
    try:
        ip = gethostbyname(targetHost)
    except:
        print 'Unkown Host %s' %s (targetHost)
    
    try:
        targetName = gethostbyaddr(ip)
        print '[*] Scan Results For: ' + targetName;
    except:
        print '[*] Scan Results For: ' + ip
    
    setdefaulttimeout(1)
    
    for port in targetPorts:
        t = Thread(target=connectionScan, args=(targetHost, int(port)))
        t.start()


def main():
    parser = optparse.OptionParser('Usage: ' + 'Usage: ./advancerscanner.py -H <target Host> -p <Target Ports>')
    parser.add_option('-H', dest='targetHost', type='string', help='Specify Target Host')
    parser.add_option('-p', dest='targetPorts', type='string', help='Specify Ports separated by commas')
    (options, args) = parser.parse_args()
    targetHost = options.targetHost
    targetPorts = str(options.targetPorts).split(',')
    
    if (targetHost == None) | (targetPorts[0] == None):
        print(parser.usage)
        exit(0)

    portScan(targetHost, targetPorts)

if __name__ == '__main__':
    main()
