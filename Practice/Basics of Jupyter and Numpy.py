#!/usr/bin/env python
# coding: utf-8

# ## To convert cell into bash command line use ! symbol

# In[ ]:


get_ipython().system(' pip list')


# In[ ]:


get_ipython().system(' python -V')


# ## List of magic commands

# In[1]:


get_ipython().run_line_magic('lsmagic', '')


# In[2]:


get_ipython().run_line_magic('pwd', '')


# In[ ]:


get_ipython().run_line_magic('ls', '-la')


# In[3]:


get_ipython().run_cell_magic('HTML', '', '<a class="js-photo-page-image-download-link" download="" href="https://images.pexels.com/photos/459225/pexels-photo-459225.jpeg?cs=srgb&amp;dl=daylight-environment-forest-459225.jpg&amp;fm=jpg" target="_blank">\n<div class="js-photo-zoom-container photo-page__photo__image" data-zoom-src="https://images.pexels.com/photos/459225/pexels-photo-459225.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=3&amp;h=750&amp;w=1260">\n<iframe allowfullscreen="" class="js-photo-page-video-iframe" frameborder="0" mozallowfullscreen="" style="background: white; display: none;" webkitallowfullscreen=""></iframe>\n<img class="js-photo-page-image-img" alt="Plain Field in Front of Mountain Peak" data-pin-media="undefined" src="https://images.pexels.com/photos/459225/pexels-photo-459225.jpeg?auto=compress&amp;cs=tinysrgb&amp;h=750&amp;w=1260" srcset="https://images.pexels.com/photos/459225/pexels-photo-459225.jpeg?auto=compress&amp;cs=tinysrgb&amp;h=650&amp;w=940 940w, https://images.pexels.com/photos/459225/pexels-photo-459225.jpeg?auto=compress&amp;cs=tinysrgb&amp;h=750&amp;w=1260 1260w, https://images.pexels.com/photos/459225/pexels-photo-459225.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;h=650&amp;w=940 1880w, https://images.pexels.com/photos/459225/pexels-photo-459225.jpeg?auto=compress&amp;cs=tinysrgb&amp;dpr=2&amp;h=750&amp;w=1260 2520w" style="background: rgb(135, 157, 169); max-height: 75vh; max-width: calc(158.006vh); min-height: 300px; min-width: calc(632.022px);" data-zoom-initiated="true">\n</div>\n</a>')


# # Numerical Python
# NumPy, which stands for **Numerical** Python, NumPy is an open source library available in Python that aids in mathematical, scientific, engineering, and data science programming. **NumPy** is an incredible library to perform mathematical and statistical operations.

# # Why Numpy ?
# 
# NumPy is memory efficiency, meaning it can handle the vast amount of data more accessible than any other library. Besides, NumPy is very convenient to work with, especially for matrix multiplication and reshaping. On top of that, NumPy is fast.
# 
# **The essential problem that NumPy solves is fast array processing**

# # Performance comparison for numpy

# In[ ]:


import time

def trad_version():
    t1 = time.time()
    X = range(100000000)
    Y = range(100000000)
    Z = []
    for i in range(len(X)):
        Z.append(X[i] + Y[i])
    return time.time() - t1
print(trad_version()) # 26.57


# In[ ]:


import numpy as np
def numpy_version():
    t1 = time.time()
    X = np.arange(100000000) # Just like range but gives arrray not list
    Y = np.arange(100000000) # start, stop, step
    Z = X + Y
    return time.time() - t1
print(numpy_version()) # 1.16


# # Size comparison for numpy

# In[ ]:


import sys
l=range(100000)
sys.getsizeof(5) * len(l) # size of 100000 element 


# In[ ]:


import numpy as np
arr=np.arange(100000)
arr.size * arr.itemsize


# In[ ]:




