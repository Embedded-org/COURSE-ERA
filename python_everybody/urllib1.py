import urllib.request
import re
numlist=[]
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_779667.html')
soup = BeautifulSoup(html, "html.parser")
import re
for line in soup.body:
    stuff=re.findall(r'span.*>(\d+)',str(line))
    if len(stuff)==0:continue
    for k in stuff:
        num=int(k)
        numlist.append(num)
num=0
for k in numlist:
    num=num+int(k)
print(num)
