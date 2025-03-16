import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('data/NetProfit.csv')
plt.plot('Year', 'VNM', data=df, color='b', linestyle='-', marker='o')
plt.plot('Year', 'PNJ', data=df, color='g', linestyle='--', marker='s')
plt.plot('Year', 'VCB', data=df, color='#FF0000', linestyle=':', marker='+')
plt.plot('Year', 'VIC', data=df, color='orange', linestyle='-.', marker='*')
plt.title("Lợi nhuận của VNM, PNJ, VCB, VIC từ 2010 đến 2020", fontweight='bold')
plt.xlabel("Năm", fontweight='bold')
plt.ylabel("Lợi nhuận", fontweight='bold')
plt.legend()
plt.show()
