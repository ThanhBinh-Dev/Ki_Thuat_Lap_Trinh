import pandas as pd

list_sample = [['PNJ', 180.1, 182], ['VIB', 22.3, 21.2], ['VIC', 46.2, 45.6], ['VNM', 150, 146.1]]
df = pd.DataFrame(list_sample, columns=['Symbol', 'Open', 'Close'])
print(df)
