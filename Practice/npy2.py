# Boolean Elementwise
arr1 == arr2 # arr1 elements (row) match with arr2 (row-wise)
arr1 < 2
np.array_equal(arr1, arr2) # Array-wise comparison
np.logical_and(arr1 > 2, arr2 > 4)
np.logical_or(arr1 > 2, arr2 > 4)
np.logical_not(arr1 > 2)
np.logical_xor(arr1 > 2, arr2 > 4) # T xor T = F
(arr1 > 2).any() # True if any True occurs
(arr1 > 2).all() # True if all True occurs

# Arithmetic Functions
np.sum(arr2, axis=1)
arr2.sum() # randMat[0].sum(); Sum of all elements
arr2.sum(axis=0) # axis = 0 means rowsum with corresponding elements; 1 colsum
randMat.min() # Minimum from array
randMat.max(axis=1) # 0 means row-wise with max values; 1 means column-wise with max values
randMat.cumsum(axis=1) # 0 means row-wise with cumsum; 1 means column-wise with cumsum
print(randMat.mean()); print(randMat.std()); print(np.std(randMat))
