import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(arr)
arr[1][0][2]=10
print(arr[1][0])