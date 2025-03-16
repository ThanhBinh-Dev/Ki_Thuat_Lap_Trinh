import pandas as pd

df = pd.read_csv('./data/SampleData_NaN.csv')
# Xóa dòng chứa phần tử rỗng
df_delete_na_by_row = df.dropna(axis=0)
print(df_delete_na_by_row)
print("-"*80)
df_delete_na_by_col = df.dropna(axis=1)
print(df_delete_na_by_col)
print("-"*80)
# Điền giá trị 100 cho phần tử rỗng
df_fill_na_100 = df.fillna(100)
print(df_fill_na_100)
print("-"*80)
# Fill với giá trị liền kề phía dưới
# Phương thức cũ không được hỗ trợ trong Pandas mới và sẽ bị loại bỏ trong tương lai
# df_fill_na_bfill=df.fillna(method='bfill')
df_fill_na_bfill = df.bfill()
print(df_fill_na_bfill)
print("-"*80)
# Fill với giá trị liền kề phía trên
# Phương thức cũ không được hỗ trợ trong Pandas mới và sẽ bị loại bỏ trong tương lai
# df_fill_na_ffill=df.fillna(method='ffill')
df_fill_na_ffill=df.ffill()
print(df_fill_na_ffill)
print("-"*80)
# Fill với giá trị nội suy
# Phương thức cũ không được hỗ trợ trong Pandas mới và sẽ bị loại bỏ trong tương lai
df_fill_na_interpolate = df.interpolate()
print(df_fill_na_interpolate)
