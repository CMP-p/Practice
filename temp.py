#I practice in here with the lesson

import re

stwing1 = 'this is test one'
stwing2 = 'this is test two'
stwing3 = 'this is test three'
stwings = stwing1,stwing2,stwing3
found = list()
for i in stwings:
    if re.search(r't.+\s+t.+\s+t', i):
        found.append(re.findall(r'[set]+',i))
        print(i)
    else: print('hehe okay buddy\vI saw that')

print(found)

#Practicing with regex re.search(patter, text) and re.findall(pattern, text) 