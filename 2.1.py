#!/usr/bin/env python
# coding: utf-8

# # Using ananymous function

# In[3]:


op=list(map(lambda x:len(x),input().split(',')))
op


# # Using generator

# In[5]:


def func(l):
    for _ in l:
        yield len(_)
l=input().split(',')
list(func(l))
    
    


# In[ ]:




