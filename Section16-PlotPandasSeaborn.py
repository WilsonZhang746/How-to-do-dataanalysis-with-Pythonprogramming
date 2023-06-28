# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""



### Section 16. Plotting with Pandas and Seaborn

## Lecture 1. Line Plots and Bar Plots with Pandas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

#line plot of a Series
s = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
s.plot(title='Cumulative Random Number')



#Line plot of a DataFrame


data = {'length' : [28, 56, 32, 77, 62,45, 21, 43 ],
        'weight' : [150, 221, 123, 173, 293, 98, 78, 108],
        'price' : [1.2, 1.0, 0.6, 0.9, 1.7,1.4,0.9,1.8]}
frame = pd.DataFrame(data)
frame
frame.plot(figsize = (10,6), title = 'Product Information')

#Line plot of one variable of a DataFrame
frame.plot(y='price',figsize = (10,6), title = 'Product Information', ylabel='USD')


# Bar Plots of 2 Series in each subplot

fig, axes = plt.subplots(2, 1)
data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
data.plot.bar(ax=axes[0], color='k', alpha=0.7)
data.plot.barh(ax=axes[1], color='k', alpha=0.7)





np.random.seed(12348)

#bar plot of DataFrame

df = pd.DataFrame(np.random.rand(6, 4),
                  index=['one', 'two', 'three', 'four', 'five', 'six'],
                  columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df
df.plot.bar(title='Product Info')


plt.figure()



#Horizontal stacked barplot of DataFrame

df.plot.barh(stacked=True, alpha=0.5, title='Product Info')



plt.close('all')




# Bar plot, Normalizing to sum to 1 each row

df = pd.DataFrame(np.random.rand(6, 4),
                  index=['one', 'two', 'three', 'four', 'five', 'six'],
                  columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df

df_norm = df.div(df.sum(1), axis=0)
df_norm
df_norm.plot.bar(title='Product Info(in percentage)')




plt.close('all')

















### Lecture 2. Swarm plot using Seaborn

# Example 1: Basic visualization of “fmri” dataset using swarmplot() 

import seaborn
 
 
seaborn.set(style='whitegrid')
fmri = seaborn.load_dataset("fmri")
 
seaborn.swarmplot(x="timepoint",
                  y="signal",
                  data=fmri,
                  palette="Set2",
                  s=1.5)



#Example 2: Grouping data points on the basis of category, 
#here as region and event.

import seaborn
 
 
seaborn.set(style='whitegrid')
fmri = seaborn.load_dataset("fmri")
 
seaborn.swarmplot(x="timepoint",
                  y="signal",
                  hue="region",
                  data=fmri,
                  palette="Set2",
                  s=5)



#Example 3. students scores by gender and country
import numpy as np
import pandas as pd
#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)

dataset = pd.read_csv("./University-Fullname-3column.csv")

dataset.head()

seaborn.swarmplot( x ='Gender', y= 'Math', hue='Country', data=dataset,
         palette="Set2", dodge=True, s=10)















### Lecture 3. Joint plot using Seaborn

#seaborn.jointplot(x,  y,  data, stat_func)

#example 1, a basic Joint plot
import seaborn as sns
import matplotlib.pyplot as plt


import numpy as np
import pandas as pd
#setting working directory
import os
work_path="d:\\PythonBeginningCourse"
os.chdir(work_path)

dataset = pd.read_csv("./University-Fullname-full.csv")

dataset.head()

list(dataset.columns)


sns.jointplot(x = "Math", y = "Physics",
               data = dataset)
# show the plot
plt.show()


#example 2. add hue for grouping
sns.jointplot(x = "Math", y = "Physics",
               data = dataset, hue='Gender')
# show the plot
plt.show()


#example 3: add regression line
sns.jointplot(x = "Math", y = "Physics",
               data = dataset, kind='reg')
# show the plot
plt.show()

  


## example 4. Add hex kind
sns.jointplot(x = "Math", y = "Physics",
               data = dataset, kind='hex')
# show the plot
plt.show()



## example 5. Add kde kind
sns.jointplot(x = "Math", y = "Physics",
               data = dataset, kind='kde')
# show the plot
plt.show()






















### Lecture 2. Seaborn plotting tutorial

#Getting Started
#a simple line plot using the iris dataset
import seaborn as sns 
  
# loading dataset 
data = sns.load_dataset("iris") 
  
# draw lineplot 
sns.lineplot(x="sepal_length", y="sepal_width", data=data)


#Using Seaborn with Matplotlib
#invoke the Seaborn Plotting function as normal, and then we 
#can use Matplotlib’s customization function.

#using the above example and will add the title to the plot 
#using the Matplotlib.

# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
  
# loading dataset 
data = sns.load_dataset("iris") 
  
# draw lineplot 
sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
  
# setting the title using Matplotlib
plt.title('Title using Matplotlib and Seaborn')
  
plt.show()


#Setting the xlim and ylim
# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
  
# loading dataset 
data = sns.load_dataset("iris") 
  
# draw lineplot 
sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
  
# setting the x limit of the plot
plt.xlim(5)
  
plt.show()




#Customizing Seaborn Plots
#Changing Figure Aesthetic
#There are five themes available in Seaborn.
#darkgrid
#whitegrid
#dark
#white
#ticks

#Using the dark theme

# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
  
# loading dataset 
data = sns.load_dataset("iris") 
  
# draw lineplot 
sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
  
# changing the theme to dark
sns.set_style("dark")
plt.show()



#Removal of Spines
#Spines are the lines noting the data boundaries and connecting 
#the axis tick marks. It can be removed using the despine() method.
# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
  
# loading dataset 
data = sns.load_dataset("iris") 
  
# draw lineplot 
sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
  
# Removing the spines
sns.despine()
plt.show()




#Changing the figure Size
#The figure size can be changed using the figure() method of Matplotlib
# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
  
# loading dataset 
data = sns.load_dataset("iris") 
  
# changing the figure size
plt.figure(figsize = (2, 4))
  
# draw lineplot 
sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
  
# Removing the spines
sns.despine()
  
plt.show()


#Scaling the plots
#It can be done using the set_context() method. It allows us to 
#override default parameters. This affects things like the 
#size of the labels, lines, and other elements of the plot, 
#but not the overall style. The base context is “notebook”, 
#and the other contexts are “paper”, “talk”, and “poster”. 
#font_scale sets the font size.

# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
  
# loading dataset 
data = sns.load_dataset("iris") 
  
# draw lineplot 
sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
  
# Setting the scale of the plot
sns.set_context("paper")
  
plt.show()



#Setting the Style Temporarily
#axes_style() method is used to set the style temporarily. 
#It is used along with the with statement.
# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
  
# loading dataset 
data = sns.load_dataset("iris") 
  
  
def plot():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
  
with sns.axes_style('darkgrid'):
      
    # Adding the subplot
    plt.subplot(211)
    plot()
      
plt.subplot(212)
plot()



#Color Palette
#Colormaps are used to visualize plots effectively and easily. 
#One might use different sorts of colormaps for different kinds 
#of plots. color_palette() method is used to give colors to the plot. 
#Another function palplot() is used to deal with the color palettes 
#and plots the color palette as a horizontal array.


# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt
  
# current colot palette
palette = sns.color_palette()
  
# plots the color palette as a
# horizontal array
sns.palplot(palette)
  
plt.show()



#Diverging Color Palette
#This type of color palette uses two different colors where 
#each color depicts different points ranging from a common 
#point in either direction. Consider a range of -10 to 10 so the 
#value from -10 to 0 takes one color and values from 0 to 10 take 
#another.

#In the following example, we use an in-built diverging color 
#palette which shows 11 different points of color. The color 
#on the left shows pink color and color on the right shows 
#green color.

# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt
  
# current colot palette
palette = sns.color_palette('PiYG', 11)
  
# diverging color palette
sns.palplot(palette)
  
plt.show()





#Sequential Color Palette
#A sequential palette is used where the distribution ranges from 
#a lower value to a higher value. To do this add the character 
#‘s’ to the color passed in the color palette.
# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt
  
# current colot palette
palette = sns.color_palette('Greens', 11)
  
# sequential color palette
sns.palplot(palette)
  
plt.show()




#Setting the default Color Palette
#set_palette() method is used to set the default color palette 
#for all the plots. The arguments for both color_palette() and 
#set_palette() is same. set_palette() changes the default 
#matplotlib parameters.

# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt
  
# loading dataset 
data = sns.load_dataset("iris") 
  
def plot():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)
  
# setting the default color palette
sns.set_palette('vlag')
plt.subplot(211)
  
# plotting with the color palette
# as vlag
plot()
  
# setting another default color palette
sns.set_palette('Accent')
plt.subplot(212)
plot()
  
plt.show()



#Multiple plots with Seaborn

#Using Matplotlib

#Using add_axes() method
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
  
  
# loading dataset
data = sns.load_dataset("iris")
  
def graph():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)
  
