import pandas as pd

df = pd.read_csv('./data/TCB_2018_2020.csv')
print(df)
df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print(df.head())
df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print('Xuất dữ liệu với điều kiện giá đóng cửa lớn hơn 98')
print(df[df['Close']>98])
print('Truy Xuất Dữ Liệu Theo Cột')
print(df[["High", "Low"]].tail())
df = pd.read_csv('./data/TCB_2018_2020.csv', header=None)
print(df[[0, 2, 3]].tail())
print('Truy Xuất Dữ Liệu Theo Dòng')
df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print(df.loc['2020-06-15'])
df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print(df.loc[['2019-06-10', '2020-06-10']])
df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print(df.iloc[0]) #Dòng Đầu
df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print(df.iloc[[0, 2]]) #Nhiều Dòng
df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print(df.iloc[35:41]) # Nhiều dòng liên tiếp
print('Truy Xuất Theo Phần Tử')
df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)

print('Truy xuất giá đóng cửa ngày 20-08-2019')
print(df.loc['2019-08-20', 'Close'])
print(df.loc['2020-12-25':, 'Open'])
df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)

print('Truy xuất dòng thứ 5 và cột đầu tiên')
print(df.iloc[4, 0])
print('Truy xuất dòng từ dòng thứ 648 với tất cả các cột')
print(df.iloc[648:, :])







