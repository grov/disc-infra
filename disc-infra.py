#!/usr/bin/python
import os
import sys

print("Automatic Infrastructure Discovery")
print("* Nmap")
print("* Dnsmap")
print("* SslScan")
print("* Dirb")

#Domaine renseigne
host = raw_input("Domaine ? ")

# NMAP
def nmap():
	nmap = "nmap -sC -sS -sV -p 1-65535 -O -v --max-scan-delay 25 "
	print("Commande : ") + nmap, host
	os.system("nmap"" " + str(host))
nmap()

# DNSMAP
def dnsmap():
	dnsmap = "dnsmap"
	print("Commande : ") + dnsmap, host
	os.system("dnsmap"" " + str(host))
dnsmap()

#sslscan
def ssl():
	ssl = "sslscan"
	print("Commande : ") + ssl, host
	os.system("sslscan"" " + str(host))
ssl()

#dirb
def dirb():
	dirb = "dirb"
	host2='https://'+host+' /usr/share/wordlists/dirb/common.txt'
	print("Commande : ") + dirb, host2
	os.system("dirb"" " + str(host2))
dirb()