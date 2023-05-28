# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""


##Section 10. The NumPy library

##Lecture 1. Introducing NumPy library
import numpy as np

#a simple numeric one-dimensional array
a = np.array([1, 2, 3])
a

type(a)

a.dtype

a.ndim

a.size

a.shape

#a two-dimensional array
b = np.array([[1.3, 2.4], [0.3, 4.1]])

b.dtype

b.ndim

b.size

b.shape












##Lecture 2. Creation of ndarray
import numpy as np

#list as argument in array() function
c = np.array([[1, 2, 3], [4, 5, 6]])
c

#The array() function, can accept tuples and sequences of tuples
d = np.array(((1, 2, 3), (4, 5, 6)))
d


e = np.array([(1, 2, 3), [4, 5, 6], (7, 8, 9)])
e


# ###  Types of data
#dtype for string
g = np.array([['a', 'b'], ['c', 'd']])
g


g.dtype


g.dtype.name


# ### The dtype Option

f = np.array([[1, 2, 3], [4, 5, 6]], dtype=complex)
f


# ### Intrinsic Creation of an Array 


np.zeros((3,3))


np.ones((2,3,4))


#sequence between 0 and 10, gap is 1
np.arange(0, 10)

#sequence between 4 and 10, gap is 1
np.arange(4, 10)


#gap is 3
np.arange(0, 12, 3)

#gap is 0.6
np.arange(0, 6, 0.6)


np.arange(0, 12).reshape(3, 4)


#5 values sequence equally distanced between 0 and 10
np.linspace(0, 10, 5)

#random number between 0 and 1
np.random.random(3)


np.random.random((3, 3))












# ## Lecture 3. Basic Operations of NumPy ndarray

# ### Arithmetic Operators
import numpy as np
a = np.arange(4)

a + 4

a * 2


b = np.arange(4, 8)
b

a + b


a * b

#operation with functions
a * np.sin(b)


a * np.sqrt(b)

#Multidimensional array operations

A = np.arange(0, 9).reshape(3, 3)

B = np.ones((3, 3))

A * B


# ### The Matrix Product (not element-wise)

np.dot(A, B)


A.dot(B)


np.dot(B, A)


# ### Increment and Decrement Operators

a = np.arange(4)

a += 1
a

a -= 1
a


a = np.arange(4)
a += 4
a

a *= 2
a


# #### Universal Functions (ufunc)


a = np.arange(1, 5)
a


np.sqrt(a)


np.log(a)


np.sin(a)


# ### Aggregate Functions

a = np.array([3.3, 4.5, 1.2, 5.7, 0.3])
a

a.sum()


a.min()

a.max()


a.mean()


a.std()















##Lecture 4. Indexing, Slicing, and Iterating of NumPy arrays
# ## Indexing, Slicing and Iterating

# ### Indexing

import numpy as np
a = np.arange(10, 16)
a

a[4]

a[-1]

a[-6]

a[[1, 3, 4]]


A = np.arange(10, 19).reshape((3, 3))
A

A[1, 2]


# ### Slicing
a = np.arange(10, 16)
a

a[1:5]      #second to the fifth element

a[1:5:2]    #array([11, 13])

a[::2]      #array([10, 12, 14])

a[:5:2]     #array([10, 12, 14])

a[:5:]      #array([10, 11, 12, 13, 14])

#two-dimensional array
A = np.arange(10, 19).reshape((3, 3))

A[0, :]     #first row

A[:, 0]     #first column


#array([[10, 11],
#      [13, 14]])
A[0:2, 0:2]

#If the indexes of the rows or columns to be extracted are 
#not contiguous
A[[0, 2], 0:2]


# ### Iterating an Array 

for i in a:
    print(i)

#for matrix, will get each row
for row in A:
    print(row)

#to iterate each element of a matrix
for item in A.flat:
    print(item)


np.apply_along_axis(np.mean, axis=0, arr=A)  #array([ 13., 14., 15.])


np.apply_along_axis(np.mean, axis=1, arr=A)  #array([ 11., 14., 17.])


def foo(x):
    return x/2


np.apply_along_axis(foo, axis=1, arr=A)

np.apply_along_axis(foo, axis=0, arr=A)


