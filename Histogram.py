# 2019-04-15
# John Dunne
# To create a histogram of the data using matplotlib.pyplot 
# Script adapted from example analysis read here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

import matplotlib.pyplot as pl
# imported matplotlib.pyplot which will be used to plot the histogram
# matplotlib.pyplot documentation: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html and https://matplotlib.org/gallery/statistics/hist.html
import pandas as pd
# pandas imported - will be used to read in the data set from my repository
# pandas documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hist.html
data = "https://raw.githubusercontent.com/johndunne2019/pands-project/master/Fishers_Iris_data_set.csv"
# link to the data set saved in my repository
dataset = pd.read_csv(data, header=0)
# pandas.read used to read in the data set from my repository, header set to first row of data in the data set
# I read about pandas.read here: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
dataset.hist()
# A histogram is plotted of the data set 
# Adapted from the example analysis here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# Further reading: https://matplotlib.org/gallery/statistics/histogram_features.html
# pyplot.hist: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html
pl.show()
# pyplot.show() command shows the histogram on the screen 
# I read about the show command here: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.show.html