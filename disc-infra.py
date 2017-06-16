#!/usr/bin/python
import os
import sys

print("Automatic Infrastructure Discovery")
print("* Nmap")
print("* Dnsmap")
print("* SslScan")
print("* Dirb")
print("* Nikto")


#Domain ?
host = raw_input("Domain ? ")
output_dir = raw_input("Output Directory ? ")

# NMAP
def nmap():
	nmap = "nmap -sC -sS -sV -p 1-65535 -O -v --max-scan-delay 25 -oA nmap "
	print("Command : ") + nmap, host
	os.system(nmap + ' ' + host)
nmap()

# DNSMAP
def dnsmap():
        dnsmap = "dnsmap"
        prefix = "-c dnsmap.csv"
        print("Command : ") + dnsmap, host, prefix
        os.system(dnsmap+' '+host+' '+prefix)
dnsmap()

#SSLSCAN
def ssl():
	ssl = "sslscan --xml=sslscan.xml"
	print("Command : ") + ssl, host
	os.system(ssl+' '+host)
ssl()

#DIRB
def dirb():
	dirb = "dirb"
	host2='https://'+host+' /usr/share/wordlists/dirb/common.txt'
	print("Command : ") + dirb, host2
	os.system(dirb+' '+host2+' '">dirb.txt")
dirb()

#NIKTO
def nikto():
        nikto = "nikto -output nikto.html -h "
        print("Command : ") + nikto, host
        os.system(nikto+' '+host)
nikto()
