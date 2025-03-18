import seaborn as sns
sns.set(style='darkgrid')
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

sample_datasets = sns.get_dataset_names()
print(sample_datasets)