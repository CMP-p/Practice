'''A program that takes user input until user types "done", in which case the program ends, says the total, average and count. 
While also checking for valid data.
'''
print('Enter numbers. When finished type "done" and your total & Average will be shown at the end')
count, average, total = None, 0, 0

while True:
    if count is None: count = 1
    else: count += 1
    value = input()

    try: value = float(value)
    except: 
        if value == 'done': break
        print('invalid input. Please enter a number\n')
        continue

    total += value

average = total/count
print(f"Your Average is: {average}\nYour Count is:{count},\nYour Total is {total}") 
    
    