import pandas as pd

df = pd.read_csv('./data/SampleData.csv', index_col=0)
print(df)
# Xóa cột Price
del df['Price']
print(df)
# Xóa cột index 2
print(df.drop(df.index[2]))
