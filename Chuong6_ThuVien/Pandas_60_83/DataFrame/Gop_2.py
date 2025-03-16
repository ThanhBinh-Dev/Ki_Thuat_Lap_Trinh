import pandas as pd

df=pd.read_csv('./data/SampleData2.csv')
df1 = df[['Symbol','Price','Group']]
df1 = df1.drop(df1.index[3])
df2 = df[['Symbol','PE','Group']]
print(df1)
print()
print(df2)
print("-"*40)
df_merge = pd.merge(df1, df2)
print(df_merge)
print()
df_merge = pd.merge(df1, df2, how='outer')
print(df_merge)