# ## Conditions and Boolean Arrays
A = np.random.random((4, 4))
A


A < 0.5


A[A < 0.5]

















##Lecture 5. Joining, Splitting and Shape Manipulation of NumPy arrays
# ## Shape Manipulation
import numpy as np

a = np.random.random(12)
a

A = a.reshape(3,4)
A


a.shape = (3, 4)
a

#convert a two-dimensional array into a one-dimensional array
a = a.ravel()
a

a = np.random.random(12).reshape(3,4)
a.shape = (12)
a


#transposing
A.transpose()


# ## Joining Arrays
#vstack() and hstack()
A = np.ones((3, 3))
B = np.zeros((3, 3))
np.vstack((A, B))

np.hstack((A, B))


#column_stack() and row_stack()
a = np.array([0, 1, 2])
b = np.array([3, 4, 5])
c = np.array([6, 7, 8])
np.column_stack((a, b, c))

np.row_stack((a, b, c))


# ### Splitting Arrays
#hsplit() and vsplit()
A = np.arange(16).reshape((4, 4))
A

[B, C] = np.hsplit(A, 2)
B
C


[B, C] = np.vsplit(A, 2)
B

C


#split()
[A1, A2, A3] = np.split(A, [1,3], axis=1)
A1

A2

A3


[A1, A2, A3] = np.split(A, [1, 3], axis=0)
A1

A2


A3






















# ## Lecture 6. Copies and Views, difference between NumPy arrays and Python lists

# ### Copies or Views of NumPy arrays
#assignment
import numpy as np
a = np.array([1, 2, 3, 4])
b = a
b


a[2] = 0
b


#slicing
c = a[0:2]
c

a[0] = 0
c

#use copy()
a = np.array([1, 2, 3, 4])
c = a.copy()
c


a[0] = 0
c

c=a.copy()


##Python lists
#assignment
a  = [1,2,3,4]
b = a

b.append(5)
a[1] = 10
b

a


#slicing
a = [1,2,3,4]
f = a[:3]

f

a

a[1] = 10
f.append(100)


#use copy()
a=[1,2,3,4]
c = a.copy()

a
c

a[1]=10
c.append(10)

a
c




























# ### Lecture 7. Broadcasting

import numpy as np
#add a matrix with a one-dimensioanl array
A = np.arange(16).reshape(4, 4)
b = np.arange(4)
A
b
A + b

#demean each column of an array by subtracting the column
#means.

arr = np.random.randn(4, 3)
arr.mean(0)
demeaned = arr - arr.mean(0)
demeaned
demeaned.mean(0)



#demean each row of an array by subtracting the row
#means, need to reshape first
arr
row_means = arr.mean(1)
row_means.shape
row_means.reshape((4, 1))
demeaned = arr - row_means.reshape((4, 1))  #need to reshape first
demeaned.mean(1)



## Broadcasting with higher dimensions
#using np.newaxis() function to reshape
arr = np.zeros((4, 4))
arr_3d = arr[:, np.newaxis, :]
arr_3d.shape
arr_1d = np.random.normal(size=3)
arr_1d[:, np.newaxis]       # (3,1)
arr_1d[np.newaxis, :]       # (1,3)


# In[ ]:

#If we had a three-dimensional array and wanted to 
#demean axis 2

arr = np.random.randn(3, 4, 5)
depth_means = arr.mean(2)
depth_means
depth_means.shape        # (3, 4)
demeaned = arr - depth_means[:, :, np.newaxis]
demeaned.mean(2)




























##lecture 8. Random number generation in Python and NumPy
#Generating random number in Python using random()
#generates a random float number between 0.0 and 1.0
import random
num = random.random()
print(num)


#Generating a random item using choice()
import random
 
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
 
# prints a random item from the string
string = "striver"
print(random.choice(string))


#TGenerating random numbers from a specified range and step 
#using randrange()
# using randrange() to generate in range from 20
# to 50. The last parameter 3 is step size to skip
# three numbers when selecting.
print(random.randrange(20, 50, 3))



#The seed function is used to save the state of a random 
#function so that it can generate same random numbers on 
#multiple executions
# using seed() to seed different random number
random.seed(7)
 
# printing mapped random number
print("The mapped random number with 7 is : ", end="")
print(random.random())
 
