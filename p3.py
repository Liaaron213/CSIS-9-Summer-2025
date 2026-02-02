# input.py
# Aaron Li
# 06/03/2025
# Python 3.13.3
# Description: Program to take input in Python

name = input ("Please put your name: ") # input for name  
weightLbs = float(input("Please enter your weight in lbs: ")) # input for weightLbs variable will be a float
age = int(input ("Please enter your age (whole number): ")) # input for weightLbs variable must be an integer
weightKg = weightLbs*0.453592 # conversion of lbs to kg 
title = "Human" # Human is a string for the variable, title

print ("Hello", title, name, "your weight is") # results of the inputs are printed in these four lines
print (weightLbs, "lbs")
print ("which equals = %.2f" %weightKg, end=' ')
print ("kilograms ")

'''
>>>
====== RESTART: C:\Users\liaar\OneDrive\Documents\CSIS9 Assignments\p3.py ======
Please put your name: Aaron Li
Please enter your weight in lbs: 195
Please enter your age (whole number): 22
Hello Human Aaron Li your weight is
195.0 lbs
which equals = 88.45 kilograms 
>>>
'''

