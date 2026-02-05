import numpy as np
# Append: add a element at the end
arr = np.array([10,20,30])
new_arr = np.append(arr, [40,50,60])
print(new_arr)

# Concate: add two or more array list in one array list
# syntax: np.concatenate((array1, array2), axis = none)
# axis = 0, Vertically stacking(row-wise)
# axis = 1, Horizontally stacking(column-wise) 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
new_arr = np.concatenate((arr1, arr2))
print(new_arr)


# removing element
# np.delete()
# syntax: np.delete(array, index, axis=none)
arr = np.array([10,20,30,40,50,60])
new_arr = np.delete(arr, 0)
print(new_arr)

arr_2d = np.array([[10,20,30],[40,50,60]])
new_arr = np.delete(arr_2d, 0 , axis = 0)
print(new_arr)

