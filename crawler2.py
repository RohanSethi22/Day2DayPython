import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/known_by_Rafif.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

pos=int(input('Enter position: '))
rep=int(input('Enter loop limit: '))

# Retrieve all of the anchor tags
tags = soup('a')
next_url=tags[pos-1].get('href', None)
while rep>0:
	next_url=tags[pos-1].get('href', None)
	print(next_url)
	last_name=tags[pos-1].contents[0]
	html = urllib.request.urlopen(next_url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	rep-=1
print(last_name)
