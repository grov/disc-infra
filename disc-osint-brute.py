#!/usr/bin/python
# coding: utf8
import os
import sys
from termcolor import colored
print ""
print(colored("╔════════════════════════════════════════════════════════════════╗",'green'))
print(colored("║                  Automatic Osint Discovery                     ║",'green'))
print(colored("╚════════════════════════════════════════════════════════════════╝",'green'))
print ""
print("Used Tools :")
print(colored("*  Nmap",'green'))
print(colored("*  Automater",'green'))
print(colored("*  Dnsmap",'green'))
print(colored("*  DnsEnum",'green'))
print(colored("*  Testssl.sh",'green'))
print(colored("*  Dirb",'green'))
print(colored("*  Nikto",'green'))
print(colored("*  WafW00f",'green'))
print(colored("*  THEHARVESTER",'green'))
print ""
print ""

#Entreprise ?
host = raw_input("Entreprise ? ")
path = os.getcwd()
print(colored("Repertoire : ",'green')) + path
print ""
print "╔════════════════════════════════════════════════════════════════╗"
print "║                             Nmap                               ║"
print "╚════════════════════════════════════════════════════════════════╝"
#Nmap
def nmap():
	nmap = "nmap -sS -sV -oA nmap"
	print(colored("Command : ",'green')) + nmap, host
	os.system(nmap + ' ' + host)
nmap()

copie = "cp nmap.nmap brutespray/"
os.system(copie)

print ""
print "╔════════════════════════════════════════════════════════════════╗"
print "║                             BruteSpray                         ║"
print "╚════════════════════════════════════════════════════════════════╝"
# BruteSpray
def brute():
        brute = "python brutespray/brutespray.py -f nmap.nmap"
        print(colored("Command : ",'green')) + brute
        os.system(brute)
brute()

create = "mkdir " + host
os.system(create)
copie2 = "cp -R *.nmap *.html *.txt *.gmap " + host
os.system(copie2)