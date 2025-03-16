import numpy as np

arr=np.random.randint(10,80,8)
print(arr)
indices=np.where(arr>40)
print(indices)
print(arr[indices])
print(np.extract(arr>35,arr))
print(np.extract(np.mod(arr,2)==0,arr))