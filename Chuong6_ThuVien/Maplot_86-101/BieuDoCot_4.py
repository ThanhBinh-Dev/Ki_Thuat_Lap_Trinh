import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('data/Income.csv')
print(df)

plt.scatter('Income', 'Expenditure', data=df, color='darkgreen')
plt.xlabel('Thu nhập', fontweight='bold')
plt.ylabel('Chi tiêu', fontweight='bold')
plt.show()
