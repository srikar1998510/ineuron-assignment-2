#!/usr/bin/env python
# coding: utf-8

# # Using generators

# In[9]:


def filter_long_words(l,n):
    for _ in l:
        if len(_)>n:
            yield _
print(list(filter_long_words(input().split(','),int(input()))))


# # Using filter function

# In[11]:


l1=input().split(',')
n=int(input())
print(list(filter(lambda x:len(x)>n,l1)))


# In[ ]:




