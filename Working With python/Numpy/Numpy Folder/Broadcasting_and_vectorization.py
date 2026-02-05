''' > Matching dimension
      example: [1,2,3],[4,5,6],[7,8,9] # 3 element in each array
    > Expanding single elements
      example: [1,2,3] + 10
                [11,12,13] automatically
    > Incompatible shape
      Example: [1,2,3] + [1,2]
                  3         2   elements
                    error
'''
import numpy as np

# Example1: of broadcasting with single array
arr = np.array([100,200,300])
result = arr * 2
print(result)

# Example 2: 
matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([10,20,30])

result = matrix + vector
print(result)

# Example 3:
# arr1 = np.array([[1,2,3],[4,5,6]])
# arr2 = np.array([1,2])
# result = arr1 + arr2   # it is show error
# print(result)

# let's understand this with different type example
import numpy as np
prices = np.array([100,200,300])
discount = 10
final_prices = prices - (prices * discount/100)
print(final_prices)


# Vectorization
# Ek entire array par ek baar ke operation apply kare bina loops ka use karna
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

reuslt = arr1 + arr2  # vectorizatiion addition
print(result)

result1 = arr1 * arr2 # Vectorization Subtraction
print(result1)

arr = np.array([10,20,30])
multiplied = arr*3
print(multiplied)