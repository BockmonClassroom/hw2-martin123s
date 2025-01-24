# 01/24/2025
# Shuiming Chen

import pandas as pd
import matplotlib.pyplot as plt


# get the data from csv file
data = pd.read_csv("./data/flowers.csv")

# Separate data by species
species = data.groupby("Species")

# figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

# Plot the total data on the first subplot
axes[0].hist(data['leafWidthCm'])
axes[0].set_xlabel('All')
axes[0].set_ylabel('Count')

# Plot data of each species to the remaining subplots
for ax, (name, group) in zip(axes[1:], species):
    ax.hist(group['leafWidthCm'])
    ax.set_xlabel(name)
    ax.set_ylabel('Count')

# Add super title to the figure
fig.suptitle('leaves width (cm)')
plt.show()




