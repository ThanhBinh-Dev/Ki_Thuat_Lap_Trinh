import pandas as pd

dic = {'FPT':76.3, 'ACB':23.1, 'VNM':102.4,'AGH': 7.8, 'FLC':3.5, 'HTC':24.2}
ser = pd.Series(dic)
print(ser)
print(ser.drop(ser.index[[0,2]]))
print(ser.drop(['FLC','AGH']))
