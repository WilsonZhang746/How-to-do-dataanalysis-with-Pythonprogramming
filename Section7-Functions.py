# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@python32
"""

##Section 7. Functions

##Lecture 1. Defining a function
#Defining a simple Function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()


#Passing Information to a Function
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
    
greet_user('jesse')

greet_user('Wilson')














##Lecture 2.  Passing arguments to function
#Example of pets type and its name
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#Positional Arguments
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#Keyword Arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


#Default Values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')


# Equivalent calls
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

#A hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')












##Lecture 3. Functions: Returning a Simple Value
#a function that takes a first and last name, and returns 
#a neatly formatted full name
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


#Making an Argument Optional
#A first attempt to include middle names might look like this:
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' +  middle_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)



#A better solution is to to make the middle name optional. 
#We can give the middle_name argument an empty default value 
#and ignore the argument unless the user provides a value:
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' +  middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)















##Lecture 4. Functions: Return a Dictionary
#returns a dictionary representing a person
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)



#Returning a Dictionary,'age' as optional
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)















##Lecture 5. Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
    













##Lecture 6. Passing a List to function
#Passing a List of names to a function called greet_users(),
#which greets each person in the list individually
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)



#Modifying a List in a Function
#does this without using functions
# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    

#Modifying a List in a Function, using 2 functions    
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
    
        # Simulate creating a 3d print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
        
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
unprinted_designs  #empty now


#If you do not want to modify the original list
#You can use a copy of a list when you are calling the function
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
unprinted_designs      #not modified











#Lecture 7. Passing an arbitrary number of arguments to function
#Passing an Arbitrary Number of Arguments to Function
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


#replace the print statement with a loop that runs through
#the list of toppings and describes the pizza being ordered
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
        
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')




#Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')




#Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)















##Lecture 8. Storing Your Functions in Modules
#Importing an Entire Module
#A module file pizza.py, saved in the same directory as this 
#source file in your computer.
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory

#Now we can import the module pizza we just created and 
#then makes two calls to make_pizza():      
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



#Importing Specific Functions
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, "mushrooms", "green peppers", "extra cheese")


#Using as to Give a Function an Alias
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


#Using as to Give a Module an Alias
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


#Importing All Functions in a Module
#*** just know this form if you see another code 
#best not use this form, however
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

















### Lecture 9. Map() function

# Return double of n
def summation(n):
    return n + n
 
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(summation, numbers)
print(list(result))


# Double all numbers using map and lambda
 
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))



# Add two lists using map and lambda
 
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
 
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))



# List of strings
lst = ['sat', 'bat', 'cat', 'mat']
 
# map() can listify the list of strings individually
test = list(map(list, lst))
print(test)




# Define a function that doubles even numbers and leaves odd 
#numbers as is
def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num
 
# Create a list of numbers to apply the function to
numbers = [1, 2, 3, 4, 5]
 
# Use map to apply the function to each element in the list
result = list(map(double_even, numbers))
 
# Print the result
print(result)  # [1, 4, 3, 8, 5]

















### Lecture 10. Lambda function

# A simple regular user-defined function, and its lambda function
#alternative

def f_square(x):
    return x**2

f_square(10)


lambda x: x**2

(lambda x: x**2)(10)

result= lambda x: x**2

result(10)


#A lambda function which contains simple conditional test.
calc = lambda num: "Odd number" if num % 2 != 0 else "Even number"
 
print(calc(20))
print(calc(19))



# Invoking lambda return value to perform various string operations
concate = lambda s: ''.join([char for char in s if not char.isdigit()])
print("filter_nums():", concate("Wilson32"))
 
do_exclaim = lambda s: s + '!'
print("do_exclaim():", do_exclaim("I like programming"))
 
find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(301301))
















### Lecture 11. Lambda and Map, Filter

#The lambda function gets more helpful when used inside a function.
#We can use lambda function inside map(), filter(), sorted() 
#and many other functions.

lst = ["23", "32", "56", "0", "-3", "-18"]
# sort list[str] numerically using sorted()
# and custom sorting key using lambda
print("Sorted numerically:",
      sorted(lst, key=lambda x: int(x)))
 
# filter positive even numbers
# using filter() and lambda function
print("Positive even numbers have been excluded:",
      list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), lst)))
 
# added 10 to each item after type and
# casting to int, then convert items to string again
print("Operation on each item using lambda and map()",
      list(map(lambda x: str(int(x) + 10), lst)))
























### Lecture 12. partial() function
from functools import partial

#example 1
  
# A normal function
def f(x1, x2, x3):
    return x1*2 + x2**2  + x3/2
  
# A partial function that calls f with
# x1 as 32, x2 as 22.
g = partial(f, 32,22)
  
# Calling g()
#Since we have pre-filled our function with some constant values
# of x1, x2. And g() just takes a single argument i.e. the variable x3.
print(g(20))



#Example 2

# A normal function
def add(x1, x2, x3):
    return 32 * x1 + 22 * x2 + x3
  
# A partial function with b = 1 and c = 2
add_part = partial(add, x3 = 20, x2 = 22)
  
# Calling partial function
#Since we have pre-filled our function with some constant values
# of x3, x2. And add_part() just takes a single argument i.e. 
#the variable x1.
print(add_part(32))














