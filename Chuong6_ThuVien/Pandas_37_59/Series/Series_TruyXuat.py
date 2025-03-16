import numpy as np
import pandas as pd

arr_price=np.array([76.3,23.1,102.4])
arr_symbol=np.array(['FPT','ACB','VNM'])
ser=pd.Series(arr_price,index=arr_symbol)
print(ser)

dic = {'FPT':76.3, 'ACB':23.1, 'VNM':102.4}
ser = pd.Series(dic)
print(ser)

# Truy Xuất
print(ser['ACB'])
print(ser[2])
print(ser[1:])
print(ser[['FPT','VNM']])
########################################
print(ser.size)
print(len(ser))
print(ser.values)
print(ser.index)
print(ser.axes)
