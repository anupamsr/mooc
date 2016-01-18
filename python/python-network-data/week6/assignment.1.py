# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:32:20 2016

@author: anupam.srivastava
"""

import urllib
import json

url = raw_input('Enter location: ')
print 'Retrieving', url
data = urllib.urlopen(url).read()
print 'Retrieved', len(data), 'characters'
info = json.loads(data)

count = 0
total = 0
for item in info['comments']:
    count = count + 1
    total = total + int(item['count'])

print "Count", count
print "Sum", total