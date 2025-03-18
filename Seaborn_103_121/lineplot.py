import pandas as pd
import seaborn as sns
df=pd.read_csv('./Data/Housing.csv')
dat=df.sample(1000)
sns.lineplot(x='housing_median_age',y='median_house_value',data=dat,hue='ocean_proximity')