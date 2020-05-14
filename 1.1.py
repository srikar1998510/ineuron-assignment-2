#!/usr/bin/env python
# coding: utf-8

# In[20]:


class sides:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
class area(sides):
    def ar(self):
        p,q,r=self.a,self.b,self.c
        s=(p+q+r)/2
        return pow(s*(s-p)*(s-q)*(s-r),0.5)
a=area(int(input()),int(input()),int(input()))
a.ar()
        


# In[ ]:





# In[ ]:




