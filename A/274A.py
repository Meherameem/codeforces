#!/usr/bin/env python
# coding: utf-8

# In[1]:


s = input()
s = int(s)
s = s + 1
x = 1
while x == 1:
    p = len(set(str(s)))
    if len(str(s)) == p:
        print(s)
        x = 2

    else:
        s = int(s) + 1

# In[ ]:

