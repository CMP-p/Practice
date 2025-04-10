#All of the commands i know, print(), if, for,
#while, else, elif, def():, range(), input(), str()
#int(), bool(), float(), True, False, variable = val
#<,<=,>,>=,==, is, is not, +, -, *, **, %, #, 
#var.capitalize, var.title, var.upper, var.lower,
#set(), list(), dict(), dict={key:val}, list = [val]
#set = {val}, tuple = val1, val2... or atuple = ()
#tuple(), print('txt \n' 'newline'), list2 = [0:2],
#newlist = alist[2:4], type(), var = list[0], 
#vars = set or vars = list, newlist=[-4:-3] start stop step
#len(), a_str.find(), list.append(), list.inset(dex,val)

vari = input()
#Random function play
def hey():
    for i in range(100):
        print('hey' + 'y'*i)
    print ("NO"+'o'*len(vari))
#calling said function
hey()

knowledge = input('so... what do you want to know?\n')

print('ohhh, so', knowledge, '...\n hmmmmmm?')
input()
print(input('well, what about ' + str(vari) + '?\n')+ '???', '\nokay, well solve this')

#question to pass the first gate
test2 = 3**4
answer2 = int(input('What is 3^4?:'))


Gated = True
while Gated == True:
    if answer2 == test2:
        print ('Well done! Pass!')
        Gated = False
    else: 
        print(test2)
        answer2 = int(input('NOPE! trry again:\n'))
Gated = False
print('\n\n\n\n\n\n')
print('Welcome to they new Palace!')