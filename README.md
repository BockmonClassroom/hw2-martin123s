[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AV-xh9XP)
# HW2
DS5110  
Homework 2 - Data Collection  
Shuiming Chen
01/20/2025

# Answer the following (20 points):
### 1. Explain your data collection process.
* 1.1 data come from the flowers bought from hannaford.
* 1.2 pick up those with enough leafs flowers and google the species name.
* 1.3 using scale with centimeter to measure the length and width and write it down.

### 2. What instrument did you use to collect data with?
* Scale bought from home depot with centimeter measurement.

### 3. Argue the accuracy and precision of your instrument.
* Very high accuracy and precision cause it's a standard product.

### 4. How many data points did you collect? Why?
* 34 lists in total, and each species has a different numbers, because the flowers were mixed by different species, and the leaves were limited.

### 5. Define the size of your data in terms of both N (full data set size) and n (each subset size).
* subset size are:
* Species(a) Alstroemeriaceae: 11 leaves
* Species(b) Orange-lily: 8 leaves
* Species(c) Cinnamomum-osmophloeum: 15 leaves
* full data set size is: N here is n(a) + n(b) + n(c) = 34

### 6. Explain any problems that you ran into during the data collection process.
* 6.1 manaual measurment can lead to some tiny inaccuracies, mabye up to 0.1 to 0.2 centimeter inaccuracies.
* 6.2 data set are not big enough to get the pattern of leaves size range.


# Analysis/Visualization - (50 points):
### 1. Graph histograms of your data with appropriate labels.
* see histogram-length.py and histogram-width.py
### 2. Graph boxplots of your data with appropriate labels.
* see boxplot-length.py and boxplot-width.py
### 3. Graph a scatter plot of your entire data set with each subset different color and a ledger.
* see scatter-graph.py
### 4. Explain each graph in terms of variance, mean, median, and standard deviation.
#### histograms
* variance: x label of the figure width which is the distributions indicate variance in leaf length, the narrower of the width, the smaller of the leaves variance, and vice verse.
* mean/median: The peak of the bin can help to estimate the mean/median for each species. if the dataset are normalization, the mean and median would be in the same spot, otherwise their results would be close to each other.
* standard deviation: the narrower of the bin means lower standard deviation, and vice verse.

#### boxplots
* Boxpots does not directly show the variance, standatd deviation and mean. however, we can infer from the boxplot of median, which is the line inside the box.
* Boxplots has first quartile(Q1) which means the median of upper half, and third quartile(Q3) which is the median of lower half.
* We can also infer from the boxplots of minimum and maximum values which is called whiskers, and outliers which are data points outside of whiskers.
* We can say that a wider box and longer whiskers can be used to imply higher standard deviation.

#### scatters
* variance: how spread out of the points are can be used to detect variance.
* mean/median: They can be inferred by looking for the central tendency of the points.
* standard deviation: The more spread out of the points from the central point (mean), the higher the standard deviation.

### 5. What can you infer with data and graphs that you have?
* Cinnamomum-osmophloeum: the width of the leaves are relatively close to 4cm, but the length are reange differently.
* Orange-lily: expect those tender leaves, all other leaves are having the similar length and width.
* Alstroemeriaceae: the length are pretty stable but the width are more changeable.


