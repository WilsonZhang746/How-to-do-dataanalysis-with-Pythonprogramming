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



































# ### Lecture 2. Using Regular Expressions to Parse TXT Files with Pandas

import numpy as np
import pandas as pd

#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


pd.read_table('sec12_04.txt', sep='\s+', engine='python')



pd.read_table('sec12_05.txt', sep='\D+', header=None, engine='python')


























# ### Lecture 3.Writing Data in CSV with Pandas

import numpy as np
import pandas as pd

#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


frame = pd.DataFrame(np.arange(16).reshape((4,4)),
          index=['red', 'blue', 'yellow', 'white'],
          columns=['ball','pen','pencil','paper'])
frame


frame.to_csv('sec12_07.csv')



frame.to_csv('sec12_07b.csv', index=False, header=False)



frame3 = pd.DataFrame([[6,np.nan,np.nan,6,np.nan],
              [np.nan,np.nan,np.nan,np.nan,np.nan],
              [np.nan,np.nan,np.nan,np.nan,np.nan],
              [20,np.nan,np.nan,20.0,np.nan],
              [19,np.nan,np.nan,19.0,np.nan]
             ],
                     index=['blue','green','red','white','yellow'],
                     columns=['ball','mug','paper','pen','pencil'])


frame3.to_csv('sec12_08.csv')


frame3.to_csv('sec12_09.csv', na_rep = 'NaN')




















# ## Lecture 4.Reading and Writing Data on Microsoft Excel Files with Pandas

import numpy as np
import pandas as pd

#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


pd.read_excel('sec12_data.xlsx',index_col=0)

pd.read_excel('sec12_data.xlsx', 'Sheet2',index_col=0)

pd.read_excel('sec12_data.xlsx', 1 ,index_col=0)


#write to excel


frame = pd.DataFrame(np.random.random((4,4)),
                    index = ['exp1','exp2','exp3','exp4'],
                    columns = ['Jan2015','Feb2015','Mar2015','Apr2015'])
frame

frame.to_excel('sec12_data02.xlsx')



























# ## Lecture 5. Reading and Writing HTML Files with Pandas

# ### Writing Data in HTML

import numpy as np
import pandas as pd

#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


frame = pd.DataFrame(np.arange(4).reshape(2,2))
print(frame.to_html())



frame = pd.DataFrame( np.random.random((4,4)),
                    index = ['white','black','red','blue'],
                    columns = ['up','down','right','left'])
frame


s = ['<HTML>']
s.append('<HEAD><TITLE>My DataFrame</TITLE></HEAD>')
s.append('<BODY>')
s.append(frame.to_html())
s.append('</BODY></HTML>')
html = ''.join(s)


html_file = open('myFrame.html','w')
html_file.write(html)
html_file.close()


# ### Reading Data from an HTML File

web_frames = pd.read_html('myFrame.html')
web_frames[0]



ranking = pd.read_html('https://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/')

ranking[0]























# ### Lecture6. Reading Data from XML

import numpy as np
import pandas as pd

#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory


from lxml import objectify
xml = objectify.parse('books.xml')
xml


root = xml.getroot()

root.Book.Author


root.Book.PublishDate


root.getchildren()



[child.tag for child in root.Book.getchildren()]



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


etree2df(root)

























# ## Lecture 7.Reading and Writing JSON Data with Pandas

import numpy as np
import pandas as pd

#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory

#writing to a json file
frame = pd.DataFrame(np.arange(16).reshape(4,4),
                    index=['white','black','red','blue'],
                    columns=['up','down','right','left'])
frame.to_json('frame.json')



##reading json file
pd.read_json('frame.json')


from pandas.io.json import json_normalize



file = open('books.json','r')
text = file.read()
text = pd.io.json.loads(text)



pd.json_normalize(text,'books')



pd.json_normalize(text,'books',['writer','nationality'])
































