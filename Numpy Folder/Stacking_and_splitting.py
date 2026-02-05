""" vertically
    horizontally
    vstack() = row-wise
    hstack() = column-wise
"""
#Stacking array
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))

""" np.split() = equal
    np.hsplit() = horizontal
    np.vsplit() = vertically
"""
# splitting array
arr = np.array([10,20,30,40,50,60])
print(np.split(arr, 2))
print(np.hsplit(arr, 1))

