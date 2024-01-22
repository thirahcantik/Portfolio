#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_universities_in_Malaysia'


# In[3]:


page = requests.get(url)


# In[4]:


soup = BeautifulSoup(page.text, 'html')


# In[5]:


print(soup.prettify())


# In[6]:


table = soup.find_all('table')[1]


# In[7]:


print(table)


# In[8]:


soup.find_all('th')


# In[9]:


companies = table.find_all('th')


# In[10]:


companies


# In[11]:


companies_table = [title.text.strip() for title in companies]

print(companies_table)


# In[12]:


import pandas as pd


# In[13]:


df = pd.DataFrame(columns = companies_table)

df


# In[14]:


column_data = table.find_all('tr')


# In[15]:


column_data


# In[16]:


for row in column_data[1:]:
    row_data = (row.find_all('td'))
    details_row_data= [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = details_row_data


# In[17]:


df


# In[20]:


df.to_csv(r'C:\Users\User\Desktop\SEM 9\portfolio\Politeknik3.csv', index = False)

