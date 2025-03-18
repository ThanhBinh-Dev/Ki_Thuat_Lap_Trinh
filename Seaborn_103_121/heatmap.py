import seaborn as sns
flights_long = sns.load_dataset('flights')
flights = flights_long.pivot(index='month', columns='year', values='passengers')
sns.heatmap(flights, annot=True, fmt='d', linewidths=.5)
