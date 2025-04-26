#excercise 9 i think lmao. 
#Count word frequency using a dictionary
#my bonus, produce an average between all word counts
strike = 3
while True:
    try:
        handle = open(input('Enter file name to begin: \n'))
        break
    except: 
        strike -=1
        print(f'Invalid file name. {strike} more tries')
        if strike == 0:
            print(print('closing program'),quit())

#Tracks how many time eacch word is said
words = []
count = {}
for line in handle: 
    words = line.rstrip().split()
    for word in words:
        count[word] = count.get(word,0) + 1

#Finds the most repeated word from the file
highest_key = ...
highest_value = ...
for key,value in count.items():
    ...
    if highest_value is ... or highest_value < value:
        highest_key,highest_value = key,value
print('The most common word was "',highest_key.capitalize()+'. "','Being said',highest_value,'times.\n\n')

words = [i for i in count.keys()]
number = 0
for value in count:
    ...
    number += count[value]
avg = number/len(words)
print(f'There are {len(words)} unique words, {number} words total. Each word was repeated {avg} times, on average.\n\n')


'''
#this is an alternate method to getting the key-value pair that has the highest repition
altkey,altvalue = max(count, key=count.get),max(count.(values))
print(altkey,altvalue)
'''


alt_min_v = min(count.values()) #records the lowest repeated word, takes only first value if shared values
alt_min_mult = [key for key,value in count.items() if value <= alt_min_v] #records every key matching lowest value
# alt_min_k = min(count, key = count.get) #gets only one key, if you're certain all unique values
print(f'The least said word(s) was {alt_min_mult}, being said {alt_min_v} time(s).')