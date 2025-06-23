''''''
import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl
''''''
#ssl wasn't explained or gone over. just a simple "it makes secure http work. just do it." so I'll learn it DIY later
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#the html variable -- where it's `library`.`module`.method/function was also not explained.
#however, it was made relatively clear that the html variable returns a string
#unfortuneately, the soup object, and even calling the BeautifulSoup function, wasn't super clear.  
url = input('website: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, ('html.parser'))

rturned_tags = soup('a')
for tag in rturned_tags:
    print(tag.get('href', ...))


#the practice for the practice