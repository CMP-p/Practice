#I practice in here with the lesson
import urllib.request, urllib.parse, urllib.error

urlhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = {}
for line in urlhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

sum = 0
for k,v in counts.items():
    sum += v
print(counts, f'\n{sum}')
    


#importing urllib library modules and some dictionary refreshing