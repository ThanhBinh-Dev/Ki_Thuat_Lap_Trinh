import pandas as pd

df = pd.read_csv('./data/SampleData_NaN.csv')
print(df)
print("-"*80)
print(df.isnull())
print("-"*80)
# Kiểm tra dữ liệu rỗng cho từng cột
print(df.isnull().any())
print("-"*80)
# Kiểm tra dữ liệu rỗng cho toàn bộ DataFrama
print(df.isnull().values.any())
print("-"*80)
# Kiểm tra số lượng dữ liệu rỗng
print(df.isnull().sum())
print(df.isnull().sum().sum())



