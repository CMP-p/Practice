''''''
import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl
''''''

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('website: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, ('html.parser'))

rturned_tags = soup('a')
for tag in rturned_tags:
    print(tag.get('href', ...))


#the practice