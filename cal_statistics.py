# 01/31/2025
# Shuiming Chen

import pandas as pd

# get the data from csv file
data = pd.read_csv("./data/flowers.csv")

# print out the leaves length statistical data
stats_length = data.groupby(["Species"])["leafLengthCm"].agg(["mean", "median", "var", "std"])

# print out the leaves length statistical data
stats_width = data.groupby(["Species"])["leafWidthCm"].agg(["mean", "median", "var", "std"])
print("\nLeaves' length data \n", stats_length)
print("\n")
print("Leaves' width data \n", stats_width)