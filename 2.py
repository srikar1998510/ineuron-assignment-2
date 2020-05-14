#!/usr/bin/env python
# coding: utf-8

# # List Comprehensions

# In[1]:


[_ for _ in 'ACADGILD']


# In[4]:


[a*b for a in 'xyz' for b in range(1,5)]


# In[5]:


[a*b for a in range(1,5) for b in 'xyz']


# In[8]:


[[i+j] for j in range(3) for i in range(2,5)]


# In[11]:


[[i+j for i in range(2,6)] for j in range(4)]


# In[13]:


[(i,j) for j in range(1,4) for i in range(1,4)]


# In[ ]:




