#!/usr/bin/env python
# coding: utf-8

# In[160]:


import pandas as pd
import numpy as np


# In[162]:


df = pd.read_csv("budget_data.csv")
df


# In[164]:


Months = df["Date"].count()
Months


# In[115]:


Balance = df["Profit/Losses"].sum()
Balance


# In[169]:


Change = df["Profit/Losses"].diff()
Change

Avg_Change = Change.mean()
Avg_Change


# In[170]:


Increase = Change.max()
Increase


# In[171]:


Decrease = Change.min()
Decrease


# In[179]:


summary = (
    "Months : 86",
    "Net Balance : $38,382,578",
    "Average Change : -$2,315", 
    "Greatest Increase : $1,926,159",
    "Greatest Decrease : -$2,196,167"
)


# In[182]:


print ("Financial Analysis")
print ("------------------")
print (summary)

