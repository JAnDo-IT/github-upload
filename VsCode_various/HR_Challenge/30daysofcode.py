# Day 1: Data Types
i = 4
d = 4.0
s = "HackerRank "
# Declare second integer, double, and String variables.
ii = int (5)
dd = float(5.0)
ss = str(" HR2 ")

# Read and save an integer, double, and String to your variables.
#ii = int(input(" int value: "))
#dd = float(input(" double value: "))
#ss = str(input(" string value: "))
#In the Test output is printed should
ii = int(input())
dd = float(input())
ss = str(input())

#print()

#print (ii)
#print("{0:.1f}".format(dd))
#print(ss)

# Print the sum of both integer variables on a new line.
sumi = i + ii
print(sumi)

# Print the sum of the double variables on a new line.
sumd = d + dd
print("{0:.1f}".format(sumd))

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+ss)

#optional
#sums = s + ss
#print(sums)

###### Day 2 Operators
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    mTip = meal_cost*(tip_percent/100)
    mTax = meal_cost*(tax_percent/100)
    mealTotal = meal_cost + mTip + mTax
    total = round(mealTotal)
    print(total)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

## Day3 Conditionals
import math
import os
import random
import re
import sys

#n=-100
def sConditional(n):
    # print("Ok: " + str(n))
    if (n%2 != 0):
        print("Weird")
    elif (n%2 == 0): #Checking only once
        if (n>=2 and n<=5):
            print("Not Weird")
        elif (n>=6 and n<=20):
            print("Weird")        
        elif (n>20):
            print("Not Weird")
        else:
            pass
    else:
        print("Not evaluated")

if __name__ == "__main__":
    N = int(input())
    if N>= 1 and N<=100:
        sConditional(N)
    else:
        print("value not in range: try again")

# Day4 - Class vs. Instance
class Person:
    age=0
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge<0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        elif initialAge<=30:
            self.age = initialAge
        else:
            print("age out of range")

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        age = self.age
        if age < 13:
            print("You are young.")
        elif (age >= 13 and age < 18) :
            print("You are a teenager.")
        else:
            print("You are old.")
    
    def yearPasses(self):
        # Increment the age of the person in here
        self.age+=1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

