# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""



###String Format Manipulation in Python
#example
print("Please enter the amount of dollar")
money = eval(input("Dollars: "))
print("The total value of your change is ${0:0.2f}".format(money))

#The simplest template strings just specify where to 
#plug in the parameters.
#'Hello Mr. Smith, you may have won $10000'
print("Hello {0} {1}, you may have won ${2}".format("Mr.","Smith", 10000))



#control the width and/ or precision of a numeric value
#'This int,     7, was placed in a field of width 5'
print("This int, {0:5}, was placed in a field of width 5".format(7))


#'This float,       3.1416, has width 10 and precision 5'
print("This float, {0:10.5}, has width 10 and precision 5".format(3.1415926))


#'This float,       3.14159, is fixed at 5 decimal places'
print("This float, {0:10.5f}, is fixed at 5 decimal places".format(3.1415926))


#'This float, 3.1416, has width 0 and precision 5'
print("This float, {0:0.5}, has width 0 and precision 5".format(3.1415926))


#'Compare 3.14 and 3.1400000000000001243'
print("Compare {0} and {0:0.20}".format(3.14))




##Justification
#'left justification : Hi ! '
print(" leftjustification: {0:<10}".format("Hi !"))


#'right justification : Hi! '
print(" right justification:{0:>10}".format("Hi !"))


#'centered : Hi ! '
print("centered : {0:^5}".format("Hi!"))






















