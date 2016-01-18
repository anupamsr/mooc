# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 21:41:44 2016

@author: Anupam Srivastava
"""

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip().split()
    for word in words:
        if word not in lst:
            lst.append(word)

lst.sort()
for word in lst:
    print word