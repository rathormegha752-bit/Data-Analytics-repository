'''Indexing type
> fancy indexing
> boolean masking (certain condition)
'''
import numpy as np

#access element
arr = np.array([10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[-1])


#slicing 
''' array[start,stop,step]
arr[start:end] start to end
negative step, -1 reverse
'''
arr = np.array([10,20,30,40,50])
print(arr[1:5])
print(arr[:4])
print(arr[::2])
print(arr[::-1])

#filtering data(boolean masking)
#aa element ko kisi ek condition he basis par filter kar sakte ho aur vahi value
# return karega jo apke fulfill kar sakti hai
arr = np.array([10,20,30,40,50])
print(arr[arr > 25])