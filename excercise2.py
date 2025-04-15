#Tracking excercises 6-10 perhaps

#Rewriting pay calculator with overtime, in a function, with value returned

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
    print(f'your check will have {'$'+ str(Hours*Wage) +'0'}  on it', '\n'*3)
    
  
########################### Defined Function #######################################


Payment = pay(input('How many hours did you work?: \n'), input('And Whats your hourly wage?: \n'))
print(f'your check will have {Payment} on it', '\n'*3)
print('end')