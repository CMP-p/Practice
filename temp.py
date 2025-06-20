import urllib.error, urllib.request, urllib.parse
from bs4 import BeautifulSoup as bs

website = input('Enter -')
html = urllib.request.urlopen(website).read()
soup = bs(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))


#had to do some practice for telnet. That was SO hard
    #GET /Romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n

'''GET /romeo.txt HTTP/1.1
Host: data.pr4e.org
Connection: close

lflf

GET /romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n
GET http://data.pr4e.org/romeo.txt HTTP/1.0
'''