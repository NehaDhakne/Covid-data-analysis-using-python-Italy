#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv(r"C:\Users\91950\Desktop\Data Science Project 1\italy.csv")


# In[3]:


data.head()


# In[4]:


data.columns


# In[5]:


data.tail()


# In[6]:


data.describe()


# In[7]:


data.isnull()


# In[8]:


data.isnull().sum()


# # relating the variables with scatterplots
# 

# In[9]:


sns.relplot(x="TotalPositiveCases", y="Recovered", data=data)


# In[10]:


sns.relplot(x="TotalPositiveCases", y="Deaths", data=data)


# In[11]:


sns.relplot(x="HospitalizedPatients",y="IntensiveCarePatients", data=data)


# In[12]:


sns.pairplot(data)


# In[13]:


sns.relplot(x="HomeConfinement", y="TotalPositiveCases", kind = "line" , data=data)


# In[15]:


sns.relplot(x="Date", y="NewPositiveCases", kind = "line", data=data)


# In[ ]:




