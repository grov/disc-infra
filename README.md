# disc-infra
Automatique Infrastructure discovery, not yet finished (started ?) using :

- Nmap
- DNSmap
- DnsEnum
- ~~SSLscan~~
- testssl.sh
- Dirb
- Nikto
- Wafw00f
- THEHARVESTER (google)
- soon more ...


#  Install on Kali 

Easy Peasy ... :

```shell
pip install termcolor
python disc-infra-kali.py
```
# Install on Debian (ubuntu, mint etc.)
```shell
sed -i '$ a\deb http://http.kali.org/kali kali-rolling main contrib non-free' /etc/apt/sources.list
apt-get update && apt-get upgrade
apt-get install nmap dnsmap dnsenum sslscan dirb nikto wafw00f theharvester
mkdir /etc/testssl.sh
git clone https://github.com/drwetter/testssl.sh.git /etc/testssl.sh
pip install setuptools
pip install termcolor
python disc-infra-debian.py
```
# Know Bug
I dunno how to handle "bad interpreter" error or something like that so just do :
```shell
tr -d '\r' < disc-infra.py > disc-infra2.py
python disc-infra2.py
```
