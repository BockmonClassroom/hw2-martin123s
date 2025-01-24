# 01/24/2025
# Shuiming Chen

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# get the data from csv file
data = pd.read_csv("./data/flowers.csv")

# define the figure size
plt.figure(figsize=(11, 7))

# Add 'All' in the Species column to include all data
all_data = data.copy()
all_data['Species'] = 'All'
df = pd.concat([all_data, data]);

# create a boxplot
sns.boxplot(x='Species', y='leafWidthCm', data=df)
plt.title("flowers' leaves width")
plt.xlabel('')
plt.ylabel('')
plt.show()
