# 2019-04-13
# Adapted from: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
import pandas #imported pandas module
data = "https://raw.githubusercontent.com/johndunne2019/pands-project/master/Fishers_Iris_data_set.csv"
# url given to data set saved in my repository.
# I had to change this to be the raw version of the data set by clicking the raw button and taking the url from there
columns = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# variable columns set to the headings of the 5 columns of the data set
dataset = pandas.read_csv(data, names=columns)

print(dataset.shape)
# the number of rows and columns are printed