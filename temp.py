''''''
import xml.etree.ElementTree as ET
''''''
#parsing xml using ElementTree and a small class-created document.
input = '''<stuff>
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
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('list:',lst)

for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id'))
    print('Attribute', item.get('x'))

#the practice for the practice