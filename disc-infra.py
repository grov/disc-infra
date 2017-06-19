#!/usr/bin/python
import os
import sys
from termcolor import colored


print(colored("Automatic Infrastructure Discovery",'green'))
print(colored("* Nmap",'green'))
print(colored("* Dnsmap",'green'))
print(colored("* DnsEnum",'green'))
print(colored("* SslScan",'green'))
print(colored("* Dirb",'green'))
print(colored("* Nikto",'green'))
print(colored("* WafW00f",'green'))
print(colored("* THEHARVESTER",'green'))



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

# DnsEnum
def dnsenum():
        dnsenum = "dnsenum -o dnsenum.txt -f /usr/share/wordlists/dnsmap.txt -v$
        print(colored("Command : ",'green')) + dnsenum, host
        os.system(dnsenum + ' ' + host)
dnsenum()

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

# WafW00f
def wafw00f():
        wafw00f = "wafw00f"
        print(colored("Command : ",'green')) + wafw00f, host
        os.system(wafw00f+ ' ' + host+' '+">wafw00f.txt")
wafw00f()

# THEHARVESTER
def theharvester():
        theharvester = "theharvester -b google -d "
        print(colored("Command : ",'green')) + theharvester, host
        os.system(theharvester + ' ' + host + ' ' +">theharvester.txt")
theharvester()