# Creating a new figure with width = 5 inches
# and height = 4 inches
fig = plt.figure(figsize =(5, 4)) 
  
# Creating first axes for the figure
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 
  
# plotting the graph
graph()
  
# Creating second axes for the figure
ax2 = fig.add_axes([0.5, 0.5, 0.3, 0.3])
  
# plotting the graph
graph()
  
plt.show()
 



#Using subplot() method
# importing packages 
import seaborn as sns 
import matplotlib.pyplot as plt
  
# loading dataset 
data = sns.load_dataset("iris") 
  
def graph():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)
  
# Adding the subplot at the specified
# grid position
plt.subplot(121)
graph()
  
# Adding the subplot at the specified
# grid position
plt.subplot(122)
graph()
  
plt.show()
 
 

#Using subplot2grid() method
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
  
# loading dataset
data = sns.load_dataset("iris")
  
def graph():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)
  
# adding the subplots
axes1 = plt.subplot2grid (
  (7, 1), (0, 0), rowspan = 2,  colspan = 1) 
graph()
  
axes2 = plt.subplot2grid (
  (7, 1), (2, 0), rowspan = 2, colspan = 1) 
graph()
    
axes3 = plt.subplot2grid (
  (7, 1), (4, 0), rowspan = 2, colspan = 1)
