# 2019-04-13
# Adapted from: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
import pandas #imported pandas module
data = "https://github.com/johndunne2019/pands-project/blob/master/Fishers_Iris_data_set.csv"
# url given to data set
columns = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# variable columns set to the headings of the 5 columns of the data set
dataset = pandas.read_csv(data, names=columns)

print(dataset.shape)
# the number of rows and columns are printed