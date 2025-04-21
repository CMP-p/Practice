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
    

# Excercises 8? idk I've lost count
# Locating and converting a float in a known string
prompt_str = 'X-DSPAM-Confidence: 0.8475 '
# nums = float(prompt_str[prompt_str.find(': ') +1:].strip()) # This version is hard to read, but does the same as below
col_loc = prompt_str.find(': ')
new_str = prompt_str[col_loc + 1:]#slicing to the end of the string
nums = new_str.strip() #removing whitespaces
nums = float(nums) #converting to float
print(nums, type(nums)) 