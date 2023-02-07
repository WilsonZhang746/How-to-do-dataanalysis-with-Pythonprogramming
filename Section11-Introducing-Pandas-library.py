# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""


### Section 11. Introducing The Pandas library
##Lecture 1. Getting started with pandas

import pandas as pd
import numpy as np



# ### Declaring a Series 

s = pd.Series([12, -4, 7, 9])
s


s = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
s


s.values


s.index


# Defining a DataFrame

data = {'color' : ['blue', 'green', 'yellow', 'red', 'white'],
        'object' : ['ball', 'pen', 'pencil', 'paper', 'mug'],
        'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)
frame


















##Lecture 2. Introduction of pandas Data Structures: The Series
import pandas as pd
import numpy as np

# ### Declaring a Series 

s = pd.Series([12, -4, 7, 9])
s


s = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
s


s.values


s.index


# ### Selecting the Internal Elements

s[2]


s['b']


s[0:2]


s[['b','c']]


# ### Assigning Values to the Elements

s[1] = 0
s


s['b'] = 1
s


##Series object itself and its index have a name attribute
s.name = 'count'
s.index.name = 'alphabet'
s


# ### Defining Series from NumPy Arrays and Other Series

arr = np.array([1, 2, 3, 4])
s3 = pd.Series(arr)
s3


s4 = pd.Series(s)
s4






















### Lecture 3. Pandas Series Operations

# ### Filtering Values 
import pandas as pd
import numpy as np
s = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
s

s[s > 8]


# ### Mathematical Operations

s / 2

np.log(s)

np.exp(s)

# ### Evaluating Values

serd = pd.Series([1,0,2,1,2,3], index=['white', 'white', 'blue', 'green', 'green', 'yellow'])
serd


serd.unique()


serd.value_counts()


serd.isin([0,3])


serd[serd.isin([0,3])]


# ### NaN Values

s2 = pd.Series([5, -3, np.NaN, 14])
s2


s2.isnull()

s2[s2.isnull()]


s2.notnull()


s2[s2.notnull()]



# ### Series as Dictionaries


mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}
myseries = pd.Series(mydict)
myseries



colors = ['red', 'yellow', 'orange', 'blue', 'green']
myseries = pd.Series(mydict, index=colors)
myseries


# ### Operations between Series

mydict2 = {'red': 400, 'yellow': 1000, 'black': 700}
myseries2 = pd.Series(mydict2)
myseries + myseries2




















###Lecture 4. Introduction of pandas Data Structures: The DataFrame

# ### Defining a DataFrame
import pandas as pd
import numpy as np
data = {'color' : ['blue', 'green', 'yellow', 'red', 'white'],
        'object' : ['ball', 'pen', 'pencil', 'paper', 'mug'],
        'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)
frame


frame2 = pd.DataFrame(data, columns=['object', 'price'])
frame2



frame2 = pd.DataFrame(data, index=['one', 'two', 'three', 'four', 'five'])
frame2

frame3 = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red', 'blue', 'yellow', 'white'],
                     columns=['ball', 'pen', 'pencil', 'paper'])
frame3


# ### Selecting Elements


frame.columns


frame.index


frame.values

#selecting columns
frame['price']


frame.price

#to select elements using numeric or axis labels,using loc()
a = frame.loc[2]
a

frame.loc[[2,4]]

frame.loc[[0,3], ['color','price']]

#to select elements using integer indexing,using iloc()
frame.iloc[2]


frame.iloc[[2,4]]

frame.iloc[[0,3], [0,2]]


#to select rows, return a dataframe
frame[0:1]



frame[1:3]


# to select a single value

frame['object'][3]






























###Lecture 5. Basic manipulation of Pandas DataFrame


