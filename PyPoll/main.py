#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


csv_path = "election_data.csv"

election_df = pd.read_csv("election_data.csv")

election_df.head ()


# In[4]:


total_votes = election_df["Voter ID"].count()
total_votes


# In[49]:


vote_counts = pd.DataFrame(election_df["Candidate"].value_counts())
vote_counts.rename(columns={"Candidate": "Total Votes"}, inplace=True)
vote_counts


# In[60]:


vote_percent = vote_counts.apply(lambda x : x/x.sum())
vote_percent


# In[52]:


winner = vote_counts.iloc[0,:]
winner


# In[75]:


print ("Election Results")
print ("----------------")
print ("Total Votes", total_votes)
print ("----------------")
print (vote_counts)
print ("----------------")
print ("Winner", winner)


# In[ ]:




