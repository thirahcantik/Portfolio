#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_excel(r"C:\Users\User\Downloads\population_state.xlsx")
df = df.set_index('state')
df


# In[5]:


#delete all word with overall

df = df[~df.apply(lambda row: row.astype(str).str.contains('overall').any(), axis=1)]
df


# In[10]:


#replace 00:00:00 to none value
df['age'] = df['age'].str.replace(' 00:00:00', '')


# In[11]:


df


# In[12]:


#delete Nan Values
df = df.dropna(subset=['age'])
df


# In[13]:


df.plot(kind='line', subplots=True, figsize= (10, 10))


# In[49]:


ethnicity_counts = df['ethnicity'].value_counts()
ethnicity_counts


# In[ ]:


df['population'].plot(kind = 'bar', stacked = True)


# In[ ]:




