import pandas as pd

df = pd.read_csv('./data/SampleData2.csv')
print(df)
print(df.groupby('Group').sum())
