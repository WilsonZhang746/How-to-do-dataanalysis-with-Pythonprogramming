# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""


#### Section 14. Data visualization with matplotlib

## Lecture 1. Getting started using matplotlib

import matplotlib.pyplot as plt

#plot a line
plt.plot([1,2,3,4])
plt.show()


# ## Set the properties of the plot

plt.plot([1,2,3,4],[1,4,9,16],'ro')

plt.show()


#sett axis range and title

plt.axis([0,5,0,20])
plt.title('My first plot')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
#plt.plot([1,2,3,4],[1,4,9,16])
plt.show()

# ### matplotlib and NumPy

import math
import numpy as np

t = np.arange(0,2.5,0.1)
y1 = np.sin(math.pi*t)
y2 = np.sin(math.pi*t+math.pi/2)
y3 = np.sin(math.pi*t-math.pi/2)
plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys')
plt.show()


# In[8]:
plt.plot(t,y1,'b',t,y2,'g',t,y3,'r')
plt.show()

plt.plot(t,y1,'b--',t,y2,'g',t,y3,'r-.')
plt.show()



# ## Using the kwargs
#The objects that make up a chart have many attributes that 
#characterize them. These attributes are all default values, 
#but can be set through the use of keyword args, often
#referred as kwargs.

#set thickness
plt.plot([1,2,4,2,1,0,1,2,1,4], linewidth=2.0)
plt.show()


# ### Working with multiple Figures and Axes

#matplotlib allows you to manage multiple figures simultaneously, 
#and within each figure, it offers the ability to view different
#plots defined as subplots

#The argument of the subplot() function is composed of three integers.
# The first number defines how many parts the figure is split
#into vertically. The second number defines how many parts the 
#figure is divided into horizontally. The third issue selects 
#which is the current subplot on which you can direct commands.

#plot sin and cos in two subplots vertically
t = np.arange(0,5,0.1)
y1 = np.sin(2*np.pi*t)
y2 = np.sin(2*np.pi*t)
plt.subplot(211)
plt.plot(t,y1,'b-.')
plt.subplot(212)
plt.plot(t,y2,'r--')
plt.show()


#plot sin and cos in two subplots horizontally
t = np.arange(0.,1.,0.05)
y1 = np.sin(2*np.pi*t)
y2 = np.cos(2*np.pi*t)
plt.subplot(121)
plt.plot(t,y1,'b-.')
plt.subplot(122)
plt.plot(t,y2,'r--')
plt.show()














### lecture 2. Adding text to charts in matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np

# ### Adding text

#add x,y axis labels
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.xlabel('Counting')
plt.ylabel('Square values')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()


