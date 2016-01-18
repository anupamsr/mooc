# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 03:53:38 2016

@author: Anupam Srivastava
"""

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()
for line in handle:
    if line.startswith("From "):
        email = line.rstrip().split()[1].lower()
        emails[email] = emails.get(email, 0) + 1

result = None
max_count = None
for email, count in emails.items():
    if max_count == None or max_count < count:
        max_count = count
        result = email
        
print result, max_count