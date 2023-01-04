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


    

    
    


    

    
    

























     

     

     
