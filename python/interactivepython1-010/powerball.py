# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 13:10:55 2016

@author: anupam.srivastava
"""

import random

def getrand(atleast, atmax, without = (None, )):
    rand_num = None
    while rand_num == None:
        rand_num = random.randrange(atmax + 1) + atleast
        if rand_num in without:
            rand_num = None
    return rand_num
    
def powerball():
    num_1 = getrand(1, 59)
    num_2 = getrand(1, 59, (num_1, ))
    num_3 = getrand(1, 59, (num_1, num_2))
    num_4 = getrand(1, 59, (num_1, num_2, num_3))
    num_5 = getrand(1, 59, (num_1, num_2, num_3, num_4))
    num_pb = getrand(1, 35)
    print "Today's numbers are %d, %d, %d, %d, and %d. The Powerball number is %d." %\
    (num_1, num_2, num_3, num_4, num_5, num_pb)

powerball()
powerball()
powerball()
