# -*- coding: utf-8 -*-

#import xml.etree.ElementTree as ET
#
#data ='''
#<stuff>
#    <users>
#        <user x="2">
#            <id>001</id>
#            <name>Chuck</name>
#        </user>
#        <user x="7">
#            <id>009</id>
#            <name>Brent</name>
#        </user>
#    </users>
#</stuff>'''
#
#stuff = ET.fromstring(data)
##print 'Name:', tree.find('name').text
##print 'Attr:', tree.find('email').get('hide')
#lst = stuff.findall('users/user')
#print 'User count:', len(lst)
#for item in lst:
#    print 'Name', item.find('name').text
#    print 'Id', item.find('id').text
#    print 'Attribute', item.get('x')

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()

print 'Retrieved', len(data), 'characters'
tree = ET.fromstring(data)
results = tree.findall('.//count')
count = 0
total = 0
for item in results:
    count = count + 1
    total = total + int(item.text)

print 'Count:', count
print 'Sum:', total