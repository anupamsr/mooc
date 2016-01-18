# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:14:13 2016

@author: Anupam Srivastava
"""

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
total = 0
for tag in tags:
#    print 'TAG:',tag
#    print 'URL:',tag.get('class', None)
#    print 'Contents:',tag.contents[0]
#    print 'Attrs:',tag.attrs
    count = count + 1
    total = total + int(tag.contents[0])

print "Count", count
print "Sum", total