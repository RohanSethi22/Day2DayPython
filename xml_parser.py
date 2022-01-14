import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url='http://py4e-data.dr-chuck.net/comments_428421.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print(data.decode())
tree = ET.fromstring(data)
nsum=0
results = tree.findall('comments/comment')
for ele in results:
    num = ele.find('count').text
    nsum+=int(num)
print(nsum)
