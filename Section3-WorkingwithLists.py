# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""

##Section 3 Working with Lists

##Lecture 1. Introducing lists
Numberlist = [1,2,3,4,5] 


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accessing Elements in a List
print(bicycles[0])
print(bicycles[0].title())  #combined with string method

#index start from 0
print(bicycles[1])    #second item
print(bicycles[3])    #fourth item
print(bicycles[-1])      #access the last item in a list
print(bicycles[-2]) #the second item from the end of the list

#Using Individual Values from a List
message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)



##Lecture 2. Changing, Appending,Removing items of Lists
#Changing elements of a list
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#append items into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#append items into a list, starting with an empty list
motorcycles = []           #start with an empty list
motorcycles.append('honda')     
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#insert element into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')    
print(motorcycles)

#remove item from a list
#Removing an Item according to its position Using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]  #first item removed 
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]      #second item removed  
print(motorcycles)


#Removing an Item Using the pop() Method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#Popping Items from any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")



##Lecture 3. Organizing lists
#Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse alphabetical list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)


#Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)


#Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)




##Lecture 4. Looping Through a List
#Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)        #need tab indent here
    

#Doing More Work Within a for Loop
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!")  
    print("I can't wait to see your next trick, " + magician.title() + ".\n")     
    
print("Thank you everyone, that was a great magic show!")




##lecture 5. Making Numerical Lists
#Using the range() Function
for value in range(1,5):
    print(value)

#Using range() to Make a List of Numbers
#using list() to make a list
numbers = list(range(1,6)) 
print(numbers) 


#list the even numbers between 1 and 10
even_numbers = list(range(2,11,2)) 
print(even_numbers)


#using append()
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    
print(squares)

#To write this code more concisely
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)



##Lecture 6. List comprehension and Working with Part of a List
#List comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

#Working with Part of a List
#Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])         #return first three elements
print(players[1:4])         #return second ,third,fourth element
print(players[:4])      #automatically starts your slice at the beginning of the list
print(players[2:])      #slice that includes the end of a list
print(players[-3:])    #the last three players

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
#copying a list
#if you copy a list, must use slice form
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]     #useing slice form to copy a list

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#To prove that we actually have two separate lists
my_foods.append('cannoli') 
friend_foods.append('ice cream') 

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


#using this form if to connect two list, then append item into one list
#will also do for the other
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


##Lecture 7. tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#change one of the items in the tuple
dimensions = (200, 50)
dimensions[0] = 250

#looping over all values in a tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
#Writing over a Tuple   
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)















