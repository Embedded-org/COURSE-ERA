import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
data=data.decode()
print(data)
commentinfo = ET.fromstring(data)
result_list = commentinfo.findall('comments/comment')
#print("result list is",result_list)
#print("comment count",len(result_list))
final_list=[]
for item in result_list:
    str1=item.find('count').text
    final_list.append(str1)
num=0
for k in final_list:
    num=num+int(k)
print("Sum:",str(num))