# using seed() to seed to 5 again
random.seed(5)
 
# printing mapped random number
print("The mapped random number with 5 is : ", end="")
print(random.random())

# using seed() to seed to 7 again
random.seed(7)
 
# printing mapped random number
print("The mapped random number with 7 is : ", end="")
print(random.random())



#Generating random number list in Python using shuffle()
import random
 
 
# declare a list
sample_list = ['A', 'B', 'C', 'D', 'E']
 
print("Original list : ")
print(sample_list)
 
# first shuffle
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)

# second shuffle
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)




#Generating random number list in Python using uniform()
#using uniform() to generate random floating number in range
# prints number between 5 and 10
print(random.uniform(5, 10))



##Random Number Generation with NumPy’s random module
#generate a 4 × 4 array of samples from the standard 
#normal distribution using normal()
import numpy as np
#standard normal distribution 
samples = np.random.normal(size=(4, 4))
samples

#normal distribution with mean 5 standard deviation 2
samples = np.random.normal(5,2,size=(4, 4))
samples


#set random seed()
np.random.seed(1234)
samples = np.random.normal(size=(4, 4))
samples


#standard normal also
np.random.randn(10)



# to shuffle an numpy array
import numpy as np
 
# Assign array
arr = np.array([1, 2, 3, 4, 5, 6])
 
# Display original array
print("Original array: ", arr)
 
# Shuffle array
np.random.shuffle(arr)
 
# Display shuffled array
print("Shuffled array: ", arr)



#numpy.random.permutation() method, to get the random samples 
#of sequence of permutation
#get the random sequence permutation of an array
import numpy as np
  
gfg = np.random.permutation(20)
gfg


#get the random sequence permutation of a 2-dimensional array
arr = np.arange(12).reshape((4, 3))
gfg = np.random.permutation(arr)
gfg






















# ## Lecture 9. Reading and Writing NumPy Array Data on Files
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory

# ### Loading and Saving Data in Binary Files
data = np.random.random(12)
data = data.reshape(4,3)
data


np.save('saved_data', data)


loaded_data = np.load('saved_data.npy')
loaded_data


# ### Reading File with Tabular Data using genfromtxt()

data = np.genfromtxt('tab_data.csv', delimiter=',', names=True)
data


data['id']


data[0]

#missing value
data = np.genfromtxt('tab_data_miss.csv', delimiter=',', names=True)
data


data['id']


data[0]
data[1]



#Reading File with Tabular Data using numpy.loadtxt( )
#numpy.loadtxt( ) is equivalent function to 
#numpy.genfromtxt( ) when no data is missing.
# Text file data converted to integer data type
File_data = np.loadtxt("number1.txt", dtype=int)
print(File_data)



# skipping first row
# converting file data to string
data = np.loadtxt("test_text_1.txt", skiprows=1, dtype='str')
print(data)


















### Lecture 10. Difference between reshape() and resize() method 
# for Numpy ndarray

# importing the module
import numpy as np 
    
# creating an array 
testarray = np.arange(0, 20) 
print("Original array:")
print(testarray)  
  
# using reshape()
print("Changed array")
print(testarray.reshape(4, 5)) 
    
print("Original array:")
print(testarray)


#Example 2: Using resize()

# importing the module
import numpy as np 
    
# creating an array 
testarray = np.arange(0, 20) 
print("Original array:")
print(testarray)
 
  
# using resize()
print("Changed array")
# this will print nothing as None is returned
testarray.resize(4, 5)
print(testarray.resize(4, 5)) 
    
print("Original array:")
print(testarray)






















# ## Linear Algebra with ndarray in Numpy

#matrix multiplication using dot()
import numpy as np
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
x
y
x.dot(y)

np.dot(x, y)


np.dot(x, np.ones(3))


#matrix multiplication using @
x @ np.ones(3)


#inverse matrix and matrix decomposition using numpy.linalg
from numpy.linalg import inv, qr
X = np.random.randn(5, 5)
mat = X.T.dot(X)
inv(mat)
mat.dot(inv(mat))


#Factor the matrix a as qr, where q is orthonormal and 
#r is upper-triangular
q, r = qr(mat)
r
q




