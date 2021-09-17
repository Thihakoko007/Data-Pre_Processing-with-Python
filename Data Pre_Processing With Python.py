#!/usr/bin/env python
# coding: utf-8

# In[8]:


#inviting padas library
import pandas as pd

# Getting csv data file from myanmar data science git hub 
data = pd.read_csv('https://raw.githubusercontent.com/myanmards/resource_files/master/sample-clean.csv')

#Checking the first 5 rows from a data set
data.head()


# In[9]:


#To know total number of rows in each column from a data set
data.count()


# In[10]:


#deleting the rows which include missing value 
data.dropna()


# In[11]:


#deleting the columns which include missing value
data.dropna(axis=1)


# In[12]:


#pulling out the rows which includ missing value
data[data.isnull().any(axis=1)]


# In[13]:


# filling the missing value from weight column with it's mean value
avg_weight = round (data['weight'].mean(), 2)
data['weight'] = data['weight'].fillna(avg_weight)
data.head(20)


# In[14]:


#checking whether weight column has missing value

data.count()


# In[15]:


# pulling out the unique value from birth place column
data.birth_place.unique()


# In[17]:


# Standardization 'NY' to 'New York', 'LA' to 'Los Angeles', ' WDC' to 'Washington D.C.'

data['birth_place'] = data['birth_place'].str.replace('NY','New York')
data['birth_place'] = data['birth_place'].str.replace('LA','Los Angeles')
data['birth_place'] = data['birth_place'].str.replace('WDC','Washington D.C.')


# In[18]:


# checking whether standardization is successful

data.birth_place.unique()


# In[19]:


# changing weight columns from kilograms(kg) to pounds(lb)

data['weight'] = data['weight'] * 2.205
data.head()


# In[ ]:




