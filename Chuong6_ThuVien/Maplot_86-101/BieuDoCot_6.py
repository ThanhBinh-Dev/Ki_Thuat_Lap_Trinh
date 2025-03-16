import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('data/Income.csv')
print(df)

dat = np.random.normal(12, 2, 400)
plt.hist(dat, color='darkgreen', edgecolor='orange')
plt.xlabel('Lương')
plt.ylabel('Tần suất')
plt.show()
