import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(arr)
print(np.max(arr))
print(np.mean(arr[1]))
print(arr[np.where(arr>8)])