import numpy as np
import pandas as pd

arr_price=np.array([76.3,23.1,102.4])
arr_symbol=np.array(['FPT','ACB','VNM'])
ser=pd.Series(arr_price,index=arr_symbol)

ser['FPT']=81
ser[2]=106
print(ser)
