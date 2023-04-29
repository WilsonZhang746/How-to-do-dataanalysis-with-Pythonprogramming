# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""




### Section 17. Python data processing examples


## Example 1. Concatenate Multiple Text Files in to one object
import os
os.getcwd()    #gettinh current working directory
#Setting new working directory
work_path="d:\\Pythondemo"
os.chdir(work_path)      #setting new working directory
os.getcwd()


import glob

# Load all txt files in path
demofiles = glob.glob('.\\*.txt')
demofiles

# Concatenate files to new file
with open('demo_output.txt', 'w') as out_file:
    for file in demofiles:
        with open(file) as from_file:
            out_file.write(from_file.read())
            out_file.write("\n")

# Read file and print
with open('demo_output.txt', 'r') as new_file:
    lines = [line.strip() for line in new_file]
for line in lines: print(line)



















#Example 2. Check if a Substring is Present in a Given String


#Method 1: using the if… in

lstring = "I like both programming language Python and R"
 
if "like" in lstring:
    print("The string is present")
else:
    print("The is not present")





#Method 2: using the split() method
#First split the given string into words and store them in a variable
#then using the if condition

lstring = "I like both programming language Python and R"
sstring = "Python"  
 
# splitting words in a given string
s = lstring.split()
 
# checking condition

if sstring in s:
    print("yes")
else:
    print("no")




#Method3: using the find() method
#inbuilt function find() which checks if a substring is present 
#in the string, which is done in one line. 
#find() function returns -1 if it is not found, 
#else it returns the first occurrence

def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")
 
 
# driver code
lstring = "I like both programming language Python and R"
sstring = "Python" 
check(lstring, sstring)




#Method 4: using “count()” method
#count the number of occurrences of substring in a string
#If the substring is found then “yes ” will print otherwise “no will be printed”.

def check(string, substring):
    if (string.count(substring) > 0):
        print("YES")
    else:
        print("NO")
 
 
lstring = "I like both programming language Python and R"
sstring = "Python" 
check(lstring, sstring)




#Method 5: using regular expressions 
#RegEx can be used to check if a string contains the specified 
#search pattern. Python has a built-in package called re, 
#which can be used to work with Regular Expressions.

import re
 
lstring = "I like both programming language Python and R"
sstring = "Python" 
 
# re.search() returns a Match object
# if there is a match anywhere in the string
if re.search(sstring, lstring):
    print("YES,string '{0}' is present in string '{1}'" .format(
        sstring, lstring))
else:
    print("NO,string '{0}' is not present in string '{1}' " .format(
        sstring, lstring))












 





