# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""

##Section 9. Files and Exceptions
##Lecture 1. Reading from a File
#Reading an Entire File
#opens file pi_digits.txt, reads it, and prints the contents
#of the file to the screen:
with open('pi_digits.txt') as file_object:
     contents = file_object.read()
     print(contents.rstrip())
     
#use a relative file path
with open('test\\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    
#use an absolute file path 
file_path = 'd:\\test\\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

    
#Reading Line by Line
#Reading Line by Line    
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

    
#remove extra blank lines
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip()) 

    
#Making a List of Lines from a File
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())  
    

#Working with a File’s Contents
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))



#get rid of whitespace at the left side of digits
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()    #use strip here 

print(pi_string)
print(len(pi_string))



#Large Files: One Million Digits
#print just the first 50 decimal places
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))




#Is Your Birthday Contained in Pi?
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


    
    



##Lecture 2. Writing to a File
#Writing to an Empty File
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming")
    
    
#Writing Multiple Lines
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    

#Appending to a File
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")







##Lecture 3. Using try-except Blocks Exception
#Handling zero-division error
print(5/0)

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

    
    
#Using Exceptions to Prevent Crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

#a loop never stopped unless with q
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
        
        
        
        
        
        
        
        
        
        
##Lecture 4. Handling the FileNotFoundError Exception
#try to open and read a file which has not been saved in the
#current working directory
#FileNotFoundError
filename = 'alice1.txt'
with open(filename) as f_obj:
    contents = f_obj.read()
 
    
#Use a try-except block instead
filename = 'alice1.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
    

#analyze text with try-except-else block    
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
    


#Create a function holding try-except-else block
#working with multiple books
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read() 
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha1.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


    

    
    


##Lecture 5. Using Try, Except, else and Finally in Python
#Try, Except, else and Finally
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally: 
        # this block is always executed  
        # regardless of exception generation. 
        print('This is always executed')  
        
# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)      



#Failing Silently with pass
#Failing Silently and do nothing with error
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read() 
    except FileNotFoundError:
        pass
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha1.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)  

    

    
    


##Lecture 6. Storing Data using json() module
#stores a set of numbers using json()

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)


#reads these numbers back into memory
import json

filename = 'numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)
    
print(numbers)





#Saving and Reading User-Generated Data
#storing the user’s name
import json

username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")



#greets a user whose name has already been stored:
import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")







##Lecture 7. Refactoring
#a function includes storing, getting and greeting user. 
import json

def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")


greet_user()





#moving the code for retrieving a stored username to a 
#separate function get_stored_username(), and moving
#the part of get new user to another function get_new_username():
    
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




















     

     

     
