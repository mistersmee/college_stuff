#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sms
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


df = pd.read_csv('~/AM37/zomato.csv', encoding='unicode_escape')


# In[18]:


df


# In[19]:


df.head(5)


# In[20]:


df.tail(5)


# In[15]:


df.describe()


# In[16]:


df.isnull()


# df.isnull().sum()>0

# In[17]:


df.isnull().sum()>0


# In[21]:


df.count()


# In[22]:


df.isnull().count()


# In[24]:


df.shape


# In[25]:


df.isnull().sum()


# In[29]:


[features for features in df.columns if df[features].isnull().sum()>0]


# sms.heatmap(df.isnull())

# In[31]:


sms.heatmap(df.isnull(),yticklabels=False)

