''' np.insert(array, index, value, axis=none)
    array - original array
    index - vo position number jaha par aap value insert karna chahte ho
    value - actual data
    axis - if it is none than it is inserted into a flatten array
    axis = 0, row-wise
    axis = 1, column-wise
'''
#insert in 1d array
import numpy as np
arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr_1d = np.insert(arr , 2 , 100 , axis = 0)
print(new_arr_1d)

#insert in 2d array
arr_2d = np.array([[1,2],[3,4]])

#insert a new row at index 1
new_arr_2d = np.insert(arr_2d, 1, [5,6], axis=0)
print(new_arr_2d)


