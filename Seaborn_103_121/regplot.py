import pandas as pd
import seaborn as sns
df = pd.read_csv('./data/Income_1.csv')
sns.regplot(x='Income', y='Expenditure', data=df)
