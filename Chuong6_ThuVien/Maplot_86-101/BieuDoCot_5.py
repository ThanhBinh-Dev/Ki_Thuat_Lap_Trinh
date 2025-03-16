import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('data/Income.csv')
print(df)

colors = np.random.rand(df.shape[0]) # Random màu ngẫu nhiên
area = df['Income'].values * 50 # Kích thước điểm dữ liệu
plt.scatter('Income', 'Expenditure', data=df, c=colors, s=area,alpha=0.8)
plt.xlabel('Thu nhập', fontweight='bold')
plt.ylabel('Chi tiêu', fontweight='bold')
plt.show()