#modify the title by changing the font and increasing the size of 
#the character, and modify the color of the axis labels
plt.axis([0,5,0,20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values',color='gray')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()


# text() allows you to add text to any position within a chart.
#text(x,y,s, fontdict=None, **kwargs)
#The first two arguments are the coordinates of the location 
#where you want to place the text. s is the string of text to 
#be added, and fontdict (optional) is the font that you
#want to use. Finally, you can add the keywords.

#Add the label to each point of the plot

plt.axis([0,5,0,20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()


# matplotlib offers the possibility to integrate LaTeX expressions
#mostly usef for mathematical expressions.
#To do this, you can add a LaTeX expression to the text, enclosing 
#it between two $ characters. The interpreter will recognize them 
#as LaTeX expressions and convert them to the corresponding graphic, 
#which can be a mathematical expression, a formula,mathematical 
#characters, or just Greek letters. Generally you have to precede 
#the string containing LaTeX expressions with an r, which indicates
# raw text, in order to avoid unintended escape sequences

#add a formula describing the trend followed by the point 
#of the plot and enclose it in a colored bounding box
plt.axis([0,5,0,20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,r'$y = x^2$', fontsize=20, bbox={'facecolor':'yellow','alpha':0.2})         
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()


















# ### Lecture 3. Adding a grid in matplotlib
#Grid lets you better understand the position occupied by 
#each point on the chart

import matplotlib.pyplot as plt
import math
import numpy as np


plt.axis([0,5,0,20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,r'$y = x^2$', fontsize=20, bbox={'facecolor':'yellow','alpha':0.2})  
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.show()




x = np.arange(-5, 5, 0.01)
y = np.sin(2*np.pi*x)
plt.plot(x, y)
# Specify grid with line attributes
plt.grid(color='r', linestyle='--')
plt.show()




















# ### Lecture 4. Adding Legend to charts in matplotlib
#Add a legend to your chart with the legend() function and a string
#indicating the words with which you want the series to be shown
import matplotlib.pyplot as plt
import math
import numpy as np

#assign the First series name to the input data array
plt.axis([0,5,0,20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,r'$y = x^2$', fontsize=20, bbox={'facecolor':'yellow','alpha':0.2})  
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
#A legend is added in the upper-right corner by default
plt.legend(['First series'])
plt.show()




#the position occupied by the legend is set by assigning numbers 
#from 0 to 10 to the loc kwarg. Each of these numbers characterizes 
#one of the corners of the chart
#0 best
#1 upper-right
#2 upper-left
#3 lower-right
#4 lower-left
#5 right
#6 center-left
#7 center-right
#8 lower-center
#9 upper-center
#10 center

#move the legend in the upper-left corner
plt.axis([0,5,0,20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,r'$y = x^2$', fontsize=20, bbox={'facecolor':'yellow','alpha':0.2})  
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[0.8,3.5,8,15],'g^')
plt.plot([1,2,3,4],[0.5,2.5,4,12],'b*')
plt.legend(['First series','Second series','Third series'], loc=2)
plt.show()

















#### Lecture 5. Save your charts in matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np

import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory

# ### Saving your chart directly as an Image

plt.axis([0,5,0,20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,r'$y = x^2$', fontsize=20, bbox={'facecolor':'yellow','alpha':0.2})  
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[0.8,3.5,8,15],'g^')
plt.plot([1,2,3,4],[0.5,2.5,4,12],'b*')
plt.legend(['First series','Second series','Third series'], loc=2)
plt.savefig('my_chart.png')















### Lecture 6. Handling Date Values of charts in matplotlib
import datetime
import numpy as np
import matplotlib.pyplot as plt

#problematic showing date ticks on x-axis using default setting
#for day-month-year
events = [datetime.date(2015,1,23), 
          datetime.date(2015,1,28),
          datetime.date(2015,2,3),
          datetime.date(2015,2,21),
          datetime.date(2015,3,15),
          datetime.date(2015,3,24),
          datetime.date(2015,4,8),
          datetime.date(2015,4,24)]
readings = [12,22,25,20,18,15,17,14]
plt.plot(events,readings)
plt.show()



#To manage dates it is therefore advisable to define a time scale 
#with appropriate  objects. First you need to import matplotlib.dates,
#a module specialized for this type of data. Then you define the 
#scales of the times, as in this case, a scale of days and one of
#the months, through the MonthLocator() and DayLocator() functions. 
#In these cases, the formatting is also very important, and to avoid 
#overlap or unnecessary references,you have to limit the tick labels 
#to the essential, which in this case is year-month. This format 
#can be passed as an argument to the DateFormatter() function. After
#you defined the two scales, one for the days and one for the months, 
#you can set two different kinds of ticks on the x-axis, using the 
#set_major_locator() and set_minor_locator() functions on the 
#xaxis object. To set the text format of the tick labels referred 
#to the months you have to use the set_major_formatter() function.


import matplotlib.dates as mdates

months = mdates.MonthLocator()
days = mdates.DayLocator()
timeFmt = mdates.DateFormatter('%Y-%m')
events = [datetime.date(2015,1,23), 
          datetime.date(2015,1,28),
          datetime.date(2015,2,3),
          datetime.date(2015,2,21),
          datetime.date(2015,3,15),
          datetime.date(2015,3,24),
          datetime.date(2015,4,8),
          datetime.date(2015,4,24)]
readings = [12,22,25,20,18,15,17,14]
fig, ax = plt.subplots()
plt.plot(events, readings)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_minor_locator(days)
plt.show()














### Line charts with matplotlib
import datetime
import numpy as np
import matplotlib.pyplot as plt

#A mathematical function represented in a line chart
x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(3*x)/x
plt.plot(x,y)
plt.show()



#display a family of functions:
#a different color is automatically assigned to each line.
#All the plots are represented on the same scale; #that is, the data
#points of each series refer to the same x-axis and y-axis.
x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x
plt.plot(x,y)
plt.plot(x,y2)
plt.plot(x,y3)
plt.show()



#specify color and styles for lines

x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x
plt.plot(x,y,'k--',linewidth=3)
plt.plot(x,y2,'m-.')
plt.plot(x,y3,color='#87a3cc',linestyle='--')
plt.show()


##Using tick labels in LaTeX format

#by default, values on ticks are shown in numerical form. 
#you replace the numerical values with multiple of π. 
#You can also replace the ticks on the y-axis. 
#To do all this, you have to use xticks() and yticks() functions.
#passing to each of them two lists of values. 
#The first list contains values corresponding to the positions 
#where the ticks are to be placed,and the second contains the 
#tick labels. 
#you can use strings containing LaTeX format in order to correctly 
#display the symbol π. 
#For LaTex, you need to define them within two $ characters 
#and to add a r as the prefix.


x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x
plt.plot(x,y,color='b')
plt.plot(x,y2,color='r')
plt.plot(x,y3,color='g')
plt.xticks([-2*np.pi,-np.pi,0, np.pi, 2*np.pi],
           [r'$-2\pi$',r'$-\pi$',r'$0$',r'$+\pi$',r'$+2\pi$'])
plt.yticks([-1,0,1,2,3],
           [r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])
plt.show()



#to have the two axes passing through the origin (0, 0)
#the two axes crossing in the middle of the figure

#To do this, you must first capture the Axes object through the 
#gca() function. Then through this object, you can select each of 
#the four sides making up the bounding box,specifying for each one 
#its position: right, left, bottom, and top. Crop the sides that 
#do not match any axis (right and top) using the set_color() 
#function and indicating none for color

x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x
plt.plot(x,y,color='b')
plt.plot(x,y2,color='r')
plt.plot(x,y3,color='g')
plt.xticks([-2*np.pi,-np.pi,0, np.pi, 2*np.pi],
           [r'$-2\pi$',r'$-\pi$',r'$0$',r'$+\pi$',r'$+2\pi$'])
plt.yticks([-1,0,1,2,3],
           [r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#representing the x-axis
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
#representing the y_axis
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()



#to specify a particular point of the line using a notation 
#and optionally add an arrow to better indicate the position
#of the point

#using function annotate(), 
#The first argument is the string to be represented containing 
#the expression in LaTeX; 
#The point of the chart to note is indicated by a list containing 
#the coordinates of the point [x, y]. 
#The distance of the textual notation from the point to be highlighted 
#is defined by the xytext kwarg, and represented by means of a curved 
#arrow

#get the chart with the mathematical notation of the limit

x = np.arange(-2*np.pi,2*np.pi,0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3 = np.sin(x)/x
plt.plot(x,y,color='b')
plt.plot(x,y2,color='r')
plt.plot(x,y3,color='g')
plt.xticks([-2*np.pi,-np.pi,0, np.pi, 2*np.pi],
           [r'$-2\pi$',r'$-\pi$',r'$0$',r'$+\pi$',r'$+2\pi$'])
plt.yticks([-1,0,1,2,3],
           [r'$-1$',r'$0$',r'$+1$',r'$+2$',r'$+3$'])
plt.annotate(r'$\lim_{x\to 0}\frac{\sin(x)}{x}= 1$', xy=[0,1],xycoords='data',
             xytext=[30,30],fontsize=16, textcoords='offset points', arrowprops=dict(arrowstyle="->",
             connectionstyle="arc3,rad=.2"))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()


# ## Line Charts with pandas

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = {'series1':[1,3,4,3,5],
        'series2':[2,4,5,2,4],
        'series3':[3,2,3,1,3]}
df = pd.DataFrame(data)
x = np.arange(5)
plt.axis([0,5,0,7])
plt.plot(x,df)
plt.legend(data, loc=2)
plt.show()






















# ## Lecture 8.Histograms using matplotlib in Python

import matplotlib.pyplot as plt
import numpy as np

#simple example
# Creating dataset
test = np.array([25, 57, 15, 93, 34,
              73, 54, 54, 11,
              20, 51, 52, 75, 31,
              27, 39,29])
 
# Creating histogram, setting the bin bounding
fig, ax = plt.subplots(figsize =(12, 9))
ax.hist(test, bins = [0, 20, 40, 60, 80, 100])
 
# Show plot
plt.show()



#setting bin number
test2 = np.random.randint(0,200,200)
test2


n, bin, patches = plt.hist(test2, bins=20)
plt.show()

n
bin


#Customization of Histogram
#different color for different bins
#adjust axis
#add text


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
 
 
# Creating dataset
np.random.seed(23685752)
N_points = 10000
n_bins = 20
 
# Creating distribution
x = np.random.randn(N_points)
y = .8 ** x + np.random.randn(10000) + 25
legend = ['distribution']

# Creating histogram
fig, axs = plt.subplots(1, 1,
                        figsize =(10, 7),
                        )
 
 
# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    axs.spines[s].set_visible(False)
 
# Remove x, y ticks
axs.xaxis.set_ticks_position('none')
axs.yaxis.set_ticks_position('none')
   
# Add padding between axes and labels
axs.xaxis.set_tick_params(pad = 5)
axs.yaxis.set_tick_params(pad = 10) 

# Add x, y gridlines
axs.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.6)
 
# Add Text watermark
fig.text(0.9, 0.15, 'Jeeteshgavande30',
         fontsize = 12,
         color ='red',
         ha ='right',
         va ='bottom',
         alpha = 0.7)

# Creating histogram
N, bins, patches = axs.hist(x, bins = n_bins)
 
# Setting color
fracs = ((N**(1 / 5)) / N.max())
norm = colors.Normalize(fracs.min(), fracs.max())
 
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)
 
# Adding extra features   
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend(legend)
plt.title('Customized histogram')
 
# Show plot
plt.show()




















# ## Lecture 9. Bar Charts using matplotlib in Python

import matplotlib.pyplot as plt
# a simple bar chart in which indices are drawn on the x-axis
index = [0,1,2,3,4]
values = [5,7,3,4,6]
plt.bar(index,values)
plt.show()



#specify the categories through the tick label
#by passing a  list of strings to the xticks() function

import matplotlib.pyplot as plt
import numpy as np

index = np.arange(5)
values1 = [5,7,3,4,6]
plt.bar(index, values1)
plt.xticks(index+0.4,['A','B','C','D','E'])
plt.show()





import matplotlib.pyplot as plt
import numpy as np

#bar chart with error bar
#refine the bar chart, adding standard deviations of each bar,through
#the yerr kwarg along with a list containing the standard deviations

index = np.arange(5)
values1 = [5,7,3,4,6]
std1 = [0.8,1,0.4,0.9,1.3]
plt.title('A Bar Chart')
plt.bar(index, values1, yerr=std1, error_kw={'ecolor':'0.1','capsize':6},alpha=0.7,label='First')
plt.xticks(index+0.4,['A','B','C','D','E'])
plt.legend(loc=2)
plt.show()


# ### Horizontal Bar Chart
#barh(). The arguments and the kwargs valid for the bar() function 
#remain the same for this function.The only change that the categories
# are represented on the y-axis and the numerical values are
#shown on the x-axis now
import matplotlib.pyplot as plt
import numpy as np

index = np.arange(5)
values1 = [5,7,3,4,6]
std1 = [0.8,1,0.4,0.9,1.3]
plt.title('A Horizontal Bar Chart')
plt.barh(index, values1, xerr=std1, error_kw={'ecolor':'0.1','capsize':6},alpha=0.7,label='First')
plt.yticks(index+0.4,['A','B','C','D','E'])
plt.legend(loc=5)
plt.show()


# ### Multiserial Bar Chart
#to define a sequence of indexes, each corresponding to a bar, 
#to be assigned to the x-axis. These indices should represent
# categories.
import matplotlib.pyplot as plt
import numpy as np

index = np.arange(5)
values1 = [5,7,3,4,6]
values2 = [6,6,4,5,7]
values3 = [5,6,5,4,6]
bw = 0.3
plt.axis([0,5,0,8])
plt.title('A Multiseries Bar Chart', fontsize=20)
plt.bar(index, values1, bw, color='b')
plt.bar(index+bw, values2, bw, color='g')
plt.bar(index+2*bw, values3, bw, color='r')
plt.xticks(index+1.5*bw,['A','B','C','D','E'])
plt.show()


# Multiserial hotizontal Bar Chart
#have to reverse the axis range value
#using yticks
import matplotlib.pyplot as plt
import numpy as np

index = np.arange(5)
values1 = [5,7,3,4,6]
values2 = [6,6,4,5,7]
values3 = [5,6,5,4,6]
bw = 0.3
plt.axis([0,8,0,5])
plt.title('A Multiseries Bar Chart', fontsize=20)
plt.barh(index, values1, bw, color='b')
plt.barh(index+bw, values2, bw, color='g')
plt.barh(index+2*bw, values3, bw, color='r')
plt.yticks(index+0.4,['A','B','C','D','E'])
plt.show()


# ### Multiseries Bar Chart with pandas DataFrame

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

index = np.arange(5)
data = {'series1': [1,3,4,3,5],
        'series2': [2,4,5,2,4],
        'series3': [3,2,3,1,3]}
df = pd.DataFrame(data)
df.plot(kind='bar')
plt.show()


# Multiseries horizontal Bar Chart with pandas DataFrame

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

index = np.arange(5)
data = {'series1': [1,3,4,3,5],
        'series2': [2,4,5,2,4],
        'series3': [3,2,3,1,3]}
df = pd.DataFrame(data)
df.plot(kind='barh')
plt.show()


# ### Multiseries Stacked Bar Charts

# bars are stacked one on the other, by adding the bottom
#kwarg to each bar() function, and Each series must be assigned 
#to the corresponding bottom kwarg.

import matplotlib.pyplot as plt
import numpy as np

series1 = np.array([3,4,5,3])
series2 = np.array([1,2,2,5])
series3 = np.array([2,3,3,4])
index = np.arange(4)
plt.axis([-0.5,3.5,0,15])
plt.title('A Multiseries Stacked Bar Chart')
plt.bar(index,series1,color='r')
plt.bar(index,series2,color='b',bottom=series1)
plt.bar(index,series3,color='g',bottom=(series2+series1))
plt.xticks(index,['Jan18','Feb18','Mar18','Apr18'])
plt.show()


# Multiseries horizontal Stacked Bar Charts


import matplotlib.pyplot as plt
import numpy as np

series1 = np.array([3,4,5,3])
series2 = np.array([1,2,2,5])
series3 = np.array([2,3,3,4])
index = np.arange(4)
plt.axis([0,15,-0.5,3.5])
plt.title('A Multiseries Horizontal Stacked Bar Chart')
plt.barh(index,series1,color='r')
plt.barh(index,series2,color='b',left=series1)
plt.barh(index,series3,color='g',left=(series2+series1))
plt.yticks(index,['Jan18','Feb18','Mar18','Apr18'])
plt.show()


# use hatches that allow you to fill the various bars with 
#strokes drawn in a different way
#To do this, you have first to set the color of the bar as white 
#and then you have to use the hatch kwarg to define how the hatch 
#is to be set. The various hatches have codes distinguishable 
#among these characters (|, /, -, \, *, -) corresponding to the 
#line style filling the bar. The more a symbol is replicated, 
#the denser the lines forming the hatch will be. For example, 
#/// is more dense than //, which is more dense than /
import matplotlib.pyplot as plt
import numpy as np

series1 = np.array([3,4,5,3])
series2 = np.array([1,2,2,5])
series3 = np.array([2,3,3,4])
index = np.arange(4)
plt.axis([0,15,-0.5,3.5])
plt.title('A Multiseries Horizontal Stacked Bar Chart')
plt.barh(index,series1,color='w',hatch='xx')
plt.barh(index,series2,color='w',hatch='///',left=series1)
plt.barh(index,series3,color='w',hatch='\\\\\\',left=(series2+series1))
plt.yticks(index,['Jan18','Feb18','Mar18','Apr18'])
plt.show()


# ### Stacked Bar Charts with pandas DataFrame

import matplotlib.pyplot as plt
import pandas as pd

data = {'series1': [1,3,4,3,5],
        'series2': [2,4,5,2,4],
        'series3': [3,2,3,1,3]}
df = pd.DataFrame(data)
df.plot(kind='bar',stacked=True)
plt.show()























# ## Lecture 10. Pie Charts using matplotlib in Python

import matplotlib.pyplot as plt

#colors kwarg let you define the sequence of the colors, 
#labels kwarg will assign a list of strings 
#containing the labels to be displayed in sequence
#axis() function to draw the pie chart in a perfectly spherical way

#a simple pie chart

labels = ['Nokia','Samsung','Apple','Lumia']
values = [10,30,45,15]
colors = ['yellow','green','red','blue']
plt.pie(values,labels=labels,colors=colors)
plt.axis('equal')
plt.show()


# explode kwarg let you draw a slice extracted from the pie
#add a title
#startangle kwarg to adjust the angle of rotation of the pie


import matplotlib.pyplot as plt

labels = ['Nokia','Samsung','Apple','Lumia']
values = [10,30,45,15]
colors = ['yellow','green','red','blue']
explode = [0.3,0,0,0]
plt.title('A Pie Chart')
plt.pie(values,labels=labels,colors=colors,explode=explode,startangle=180)
plt.axis('equal')
plt.show()


# autopct kwarg adds to the center of each slice a text label 
#showing the corresponding value.

import matplotlib.pyplot as plt

labels = ['Nokia','Samsung','Apple','Lumia']
values = [10,30,45,15]
colors = ['yellow','green','red','blue']
explode = [0.3,0,0,0]
plt.title('A Pie Chart')
plt.pie(values,labels=labels,colors=colors,explode=explode,shadow=True,autopct='%1.1f%%',startangle=180)
plt.axis('equal')
plt.show()


# ### Pie Charts with pandas DataFrame

import matplotlib.pyplot as plt
import pandas as pd

data = {'series1': [1,3,4,3,5],
        'series2': [2,4,5,2,4],
        'series3': [3,2,3,1,3]}
df = pd.DataFrame(data)
df['series1'].plot(kind='pie', figsize=(6,6))
plt.show()

















### Lecture 11. Google Map using gmplot package

import gmplot


import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)      #setting new working directory

# First two arugments are the geogrphical coordinates .i.e. Latitude and Longitude
#and the zoom resolution.

#Molde, Norway
#Note − Above screen display we see this because Google Maps 
#service is not free now in case you are accessing through an API.
# You need to add your API_KEY to see a better google map view. 
# Below is the code to accomplish this −
#gmap.apikey = "AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8"

gmap1 = gmplot.GoogleMapPlotter(62.7426017,7.0121223, 18 )

#AALesund, Norway  
gmap2 = gmplot.GoogleMapPlotter(62.4681223,6.0766385,18)

#Oslo, Norway
gmap3 = gmplot.GoogleMapPlotter(59.8937879,10.4554652,18)

# Pass the path, to save
gmap1.draw( ".\\map11.html" )
gmap2.draw( ".\\map12.html" )
gmap3.draw( ".\\map13.html" )



#Scatter points on the google map and draw a line in between them .
# import gmplot package
import gmplot
  
latitude_list = [ 62.7426017, 62.4681223,59.8937879 ]
longitude_list = [7.0121223, 6.0766385,10.4554652 ]
  
gmap4 = gmplot.GoogleMapPlotter(59.8937879,10.4554652,13)
  
# scatter method of map object 
# scatter points on the google map
gmap4.scatter( latitude_list, longitude_list, '# FF0000',
                              size = 40, marker = False )
  
# Plot method Draw a line in
# between given coordinates
gmap4.plot(latitude_list, longitude_list,
            edge_width = 2.5)
  
gmap4.draw( ".\\map14.html" )



#To draw a polygon on the google map

# import gmplot package
import gmplot
  
latitude_list = [ 62.7426017, 62.4681223,59.8937879 ]
longitude_list = [7.0121223, 6.0766385,10.4554652 ]
  
gmap5 = gmplot.GoogleMapPlotter(59.8937879,10.4554652,13)
  
gmap5.scatter( latitude_list, longitude_list, '# FF0000',
                                size = 40, marker = False)
  
# polygon method Draw a polygon with
# the help of coordinates
gmap5.polygon(latitude_list, longitude_list,
                   color = 'cornflowerblue')
  
gmap5.draw( ".\\map15.html" )


















### Lecture 12. Google Map using folium package

#1 : To create a Base Map.
# import folium package
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path) 


# to install folium package, run the following in Anaconda prompt window:
# "pip install folium" 
import folium
 
# plot a base googlemap of Molde Football Stadium
# and starting Zoom level = 12
#find the coordinates from googlemap
my_map1 = folium.Map(location = [62.7330259, 7.1452503],
                                        zoom_start = 12 )
 
# save method of Map object will create a map
my_map1.save(" my_map1.html " ) 




#2 : Add a circular marker
import folium
 
my_map2 = folium.Map(location = [62.7330259,7.1452503],
                                         zoom_start = 12)
 
# CircleMarker with radius
folium.CircleMarker(location = [62.7330259,7.1452503],
                    radius = 50, popup = ' Molde Aker Stadium ').add_to(my_map2)
 
# save as html
my_map2.save(" my_map2.html ")



#3 : Add a simple_marker for parachute style marker with pop-up text. 
# import folium package
import folium
 
my_map3 = folium.Map(location = [62.7330259,7.1452503],
                                        zoom_start = 15)
 
# Pass a string in popup parameter
folium.Marker([62.7330259,7.1452503],
               popup = ' Molde Aker Stadium ').add_to(my_map3)
 
 
my_map3.save(" my_map3.html ")






#4 : Add a line to the map
import folium
 
my_map4 = folium.Map(location = [62.7330259,7.1452503],
                                        zoom_start = 12)
 
folium.Marker([62.7330259,7.1452503],
              popup = 'Molde Aker Stadium').add_to(my_map4)
 
folium.Marker([62.4701708,6.1854081],
              popup = 'AAlesund Colorline Stadium').add_to(my_map4)
 
# Add a line to the map by using line method .
# it connect both coordinates by the line
# line_opacity implies intensity of the line
 
folium.PolyLine(locations = [(62.7330259,7.1452503), (62.4701708,6.1854081)],
                line_opacity = 0.5).add_to(my_map4)
 
my_map4.save("my_map4.html")
















### Lecture 13. Donut charts

#Creating a Simple Donut Chart
#Create a Pie Chart
#Draw a circle of suitable dimensions.
#Add circle at the Center of Pie chart

import matplotlib.pyplot as plt
 
# Setting labels for items in Chart
Familymember = ['Wilson', 'Dudu', 'Maomao',
            'Miaomiao', 'Mico', 'Mia']
 
# Setting size in Chart based on
# given values
Income = [32000, 20000, 22000, 10000, 8000, 3000]
 
# colors
colors = ['#FF0000', '#0000FF', '#FFFF00',
          '#ADFF2F', '#FFA500','#FF00FF',]
# explosion
explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05)


# Pie Chart
plt.pie(Income, colors=colors, labels=Familymember,
        autopct='%1.1f%%', pctdistance=0.85,
        explode=explode)
 
# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
#gcf() : get current figure
fig = plt.gcf()
 
# Adding Circle in Pie chart
#gca() : get current axes
fig.gca().add_artist(centre_circle)
 
# Adding Title of chart
plt.title('Employee Salary Details')
 
# Displaying Chart
plt.show()




#Customizing the Donut Chart
#Adding Legends to the Donut Chart 

import matplotlib.pyplot as plt
 
 
# Setting size in Chart based on
# given values
Income = [32000, 20000, 22000, 10000, 8000, 3000]
 
# Setting labels for items in Chart
Familymember = ['Wilson', 'Dudu', 'Maomao',
            'Miaomiao', 'Mico', 'Mia']
 
# colors
colors = ['#FF0000', '#0000FF', '#FFFF00',
          '#ADFF2F', '#FFA500','#FF00FF',]
 
# explosion
explode = (0.05, 0.05, 0.05, 0.05, 0.05,0.05)


# Pie Chart
plt.pie(Income, colors=colors, labels=Familymember,
        autopct='%1.1f%%', pctdistance=0.85,
        explode=explode)
 
# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()        #get the current figure
 
# Adding Circle in Pie chart
#gca() to get the current axes
fig.gca().add_artist(centre_circle)


# Adding Title of chart
plt.title('Family Member Income')
 
# Add Legends
plt.legend(Familymember, loc="upper right", title="Member Color")
 
# Displaying Chart
plt.show()






















### Lecture 14. Stack plot

#example 1. Family income
import matplotlib.pyplot as plt
 
# List of family member
Familymember = ['Wilson', 'Dudu', 'Maomao', 'Miaomiao', 'Mico', 'Mia']
 
# Income list
Salary = [7, 8, 6, 11, 7,5]
 
# Allowance list
Allowance =  [8, 5, 7, 8, 13,4]
 
# Stackplot with X, Y, colors value
plt.stackplot(Familymember, Salary, Allowance,
              colors =['r', 'c'])
 
# X label
plt.xlabel('Familymember')
 
# Y label
plt.ylabel('Income')
 
# Title of Graph
plt.title('Income of Salary and Allowance')
 
# Displaying Graph
plt.show()


## example 2. patients cases
import matplotlib.pyplot as plt
 
# List of 7-days
days = [x for x in range(0, 7)]
 
# List of Suspected cases
Suspected = [12, 18, 35, 50, 72, 90, 100]
 
# List of Cured Cases
Cured = [4, 8, 15, 22, 41, 55, 62]
 
# List of Number of deaths
Deaths = [1, 3, 5, 7, 9, 11, 13]
 
# Plot x-labels, y-label and data
plt.plot([], [], color ='blue',
         label ='Suspected')
plt.plot([], [], color ='orange',
         label ='Cured')
plt.plot([], [], color ='brown',
         label ='Deaths')
 
# Implementing stackplot on data
plt.stackplot(days, Suspected, Cured,
              Deaths, baseline ='zero',
              colors =['blue', 'orange',
                       'brown'])
 
plt.legend()
 
plt.title('No of Cases')
plt.xlabel('Day of the week')
plt.ylabel('Overall cases')
 
plt.show()




## example 3. Patient cases, value of baseline is set to sym 
import matplotlib.pyplot as plt
 
# List of 7-days
days = [x for x in range(0, 7)]
 
# List of Suspected cases
Suspected = [12, 18, 35, 50, 72, 90, 100]
 
# List of Cured Cases
Cured = [4, 8, 15, 22, 41, 55, 62]
 
# List of Number of deaths
Deaths = [1, 3, 5, 7, 9, 11, 13]
 
# Plot x-labels, y-label and data
plt.plot([], [], color ='blue',
         label ='Suspected')
plt.plot([], [], color ='orange',
         label ='Cured')
plt.plot([], [], color ='brown',
         label ='Deaths')
 
# Implementing stackplot on data
plt.stackplot(days, Suspected, Cured,
              Deaths, baseline ='sym',
              colors =['blue', 'orange',
                       'brown'])
 
plt.legend()
 
plt.title('No of Cases')
plt.xlabel('Day of the week')
plt.ylabel('Overall cases')
 
plt.show()














### Lecture 15. Box plot

# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
# example a simple boxplot for 1000 random numbers with
#normal distribution
# Creating dataset
np.random.seed(10)
data = np.random.normal(50, 10,1000 )
 
fig = plt.figure(figsize =(8, 6))
 
# Creating plot
plt.boxplot(data)
 
# show plot
plt.show()



#Customizing Box Plot
#The notch = True attribute creates the notch format to the box plot,
#patch_artist = True fills the boxplot with colors, 
#we can set different colors to different boxes.
#The vert = 0 attribute creates horizontal box plot. 
#labels takes same dimensions as the number data sets.

# Example 2 plot 4 boxplots in one plot
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
 
# Creating dataset
np.random.seed(10)
 
data_1 = np.random.normal(80, 5, 1000)
data_2 = np.random.normal(70, 10, 1000)
data_3 = np.random.normal(60, 15, 1000)
data_4 = np.random.normal(50, 20, 1000)
data = [data_1, data_2, data_3, data_4]
 
fig = plt.figure(figsize =(10, 7))
 
# Creating axes instance
#denoting the lower left point of the new axes in figure coodinates
# (0,0) and its width and height(1,1). 
ax = fig.add_axes([0, 0, 1, 1])
 
# Creating plot
bp = ax.boxplot(data)
 
# show plot
plt.show()






## example 3. customizing each box in plot

# Import libraries
import matplotlib.pyplot as plt
import numpy as np
 
# Creating dataset
np.random.seed(10)
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]
 
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)
 
# Creating axes instance
bp = ax.boxplot(data, patch_artist = True,
                notch ='True', vert = 0)
 
colors = ['#0000FF', '#00FF00',
          '#FFFF00', '#FF00FF']
 
#zip will create a list of tuple of (box, color)
#then set color for each box
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
 
# changing color and linewidth of
# whiskers
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")
 
# changing color and linewidth of caps
# (boundary for outlier)
for cap in bp['caps']:
    cap.set(color ='#8B008B',
            linewidth = 2)
 
# changing color and linewidth of
# medians
for median in bp['medians']:
    median.set(color ='red',
               linewidth = 3)
 
# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker ='D',
              color ='#e7298a',
              alpha = 0.5)
     
# x-axis labels
ax.set_yticklabels(['data_1', 'data_2',
                    'data_3', 'data_4'])
 
# Adding title
plt.title("Customized box plot")
 
# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
     
# show plot
plt.show()

















### Lecture 16. Plot Subplots Within Other Subplots

import matplotlib.pyplot as plt


# ## Multi-Panel Plots

# ### Display Subplots within Other Subplots


import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
inner_ax = fig.add_axes([0.6,0.6,0.25,0.25])

plt.show()



import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
inner_ax = fig.add_axes([0.6,0.6,0.25,0.25])
x1 = np.arange(10)
y1 = np.array([1,2,7,1,5,2,4,2,3,1])
x2 = np.arange(10)
y2 = np.array([1,3,4,5,4,5,2,6,4,3])
ax.plot(x1,y1)
inner_ax.plot(x2,y2)
plt.show()
















### Lecture 17. Drawing 2D Heatmap using Matplotlib in Python
#Basic Heatmap Using Python Matplotlib Library 
#Create a 10×10 Heatmap with Random data using Matplotlib

# Program to plot 2-D Heat map
# using matplotlib.pyplot.imshow() method
import numpy as np
import matplotlib.pyplot as plt
 
data = np.random.random(( 10 , 10 ))
plt.imshow( data )
 
plt.title( "2-D Heat Map" )
plt.show()



#Choosing Different Colormaps in Heatmap Using Matplotlib
# using the cmap parameter

# Program to plot 2-D Heat map
# using matplotlib.pyplot.imshow() method
import numpy as np
import matplotlib.pyplot as plt
 
data = np.random.random((10, 10))
plt.imshow(data, cmap='autumn')
 
plt.title("Heatmap with different color")
plt.show()


#Adding Colorbar to Heatmap Using Matplotlib to show the 
# weight of color relatively between a certain range.
# using plt.colorbar().

data = np.random.random((12, 12))
plt.imshow(data, cmap='autumn', interpolation='nearest')
 
# Add colorbar
plt.colorbar()
 
plt.title("Heatmap with color bar")
plt.show()



#Customized Heatmap 
#use plt.annotate()  to annotate values in the heatmap

import matplotlib.colors as colors
 
# Generate random data
data = np.random.randint(0, 100, size=(8, 8))
 
# Create a custom color map
# with blue and green colors
colors_list = ['#0099ff', '#33cc33']
cmap = colors.ListedColormap(colors_list)
 
# Plot the heatmap with custom colors and annotations
#vmin and vmax define the data range that the colormap covers. 
#extent: The bounding box in data coordinates that the image will fill.
plt.imshow(data, cmap=cmap, vmin=0, vmax=100, extent=[0, 8, 0, 8])
for i in range(8):
    for j in range(8):
        plt.annotate(str(data[i][j]), xy=(j+0.5, i+0.5),
                     ha='center', va='center', color='white')
 
# Add colorbar
cbar = plt.colorbar(ticks=[0, 50, 100])
cbar.ax.set_yticklabels(['Low', 'Medium', 'High'])
 
# Set plot title and axis labels
plt.title("Customized heatmap with annotations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
 
# Display the plot
plt.show()




# Heatmap Using Seaborn Library

# importing the modules
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
   
# generating 2-D 10x10 matrix of random numbers
# from 1 to 100
data = np.random.randint(low=1,
                         high=100,
                         size=(10, 10))
   
# plotting the heatmap
hm = sns.heatmap(data=data,
                annot=True)
   
# displaying the plotted heatmap
plt.show()































