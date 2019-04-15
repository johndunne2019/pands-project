# 2019-04-15
# John Dunne
# To create a histogram of the data using matplotlib.pyplot 
# Example read here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# pandas documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hist.html

import matplotlib.pyplot as pl
# imported matplotlib.pyplot which will be used to plot the histogram
# matplotlib.pyplot documentation: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html and https://matplotlib.org/gallery/statistics/hist.html
import pandas as pd
# pandas imported - will be used to read in the data set from my repository
data = "https://raw.githubusercontent.com/johndunne2019/pands-project/master/Fishers_Iris_data_set.csv"
# link to the data set saved in my repository
dataset = pd.read_csv(data, header=0)
# pandas.read used to read in the data set from my repository, header set to first row of data in the data set