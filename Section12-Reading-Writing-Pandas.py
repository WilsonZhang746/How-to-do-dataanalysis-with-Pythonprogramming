# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""


### Section 12. Reading and Writing Data with Pandas library
##Lecture 1. Reading Data in CSV or Text Files with Pandas

import numpy as np
import pandas as pd

#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


csvframe = pd.read_csv('sec12_01.csv')
csvframe


pd.read_table('sec12_01.csv', sep=',')



pd.read_csv('sec12_02.csv', header=None)


pd.read_csv('sec12_02.csv', names=['white','red','blue','green','animal'])


pd.read_csv('sec12_03.csv', index_col=['color','status'])




# ### Reading TXT Files into Parts or Partially

pd.read_csv('sec12_02.csv',skiprows=[2],nrows=3,header=None)



































# ### Lecture 2. Using RegExp to Parse TXT Files with Pandas

# In[8]:


pd.read_table('ch05_04.txt', sep='\s+', engine='python')


# In[9]:


pd.read_table('ch05_05.txt', sep='\D+', header=None, engine='python')


# In[10]:


pd.read_table('ch05_06.txt', sep=',', skiprows=[0,1,3,6])




# ### Writing Data in CSV

# In[13]:


frame = pd.DataFrame(np.arange(16).reshape((4,4)),
          index=['red', 'blue', 'yellow', 'white'],
          columns=['ball','pen','pencil','paper'])
frame


# In[14]:


frame.to_csv('ch05_07.csv')
frame2 = pd.read_csv('ch05_07.csv')
frame2


# In[15]:


frame.to_csv('ch05_07b.csv', index=False, header=False)
frame2 = pd.read_csv('ch05_07b.csv')
frame2


# In[16]:


frame3 = pd.DataFrame([[6,np.nan,np.nan,6,np.nan],
              [np.nan,np.nan,np.nan,np.nan,np.nan],
              [np.nan,np.nan,np.nan,np.nan,np.nan],
              [20,np.nan,np.nan,20.0,np.nan],
              [19,np.nan,np.nan,19.0,np.nan]
             ],
                     index=['blue','green','red','white','yellow'],
                     columns=['ball','mug','paper','pen','pencil'])


# In[17]:


frame3.to_csv('ch5_08.csv')
frame4 = pd.read_csv('ch5_08.csv')
frame4


# In[18]:


frame3.to_csv('ch5_09.csv', na_rep = 'NaN')
frame5 = pd.read_csv('ch5_09.csv')
frame5


# ## Reading and Writing HTML Files

# ### Writing Data in HTML

# In[36]:


frame = pd.DataFrame(np.arange(4).reshape(2,2))
print(frame.to_html())


# In[37]:


frame = pd.DataFrame( np.random.random((4,4)),
                    index = ['white','black','red','blue'],
                    columns = ['up','down','right','left'])
frame


# In[38]:


s = ['<HTML>']
s.append('<HEAD><TITLE>My DataFrame</TITLE></HEAD>')
s.append('<BODY>')
s.append(frame.to_html())
s.append('</BODY></HTML>')
html = ''.join(s)


# In[39]:


html_file = open('myFrame.html','w')
html_file.write(html)
html_file.close()


# ### Reading Data from an HTML File

# In[40]:


web_frames = pd.read_html('myFrame.html')
web_frames[0]


# In[41]:


ranking = pd.read_html('https://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/')
ranking[0]


# ### Reading Data from XML

# In[42]:


from lxml import objectify
xml = objectify.parse('books.xml')
xml


# In[43]:


root = xml.getroot()


# In[44]:


root.Book.Author


# In[45]:


root.Book.PublishDate


# In[46]:


root.getchildren()


# In[47]:


[child.tag for child in root.Book.getchildren()]


# In[48]:


[child.text for child in root.Book.getchildren()]


# In[49]:


def etree2df(root):
    column_names = []
    for i in range(0, len(root.getchildren()[0].getchildren())):
        column_names.append(root.getchildren()[0].getchildren()[i].tag)
    xmlframe = pd.DataFrame(columns=column_names)
    for j in range(0, len(root.getchildren())):
        obj = root.getchildren()[j].getchildren()
        texts = []
        for k in range(0, len(column_names)):
            texts.append(obj[k].text)
        row = dict(zip(column_names, texts))
        row_s = pd.Series(row)
        row_s.name = j
        xmlframe = xmlframe.append(row_s)
    return xmlframe


# In[50]:


etree2df(root)


# ## Reading and Writing Data on Microsoft Excel Files

# In[51]:


pd.read_excel('ch05_data.xlsx')


# In[52]:


pd.read_excel('ch05_data.xlsx','Sheet2')


# In[53]:


pd.read_excel('ch05_data.xlsx',1)


# In[54]:


