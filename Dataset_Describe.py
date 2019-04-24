# 2019-04-14
# John Dunne
# This script will provide a description of the data set
# This will be done using the dataset.describe() function within pandas
# I first saw an example of the dataset.describe() being user to analyse the Fisher's Iris data set here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# I then researched further: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html and https://stackoverflow.com/questions/38545828/pandas-describe-by-additional-parameters
print("pandas dataframe.describe() has printed a description of the data set to the screen below:")
import pandas as pd # pandas imported and given shortened name 
data = "https://raw.githubusercontent.com/johndunne2019/pands-project/master/Fishers_Iris_data_set.csv"
# the csv file will be read directly from my repository (raw version) using the url
# I read how to do this here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
dataset = pd.read_csv(data, header=0)
# pandas.read used to read in the csv file, I read about it here: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
# header=0 used to set the first row of data as the header, read here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
print(dataset.describe())
# I read about using dataframe.describe() here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
# A description of the data set will be printed to the screen 
# The description will be made up of: count of rows, mean, standard deviation, min and max
# Also included is lower, middle and upper percentiles which by default are 25%, 50% and 75%
# I read about what is included in the dataset.describe() output here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
# I will provide a description of what each line in the output is in my readme file
print("Please see Readme file for further information")