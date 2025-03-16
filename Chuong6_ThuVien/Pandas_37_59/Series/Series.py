import numpy as np
import pandas as pd

ser=pd.Series([2,4,6,8])
print(ser)

arr_price=np.array([76.3,23.1,102.4])
arr_symbol=np.array(['FPT','ACB','VNM'])
ser=pd.Series(arr_price,index=arr_symbol)
print(ser)

dic = {'FPT':76.3, 'ACB':23.1, 'VNM':102.4}
ser = pd.Series(dic)
print(ser)

