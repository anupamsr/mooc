# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 13:35:43 2016

@author: Anupam Srivastava
"""

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict()
for from_line in handle:
    if from_line.startswith("From "):
        hour = from_line.split()[5].split(":")[0]
        hours[hour] = hours.get(hour, 0) + 1
handle.close()
for key, val in sorted(hours.items()):
    print key, val
