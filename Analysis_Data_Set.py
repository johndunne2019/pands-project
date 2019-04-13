# 2019-04-13
# Adapted from: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
import pandas #imported pandas module
data = "https://raw.githubusercontent.com/johndunne2019/pands-project/master/Fishers_Iris_data_set.csv"
# url given to data set saved in my repository. The data is read in a as a data frame. 
# I had to change this to be the raw version of the data set by clicking the raw button and taking the url from there
# The original url I used was tp the csv file and didnt work properly: https://github.com/johndunne2019/pands-project/blob/master/Fishers_Iris_data_set.csv
Columns = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# variable columns set to the headings of the 5 columns of the data set
dataset = pandas.read_csv(data, header=0, names=Columns)
# header=0 added as without this the first row was being printed to the screen twice
print(dataset.shape)
# the number of rows and columns are printed
print(dataset.head(10))
# dataset.head prints rows to the screen from the parameter entered. In this case I have entered 10 to print the first 10 rows.
# Note- script must be run while command prompt/cmder is in full screen mode to view all data