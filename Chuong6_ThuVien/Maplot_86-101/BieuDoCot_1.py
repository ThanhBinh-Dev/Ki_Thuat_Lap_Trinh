import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('data/PVD_Asset.csv')
print(df)
plt.bar('Year', 'Liabilities', data=df)
plt.title("Nợ của PVD qua các năm")
plt.xlabel("Năm")
plt.ylabel("Nợ")
plt.show()
