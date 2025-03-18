import pandas as pd
import seaborn as sns
df=pd.read_csv('./Data/Housing.csv')
dat=df.sample(400)
sns.scatterplot(x='housing_median_age',y='median_house_value',data=dat,hue='ocean_proximity',size='median_income')