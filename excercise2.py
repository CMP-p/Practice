#Tracking excercises 6 & 7

#Excercise 6, Rewriting pay calculator with overtime, in a function, with value returned

def pay(Hours,Wage):
    check = True
    while check is True:
        try:
            Hours = float(Hours)
            check = False

        except:
            Hours = input('please enter a valid number for Hours: \n')
    
    #checking for valid numbers to float input
    check = True
    while check is True:
        try:
            Wage = float(Wage)
            check = False

        except:
            Wage = input('please enter a valid number for Wage: \n')

    #checking for overtime, and adding hours/ equivalent to adjusting pay.
    if Hours > 40:
        Hours = ((Hours-40) * 0.5) + Hours
    
    #calculates pay, formats numbers
    Pay = '$' + str(Wage*Hours) + '0'
    return Pay
    
  
########################### Defined Function #######################################


Payment = pay(input('How many hours did you work?: \n'), input('And Whats your hourly wage?: \n'))
print(f'your check will have {Payment} on it', '\n'*3)
print('end',quit())


#Excercise 7
c = 0
while True:
    c += 1
    if c < 5:
        print('c less than 5')
        continue
    elif c > 5:
        print('C greater than 5', 'x'*c)
    else : pass
    print('nearing the end')
    if c >= 10:
        break