frame = pd.DataFrame(np.random.random((4,4)),
                    index = ['exp1','exp2','exp3','exp4'],
                    columns = ['Jan2015','Feb2015','Mar2015','Apr2015'])
frame


# In[55]:


frame.to_excel('ch05_data02.xlsx')


# ## JSON Data

# In[56]:


frame = pd.DataFrame(np.arange(16).reshape(4,4),
                    index=['white','black','red','blue'],
                    columns=['up','down','right','left'])
frame.to_json('frame.json')


# In[57]:


pd.read_json('frame.json')


# In[58]:


from pandas.io.json import json_normalize


# In[59]:


file = open('books.json','r')
text = file.read()
text = pd.io.json.loads(text)


# In[60]:


json_normalize(text,'books')


# In[61]:


json_normalize(text,'books',['writer','nationality'])


# ## The Format HDF5

# In[62]:


from pandas.io.pytables import HDFStore


# In[63]:


frame = pd.DataFrame(np.arange(16).reshape(4,4),
                    index=['white','black','red','blue'],
                    columns=['up','down','right','left'])
store = HDFStore('ch05_data.h5')
store['obj1'] = frame


# In[64]:


frame2 = pd.DataFrame(np.arange(0,8,0.5).reshape(4,4))
frame2


# In[65]:


store['obj2'] = frame2


# In[66]:


store


# In[67]:


store['obj2']


# ## Pickle - Python Object Serialization

# ### Serialize a Python Object with cPickle

# In[68]:


#On python3.x cPickle has changed from cPickle to _pickle. Thus in python3.x, you can do the following if you want to use cPickle:
import _pickle as pickle


# In[69]:


data = { 'color': ['white','red'], 'value': [5, 7]}
pickled_data = pickle.dumps(data)
pickled_data


# In[70]:


print(pickled_data)


# In[71]:


nframe = pickle.loads(pickled_data)
nframe


# ### Pickling with pandas

# In[72]:


frame = pd.DataFrame(np.arange(16).reshape(4,4),
                    index=['up','down','left','right'])
frame.to_pickle('frame.pkl')


# In[73]:


pd.read_pickle('frame.pkl')


# ## Interacting with Databases

# In[74]:


from sqlalchemy import create_engine


# In[75]:


engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')


# ### Loading and Writing Data with SQLite3

# In[76]:


frame = pd.DataFrame(np.arange(20).reshape(4,5),
                    columns=['white','red','blue','black','green'])
frame


# In[77]:


engine = create_engine('sqlite:///foo.db')


# In[78]:


frame.to_sql('colors',engine)


# In[79]:


pd.read_sql('colors',engine)


# In[80]:


import sqlite3
query = """
         CREATE TABLE test
         (a VARCHAR(20), b VARCHAR(20),
          c REAL,        d INTEGER
         );"""
con = sqlite3.connect(':memory:')
con.execute(query)


# In[81]:


con.commit()


# In[82]:


data = [('white','up',1,3),
        ('black','down',2,8),
        ('green','up',4,4),
        ('red','down',5,5)]
stmt = "INSERT INTO test VALUES(?,?,?,?)"
con.executemany(stmt, data)


# In[83]:


con.commit()


# In[84]:


cursor = con.execute('select * from test')
cursor


# In[85]:


rows = cursor.fetchall()
rows


# In[86]:


cursor.description


# In[87]:


pd.DataFrame(rows, columns=zip(*cursor.description)[0])


# ### Loading and Writing Data with PostgreSQL

# In[88]:


pd.__version__


# In[90]:


import psycopg2
engine = create_engine('postgresql://postgres:password@localhost:5432/postgres')


# In[92]:


frame = pd.DataFrame(np.random.random((4,4)),
                    index=['exp1','exp2','exp3','exp4'],
                    columns=['feb','mar','apr','may']);
frame.to_sql('dataframe',engine)


# In[ ]:


pd.read_sql_table('dataframe',engine)


# In[ ]:


pd.read_sql_query('SELECT index,apr,may FROM DATAFRAME WHERE apr > 0.5', engine)


# ## Reading and Writing Data with a NoSQL Database: MongoDB

# In[135]:


import pymongo
client = MongoClient('localhost',27017)


# In[136]:


db = client.mydatabase
db


# In[137]:


client['mydatabase']


# In[138]:


collection = db.mycollection
db['mycollection']


# In[139]:


collection


# In[140]:


frame = pd.DataFrame( np.arange(20).reshape(4,5), 
                      columns = ['white','red','blue','black','green'])
frame


# In[141]:


import json
record = json.loads(frame.T.to_json()).values
record


# In[144]:


collection.mydocument.insert(record)


# In[145]:


cursor = collection['mydocument'].find()
dataframe = (list(cursor))
del dataframe['_id']
dataframe

