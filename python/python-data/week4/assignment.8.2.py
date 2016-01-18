# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 22:14:49 2016

@author: Anupam Srivastava
"""

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From "):
        print line.rstrip().split()[1]
        count = count + 1
print "There were", count, "lines in the file with From as the first word"
