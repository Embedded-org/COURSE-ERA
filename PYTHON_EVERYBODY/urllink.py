# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
counter = input('Enter count')
counter=int(counter)
pos = input('Enter position ')
position=int(pos)
for k in range(counter):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    count=0
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        count=count+1
        if count==position:
            url=tag.get('href', None)
            break
stuff=re.findall(r'by_(\S+).html',url)
print(stuff[0])
