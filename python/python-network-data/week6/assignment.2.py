# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:32:25 2016

@author: anupam.srivastava
"""

import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'
#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = raw_input('Enter location: ')
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved', len(data), 'characters'

try: js = json.loads(str(data))
except: js = None
if 'status' not in js or js['status'] != 'OK':
    print '==== Failure To Retrieve ===='
    print data
else:
    print 'Place id', js['results'][0]['place_id']
