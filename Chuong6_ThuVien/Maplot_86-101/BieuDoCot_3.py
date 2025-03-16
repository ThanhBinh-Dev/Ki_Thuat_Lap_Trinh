import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('data/PVD_Asset.csv')
print(df)
plt.bar('Year', 'Liabilities', data=df, color='orange', label="Nợ")
plt.bar('Year', 'Equity', data=df, bottom='Liabilities', color='darkgreen', label="Vốn")
plt.title("Tài sản của PVD từ 2010-2020")
plt.xlabel("Năm")
plt.ylabel("Tỷ đồng")
plt.legend()
plt.show()
