import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url='http://py4e-data.dr-chuck.net/comments_428422.json'

urlh=urllib.request.urlopen(url, context=ctx)
data=urlh.read().decode()

info = json.loads(data)
#print(json.dumps(info, indent=4))
nsum=0
for item in info['comments']:
    nsum+=int(item['count'])
print(nsum)
