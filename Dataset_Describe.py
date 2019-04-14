# 2019-04-14
# John Dunne
# This script will provide a description of the data set
# This will be done using the dataset.describe() function within pandas
# I first saw an example of the dataset.describe() being user to analyse the Fisher's Iris data set here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# I then researched further: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html and https://stackoverflow.com/questions/38545828/pandas-describe-by-additional-parameters

import pandas as pd # pandas imported and given shortened name 
data = "https://raw.githubusercontent.com/johndunne2019/pands-project/master/Fishers_Iris_data_set.csv"
# variable data set equal to the url to the raw version of the data set in my repository
# I read how to do this here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
dataset = pd.read_csv(data, header=0)
# pandas.read used to read in the csv file, I read about it here: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
# header=0 used to set the first row of data as the header, read here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html