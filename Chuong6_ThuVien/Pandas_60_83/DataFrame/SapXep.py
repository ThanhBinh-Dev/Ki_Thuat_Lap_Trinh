import pandas as pd

sales_2020 = pd.DataFrame({'sales': [450, 360, 550, 480]},index=['Mar', 'Jun', 'Feb', 'Apr'])
print(sales_2020)
sales_2021=pd.DataFrame({'sales':[650,600,700,680]},index=['Feb','Mar','Apr','Jun'])
print(sales_2020.reindex(sales_2021.index))
