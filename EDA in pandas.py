#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"C:\Users\User\Desktop\pandas tutorial\world_population.csv")
df


# In[3]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[4]:


df


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[28]:


df.nunique()


# In[29]:


df


# In[30]:


df.sort_values(by = "2022 Population", ascending = False).head(10)


# In[31]:


df2 = df.groupby('Continent').max().sort_values(by = "2022 Population", ascending = False)
df2


# In[34]:


df[df['Continent'].str.contains('Oceania')]


# In[35]:


df2.plot()


# In[36]:


df2.transpose()


# In[37]:


df.columns


# In[38]:


df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population',]].mean().sort_values(by = "2022 Population", ascending = False)
df2


# In[39]:


df2.transpose()


# In[41]:


df3 = df2.transpose()


# In[44]:


df3.plot()


# In[43]:


df.boxplot(figsize = (20,10))

