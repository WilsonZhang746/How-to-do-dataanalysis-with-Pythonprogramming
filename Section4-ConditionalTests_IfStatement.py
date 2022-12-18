# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""

##Section 4 Conditional tests and If statement

##Lecture 1. Conditional tests
#an example
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
#Conditional Tests  
#Checking for Equality
car = 'bmw'
car == 'bmw'

car = 'audi'
car == 'bmw'

#Ignoring Case When Checking for Equality
car = 'Audi'
car == 'audi'     #False

car = 'Audi'
car.lower() == 'audi'    #True

car = 'Audi'
car.lower() == 'audi'  #The lower() function doesn’t change the value that was originally stored in car
car

#Checking for Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    
#Numerical Comparisons
age = 18
age == 18 	#True
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
age < 21	#True
age <= 21	#True
age > 21	#False
age >= 21	#False

#use and to check multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21      #False
age_1 = 22
age_0 >= 21 and age_1 >= 21      #True

#Using or to Check Multiple Conditions
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21      #True
age_0 = 18
age_0 >= 21 or age_1 >= 21      #False

#Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings     #True
'pepperoni' in requested_toppings     #False

#Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")






#Lecture 2.If Statements
#simple If statement
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")


#if-else Statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    
#The if-elif-else Chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
    

#Omitting the else Block
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")









##Lecture 3.Using if Statements with Lists

#Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


#pizzeria runs out of green peppers
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


#Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")



#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
        
print("\nFinished making your pizza!")