#Assigning label names to index and columns
import pandas as pd
import numpy as np
data = {'color' : ['blue', 'green', 'yellow', 'red', 'white'],
        'object' : ['ball', 'pen', 'pencil', 'paper', 'mug'],
        'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)

frame.index.name = 'id'; 
frame.columns.name = 'item'
frame


#add a new column
frame['new'] = 12
frame


frame['new'] = [3.0, 1.3, 2.2, 0.8, 1.1]
frame


ser = pd.Series(np.arange(5))
ser


frame['new'] = ser
frame


frame['price'][2] = 3.3



# ### Membership of a Value

frame.isin([1.0, 'pen'])


frame[frame.isin([1.0, 'pen'])]


# ### Deleting a Column

del frame['new']
frame


# ### Filtering 
data = {'price1' : [1.2, 1.0, 0.6, 0.9, 1.7],
        'pric2' : [2.1, 2.3, 0.9, 0.7, 1.9],
        'pric3' : [1.8, 3.0, 1.3, 1.6, 0.2]}
frame2 = pd.DataFrame(data)
frame2[frame2 < 1.2]


# ### DataFrame from Nested dict 


nestdict = {'red': { 2012: 22, 2013: 33},
            'white': { 2011: 13, 2012: 22, 2013: 16},
            'blue': { 2011: 17, 2012: 27, 2013: 18}}
frame2 = pd.DataFrame(nestdict)
frame2


# ### Transposition of a DataFrame 

frame3 = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red', 'blue', 'yellow', 'white'],
                     columns=['ball', 'pen', 'pencil', 'paper'])
frame3
frame3.T



























###Lecture 6. Working with Index of Pandas Data Structures
# ## The Index Objects

import pandas as pd
import numpy as np
ser = pd.Series([5, 0, 3, 8, 4], index=['red', 'blue', 'yellow', 'white', 'green'])
ser.index


# ### Methods on Index


ser.idxmin()


ser.idxmax()


# ### Index with Duplicate Labels

serd = pd.Series(range(6), index=['white', 'white', 'blue', 'green', 'green', 'yellow'])
serd


serd['white']


serd.index.is_unique


data = {'color' : ['blue', 'green', 'yellow', 'red', 'white'],
        'object' : ['ball', 'pen', 'pencil', 'paper', 'mug'],
        'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)

frame.index.is_unique


##reindexing

ser = pd.Series([2, 5, 7, 4], index=['one', 'two', 'three', 'four'])
ser


ser.reindex(['three', 'four', 'five', 'one'])



ser3 = pd.Series([1, 5, 6, 3], index=[0, 3, 5, 6])
ser3



ser3.reindex(range(6), method='ffill')


ser3.reindex(range(6), method='bfill')


frame.reindex(range(5), method='ffill', columns=['colors', 'price', 'new', 'object'])

frame.reindex(range(5), method='bfill', columns=['colors', 'price', 'new', 'object'])

# ### Dropping


ser = pd.Series(np.arange(4.), index=['red', 'blue', 'yellow', 'white'])
ser


ser.drop('yellow')


ser.drop(['blue','white'])



frame = pd.DataFrame(np.arange(16).reshape((4,4)), 
                    index=['red', 'blue', 'yellow', 'white'],
                    columns=['ball', 'pen', 'pencil', 'paper'])
frame


frame.drop(['blue','yellow'])


frame.drop(['pen','pencil'], axis=1)



























# ### Lecture 7. Operations, Functions, and Mapping of Pandas Data Structures
import pandas as pd
import numpy as np

#Arithmetic operations and Data Alignment
s1 = pd.Series([3,2,5,1],['white','yellow','green','blue'])
s2 = pd.Series([1,4,7,2,1],['white','yellow','black','blue','brown'])

s1 + s2


frame1 = pd.DataFrame(np.arange(16).reshape((4,4)),
          index=['red', 'blue', 'yellow', 'white'],
          columns=['ball','pen','pencil','paper'])
frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),
          index=['blue', 'green', 'white', 'yellow'],
          columns=['mug','pen','ball'])
frame1

frame2

frame1 + frame2


# ### Flexible Arithmetic Methods

frame1.add(frame2)


# ### Operations between DataFrame and Series

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
          index=['red', 'blue', 'yellow', 'white'],
          columns=['ball','pen','pencil','paper'])
frame


ser = pd.Series(np.arange(4), index=['ball','pen','pencil','paper'])
ser


frame - ser


ser['mug'] = 9
ser

frame - ser


# ## Function Application and Mapping

# ### Functions by Element

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
          index=['red', 'blue', 'yellow', 'white'],
          columns=['ball','pen','pencil','paper'])
np.sqrt(frame)


# ### Functions by Row or Column 

f = lambda x: x.max() - x.min()

