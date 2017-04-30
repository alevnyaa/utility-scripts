#!/usr/bin/env python
import urllib.request
from bs4 import BeautifulSoup
import os
import shutil

from fgconf import target_url, save_dir, url_pattern

os.chdir(save_dir)

req = urllib.request.Request(
        target_url, 
        headers={'User-Agent': 'Mozilla/5.0'})
html_txt = urllib.request.urlopen(req).read()

bs = BeautifulSoup(html_txt, 'html.parser')

links = []

for hyperlink in bs.find_all('a'):
    if(hyperlink.attrs.get('href').startswith(url_pattern) 
            and not hyperlink.attrs.get('class')):
        links.append(hyperlink)

progress = 0;
length = len(links)

print(str(length) + " files found")

cur_file_it = 0

for link in links:
    print("{current} out of {max_files} ({:.0%})".format(
            progress/length,
            current = progress, 
            max_files = length),
        end='\r') 
    file_req = urllib.request.Request(
            "https:" + link.attrs.get('href'), 
            headers={'User-Agent': 'Mozilla/5.0'})
    file_name = save_dir + link.get_text()
    if(file_name == save_dir):
        file_name += cur_file_it
        cur_file_it += 1
    cur_file_data = urllib.request.urlopen(file_req)
    cur_file_dir = open(file_name, 'wb')
    shutil.copyfileobj(cur_file_data, cur_file_dir)
    progress += 1

print("{current} out of {max_files} ({:.0%})".format(
        progress/length,
        current = progress, 
        max_files = length),
    end='\n') 
print("Job complete.")
