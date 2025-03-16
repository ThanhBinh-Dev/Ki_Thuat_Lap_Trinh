import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('data/Income.csv')
print(df)

lbls = ['Chuyển nhượng BĐS', 'Cho thuê BĐS', 'DV khách sạn', 'Bệnh viện', 'Giáo dục', 'Sản xuất', 'Hoạt động khác']
income = [71.576, 6.788, 4.869, 2.675, 2.244, 18.007, 4.304]
explode = [0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2]
plt.pie(income, labels= lbls, explode=explode, autopct='%1.1f%%', pctdistance=1.1, labeldistance=1.2)
plt.title('Cơ cấu doanh thu VinGroup - 2020', fontweight='bold')
# plt.legend(loc='upper right')
plt.show()
