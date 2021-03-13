#!/usr/bin/env python
# coding: utf-8

# In[71]:


sal       = 3.25
hike      = 0.2
inflation = 0.04
years     = 6
sum       = 0
start_year = 2017
mon="Jul"
future_year = start_year + years
def hiked(sal):return sal*(1+hike+inflation)
for i in range(1,years+1):
    print(f'The Salary in year ==> {i} : {mon}-{start_year+i-1} is {round(sal,2)} L')
    sum=sum+round(sal,2)
    sal = hiked(sal)
print('\n')    
print(f'The total earned amount from {mon}-{start_year} to {mon}-{future_year} is {sum} L')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




