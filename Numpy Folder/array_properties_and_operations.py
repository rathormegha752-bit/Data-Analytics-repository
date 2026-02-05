import numpy as np

# shape: it is use for to find the how many rows and columns 
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1)
print(arr1.shape)

# size: it is check total numbers of element return
arr2 = np.array([[10,20,30],[40,50,60]])
print(arr2)
print(arr2.size)

# ndim: used for check number of dimensions
arr_1d = np.array([1,2,3,4,5,6])
print(arr_1d)
print(arr_1d.ndim)

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)
print(arr_2d.ndim)

# dtype: checck the datatype of data
arr_int = np.array([10,22,25,14,5])
print(arr_int.dtype)

# arr_string = np.array(["Megha","Ram"])
# print(arr_string.dtype)

# astype: change the datatype
float_arr = np.array([1.2,2.3,4.5])
int_arr = float_arr.astype(int)
print(int_arr)

#using operator in numpy
arr = np.array([10,20,30,40,50])
print(arr + 5)  #addition
print(arr - 5)  #subtraction
print(arr * 2)  #multiplication
print(arr ** 2)


''' Aggregration function:
    data mein se summary nikalna
    statistic mein use hota hai
'''
arr = np.array([10,20,30,40,50])
print(np.sum(arr)) #find the sum
print(np.mean(arr)) #finf the average value
print(np.min(arr))  #find the minimum value 
print(np.max(arr))  #find the maximum value
print(np.std(arr))  #find the standard deviation
print(np.var(arr))  #find the variance