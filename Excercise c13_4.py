import xml.etree.ElementTree as ET

data='''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>
'''

tree =ET.fromstring(data)
print('Name', tree.find('name').text)
print('Attribute- (hide email?)', tree.find('email').get('hide'))
#---------------------------------------
xml2 = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(xml2)
lst = (stuff.findall('users/user'))
print (len(lst))

for i in lst:
    print('Name:', i.find('name').text)
    print('ID:', i.find('id').text)
    print('Attribute:', i.get('x'))
