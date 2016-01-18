# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:51:21 2016

@author: anupam.srivastava
"""

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import ssl
#from BeautifulSoup import *
from bs4 import BeautifulSoup

url = raw_input("Enter URL: ")
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))
for i in range(count):
    print "Retrieving:", url
    scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    uh = urllib.urlopen(url, context=scontext)
    data = uh.read()
    soup = BeautifulSoup(data)
    tags = soup("a")
    pos = 0
    for tag in tags:
        pos = pos + 1
        if pos == position:
            url = tag.get("href", None)
            break
print "Last Url:", url