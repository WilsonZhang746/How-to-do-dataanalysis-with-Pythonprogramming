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

# ### Copies or Views of Objects

# In[3]:


a = np.array([1, 2, 3, 4])
b = a
b


# In[4]:


a[2] = 0
b


# In[6]:


c = a[0:2]
c


# In[7]:


a[0] = 0
c


# In[8]:


a = np.array([1, 2, 3, 4])
c = a.copy()
c


# In[9]:


a[0] = 0
c


# ### Broadcasting

# In[10]:


A = np.arange(16).reshape(4, 4)
b = np.arange(4)
A


# In[11]:


b


# In[12]:


A + b


# In[13]:


m = np.arange(6).reshape(3, 1, 2)
n = np.arange(6).reshape(3, 2, 1)
m


# In[14]:


n


# In[15]:


m + n


# In[16]:


structured = np.array([(1, 'First', 0.5, 1+2j),(2, 'Second', 1.3, 2-2j),
                      (3, 'Third', 0.8, 1+3j)],dtype=('i2, a6, f4, c8'))
structured


# In[17]:


structured = np.array([(1, 'First', 0.5, 1+2j),(2, 'Second', 1.3, 2-2j),
                      (3, 'Third', 0.8, 1+3j)],dtype=('int16, a6, float32, complex64'))
structured


# In[18]:


structured['f1']


# In[19]:


structured = np.array([(1, 'First', 0.5, 1+2j),(2, 'Second', 1.3, 2-2j),(3, 'Third', 0.8, 1+3j)],
                      dtype=[('id', 'i2'),('position','a6'),('value','f4'),('complex','c8')])
structured


# In[20]:


structured.dtype.names = ('id','order','value','complex')


# In[21]:


structured['order']


# ## Reading and Writing Array Data on Files

# ### Loading and Saving Data in Binary Files

# In[22]:


data = np.random.random(12)
data = data.reshape(4,3)
data


# In[23]:


np.save('saved_data', data)


# In[24]:


loaded_data = np.load('saved_data.npy')
loaded_data


# ### Reading File with Tabular Data 

# In[25]:


data = np.genfromtxt('ch3_data.csv', delimiter=',', names=True)
data


# In[26]:


data2 = np.genfromtxt('ch3_data2.csv', delimiter=',', names=True)
data2


# In[27]:


data2['id']


# In[28]:


data2[0]


