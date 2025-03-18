import pandas as pd
import seaborn as sns
dat = pd.read_csv('./data/Income.csv')
print(dat)
sns.relplot(x='Income', y='Expenditure', data=dat, kind='scatter')
