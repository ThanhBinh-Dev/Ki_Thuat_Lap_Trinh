import numpy as np

arr1 = np.array(range(12))
print(arr1)
arr_reshape = arr1.reshape(3,4)
print(arr_reshape)
arr2 = arr_reshape.reshape(1,-1)
print(arr2)
arr3 = arr_reshape.flatten()
print(arr3)


