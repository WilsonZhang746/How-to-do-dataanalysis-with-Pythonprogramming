# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
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
    














































