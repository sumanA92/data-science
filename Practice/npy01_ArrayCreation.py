#!/usr/bin/env python
# coding: utf-8

# ## Creating Numpy Arrays
# 
# 

# In[ ]:


get_ipython().system('pip install numpy --upgrade')


# In[ ]:


import numpy as np


# #### 1. Create an array from a regular Python list or tuple using the array function

# In[ ]:


array_one = np.array([1,2,3,4])
array_one


# ### Numpy Arrays are similar to python list but Numpy arrays has varities of function available to manipulate data which are not present in python list 

# In[ ]:


numbers = [9,8,7,6]
array_two = np.array(numbers)
array_two


# 
# #### 2. NumPy offers several functions to create arrays with initial placeholder content
# Create an array of zeros with desired shape (x,y)
# * x == number of rows
# * y == number of columns in array

# In[ ]:


array_of_zeroes = np.zeros((3,4))
array_of_zeroes


# In[ ]:


array_of_ones = np.ones((3,4))
array_of_ones


# ##### Use dtype in order to specify the data type

# In[ ]:


array_of_ones_int = np.ones((3,4),dtype=np.int16)
array_of_ones_int


# #### np.empty() is not the same as np.zeros()
# One may get the same output. But np.empty() returns a new array of given shape and type, without initializing entries (the entries may be zero but not always)
# <br />
# Used when you plan to populate the array but need to create one quickly first. If you want an array of zeros, use np.zeros()

# In[ ]:


array_empty = np.empty((2,3))  
array_empty


# #### np.eye() creates an eyedentity matrix

# In[ ]:


array_eye = np.eye(3)
array_eye


# #### 3. To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists

# arange(start, stop, step, dtype)

# In[ ]:


array_of_evens = np.arange(2, 20, 2)
array_of_evens


# #### It also accepts float arguments

# In[ ]:


array_of_floats = np.arange( 0, 2, 0.3)
array_of_floats


# #### Two Dimensional Arrays

# In[ ]:


array_2d = np.array([(2,4),(3,5)]) 
array_2d


# In[ ]:


array_2d.shape


# #### Using reshape to create n dimensional arrays

# In[ ]:


np.arange(6)


# In[ ]:


np.arange(6).shape


# In[ ]:


array_nd = np.arange(6).reshape(3,2) 
array_nd


# The reshape will only take arguments that multiply to the number in arange function.
# For example:
# for arange(8), the possible combinations for reshape are (2,4), (4,2), (2,2,2)

# In[ ]:


array_nd = np.arange(6).reshape(3,4) 
array_nd


# In[ ]:


array_nd


# <b>ones_like</b> : Produce an array of all 1’s with the given shape and dtype. ones_like takes another array and produces a ones array of the same shape and dtype. <br />
# There's also a zeros_like and empty_like

# In[ ]:


array_ones = np.ones_like(array_nd)
array_ones


# In[ ]:


array_zero = np.zeros_like(array_nd)
array_zero


# In[ ]:


array_empty = np.empty_like(array_nd)
array_empty


# In[ ]:


my_list = [1, 3, 5, 7, 9] 

out_arr = np.asarray(my_list) 
out_arr 


# In[ ]:


arr5 = np.linspace(0, 10, 5) # Start, Stop, No. of points to be created that will have equal difference; Start and Stop inclusive
arr5


# In[ ]:


diagMat = np.diag([1,2,3,4]) # Diagonal Matrix
diagMat


# In[ ]:


constMat = np.full(shape=(2,2), fill_value=4) # Constant matrix
constMat


# In[ ]:


zeroMat = np.zeros(shape=(4,4), dtype='int') # Zero matrix; np.empty(shape=(4,4), dtype='int')
zeroMat


# In[ ]:


oneZeroMat = np.eye(N=3, M=3) # Diag Ones and Else Zeros, Identity Matrix
oneZeroMat


# In[ ]:


randMat = np.random.rand(4,3) # Random Matrix with given shape; np.random.random(size=(2,2))
randMat


# ### Array creation functions

# <b>array</b> : Convert input data (list, tuple, array, or other sequence type) to an ndarray either by inferring a dtype or explicitly specifying a dtype. Copies the input data by default.
# 

# <b>asarray</b> : Convert input to ndarray, but do not copy if the input is already an ndarray

# <b>arange</b> : Like the built-in range but returns an ndarray instead of a list.

# <b>ones, ones_like</b> : Produce an array of all 1’s with the given shape and dtype. ones_like takes another array and produces a ones array of the same shape and dtype.

# <b>zeros, zeros_like</b> : Like ones and ones_like but producing arrays of 0’s instead

# <b>empty, empty_like</b> : Create new arrays by allocating new memory, but do not populate with any values like ones and zeros

# <b>eye, identity</b> : Create a square N x N identity matrix (1’s on the diagonal and 0’s elsewhere)

# In[ ]:




