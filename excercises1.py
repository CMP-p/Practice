# Greet user by name

def greet():
    name = input("What's your name? \n").title()
    print(f'Wuz good {name}?')
    return name

name = greet()
#quit()


# Gross pay Calculator
Hours = float(input('How many hours did you work? \n'))
Wage = float(input("What's your hourly rate? \n"))
print("You're gross pay is" , '$' + str(Wage*Hours) + '0,', name)
