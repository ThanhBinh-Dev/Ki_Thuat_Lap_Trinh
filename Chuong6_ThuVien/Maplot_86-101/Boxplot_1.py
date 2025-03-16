import pandas as pd
from matplotlib import pyplot as plt

dat = pd.read_csv('./data/Salary_of_Developer.csv')
print(dat)

plt.boxplot(dat)
plt.ylabel("Lương (triệu đồng)")
plt.title("Boxplot thể hiện phân bổ mức lương Lập trình viên")
plt.show()
