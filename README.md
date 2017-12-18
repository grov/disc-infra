# disc-infra
Automatique Infrastructure discovery, not yet finished (started ?) using :

- Nmap
- DNSmap
- DnsEnum
- SSLScan
- Dirb
- Nikto
- Wafw00f
- THEHARVESTER (google)
- soon more ...


#  Install on Kali 

Easy Peasy ... :

```shell
pip install termcolor
python disc-infra.py
```
# Install on Debian (ubuntu, mint etc.)
```shell
sed -i '$ a\deb http://http.kali.org/kali kali-rolling main contrib non-free' /etc/apt/sources.list
apt-get update && apt-get upgrade
apt-get install nmap dnsmap dnsenum sslscan dirb nikto wafw00f theharvester
pip install setuptools
pip install termcolor
python disc-infra.py
```

Need to add a few more tools ...
