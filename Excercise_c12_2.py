import urllib.parse, urllib.request, urllib.error

wordcount = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    for word in line.decode().split():
        wordcount[word] = wordcount.get(word, 0) + 1
    print(line.decode().strip())
print(wordcount)

'''Simple urllib practice. I probably know it all to well at this point now though. Instructor wasn't clear
about not exactly needing it. :roll_eyes:'''