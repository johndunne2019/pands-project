# 2019-04-24
# John Dunne
# Box plot of the data set
# pandas box plot documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html
print("The box plot will appear on the screen momentarily")
import matplotlib.pyplot as pl
import pandas as pd
# imported the libraries needed and give shortened names
data = "https://raw.githubusercontent.com/johndunne2019/pands-project/master/Fishers_Iris_data_set.csv"
# url of the data set to be read by pandas.read
dataset = pd.read_csv(data, header=0)
# pandas.read used to read in the data set from my repository, header set to first row of data in the data set
dataset.boxplot(by= 'species', grid=True)
# pandas dataframe.boxplot used to plot box plot of data set: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html
# Added grid and set box plot to group by column 5 of the data set- species
# So in this case 4 plots of - petal width and lenght and sepal width and lenght
# Adapted from : http://cmdlinetips.com/2018/03/how-to-make-boxplots-in-python-with-pandas-and-seaborn/
pl.show()
# pyplot.show() command shows the histogram on the screen 