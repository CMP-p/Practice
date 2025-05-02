#I practice in here with the lesson
import re
fhandle = open('mbox-short.txt')
conf_list = []
pat = '^X.+C.+: ([0-9.]+)'
counter = 0
for line in fhandle:
    counter += 1
    if counter == -1: break
    finds = re.findall(pat, line)
    if len(finds) != 1: continue
    if float(finds[0]) >= 0:
        conf_list.append(finds[0])

print(conf_list,len(conf_list),)
fhandle.close()


dict2pct = {}
copies = 0

for v in conf_list:
    k = str(float(v[:5])*100)+'%'
    if k in dict2pct:
        copies += 1
        k = k + f' C {copies}'
    dict2pct[k] = v
print (dict2pct, len(dict2pct), len(conf_list))

# searching for the following line : X-DSPAM-Confidence: 0.875
#makes a dictionary andcorrolating keys to a percent, and the number it was before. I didn't include rounding because 
# Time is of the essenece,so I assigned a copy counter. xP this was allextra, not even an assignment