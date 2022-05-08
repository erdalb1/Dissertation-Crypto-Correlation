#!/usr/bin/env python
# coding: utf-8

# In[213]:


# Importing relevant libraries for the analysis, cleansing and visualization purposes
# Dataset to be read with pandas
# df.head to be appliead to see if the dataset loaded correctly

import numpy as np
import pandas as pd
import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sb

from scipy import stats
import scipy.stats
from scipy.stats import pearsonr

import statsmodels.api as sm


df = pd.read_csv('ETH adjusted 2015.csv', index_col='Date', parse_dates=True)
df.head()


# In[214]:


# Columns strip to be applied for indentation in the column names

df.columns = df.columns.str.strip()

df.info()


# In[215]:


# Indentations and object values such as M and K to be removed
# as per below codes due to above df.info results showing all
# columns are object

df['Wallets'] = df['Wallets'].str.replace(" M","")
df['ATM'] = df['ATM'].str.replace(" K","")
df['BTC'] = df['BTC'].str.replace(" M","")
df['ETH'] = df['ETH'].str.replace(" M","")


# In[216]:


# data types to be converted from object to
# float as the numbers are in decimals

df['ATM'] = pd.to_numeric(df['ATM'],errors = 'coerce')
df['Wallets'] = pd.to_numeric(df['Wallets'],errors = 'coerce')
df['BTC'] = pd.to_numeric(df['BTC'],errors = 'coerce')
df['ETH'] = pd.to_numeric(df['ETH'],errors = 'coerce')


# In[217]:


#Checking for data type to see if they need any 
# durther adjustment for the analysis purposes

df.info()


# In[218]:


# Print the actual dataset to see how everything looks like

print(df)


# In[219]:


# Df.describe function to generate descriptive statistics.
# This include summary of the central tendency with count,
# mean, standard deviation, min, max values etc.

df.describe()


# In[228]:


# Here matplotlib and pandas vizualisation tools 
# are utilized to see how data visually looks like.
# As the data were adjusted earlier in Microsoft Excel
# numbers are not far from each other drastically.
# However y axis here indexed to the highest available
# number in the dataset that is Ethereum going up to
# 180 millions. All the data are shown in the table below
# how they increase over the years that is Date in the x axis

df.plot()
plt.show()


# In[229]:


# Similar to above but this time logaritmic option is utilized
# to see the changes in the dataset closely

df.plot()

plt.yscale('log')
plt.show()


# In[222]:


# Here correlation beteween each variable
# with the pandas df.corr function is presented
# in one table

df.corr()


# In[208]:


# p-values for each correlation calculated
# separately in below lines and printed separately


# In[209]:


r, p = stats.pearsonr(df.ATM, df.Wallets)
print('correlation:', round(r, 4))
print('p-value:', round(p, 35))


# In[210]:


r, p = stats.pearsonr(df.ATM, df.BTC)
print('correlation:', round(r, 4))
print('p-value:', round(p, 35))


# In[211]:


r, p = stats.pearsonr(df.ATM, df.ETH)
print('correlation:', round(r, 4))
print('p-value:', round(p, 35))


# In[212]:


# Using pairplot function from seaborn library
# to see relationship between variables in scattere plots
# and histogram plots. Histogram plots are in the middle
# shows the distribution of the individual column/dataset.
# The rest of the scatter plots shows the jointn distribution
# of each two of the variables. This is a great way to see
# the correlational relationship between variables

sb.pairplot(df)


# In[149]:


# Similar to above, but in this one kind="reg" function
# vizualises the regressional relationship outside the
# diagonal line in below plots. As the distribution
# is closer to the slope, it shows a stronger
# correlational relationship

sb.pairplot(df, kind="reg")


# In[ ]:




