import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

np.random.seed(10) # -> Random với giá trị không đổi
dat = np.random.normal(12, 2, 400)
sns.displot(dat)
plt.xlabel('Salary')
sns.displot(dat, kde=True, color='r')
plt.xlabel('Salary')
