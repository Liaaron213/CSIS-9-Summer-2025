# output.py
# Aaron Li
# 06/02/2025
# Python 3.13.3
# Decription: Program to show output in Python

print('hello world') # single quote
print("hello world") # double quote
print ("he\nllo") # \n casues an insertion of a new line

# VARIABLES are named storage locations for numbers, strings, and lists
# STRING is anything enclosed in quotes; Example: "Hello world"
# NUMBER can either be FLOAT (eX: 9.3) or an INTEGER (Ex: 9.0)
# LISTS are things like [1,2,3] or ["Aaron", "Li"] 

myName = "Aaron" # myName is a variable of the string "Aaron"
Weight = 195 # Weight is a variable of the string "195"
Age = 22 # Age is a variable of the string "22"
Grades = [80, 96, 86] # Here, Grades is a list of integer values of my grades
nameZ = ["Aaron", "Li"] # List depicting my name 

print ("Hello", myName) # myName variable is outputted here 
print ("Your weight is", Weight, "and your age is", Age) # Weight and Age variables are outputted here 
print ("Your weight is %.2f and your age is %i" %(Weight,Age)) #weight and age shown as integers    
print ("Lists: grades =",Grades,"nameZ=",nameZ) # output of grades and name lists
print ("This is how you print", end=' ') 
print ("on the same line") # this string is for the "end" in the previous line

'''
>>>
====== RESTART: C:\Users\liaar\OneDrive\Documents\CSIS9 Assignments\p1.py ======
hello world
hello world
he
llo
Hello Aaron
Your weight is 195 and your age is 22
Your weight is 195.00 and your age is 22
Lists: grades = [80, 96, 86] nameZ= ['Aaron', 'Li']
This is how you print on the same line
>>>
'''



