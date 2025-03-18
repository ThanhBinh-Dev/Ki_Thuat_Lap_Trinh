import pandas as pd
import seaborn as sns
df = pd.read_csv('./data/Income_2.csv')
sns.jointplot(x='Income', y='Expenditure', data=df, color='orange')
