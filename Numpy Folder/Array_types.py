'''
1> one dimensional
2> two dimensional
3> Multy dimensional
   Matrix dimensional

'''
import numpy as np
arr_1d = np.array([1,2,3,4,5,6])
print(arr_1d)
print(arr_1d.ndim)

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)
print(arr_2d.ndim)

arr_multiD = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr_multiD)
print(arr_multiD.ndim)

