# Analysis of the Fisher's Iris data set
# John Dunne 02-04-2019
# Using the csv file saved in my repository to do some calculations
# Using the example from the lectures in week 9 
# week 9 video on matplotlib pyplot: https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
# week 9 video on numpy: https://web.microsoftstream.com/video/74b18405-5ee1-47f0-a42d-e8831a453a91

import numpy as np  # imported the numpy module and given shorter name

data = np.genfromtxt('Fishers_Iris_data_set.csv', delimiter= ',')
# numpy.genfromtxt is used to read the csv file 
# delimiter set as comma as data is separated on commas in csv files 

sepal_lenght= data[:,0]
# variable sepal_lenght introduced and set equal to the first column of data

meansepal_lenght= np.mean(data[:,0])
# numpy.mean used to calculate the mean of the first column of data

print(f"The mean of the sepal lenght is: {meansepal_lenght} rounded to one decimal place {(round(meansepal_lenght, 1))}")
# The output has been set to return the mean of the first column of data and the mean rounded to one decimal place
# formatted string used to return the sentence when the program is run