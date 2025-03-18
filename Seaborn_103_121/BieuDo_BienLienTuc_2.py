import seaborn as sns
tips = sns.load_dataset("tips")
print(tips.head())
sns.relplot(x='total_bill', y='tip', data=tips,hue='smoker')

