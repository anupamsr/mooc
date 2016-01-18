# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:00:11 2016

@author: Anupam Srivastava
"""

class PartyAnimal:
    x = 0
    
    def party(self):
        self.x = self.x + 1
        print "So far", self.x
    
an = PartyAnimal()
an.party()
an.party()
an.party()

print "Type", type(an)
print "Dir", dir(an)