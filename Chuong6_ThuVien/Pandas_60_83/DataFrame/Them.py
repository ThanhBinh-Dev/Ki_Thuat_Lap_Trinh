import pandas as pd

df = pd.read_csv('./data/SampleData.csv')
print(df)
df.loc[df.shape[0]] = ['VCB', 113.6, 23.09]
print(df)
