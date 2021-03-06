#!/usr/bin/python
# coding: utf8
import os
import sys
from termcolor import colored


print(colored("Automatic Infrastructure Discovery",'green'))
print(colored("* Nmap",'green'))
print(colored("* Dnsmap",'green'))
print(colored("* DnsEnum",'green'))
print(colored("* testssl.sh",'green'))
print(colored("* Dirb",'green'))
print(colored("* Nikto",'green'))
print(colored("* WafW00f",'green'))
print(colored("* THEHARVESTER",'green'))



#Domain ?
host = raw_input("Domain ? ")

print "╔════════════════════════════════════════════════════════════════╗"
print "║                             Nmap                               ║"
print "╚════════════════════════════════════════════════════════════════╝"
#NMAP
def nmap():
	nmap = "nmap -F -O -v -oA nmap "
	print(colored("Command : ",'green')) + nmap, host
	os.system(nmap + ' ' + host)
nmap()

print "╔════════════════════════════════════════════════════════════════╗"
print "║                             DNSmap                             ║"
print "╚════════════════════════════════════════════════════════════════╝"
#DNSMAP
def dnsmap():
        dnsmap = "dnsmap"
        prefix = "-r dnsmap.txt"
        print(colored("Command : ",'green')) + dnsmap, host, prefix
        os.system(dnsmap+' '+host+' '+prefix)
dnsmap()

print "╔════════════════════════════════════════════════════════════════╗"
print "║                             DNSenum                            ║"
print "╚════════════════════════════════════════════════════════════════╝"
#DNSenum
def dnsenum():
        dnsenum = "dnsenum -o dnsenum.txt -v"
        print(colored("Command : ",'green')) + dnsenum, host
        os.system(dnsenum + ' ' + host)
dnsenum()

print "╔════════════════════════════════════════════════════════════════╗"
print "║                             Testssl.sh                         ║"
print "╚════════════════════════════════════════════════════════════════╝"
#SSLSCAN
def ssl():
	ssl = "/etc/testssl.sh/testssl.sh --html"
	print(colored("Command : ",'green')) + ssl, host
	os.system(ssl+' '+host)
ssl()

print "╔════════════════════════════════════════════════════════════════╗"
print "║                             Dirb                               ║"
print "╚════════════════════════════════════════════════════════════════╝"
#DIRB
def dirb():
	dirb = "dirb"
	host2='https://'+host+' /usr/share/dirb/wordlists/common.txt'
	print(colored("Command : ",'green')) + dirb, host2
	os.system(dirb+' '+host2+' '"-o dirb.txt")
dirb()

print "╔════════════════════════════════════════════════════════════════╗"
print "║                             Nikto                              ║"
print "╚════════════════════════════════════════════════════════════════╝"
#NIKTO
def nikto():
        nikto = "nikto -output nikto.html -h "
        print(colored("Command : ",'green')) + nikto, host
        os.system(nikto+' '+host)
nikto()

print "╔════════════════════════════════════════════════════════════════╗"
print "║                             WafW00f                            ║"
print "╚════════════════════════════════════════════════════════════════╝"
# WafW00f
def wafw00f():
        wafw00f = "wafw00f"
        print(colored("Command : ",'green')) + wafw00f, host
        #os.system(wafw00f+ ' ' + host+' '+"> wafw00f.txt")
	output=os.system(wafw00f+ ' ' + host)
	
wafw00f()

print "╔════════════════════════════════════════════════════════════════╗"
print "║                             The Harvester                      ║"
print "╚════════════════════════════════════════════════════════════════╝"
# THEHARVESTER
def theharvester():
        theharvester = "theharvester -b google -d "
        print(colored("Command : ",'green')) + theharvester, host
        os.system(theharvester + ' ' + host + ' ' +"-f theharvester.txt")
theharvester()
