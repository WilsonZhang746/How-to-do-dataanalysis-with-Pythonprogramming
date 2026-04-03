# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""

##Section 5. Dictionaries

#Lecture 1. Working with dictionaries
#A simple example of dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


#Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


#Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Figure out how far to move the alien based on its speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New position: " + str(alien_0['x_position']))

#Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)













#Lecture 2. Looping Through a Dictionary
#Looping Through All Key-Value Pairs
user_0 = {'username': 'efermi',
          'first': 'enrico',
          'last': 'fermi',
          }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


#A Dictionary of favorite programming languages for a number of people
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

#Looping Through All the Keys in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
 
for name in favorite_languages.keys():
    print(name.title())


#access the value associated with any key you care about inside the loop
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
        

#use the keys() method to find out if a particular person was polled
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    

#Looping Through a Dictionary’s Keys in Order
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#Looping Through All Values in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())















##Lecture 3. Nesting dictionaries
#A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
    
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
    print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

#to change the first three aliens to yellow, medium-speed aliens 
#worth 10 points each
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        

#A List in a Dictionary
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
    

#A List in a Dictionary
favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
        }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
        
        
#A Dictionary in a Dictionary
users = {'aeinstein': {'first': 'albert',
                       'last': 'einstein',
                       'location': 'princeton'},
         'mcurie': {'first': 'marie',
                    'last': 'curie',
                    'location': 'paris'},
         }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
        

        
    










##Lecture 4. Using a while Loop with Dictionaries
#Filling a Dictionary with User Input
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the response in the dictionary:
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
    













### Lecture 5. get() method

d = {'Wilson': 32, 'Dudu': 20, 'Maomao': 22}
print(d.get('Wilson'))


#Python get() Method with default parameter.

d = {'Wilson': 32, 'Dudu': 20, 'Maomao': 22}
# since 4 is not in keys, it'll print "Not found"
print(d.get('Mia', "Not found"))



## using nested get()

test_dict = {'Wilson': {'Age': 32, 'Gender': 'male'},  'Dudu': {'Age': 20, 'Gender': 'male'}, 'Maomao': {'Age': 22, 'Gender': 'male'}}

res = test_dict.get('Wilson', {}).get('Age')

res


### Sort a list of dictionaries

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


#using dictionary's get method to sort by Age
dicts_lists.sort(key=lambda item: item.get("Age"))

dicts_lists




#Difference Between Python Dictionary get() method and dict[key]
# Using get() to get the value as a None
course={'language': 'python', 'fee': 4000}
print('duration:', course.get('duration'))



# Use dict[key], key is not in the dictionary
course={'language': 'python', 'fee': 4000}
print('duration:',course['duration'])









### Dictionary Comprehensions	
#simplest form

#{ key_expression : value_expression for expression in iterable }

# Creating a dictionary of squares:
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num**2 for num in numbers}
print(squares_dict)



#We are running a loop over each of the seven letters in 
#the string 'letters' and counting how many times that letter appears.
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}

letter_counts


#to avoid counting twice
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
letter_counts



#Filtering elements during dictionary creation:
    
words = ["apple", "banana", "cherry", "date"]
long_words_dict = {word: len(word) for word in words if len(word) > 5}
print(long_words_dict)



#Transforming existing dictionary items:
original_dict = {"apple": 1, "banana": 2, "cherry": 3}
transformed_dict = {key.upper(): value * 10 for key, value in original_dict.items()}
print(transformed_dict)    












### Gather Keyword Arguments with **		

#You can use two asterisks (**) to group keyword arguments 
#into a dictionary, where the argument names are the keys, 
#and their values are the corresponding dictionary values.

#The following example defines the function print_kwargs() 
#to print its keyword arguments:
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


#The **kwargs syntax in Python allows a function to accept an 
#arbitrary number of keyword arguments. These arguments are 
#collected into a dictionary within the function, where the 
#keys are the argument names and the values are the 
#corresponding argument values.
#Here is an example demonstrating the use of **kwargs:
    
def print_user_details(**kwargs):
    """
    Prints user details passed as keyword arguments.
    """
    print("User Details:")
    for key, value in kwargs.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

# Calling the function with various keyword arguments
print_user_details(name="Alice", age=30, city="New York")

print("\n---")

print_user_details(first_name="Bob", last_name="Smith", email="bob.smith@example.com", occupation="Engineer")









### Handle Missing Keys with setdefault() and defaultdict()

#Using the dictionary get() function to return a default 
#value avoids an exception. 
#The setdefault() function is like get(), but also assigns 
#an item to the dictionary if the key is missing:
    
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)   


#If the key was not already in the dictionary, 
#the new value is used:
carbon = periodic_table.setdefault('Carbon', 12)
carbon 

periodic_table

#If we try to assign a different default value to an 
#existing key, the original value is returned
#and nothing is changed:
    
    
helium = periodic_table.setdefault('Helium', 947)
helium
    
    
periodic_table

#defaultdict() is similar, but specifies the default 
#value for any new key up front, when
#the dictionary is created.
#we can pass the function int, which will be called as 
#int() and return the integer 0:
    
from collections import defaultdict
periodic_table = defaultdict(int)

#Now, any missing value will be an integer (int), 
#with the value 0:
    
periodic_table['Hydrogen'] = 1
periodic_table['Lead']

periodic_table

#In the following example, no_idea() is a function,  executed 
#to return a value when needed:
    

from collections import defaultdict

def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
bestiary['A']
bestiary['B']

bestiary['C']


#By the way, you can use lambda to define your default-
#making function right inside the call:
bestiary = defaultdict(lambda: 'Huh?')

bestiary['E']

#Using int is one way to make your own counter:

from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)
    

#if food_counter had been a normal dictionary instead of a
#defaultdict, Python would have raised an exception every
# time we tried to increment the dictionary element 
#food_counter[food] because it would not have been initialized.
#We would have needed to do some extra work, as shown here:

dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1

for food, count in dict_counter.items():
    print(food, count)













### Count Items with Counter()

from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
breakfast_counter

#The most_common() function returns all elements in 
#descending order

breakfast_counter.most_common()

breakfast_counter.most_common(1)


#You can combine counters

breakfast_counter


#we’ll make a new list called lunch, and a counter 
#called lunch_counter


lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
lunch_counter

#we combine the two counters is by addition, using +:
    
breakfast_counter + lunch_counter


#you subtract one counter from another by using -.

breakfast_counter - lunch_counter


lunch_counter - breakfast_counter

#common items by using the intersection operator &:

breakfast_counter & lunch_counter

#you can get all items by using the union operator |:
    
breakfast_counter | lunch_counter

















