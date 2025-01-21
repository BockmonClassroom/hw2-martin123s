# 01/21/2025
# Shuiming Chen

import pandas as pd
import matplotlib.pyplot as plt



# get the data from csv file
data = pd.read_csv("./data/flowers.csv")

#groups the data based on species name
groups = data.groupby("Species")

# define the figure size
plt.figure(figsize=(10, 8))

# create the scatter figure
for name, group in groups:
    x = group.leafLengthCm
    y = group.leafWidthCm
    plt.scatter(x, y)

#adds a legend to the graph. Has to be in order!
plt.legend(["Alstroemeriaceae","Cinnamomum-osmophloeum","Orange-lily"])
plt.title("flower leaves length vs width")
plt.xlabel("leaves_length")
plt.ylabel("leaves_width")
plt.show()