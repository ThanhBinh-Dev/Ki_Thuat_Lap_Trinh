import pandas as pd

df = pd.read_csv('./data/SampleData2.csv')
df1 = df[['Symbol','Price','Group']]
df2 = df[['Symbol','PE','Group']]
print(df1)
print("-"*40)
print(df2)

print("-"*40)
df_concat = pd.concat([df1,df2])
print(df_concat)

print("-"*40)
df_concat=pd.concat([df1,df2],join='inner')
print(df_concat)

print("-"*40)
df_concat = pd.concat([df1, df2], axis=1)
print(df_concat)
print("-"*40)
df_append = pd.concat([df1, df2], ignore_index=True)
print(df_append)
print("-"*40)
df_merge = pd.merge(df1,df2)
print(df_merge)
print("-"*40)
