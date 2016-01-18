# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 13:11:16 2016

@author: anupam.srivastava
"""

def roots(a, b, c):
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        print "Error: No real solutions"
        return None
    sqrt_disc = discriminant ** 0.5
    root_1 = (- b + sqrt_disc) / (2 * a)
    root_2 = (- b - sqrt_disc) / (2 * a)
    return (root_1, root_2)

def smaller_root(a, b, c):
    print "The smaller root of %dx^2 + %dx + %d is:" % (a, b, c)
    result = roots(a, b, c)
    if result != None:
        print min(result)

print smaller_root(1, 2, 3)
print smaller_root(2, 0, -10)
print smaller_root(6, -3, 5)