def f(x):
    return x.max() - x.min()

frame.apply(f)



frame.apply(f, axis=1)



def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
frame.apply(f)























### Lecture 8. Statistics functions
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
          index=['red', 'blue', 'yellow', 'white'],
          columns=['ball','pen','pencil','paper'])
frame.sum()         #sum of each column

frame.sum(axis=1)       #sum of each row

frame.mean()

frame.cumsum()

frame.cumsum(axis=1)

frame.describe()


# ## Correlation and Covariance

seq = pd.Series([1,2,3,4,4,3,2,1],['2006','2007','2008','2009','2010','2011','2012','2013'])
seq2 = pd.Series([3,4,3,4,5,4,3,2],['2006','2007','2008','2009','2010','2011','2012','2013'])
seq.corr(seq2)


seq.cov(seq2)


frame2 = pd.DataFrame([[1,4,3,6],[4,5,6,1],[3,3,1,5],[4,1,6,4]],
          index=['red', 'blue', 'yellow', 'white'],
          columns=['ball','pen','pencil','paper'])
frame2


frame2.corr()


frame2.cov()


ser = pd.Series([0, 1, 2, 3, 9], index=['red','blue','yellow','white','green'])
ser


frame2.corrwith(ser)


frame2.corrwith(frame)























# ## Lecture 9. Sorting and Ranking of Pandas Data Structures
import pandas as pd
import numpy as np
ser = pd.Series([5, 0, 3, 8, 4], index=['red','blue','yellow','white','green'])
ser

ser.sort_index()


ser.sort_index(ascending=False)


frame = pd.DataFrame(np.arange(16).reshape((4,4)),
          index=['red', 'blue', 'yellow', 'white'],
          columns=['ball','pen','pencil','paper'])
frame


frame.sort_index()


frame.sort_index(axis=1)



ser.sort_values()


frame.sort_values(by='pen')


frame.sort_values(by=['pen','pencil'])


ser.rank()          


ser.rank(ascending=False)


























# ## Lecture 10. Handling "Not a Number" Data with Pandas Data Structures

# ### Assigning a NaN Value
import pandas as pd
import numpy as np
ser = pd.Series([0,1,2,np.NaN,9], index=['red','blue','yellow','white','green'])
ser


ser['white'] = None
ser['white'] = np.NaN
ser



frame = pd.DataFrame(np.arange(16).reshape((4,4)),
          index=['red', 'blue', 'yellow', 'white'],
          columns=['ball','pen','pencil','paper'])
frame

frame['ball']['red'] = np.NaN
frame['ball']['red'] = None

# ### FIltering Out NaN Values

ser.dropna()

ser[ser.notnull()]



frame3 = pd.DataFrame([[6,np.nan,6],[np.nan,np.nan,np.nan],[2,np.nan,5]],
                     index=['blue','green','red'],
                     columns=['ball','mug','pen'])
frame3



frame3.dropna()


frame3.dropna(how='all')


# ### Filliing in NaN Occurrences


frame3.fillna(0)


frame3.fillna({'ball':1, 'mug':0, 'pen': 99})



























# ## Lecture 11. Hierarchical Indexing and Leveling of Pandas Data Structures

import pandas as pd
import numpy as np

mser = pd.Series(np.random.rand(8),
                index=[['white','white','white','blue','blue','red','red','red'],
                      ['up','down','right','up','down','up','down','left']])
mser


mser.index


mser['white']


mser[:,'up']


mser['white','up']


mser.unstack()


frame = pd.DataFrame(np.arange(16).reshape((4,4)),
          index=['red', 'blue', 'yellow', 'white'],
          columns=['ball','pen','pencil','paper'])
frame


frame.stack()


mframe = pd.DataFrame(np.random.randn(16).reshape(4,4),
                     index=[['white','white','red','red'], ['up','down','up','down']],
                     columns=[['pen','pen','paper','paper'],[1,2,1,2]])
mframe


# # Reordering and Sorting Levels


mframe.columns.names = ['objects','id']
mframe.index.names = ['colors','status']
mframe


mframe.swaplevel('colors','status')


mframe.sort_index(level='colors')


# ### Summary Statistic by Level


mframe.sum(level='colors')


mframe.sum(level='id',axis=1)



