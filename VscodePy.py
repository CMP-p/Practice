#All of the commands i know, print(), if, for,
#while, else, elif, def():, range(), input(), str()
#int(), bool(), float(), True, False, avariable = val
#<,<=,>,>=,==, is, is not, +, -, *, **, %, #, 
#str.capitalize, str.title, str.upper, str.lower,
#set(), list(), dict(), dict={key1:val1, key2:val2}, list = [val1, val2...]
#set = {val1, val2...}, atuple = val1, val2... or Empty_tuple = ()
#tuple(), print('txt \n' 'newline'), newlist = alist[2:4], type(), 
# var = list[0], vars = set or vars = list, newlist=[-4:-3,1] start stop step
#len(), a_str.find(), list.append(), list.inset(dex,val)

vari = input()
#Random function play
def hey():
    for i in range(len(vari)):
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
ur_list=[]


Gated = True
while Gated:
    if answer2 == test2:
        print ('Well done! Pass!')
        Gated = False
    else: 
        print(test2)
        answer2 = int(input('NOPE! trry again:\n'))
        ur_list.append(answer2)

#testing slicing and list appendages
print("Here's all yout wrong answers! ;) \n", ur_list)
list_alt = ur_list[0:2]
print (list_alt, '\ndone')

print('Welcome to the Python Palace! :)')
