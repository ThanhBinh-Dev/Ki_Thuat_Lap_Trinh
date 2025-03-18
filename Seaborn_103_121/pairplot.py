import pandas as pd
import seaborn as sns
df = pd.read_csv('./data/Income_2.csv')
sns.pairplot(df[['Income','Expenditure']])
