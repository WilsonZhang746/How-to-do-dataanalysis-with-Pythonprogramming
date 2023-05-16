"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""


### Section 13. pandas in Depth: Data Manipulation
##Lecture 1. Merging Datasets with Pandas

import numpy as np
import pandas as pd
#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


frame1 = pd.DataFrame( {'id':['ball','pencil','pen','mug','ashtray'],
                        'price': [12.33,11.44,33.21,13.23,33.62]})
frame1

frame2 = pd.DataFrame( {'id': ['pencil','pencil','ball','pen'],
                        'color':['white','red','red','black']})
frame2

pd.merge(frame1,frame2)


frame1 = pd.DataFrame( {'id': ['ball','pencil','pen',',mug','ashtray'],
                        'color': ['white','red','red','black','green'],
                        'brand': ['OMG','ABC','ABC','POD','PPOD']})
frame1

frame2 = pd.DataFrame( {'id':['pencil','pencil','ball','pen'],
                        'brand': ['OMG','POD','ABC','POD']})
frame2


pd.merge(frame1,frame2)


pd.merge(frame1, frame2, on='id')


pd.merge(frame1, frame2, on='brand')


frame2.columns = ['sid', 'brand']
frame2


pd.merge(frame1, frame2, left_on='id', right_on='sid')



frame2.columns = ['id','brand']
pd.merge(frame1,frame2,on='id')



pd.merge(frame1,frame2,on='id',how='outer')


pd.merge(frame1,frame2,on='id',how='left')


pd.merge(frame1,frame2,on='id',how='right')


pd.merge(frame1,frame2,on=['id','brand'], how='outer')


# ### Merging on Index

pd.merge(frame1,frame2,right_index=True, left_index=True)

pd.merge(frame1,frame2,right_index=True, left_index=True, how='outer')


frame1.join(frame2)     #error




frame2.columns = ['id2','brand2']
frame1.join(frame2)

















# ## Lecture 2.Concatenating Datasets with Numpy and Pandas
import numpy as np
import pandas as pd
#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


#concatenating Numpy arrays
array1 = np.arange(9).reshape((3,3))
array1

array2 = np.arange(9).reshape((3,3))+6
array2


np.concatenate([array1,array2],axis=1)


np.concatenate([array1,array2],axis=0)




#concatenating Pandas Series and Dataframes
ser1 = pd.Series(np.random.rand(4), index=[1,2,3,4])
ser1


ser2 = pd.Series(np.random.rand(4), index=[5,6,7,8])
ser2


pd.concat([ser1,ser2])


pd.concat([ser1,ser2], axis=1)



pd.concat([ser1,ser2], keys=[1,2])



pd.concat([ser1,ser2], axis=1, keys=[1,2])



frame1 = pd.DataFrame(np.random.rand(9).reshape(3,3), index=[1,2,3], columns=['A','B','C'])
frame2 = pd.DataFrame(np.random.rand(9).reshape(3,3), index=[4,5,6], columns=['A','B','C'])
pd.concat([frame1, frame2])


pd.concat([frame1, frame2], axis=1)



# ### Combining datasets


ser1 = pd.Series(np.random.rand(5), index=[1,2,3,4,5])
ser1


ser2 = pd.Series(np.random.rand(4), index=[2,4,5,6])
ser2


ser1.combine_first(ser2)


ser2.combine_first(ser1)


ser1[:3].combine_first(ser2[:3])




















# ## Lecture 3. Pivoting,Stacking,Unstacking,Long and Wide forms of Datasets with Pandas
import numpy as np
import pandas as pd
#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory

# ### Pivoting with Hierarchical Indexing

frame1 = pd.DataFrame(np.arange(9).reshape(3,3),
                     index=['white','black','red'],
                     columns=['ball','pen','pencil'])
frame1


ser = frame1.stack()
ser


ser.unstack()


ser.unstack(0)


# ### Pivoting from "Long" to "Wide" Format

