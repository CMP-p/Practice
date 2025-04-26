#I run examples in here
#make a program that takes input text, counts the words, and outputs the word with the most repitions

line = input('enter text here: \n')
words = line.split()
print('\n'*4)
counter = {}
for i in words:
    counter[i] = counter.get(i,0) + 1

key_max = None
value_max = None
for i,j in counter.items():
    if value_max is None or value_max < j:
        key_max, value_max = i,j
        


print(key_max,value_max)





'''
Alternate for dict.get(x,y)
for i in heya:
    if i not in heyo:
        heyo[i] = 1
    else:
        heyo[i] += 1
print (heyo)
'''    