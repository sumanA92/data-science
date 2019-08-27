#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


numArr = np.loadtxt(fname="winequality-red.csv", delimiter=',', skiprows=1) # Load Numeric Data file into array
numArr


# In[ ]:


numArr[0:5, 0:5]


# In[ ]:


numArr = np.loadtxt(fname="winequality-red.csv", delimiter=',') # error as it will try to load file as data type float and we are not skipping the header which is in string 
numArr


# In[ ]:


numArr = np.loadtxt("winequality-red.csv",dtype='str',delimiter=',') # Changed the data type 
numArr


# ### Another way to load file using numpy.genfromtxt
# 
# In order to load data with Numpy, you can use the functions numpy.genfromtxt or numpy.loadtxt, where the difference is that np.genfromtxt can read CSV files with missing data and gives you options like the parameters missing_values and filling_values that help with missing values in the CSV. The loading of our data in previous recipe can be done in one step by
# 
# data = np.loadtxt(data_path, delimiter=',', skiprows=1)
# or with the more powerful nunmpy.genfromtxt
# 
# data = np.genfromtxt(datas_path, delimiter=',', names=True)
# 
# where the names argument specifies to load the header, which enables us to access the columns with their header names

# In[ ]:


numArr = np.genfromtxt("winequality-red.csv",delimiter=',',names=True)
numArr


# In[ ]:


np.set_printoptions(threshold = np.nan) # to print out all the data on console 
numArr


# In[ ]:


numArr.shape


# In[ ]:


numArr.dtype


# In[ ]:


numArr.dtype.name


# In[ ]:


numArr.ndim


# In[ ]:


numArr.size


# In[ ]:


numArr[0]


# In[ ]:


np.savetxt(fname="myarray.csv", X=numArr[:30], delimiter=",") # Saving Array in file


# In[ ]:


wines = np.genfromtxt(fname="winequality-red.csv",dtype='float', delimiter=',', skip_header=1) #skip_header-skipped lines


# In[ ]:


wines


# In[ ]:


wines[0:2, 1:3] # First 2 rows and 2nd-3rd column


# In[ ]:


print(wines.dtype) # one datatype for one array


# In[ ]:


wines = wines.astype(int) # Conversion into int
wines


# In[ ]:


wines[:,11] # 11th index column ie, 12th number


# In[ ]:


np.unique(wines[:,11])


# In[ ]:


wines[:,11]


# In[ ]:


wines[:,11] > 7


# In[ ]:


~(wines[:,11] > 7)


# In[ ]:


# ~ negat
wines[~(wines[:,11] > 7)]


# In[ ]:


winesNew = wines[np.logical_and(wines[:,10] > 10, wines[:,11] > 7)]
winesNew


# In[ ]:


winesNew.astype('int')


# In[ ]:


winesNew[np.logical_and(winesNew[:,10] > 10, winesNew[:,11] > 7), 10:] = 0 # Changing values where it exists


# In[ ]:


wines.transpose().shape # Transpose shape


# In[ ]:


wines.ravel() # Flattening the arrays


# In[ ]:


wines[1,:].reshape((2,6)) # 12 elements to 2x6 array


# In[ ]:


# Combining Numpy Arrays
whitewines = np.genfromtxt(fname='winequality-white.csv', delimiter=';', skip_header=1)
print(whitewines.shape, wines.shape)


# In[ ]:


winesRW = np.vstack(tup=(wines, whitewines)) # Row-bind 
print(winesRW.shape)


# In[ ]:


winesRW = np.hstack(tup=(wines, whitewines[:len(wines)])) # Col-bind
print(winesRW.shape)


# In[ ]:


winesRW = np.concatenate((wines, whitewines[1:len(whitewines)]), axis = 0) # Vstack
print(winesRW.shape)


# In[ ]:


winesRW = np.concatenate((wines, whitewines[:len(wines)]), axis = 1) # Hstack
print(winesRW.shape)


# In[ ]:


hsplitArr = np.hsplit(winesRW, 2) # Col-wise split; equal-sized arrays
print(len(hsplitArr), hsplitArr[0].shape, hsplitArr[1].shape)


# In[ ]:


vsplitArr = np.vsplit(whitewines, 2) # Row-wise split
print(len(vsplitArr), vsplitArr[0].shape, vsplitArr[1].shape)

