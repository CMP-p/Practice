# Shouts (capitalizes all letters) all the text in a text document, and prints them to the screen.
# Using a lot of the new things I've learned here too. even the check in [no,etc] part in new.
x = 0
while True:
    usr_inp = input('Enter a (text) file name: ')
    try:
        fhandle = open(usr_inp)
        x = 0
        break
    except:
        print('File not found')
        x += 1
        if x == 5: quit() # grants 5 attempts
check = input('opening capitalized version of file. press [Enter] to continue, type NO to terminate.')
if check in ['NO', 'No', 'no']: print(print('Quitting program.\n'), quit()) # Yes this line works


for i in fhandle:
    i = i.rstrip('\n').upper()
    print(i)
    # This chunk limits to 5 lines, for debugging
    x +=1
    if x == 5:
        break
    # Below counts lines on new, empty lines
    elif i == '\n':
        print(x, '#lines printed#')