graph()





#Using Seaborn 

#Using FacetGrid() method

#FacetGrid class helps in visualizing distribution of one variable
# as well as the relationship between multiple variables separately
# within subsets of your dataset using multiple panels.
#A FacetGrid can be drawn with up to three dimensions ? row, col, 
#and hue. The first two have obvious correspondence with the 
#resulting array of axes; think of the hue variable as a third 
#dimension along a depth axis, where different levels are plotted 
#with different colors.
#FacetGrid object takes a dataframe as input and the names of 
#the variables that will form the row, column, or hue dimensions 
#of the grid. The variables should be categorical and the data at 
#each level of the variable will be used for a facet along that axis.

# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
  
# loading dataset
data = sns.load_dataset("iris")
  
plot = sns.FacetGrid(data, col="species")
plot.map(plt.plot, "sepal_width")
  
plt.show()
 


#Using PairGrid() method
#Subplot grid for plotting pairwise relationships in a dataset.
#This class maps each variable in a dataset onto a column and 
#row in a grid of multiple axes. Different axes-level plotting 
#functions can be used to draw bivariate plots in the upper and 
#lower triangles, and the marginal distribution of each variable 
#can be shown on the diagonal.
#It can also represent an additional level of conventionalization 
#with the hue parameter, which plots different subsets of data 
#in different colors. This uses color to resolve elements on a 
#third dimension, but only draws subsets on top of each other 
#and will not tailor the hue parameter for the specific visualization
#the way that axes-level functions that accept hue will.


# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
  
# loading dataset
data = sns.load_dataset("flights")
  
plot = sns.PairGrid(data)
plot.map(plt.plot)
  
plt.show()





#Creating Different Types of Plots






































































