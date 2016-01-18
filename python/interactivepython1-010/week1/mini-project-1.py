# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 20:32:25 2016

@author: anupam.srivastava
"""

# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "<" + name, "is not a correct name>"
        return None


def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "<%s is not a correct number>" % number
        return None

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print
    # print out the message for the player's choice
    print "Player chooses", player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    if player_number == None:
        return
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses", comp_choice
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if diff == 0:
        print "Player and computer tie!"
    elif diff > 2:
        print "Player wins!"
    else:
        print "Computer wins!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

#def p(x):
#    for i in range(0, 5):
#        if i != x:
#            diff = (i - x) % 5
#            print "(", i, "-", x, ") % 5 =", i - x, "% 5 =", diff, diff > 2            
#    print "---"
#
#p(0)
#p(1)
#p(2)
#p(3)
#p(4)