#!/usr/bin/env python

"""This module gets the ip addresses from various netflix urls and
generates a openvpn configuration to be included in the main conf.
"""

import subprocess

# This script gets the list of ips and generates a openvpn configuration
# to be used with services such as netflix

def dig_url(urls):
    """Uses the dig unix utility and returns a list of ip addresses"""
    ips = []
    for url in urls:
        ips.append(subprocess.check_output(['dig', "+short", url], universal_newlines=True))
    return ips

for ip in dig_url(['www.netflix.com']):
    print(ip)
