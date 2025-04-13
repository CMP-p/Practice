# Greet user by name

def greet():
    name = input("What's your name? \n").title()
    print(f'Wuz good {name}?')
    return name

name = greet()
#quit()


# Gross pay Calculator
'''''
Hours = float(input('How many hours did you work? \n'))
Wage = float(input("What's your hourly rate? \n"))
print("You're gross pay is" , '$' + str(Wage*Hours) + '0,', name)
'''

# Rewriting calculator to give 1.5 times the pay for overtime, with input capture
check = True #to exit while loops

while check is True:
    try: 
        Hours = float(input('How many hours did you work? \n'))
        check = False
    except:
        print('Please enter a valid number. \n')
check = True #resetting exit condition

while check is True:
    try:
        Wage = float(input('Whats your hourly rate? \n'))
        check = False
    except: 
        print(f"Please enter a Valid number.")
check = True

pay = False #defining variable globally before used
if Hours > 40:
    pay = ((Hours-40)*Wage*1.5)+(40*Wage)
    print('Overtime earned.')
else: pay = Wage*Hours


print('$'+str(pay)+'0', 'should be on the check buddy.') 

