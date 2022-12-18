# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 22:14:40 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""
##Section 2 Variables and simple data types

##Lecture 1. String Variables
message = "Hello Python world!"
print(message)

#single and double quotes
message = 'I told my friend, "Python is my favorite language!"'
print(message)


#Changing Case in a String with Methods
name = "ada lovelace"
print(name.title())     #each word's first letter er capitalized

name = "Ada Lovelace"
print(name.upper())     #all letters are uppercase
print(name.lower())     #all letter are lowercase


#Combining or Concatenating Strings:
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)

#Adding Whitespace to Strings with Tabs or Newlines
print("Python")
print("\tPython")    #add tab space

print("Languages:\nPython\nC\nJavaScript")   #new line
print("Languages:\n\tPython\n\tC\n\tJavaScript")  #newline and tab


#Stripping Whitespace
favorite_language = 'python '
favorite_language

favorite_language.rstrip()   #rightside whitespace removed temporarily
favorite_language

#To remove the whitespace from the string permanently, you have to
#store the stripped value back into the variable
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
favorite_language


favorite_language = ' python '
favorite_language.lstrip()    ##remove whitespace at left side
favorite_language.strip()     #remove whitespace at both side



##lecture 2. Numbers
3 ** 2      #exponents
10 % 3      #modulo

#Avoiding Type Errors with the str() Function
age = 23
message = "Happy " + str(age) + "rd Birthday!"

print(message)























