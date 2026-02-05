# Reshaping: dimension change without modifying data
# total of no. of element are same in reshape dimension
# reshape: (rows,columns) specify new shape if dimension match

import numpy as np
arr = np.array([10,20,30,40,50,60])
print(arr)

reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)

# Flattening array
# when you want to convert multy dimensional array into 1d array
# .ravel() -> it returns a view
# .flatten -> it returns a copy
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())

