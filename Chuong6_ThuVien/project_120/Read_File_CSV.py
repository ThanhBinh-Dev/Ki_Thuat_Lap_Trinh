import pandas as pd
# 1
df = pd.read_csv('./Dataset/TCB_2018_2020.csv')
print(df)
# 2
x1=float(input("Nhập giá trị x:"))
y1=float(input("Nhập giá trị y:"))
filter_df1=df[(df['Close'] < x1) & (df['Close'] > y1)]
print(filter_df1)
# # 3
x2=float(input("Nhập giá trị x:"))
y2=float(input("Nhập giá trị y:"))
filter_df2=df[(df['Low'] > x2) & (df['Close'] < y2)][['Date', 'High', 'Low']]
print(filter_df2)
# 4
print('Nhập Thông Tin Ngày Cần xuất Thông tin')
date=input("Nhập thời gian (yyyy-mm-dd):")
filter_df3=df[df['Date']==date]
print(filter_df3)
# 5
print('Nhập Thông Tin Các Ngày Cần xuất Thông tin')
date_list=input("Nhập thời gian (yyyy-mm-dd) cách nhau bởi dấu phẩy:").split(",")
filter_df4=df[df['Date'].isin(date_list)]
print(filter_df4)