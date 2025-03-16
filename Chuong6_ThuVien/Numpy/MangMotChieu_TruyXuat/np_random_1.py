import numpy as np

arr=np.random.randint(10,80,8)
print(arr)
print(arr[1])
print(arr[-2])
print(arr[[1,3,4]])
print(arr[2:5])
print(arr[arr<40])