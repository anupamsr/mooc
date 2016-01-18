# -*- coding: utf-8 -*-

# Use the file name mbox-short.txt as the file name
try:
    #fname = raw_input("Enter file name: ")
    fname = "mbox-short.txt"
    fh = open(fname)
    header = "X-DSPAM-Confidence:"
    count = 0
    total = 0
    for line in fh:
        if not line.startswith(header):
            continue
        count = count + 1
        total = total + float(line[len(header):])
    average = total / count
    print "Average spam confidence:", average
except:
    print "Bad file name"