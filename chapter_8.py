#look for lines that start with "From" in the mbox file, and extract the third word
fhandle = open('mbox-short.txt')
words = list()
for line in fhandle:
    if line[0:4] != 'From':
        continue
    # Compound Gaurdian pattern/statement
    elif 'From' not in line or len(line.split()) <= 2:
        continue
    else:
        var = line.split()
        words.append(var[2])

print(words,'done')

#alt line 8 if line.startswith('from') = False
