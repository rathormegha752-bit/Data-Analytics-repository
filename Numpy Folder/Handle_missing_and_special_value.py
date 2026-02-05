''' np.isnan -> detect missing value
    np.nan_to_num()
    np.isinf()
    nan = not a number
'''
import numpy as np

#Example of is.nan method
arr = np.array([1,2,np.nan,4,6])
print(np.isnan(arr))

# Example of np.nan_to_num method
arr = np.array([1,2,np.nan,4,6])
cleaned_arr = np.nan_to_num(arr)
print(cleaned_arr)

        # or
cleaned_arr = np.nan_to_num(arr, nan=10)
print(cleaned_arr)

# Example of isinf method
arr = np.array([1,2,np.inf,4,6,-np.inf])
print(np.isinf(arr))

        # or
arr = np.array([1,2,np.inf,4,6,-np.inf])
cleaned_arr = np.nan_to_num(arr, posinf = 100, neginf = 50)
print(cleaned_arr)