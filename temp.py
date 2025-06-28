''''''
import json
''''''
#parsion with JSON using a small class-created document.
input = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 743 000 0000"
    },
    "email" : {
        "hide" : "yes"
    },
    "age" : "45"
}
'''

input2 = '''[
    {
        "id" : "001",
        "x" : "1",
        "Name" : "Chuck"
    },
    {
        "id" : "002",
        "x" : "2",
        "Name" : "Brent"
    }
]'''
data = json.loads(input)
print('data type', type(data))
print('Name:', data['phone']['type'],'\nAge:',data['age'])

data2 = json.loads(input2)
print(data2[0]["id"])
#the practice for the practice