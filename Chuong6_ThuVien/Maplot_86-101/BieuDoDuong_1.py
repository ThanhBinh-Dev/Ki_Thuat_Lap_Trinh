import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('data/NetProfit.csv')
dat = df[['Year', 'VIC']]
print(dat)

plt.plot('Year', 'VIC', data=dat)
plt.show()


