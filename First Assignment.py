#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Write a Python program to print the following string in a specific format (see the output). 
"""
Twinkle, twinkle, little star,  
      How I wonder what you are!   
          Up above the world so high,       
          Like a diamond in the sky.  
Twinkle, twinkle, little star,   
      How I wonder what you are
"""     

#CODE
       
print("Twinkle, twinkle, little star," '\n      ' "How I wonder what you are!" '\n            ' "Up above the world so high," '\n            ' "Like a diamond in the sky." '\n' "Twinkle, twinkle, little star," '\n      ' "How I wonder what you are")


# In[2]:


#2. Write a Python program to get the Python version you are using.

#CODE

import sys

print("Phython Version:")
print(sys.version)


# In[5]:


#3.Write a Python program to display the current date and time.

#CODE

from datetime import datetime as dt
now = dt.now()
print("Current Date and Time:",now)


# In[8]:


#4.Write a Python program which accepts the radius of a circle from the user and compute the area. 

#CODE

from math import pi
r = float(input ("Input the Radius of the Circle is : "))
print ("The Area of the Circle with Radius " + str(r) + " is: " + str(pi * r**2))


# In[9]:


#5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

#CODE

first_name="Asad"
last_name="Sheikh"
print(last_name+"   "+first_name)


# In[10]:


#6. Write a python program which takes two inputs from user and print them addition.

#CODE

a=int(input('Put the value of a:'))
b=int(input('Put the vallue of b:'))
c=a+b
print("Value of c is: ",c)


# In[ ]:




