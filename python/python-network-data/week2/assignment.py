# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 10:15:12 2016

@author: Anupam Srivastava
"""

import re

try:
    with open("regex_sum_217558.txt", "r") as f:
        i = 0
        total = 0
        for line in f:
            arr = re.findall('[^0-9]*([0-9]+)', line)
            #print ">>>", line,
            if len(arr) > 0:
                for item in arr:
                    #print item,
                    i = i + 1
                    total = total + int(item)
                #print
        #print
        #print "Total =", total, "from", i, "items"
        print total
    f.close()

except:
    print "Problem opening file"
