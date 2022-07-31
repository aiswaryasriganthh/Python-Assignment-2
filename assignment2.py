#!/usr/bin/env python
# coding: utf-8

# #                                       PYTHON ASSIGNMENT-2
# 
# 
# 
# 
# # 1. REGULAR EXPRESSION
# 

# #findall() function
#  
# import re
# text = "Python assignment"
# x = re.findall("n",text)
# print(x)

# In[7]:


#serach() function

import re
text = "Python assignment"
x = re.search("Python", text)
x


# In[9]:


#split() function

import re
text = "Python assignment"
x = re.split("\s",text)
x


# In[10]:


#sub() function

import re
text = "Python assignment"
x = re.sub("a","A",text)
x


# # 2. AGGREGATE FUNCTIONS
# **i) ONE DIMENSIONAL ARRAY**

# In[18]:


import numpy as np
a = np.random.randint(1,10,4)
a


# In[20]:


#sum() function

x=np.sum(a)
x


# In[21]:


#min() function

x=np.min(a)
x


# In[22]:


#max() function

x=np.max(a)
x


# In[23]:


#prod() function
x=np.prod(a)
x


# In[29]:


#mean
x=np.mean(a)
x


# In[25]:


#standard deviation
x=np.std(a)
x


# In[26]:


#variance
x=np.var(a)
x


# In[27]:


#index of minimum value
x=np.argmin(a)
x


# In[28]:


#index of maximum value
x=np.argmax(a)
x


# In[30]:


#median
x=np.median(a)
x


# In[32]:


x=np.any(a)
x


# In[33]:


x=np.all(a)
x


#  **ii)MULTI-DIMENSIONAL ARRAY**

# In[35]:


A =np.random.randint(10,50,(3,4))
A


# In[46]:


#sum() function
x=A.sum()
y=A.sum(axis=0)
z=A.sum(axis=1)
print(x)
print(y)
print(z)


# In[49]:


#product function

x=np.prod(A)
y=np.prod(A,axis=0)
z=np.prod(A,axis=1)
print(x)
print(y)
print(z)


# In[50]:


#mean

x=np.mean(A)
x


# In[51]:


#standard deviation

x=np.std(A)
x


# In[52]:


#variance
np.var(A)


# In[55]:


#minimum
x=np.min(A)
x


# In[57]:


#maximum

np.max(A)


# In[58]:


#index of minimum value
np.argmin(A)


# In[59]:


#index of maximum value
np.argmax(A)


# In[60]:


#median
np.median(A)


# In[68]:


#percentile
np.percentile(A,3)


# In[63]:


np.any(A)


# In[64]:


np.all(A)


# # 3. EXCEPTION HANDLING

# In[77]:


print(Y)


# In[74]:


x = "hi"
print x


# In[76]:


x = 5/0
print(x)


# In[79]:


arr_1 = [10,20,30,40,50]
print(arr_1[5])


# In[84]:


import nomodule


# In[85]:


x = 100
if(x>99):
    print(greater)


# # 4. COMPARISON , MASKS AND BOOLEAN ARRAYS

# In[87]:


import numpy as np
import pandas as pd
s = np.array([1,2,3,4,5])


# In[92]:


#equal
s == 3


# In[93]:


#not equal
s != 4


# In[94]:


#greater than or equal to
s >= 5


# In[96]:


#less than or equal to
s <= 1


# In[97]:


#greater than
s > 0


# In[98]:


#less than
s < 0


# In[99]:


#compound expressions
(5 * s) == (s ** 5)


# In[104]:


x = np.random.randint(1,10,(3,4))
x


# In[105]:


x < 5


# In[106]:


np.sum(x < 6)


# In[107]:


np.sum(x < 6, axis=1)


# In[108]:


np.any(x > 8)


# In[109]:


np.any(x < 0)


# In[110]:


np.all(x < 10)


# In[111]:


np.all(x == 6)


# In[112]:


np.all(x < 8, axis=1)


# In[118]:


#boolean operators


# In[121]:


bool(0),bool(10)


# In[122]:


bool(0 and 10)


# In[123]:


bool(0 or 100)


# In[126]:


x = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
y = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
x & y


# In[127]:


x = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
y = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
x | y


# In[130]:


x = np.arange(5)
(x > 4) & (x < 2)


# # 5. INHERITANCE

# In[142]:


class parent:
    def __init__(self,name,age):
        self.pname = name
        self.page = age
    
    def displayAge(self):
        print("Age:",self.page)
        
ob = parent("Father",40)
print("Parent:",ob.pname)
ob.displayAge()


# In[143]:


#single inheritance

class Parent():
       def first(self):
           print('this is a parent class')
class Child(Parent):
       def second(self):
          print('this is a child class')
 
object = Child()
object.first()
object.second()


# In[145]:


#multilevel inheritance

class Parent:
      def myfunc1(self):
          print("this is Parent class")
class Child(Parent):
      def myfunc2(self):
          print("this is Child class")
class Child2(Child):
      def myfunc3(self):
        print("this is Another child class")
object = Child2()
object.myfunc1()
object.myfunc2()
object.myfunc3()


# In[146]:


#multiple inheritance

class Parent:
   def func1(self):
        print("parent class")
class Parent2:
   def func2(self):
        print("another parent class")
class Child(Parent , Parent2):
    def func3(self):
        print("child class")
 
object = Child()
object.func1()
object.func2()
object.func3()


# In[ ]:




