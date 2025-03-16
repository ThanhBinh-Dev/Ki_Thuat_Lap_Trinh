import pandas as pd
from matplotlib import pyplot as plt

dat = pd.read_csv('./data/Salary_of_Developer.csv')
print(dat)

orange_square = dict(markerfacecolor='orange', marker='s')
plt.boxplot(dat, notch=True, flierprops=orange_square, vert=False)
plt.xlabel("Lương (triệu đồng)")
plt.title("Boxplot thể hiện phân bổ mức lương Lập trình viên")
plt.show()

