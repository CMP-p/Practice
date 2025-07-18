''''''
import json
''''''
#Excercise c13_2
data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }    
}'''

js = json.loads(data)
print('Data',type(data),"\njs",type(js))

print(js['name'],'\n',js['email']['hide'])