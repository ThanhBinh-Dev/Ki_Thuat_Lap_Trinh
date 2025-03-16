import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('data/NetProfit.csv')
print(df)
plt.plot('Year', 'VNM', data=df)
plt.plot('Year', 'PNJ', data=df)
plt.plot('Year', 'VCB', data=df)
plt.plot('Year', 'VIC', data=df)
plt.show()

