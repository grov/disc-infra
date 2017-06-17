#!/usr/bin/python
import os
import sys
from termcolor import colored


print(colored("Automatic Infrastructure Discovery",'green'))
print(colored("* Nmap",'green'))
print(colored("* Dnsmap",'green'))
print(colored("* SslScan",'green'))
print(colored("* Dirb",'green'))
print(colored("* Nikto",'green'))


#Domain ?
host = raw_input("Domain ? ")

# NMAP
def nmap():
	nmap = "nmap -sC -sS -sV -p 1-65535 -O -v --max-scan-delay 25 -oA nmap "
	print(colored("Command : ",'green')) + nmap, host
	os.system(nmap + ' ' + host)
nmap()

# DNSMAP
def dnsmap():
        dnsmap = "dnsmap"
        prefix = "-c dnsmap.csv"
        print(colored("Command : ",'green')) + dnsmap, host, prefix
        os.system(dnsmap+' '+host+' '+prefix)
dnsmap()

#SSLSCAN
def ssl():
	ssl = "sslscan --xml=sslscan.xml"
	print(colored("Command : ",'green')) + ssl, host
	os.system(ssl+' '+host)
ssl()

#DIRB
def dirb():
	dirb = "dirb"
	host2='https://'+host+' /usr/share/wordlists/dirb/common.txt'
	print(colored("Command : ",'green')) + dirb, host2
	os.system(dirb+' '+host2+' '">dirb.txt")
dirb()

#NIKTO
def nikto():
        nikto = "nikto -output nikto.html -h "
        print(colored("Command : ",'green')) + nikto, host
        os.system(nikto+' '+host)
nikto()
