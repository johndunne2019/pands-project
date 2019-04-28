# Analysis of the Fisher's Iris data set
# John Dunne 02-04-2019
# Using the csv file saved in my repository to do some calculations
# Using the example from the lectures in week 9 
# week 9 video on matplotlib pyplot: https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
# week 9 video on numpy: https://web.microsoftstream.com/video/74b18405-5ee1-47f0-a42d-e8831a453a91

import numpy as np  # imported the numpy module and given shorter name np

data = np.genfromtxt('Fishers_Iris_data_set.csv',delimiter= ',', skip_header=1)
# numpy.genfromtxt is used to read the csv file 
# delimiter set as comma as data is separated on commas in csv files 
# skip_header used to skip the first row of data in the file, when i first wrote this script i was returned the value nan (not a number)
# I read about using skip_header here: https://docs.scipy.org/doc/numpy-1.13.0/user/basics.io.genfromtxt.html
# I read about genfromtxt here: https://www.numpy.org/devdocs/user/basics.io.genfromtxt.html

meansepal_lenght= np.mean(data[:,0])
# numpy.mean used to calculate the mean of the first column of data and subsequently the remaining columns of data
# Read about numpy.mean here: https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.mean.html
meansepal_width= np.mean(data[:,1])
meanpetal_lenght= np.mean(data[:,2])
meanpetal_width= np.mean(data[:,3])
print(f"The mean of the first column of data- sepal lenght is: {meansepal_lenght} rounded to one decimal place {(round(meansepal_lenght, 1))}")
# The output has been set to return the mean of the first column of data and the mean rounded to one decimal place
# formatted string used to return the sentence when the program is run
# round function used to round the result to one decimal place
print(f"The mean of the second column of data- sepal width is: {meansepal_width} rounded to one decimal place {(round(meansepal_width, 1))}")
print(f"The mean of the third column of data- petal lenght is: {meanpetal_lenght} rounded to one decimal place {(round(meanpetal_lenght, 1))}")
print(f"The mean of the fourth column of data- petal width is: {meanpetal_width} rounded to one decimal place {(round(meanpetal_width, 1))}")
print("The fifth column of the data set contains the name of the species Iris flower")