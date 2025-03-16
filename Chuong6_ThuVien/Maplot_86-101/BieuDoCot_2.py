import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('data/PVD_Asset.csv')
print(df)
plt.barh('Year', 'Equity', data=df)
plt.title("Vốn của PVD qua các năm")
plt.xlabel("Vốn")
plt.ylabel("Năm")
plt.show()
