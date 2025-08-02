#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('mymoviedb.csv', lineterminator = '\n')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df['Genre'].head()


# In[6]:


df.duplicated().sum()


# In[7]:


df.describe()


# Exploration Summary
# 
# we have a dataframe consisting of 9827 rows and 9 columns.
# 
# our dataset looks a bit tidy with no NaNs nor duplicated values.
# 
# Release Date column needs to be casted into date time and to extract only the year value.
# 
# Overview, Original_Languege and Poster-Url wouldn't be so useful during analysis, so we'll drop them.
# 
# there is noticable outliers in Popularity column
# 
# Vote_Average bettter be categorised for proper analysis.
# 
# Genre column has comma saperated values and white spaces that needs to be handled and casted into category. Exploration Summary

# In[8]:


df['Release_Date'] = pd.to_datetime(df['Release_Date'])
print(df['Release_Date'].dtypes)


# In[9]:


df['Release_Date'] = df['Release_Date'].dt.year
df['Release_Date'].dtypes


# In[10]:


df.head()


# Dropping the Columns

# In[11]:


cols = ['Overview', 'Original_Language','Poster_Url' ]


# In[12]:


df.drop(cols, axis = 1, inplace = True)
df.columns


# In[13]:


df.head()


# # Categorizing vote_average Columns
# 

# We would cut the Vote_Average values and make 4 categories: popular average below_avg not_popular to describe it more using catigorize_col() function provided above.

# In[20]:


def categorize_col(df, col, labels):
    edges = [df[col].describe()['min'],
            df[col].describe()['25%'],
            df[col].describe()['50%'],
            df[col].describe()['75%'],
            df[col].describe()['max']]
    df[col] = pd.cut(df[col], edges, labels = labels, duplicates = 'drop')
    return df


# In[21]:


labels = ['not_popular', 'below_avg', 'average', 'popular']
categorize_col(df, 'Vote_Average', labels)
df['Vote_Average'].unique()


# In[22]:


df.head()


# In[23]:


df['Vote_Average'].value_counts()


# In[24]:


df.dropna(inplace=True)

df.isna().sum()


# we would split genre into a list and then explode our dataframe to have only one genre per row for each movie
# 

# In[25]:


df['Genre'] = df['Genre'].str.split(', ')
df = df.explode('Genre').reset_index(drop=True)
df.head()


# In[26]:


#casting column into category
df['Genre'] = df['Genre'].astype('category')
df['Genre'].dtypes


# In[27]:


df.info()


# In[28]:


df.nunique()


# In[29]:


df.head()


# # # Data Visualization
# 

# In[30]:


sns.set_style('whitegrid')


# # What is the most frequent genre of movies released on Netflix?

# In[31]:


sns.catplot(y = 'Genre', data = df, kind = 'count',
           order = df['Genre'].value_counts().index,
           color = '#4287f5')
plt.title('Genre column distribution')
plt.show()


# # Which has highest votes in vote avg column?
# ![image.png](attachment:image.png)

# In[33]:


sns.catplot(y = 'Vote_Average', data = df, kind = 'count', 
           order = df['Vote_Average'].value_counts().index,
           color = '#4287f5')
plt.title('Votes Distributions')
plt.show()


# # What movie got the highest popularity? what's its genre?
# ![image.png](attachment:image.png)
# 

# In[35]:


df[df['Popularity'] == df['Popularity'].max()]


# # What movie got the lowest popularity? what's its genre?
# ![image.png](attachment:image.png)

# In[36]:


df[df['Popularity'] == df['Popularity'].min()]


# # Which year has the most filmmed movies?
# ![image.png](attachment:image.png)

# In[37]:


df['Release_Date'].hist()
plt.title('Release date column distribution')
plt.show()


# In[ ]:




