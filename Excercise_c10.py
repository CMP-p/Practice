#This was indeed excercise 10. Check out that final print statement huh???
inp = input()
if inp == '': inp = 'clown.txt'
fhandle = open(inp)
mydict={}

for line in fhandle:
    words = line.rstrip().split()
    for word in words:
        mydict[word] = mydict.get(word,0) +1
fhandle.close() 
###remember to close the file when you're done using it, to avoid data cleaks. Also remember close is a .method

print(dict([(i,j) for j,i in sorted([(j,i) for i,j in mydict.items()],reverse=True)[:3]]))
...