#I run examples in here
def calcul(inp):
    your_str = inp
    num = 0
    for i in your_str:
        num += ord(i)
    return num


names = ['Christian', "Kayla", "Jeremy"]
val_name = {}
for name in names:
    val_name[name] = val_name.get(name, calcul(name))

print(val_name)