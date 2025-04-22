#I run examples in here
fname = input()
fhand = open(fname)

x=0
for lines in fhand:
    x += 1
    #print(str(x)+'-', lines)

print(x,'Lines in',fname)
fhand.seek(0)
num = fhand.readlines(1)
print(num)

    

#this guy really just showed us file.open() and '\n' like breh, last lecture there was like 100 new things, now this
#this time there's only 2??? xD wth. NEXT LESSON PLEASE