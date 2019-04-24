# 2019-04-24
# John Dunne
# Scatter plot of the data set
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html
import matplotlib.pyplot as pl
import pandas as pd
# imported the libraries needed and give shortened names
data = "https://raw.githubusercontent.com/johndunne2019/pands-project/master/Fishers_Iris_data_set.csv"
# url of the data set to be read by pandas.read
dataset = pd.read_csv(data, header=0)
# pandas.read used to read in the data set from my repository, header set to first row of data in the data set
dataset.boxplot(by= 'species')
# http://cmdlinetips.com/2018/03/how-to-make-boxplots-in-python-with-pandas-and-seaborn/
pl.show()