import urllib.request, urllib.parse, urllib.error
import json
import ssl

#note that google is increasingly requiring keys for this api
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

'''if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
    '''
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    #url = serviceurl + urllib.parse.urlencode({'address':address})
    url=address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    data=data.decode()
    js=json.loads(data)
    #print(json.dumps(js,indent=4))
    list1=[]
    for k in range(len(js['comments'])):
        list1.append(js['comments'][k]['count'])
    sum=0
    for k in list1:
        sum=sum+int(k)
    print('Sum:',str(sum))
