# 2019-04-13
# Adapted from: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
import pandas #imported pandas module
data = "https://raw.githubusercontent.com/johndunne2019/pands-project/master/Fishers_Iris_data_set.csv"
# url given to data set saved in my repository. The data is read in a as a data frame. 
# I had to change this to be the raw version of the data set by clicking the raw button and taking the url from there
# The original url I used was tp the csv file but did not work properly: https://github.com/johndunne2019/pands-project/blob/master/Fishers_Iris_data_set.csv
dataset = pandas.read_csv(data, header=0))
# pandas.read used to read the csv file - https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
# header=0 added as without this the first row was being printed to the screen twice
# read about header=0 here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
print("Let's have a peek at the data set. The first 10 rows of the data set are shown below.")
print(dataset.head(10))
# dataset.head prints rows to the screen from the parameter entered. In this case I have entered 10 to print the first 10 rows.
# Note- script must be run while command prompt/cmder is in full screen mode to view all data