longframe = pd.DataFrame({ 'color':['white','white','white',
                                    'red','red','red',
                                    'black','black','black'],
                           'item':['ball','pen','mug',
                                   'ball','pen','mug',
                                   'ball','pen','mug'],
                           'value': np.random.rand(9)})
longframe


wideframe = longframe.pivot('color','item')
wideframe






















# ### Lecture 4.Removing, Mapping Operations with Pandas

import numpy as np
import pandas as pd
#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


#removing rows or columns

frame1 = pd.DataFrame(np.arange(9).reshape(3,3),
                       index=['white','black','red'],
                       columns=['ball','pen','pencil'])
frame1



del frame1['ball']
frame1



frame1.drop('white')



# ### Removing Duplicate rows

dframe = pd.DataFrame({ 'color': ['white','white','red','red','white'],
                        'value': [2,1,3,3,2]})
dframe


dframe.duplicated()


dframe[dframe.duplicated()]


dframe.drop_duplicates()


# ### Replacing Values via Mapping

frame = pd.DataFrame({ 'item':['ball','mug','pen','pencil','ashtray'],
                       'color':['white','rosso','verde','black','yellow'],
                       'price':[5.56,4.20,1.30,0.56,2.75]})
frame


newcolors = {
    'rosso': 'red',
    'verde': 'green'
}


frame.replace(newcolors)


ser = pd.Series([1,3,np.nan,4,6,np.nan,3])
ser


ser.replace(np.nan,0)


# ### Adding Values via Mapping


frame = pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                      'color':['white','red','green','black','yellow']})
frame


price = {
    'ball': 5.56,
    'mug': 4.20,
    'bottle': 1.30,
    'scissors': 3.41,
    'pen': 1.30,
    'pencil': 0.56,
    'ashtray': 2.75
}



frame['price'] = frame['item'].map(price)
frame






















# ### Lecture 5.Rename the Indexes of the Axes

import numpy as np
import pandas as pd
#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


frame = pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                      'color':['white','red','green','black','yellow'],
                      'price':[5.56,4.2,1.3,0.56,2.75]})

frame


reindex = {
    0: 'first',
    1: 'second',
    2: 'third',
    3: 'fourth',
    4: 'fifth'
}
frame.rename(reindex)


recolumn = {
    'item': 'object',
    'price': 'value'
}
frame.rename(index=reindex, columns=recolumn)


frame.rename(index={1:'first'}, columns={'item':'object'})


frame.rename(columns={'item':'object'}, inplace=True)


frame
























# ### Lecture 6. Detecting and Filtering Outliers

import numpy as np
import pandas as pd
#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


randframe = pd.DataFrame(np.random.randn(1000,3))
randframe.describe()


randframe.std()

#show the outlier, if any column has outlier value
randframe[(np.abs(randframe) > (3*randframe.std())).any(1)]


#to get the data excluding outlier observations
outindex= np.array(randframe[(np.abs(randframe) > (3 *randframe.std())).any(1)].index)
outindex

randframe.drop(outindex, inplace=True)

len(randframe)



#show the outlier observation, if one specified column has outlier
randframe = pd.DataFrame(np.random.randn(1000,3))

randframe[randframe[2] > 2.8 *randframe[2].std()]

randframe[randframe[2] <= 2.8*randframe[2].std()]













# ## Lecture 7. Discretization and Binning of Datasets with Pandas

import numpy as np
import pandas as pd
#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory



results = [12,34,67,55,28,90,99,12,3,56,74,44,87,23,49,89,87]
bins = [0,25,50,75,100]
cat = pd.cut(results, bins)
cat


cat.categories


cat.codes



pd.value_counts(cat)



bin_names = ['unlikely','less likely','likely','highly likely']
pd.cut(results, bins, labels=bin_names)


# cut into 5 bins in equal interval
pd.cut(results, 5)



#qcut will make the number of occurrence in each bin equal
quintiles = pd.qcut(results, 5)
quintiles


