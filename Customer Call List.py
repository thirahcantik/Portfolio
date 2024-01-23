#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# Extract data from excel

# In[2]:


df = pd.read_excel(r"C:\Users\User\Desktop\pandas tutorial\Customer Call List.xlsx")
df


# remove duplicates

# In[3]:


df = df.drop_duplicates()
df


# remove unused column

# In[4]:


df = df.drop(columns = "Not_Useful_Column")
df


# fix last name

# In[6]:


df["Last_Name"] = df["Last_Name"].str.lstrip("...")
df["Last_Name"] = df["Last_Name"].str.lstrip("/")
df["Last_Name"] = df["Last_Name"].str.rstrip("_")
df["Last_Name"] = df["Last_Name"].str.strip("123._/")

df


# fix phone number

# In[15]:


#df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-z0-9]','', regex = True)

#df["Phone_Number"].apply(lambda x:x[0:3] + '-' + x[3:6] + '-' + x[6:10])

#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))

#df["Phone_Number"] = df["Phone_Number"].apply(lambda x:x[0:3] + '-' + x[3:6] + '-' + x[6:10])

#df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')

#df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')
df


# split address

# In[16]:


df[["Street_Address", "State","Zip_Code"]] = df["Address"].str.split(',',n = 2, expand=True)
df


# replace word

# In[17]:


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes','Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No','N')
df


# In[18]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')
df


# In[19]:


df = df.replace('N/a','')

df = df.fillna('')
df


# In[20]:


df


# filter data

# In[21]:


for x in df.index:
    if df.loc[x,"Do_Not_Contact"] == 'Y':    
     df.drop(x, inplace=True)
    
df


# In[22]:


for x in df.index:
    if df.loc[x,"Phone_Number"] == '':    
     df.drop(x, inplace=True)
    
df


# In[23]:


df.reset_index(drop = True)
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




