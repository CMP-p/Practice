import urllib.error, urllib.request, urllib.parse

link = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')

for i in link:
    print(i.decode().strip())
link.close()
