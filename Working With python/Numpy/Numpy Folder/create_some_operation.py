import numpy as np

#array create with default function
zeroes_array = np.zeros(3)
print(zeroes_array)

#create array with 1 value
ones_array = np.ones((2,3))
print(ones_array)

#filled value as specific number
filled_array = np.full((2,2),7)
print(filled_array)

#filled value as sequence
#use arrange()
arr = np.arange(1,10,2)
print(arr)

#creating identify metrix
indentify_matrix = np.eye(3)
print(indentify_matrix)