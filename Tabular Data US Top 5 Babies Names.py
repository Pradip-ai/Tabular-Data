#!/usr/bin/env python
# coding: utf-8

# In[3]:



import pandas as pd


# In[6]:


us_babies = pd.read_csv("us_baby_name.csv")  #reading us baby name 


# In[9]:


us_babies.head()  #Top 5 rows and column


# In[7]:


us_babies


# In[10]:


#The 5 most popular baby names in 2014 in US?
#slice out rows for 2014
#sort rows in descending order by count
#top 1st five rows


us_babies['Year']


# In[11]:


us_babies['Year']==2014


# In[13]:


us_babies_2014 = us_babies.loc[us_babies['Year']==2014, :]  #Only get the rows where the year is 2014 and column is added at the end


# In[14]:


us_babies_2014


# In[17]:


#sorting the rows in descending order by the count column
sorted_us_babies_2014 = us_babies_2014.sort_values('Count',ascending = False)


# In[18]:


sorted_us_babies_2014


# In[19]:


sorted_us_babies_2014.head()   #Top 5 most popular name in us


# In[ ]:





# In[ ]:




