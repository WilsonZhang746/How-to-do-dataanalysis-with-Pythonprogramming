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












### Example 3. Concatenate Multiple CSV Files Into a DataFrame

#We first get a list of the CSV files in our path; then, 
#for each file in the path, we read the contents into its 
#own dataframe; afterwards, we combine all dataframes into 
#a single frame; finally, we print out the results to inspect.

import os
os.getcwd()    #gettinh current working directory
#Setting new working directory
work_path="d:\\Pythondemo"
os.chdir(work_path)      #setting new working directory
os.getcwd()


import glob
import pandas as pd


# Load all txt files in path
demofiles = glob.glob('.\\*.csv')
demofiles      

# Create a list of dataframe, one series per CSV
full_list = []
for file_name in demofiles:
    df = pd.read_csv(file_name, index_col=None, header=None)
    full_list.append(df)

# Create combined frame out of list of individual frames
full_frame = pd.concat(full_list, axis=0, ignore_index=True)

print(full_frame)






 








### Example 4. Zip & Unzip Files with Pandas
import os
os.getcwd()    #gettinh current working directory
#Setting new working directory
work_path="d:\\Pythondemo"
os.chdir(work_path)      #setting new working directory
os.getcwd()
import pandas as pd

# Create a dataframe
df = pd.DataFrame({'object': ['ball', 'pen', 'paper'],
	           'price': ['10', '5', '2'],
		   'color': ['blue', 'green', 'white']})

# Compress and save dataframe to file
df.to_csv('savedfile.csv.zip', index=False, compression='zip')
print('Dataframe compressed and saved to file')

# Read compressed zip file into dataframe
df_unzipped = pd.read_csv('savedfile.csv.zip',)
print(df_unzipped)
















### Example 5. Merge two lists into a dictionary

listA = ['Wilson', 'Dudu', 'Mico', 'Miaomiao', 'Wilson']
listB = [32, 20, 7, 10, 69]

#There are 3 ways to convert these two lists into a dictionary

#1- Using Python's zip, dict functionz
dict_1 = dict(zip(listA, listB))

dict_1

#2- Using the zip function with dictionary comprehensions
dict_2 = {key:value for key, value in zip(listA, listB)}

dict_2

#3- Using the zip function with a loop
items_tuples = zip(listA, listB) 
dict_3 = {} 
for key, value in items_tuples: 
    if key in dict_3: 
        pass # To avoid repeating keys.
    else: 
        dict_3[key] = value

dict_3















### Example 6. Merge two or more lists into a list of lists

#task is when we have two or more lists, and we want to collect 
#them all in one big list of lists, where all the first element (list)
#in the resulting list come from all the first elements from input
#lists, and so on. 

#For example, if I have 4 lists [1,2,3], [‘a’,’b’,’c’], [‘h’,’e’,’y’] 
#and [4,5,6] ,and we want to make a new list of those four lists; 
#it will be [[1,’a’,’h’,4], [2,’b’,’e’,5], [3,’c’,’y’,6]].



def merge(*args, missing_val = None):
    """missing_val will be used when one of the smaller lists is 
       shorter than the others.
       Get the maximum length within the smaller lists."""
    
    max_length = max([len(lst) for lst in args])
    outList = []
    for i in range(max_length):
        result = []
        for k in range(len(args)):
            if i < len(args[k]):
                result.append(args[k][i])
            else:
                result.append(missing_val)
        outList.append(result)
 
    return outList


testlistA = ["Wilson", "Dudu", "Maomao", "Miaomiao", "Mico", "Mia"]
testlistB = [32, 20, 22, 10, 7]

testlistC = merge(testlistA, testlistB)

testlistC



#Alternative code, more concise, for more experienced people
def merge(*args, missing_val = None):
    """ missing_val will be used when one of the smaller lists is shorter tham the others.
        Get the maximum length within the smaller lists."""
    max_length = max([len(lst) for lst in args])
    outList = []
    for i in range(max_length):
        result = []
        result.append([args[k][i] if i < len(args[k]) else missing_val for k in range(len(args))])
        outList.append(result)
    
    return outList



# use zip, result is list of tupoes, and length is the length of 
#the shortest input list
list(zip(testlistA, testlistB))












### Example 7. Sort a list of dictionaries

dicts_lists = [
  {
    "Name": "Wilson",
    "Age": 32,
  },
  {
     "Name": "Dudu",
     "Age": 20,
  },
  {
    "Name": "Maomao",
    "Age": 22,
  }
]

#There are different ways to sort that list
#1- Using the sort/ sorted function based on the age
#using dictionary's get method
dicts_lists.sort(key=lambda item: item.get("Age"))

dicts_lists

#2- Using itemgetter module based on name
from operator import itemgetter

dicts_lists = [
  {
    "Name": "Wilson",
    "Age": 32,
  },
  {
     "Name": "Dudu",
     "Age": 20,
  },
  {
    "Name": "Maomao",
    "Age": 22,
  }
]

sortkey = itemgetter('Name')
dicts_lists.sort(key=sortkey)

dicts_lists



















### Example 8. Sort a list based on another list

a = ['Wilson', 'Dudu', 'Maomao', 'Mico', 'MiaoMiao', 'Mia']
b = [32, 12, 25, 41, 18,69]

#simplest method
[x for _, x in sorted(zip(b, a))]

#Use list comprehensions to sort these lists
#zip the two lists.
#create a new, sorted list based on the zip using sorted().
#using a list comprehension extract the first elements of each pair from the sorted, zipped list.

sortedList =  [val for (_, val) in sorted(zip(b, a), key=lambda x: \
          x[0])]


sortedList














### Example 9. Removing unwanted characters from string

#Removing symbol from string using str.isalnum()

#isalnum() method checks whether all the characters in a 
#given string are alphanumeric or not

string = "Wi;lson * an:d ! Mi;co1 * a*n:d ! Mi:ao2:"
 
test_str = ''.join(letter for letter in string if letter.isalnum())
print(test_str)


#Removing symbol from string using replace() 
#str.replace() inside a loop can check for a bad_char and 
#then replace it with the empty string hence removing it. 

# initializing bad_chars_list
remove_chars = [';', ':', '!', "*", " "]
 
# initializing test string
test_string = "Wil;son * a:nd ! Mi;co * and*Mi:ao !"
 
# printing original string
print("Original String : " + test_string)
 
# using replace() to
# remove bad_chars
for i in remove_chars:
    test_string = test_string.replace(i, '')
 
# printing resultant string
print("Resultant list is : " + str(test_string))


def remove_char(inputstring, badstring):
    """Remove unwanted string from inputstring"""
    for i in badstring:
        inputstring = inputstring.replace(i, '')
    return inputstring

remove_char(test_string,remove_chars)


#Removing symbol from string using join() + generator

#By using Python join() we remake the string. 
#In the generator function, we specify the logic to ignore 
#the characters in bad_chars and hence construct a new 
#string free from bad characters.

# initializing bad_chars_list
bad_chars = [';', ':', '!', "*", " "]
 
# initializing test string
test_string = "Wil;son * a:nd ! Mi;co * Mi*ao:miao !"
 
# printing original string
print("Original String : " + test_string)
 
# using join() + generator to
# remove bad_chars
test_string = ''.join(i for i in test_string if not i in bad_chars)
 
# printing resultant string
print("Resultant list is : " + str(test_string))



































