# -*- coding: utf-8 -*-

# Use words.txt as the file name
try:
    fname = raw_input("Enter file name: ")
    fh = open(fname, "r")
    
    for line in fh:
        print line.rstrip().upper()
except:
    print "Bad file name"