pd.value_counts(quintiles)




#create a bin column for a dataframe
df = pd.DataFrame({'number': np.random.randint(1, 100, 10)})
df['bins'] = pd.cut(x=df['number'], bins=[1, 20, 40, 60, 80, 100],
                    labels=['1', '2', '3', '4', '5'])

print(df)
 





















# ## Lecture 8. Permutation,Random Sampling with Pandas

import numpy as np
import pandas as pd
#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


#Permutation
nframe = pd.DataFrame(np.arange(25).reshape(5,5))
nframe


new_order = np.random.permutation(5)
new_order


nframe.take(new_order)


new_order = [3,4,2]
nframe.take(new_order)


# ### Random Sampling


sample = np.random.randint(0, len(nframe), size=3)
sample


nframe.take(sample)



























# ## Lecture 9.Data Aggregation and Grouping with Pandas

import numpy as np
import pandas as pd
#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory

#Data aggregation

frame = pd.DataFrame({ 'color': ['white','red','green','red','green'],
                       'object': ['pen','pencil','pencil','ashtray','pen'],
                       'price1': [5.56, 4.20, 1.30, 0.56, 2.75],
                       'price2': [4.75,4.12,1.60,0.75,3.15]})
frame


group = frame['price1'].groupby(frame['color'])
group


group.groups


group.mean()


group.sum()


# ### Hierarchical Grouping

ggroup = frame['price1'].groupby([frame['color'],frame['object']])
ggroup.groups


ggroup.sum()


frame[['price1','price2']].groupby(frame['color']).mean()


frame.groupby(frame['color']).mean()


# ## Group Iteration

for name, group in frame.groupby('color'):
    print(name)
    print(group)


# ### Chain of Transformations
result1 = frame['price1'].groupby(frame['color']).mean()
type(result1)


result2 = frame.groupby(frame['color']).mean()
type(result2)



frame['price1'].groupby(frame['color']).mean()


frame.groupby(frame['color'])['price1'].mean()


(frame.groupby(frame['color']).mean())['price1']


means = frame.groupby('color').mean().add_prefix('mean_')
means


# ### Functions on Groups

group = frame.groupby('color')
group['price1'].quantile(0.6)


def range(series):
    return series.max() - series.min()
group['price1'].agg(range)


group.agg(range)


group['price1'].agg(['mean','std',range])

















### Lecture 10.  Reshape Wide long form pandas dataframe
### using stack,unstack and melt method

import numpy as np
import pandas as pd
#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


## stack() - from dataframe to Series
# ### Pivoting from a dataframe to Series with Hierarchical Indexing

frame1 = pd.DataFrame(np.arange(9).reshape(3,3),
                     index=['white','black','red'],
                     columns=['ball','pen','pencil'])
frame1


ser = frame1.stack()
ser



### unstack() - from Series to dataframe
## to return as a dataframe

ser.unstack()


ser.unstack(0)


# ### Pivoting - from "Long" to "Wide" Format

longframe = pd.DataFrame({ 'color':['white','white','white',
                                    'red','red','red',
                                    'black','black','black'],
                           'item':['ball','pen','mug',
                                   'ball','pen','mug',
                                   'ball','pen','mug'],
                           'value': np.random.rand(9)})
longframe


wideframe = longframe.pivot('color','item')
wideframe

wideframe.reset_index(inplace = True)
wideframe


# melt()  - from wide format to long form
frame = pd.DataFrame({'item':['ball','mug','pen','pencil','ashtray'],
                      'color':['white','red','green','black','yellow'],
                      'size' : ['large','medium','small','big','small'],
                      'price':[5.56,4.2,1.3,0.56,2.75]})

frame

df_melt = frame.melt(id_vars =['item', 'color']) 

df_melt


wideframe = df_melt.pivot(index=['item','color'], columns='variable')
wideframe


wideframe.reset_index(inplace = True)

wideframe





