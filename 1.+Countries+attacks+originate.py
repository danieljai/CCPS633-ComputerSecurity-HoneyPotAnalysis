
# coding: utf-8

# ## 1) From which countries do the attacks originate from (Top 25)?  
# 
# a. What type of data do you include/exclude?  
# b. What data (if any) would throw your results off?  
# c. Support your decision(s).

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)

df = pd.read_csv("sorted-AllTraffic.csv",sep='\t', lineterminator='\n',dtype='str')


# In[2]:


df_tor = pd.read_csv("Tor_IPs.csv",sep=',', lineterminator='\n',dtype='str')


# In[3]:


df_tor['source_ip'] = df_tor['Tor_IP']
df_tor['year'] = df_tor['Tor_Year']
df_tor['month'] = df_tor['Tor_Month']
df_tor['day'] = df_tor['Tor_Day\r']


# In[4]:


df_merge = pd.merge(df,df_tor,on=['source_ip','year','month','day'],how="left")


# In[5]:


df_merge[(df_merge.Tor_IP.isna()) & ~(df_merge.country.isna())].country.value_counts().head(25)

