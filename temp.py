#I practice in here with the lesson
import urllib.error, urllib.parse, urllib.request
from bs4 import BeautifulSoup

url = input('Enter- ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

print('done')


#importing urllib library modules and some dictionary refreshing

'''
I took a huge break. Felt a lot of overwhelm. I suppose I needed to straightne out some mental/emotional barriers.
I'm well enough to continue, taking a more mindful approach.
'''