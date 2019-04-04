# pands-project

## Programming and Scripting 2019 Project

This repository contains my project 2019 for the module Programming and Scripting at GMIT. See here for the instructions: https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf. References and resources I used in compiling this project are listed in the references section at the foot of this Readme file. 

## About this Project

The project concerns the well known Fisher's Iris data set. Through completion of this project I will endeavour to do the following:

* Research background information about the data set and write a summary about it. 
* Compile a list of references used in my research. 
* Download the data set and write some python code to investigate it. 
* Write a summary of my investigations.
* Include supporting graphics and tables. 

## Author
John Dunne

## How to download this repository

1. Go to GitHub.
2. Go to my repository: https://github.com/johndunne2019/pands-project
3. Click the clone/download button.
4. Save the repository to a local folder location on your machine.
5. You will need to navigate to this folder location on the command line in order to run the program.
6. Details on how to run each individual script in this repository is included later in this Readme file.

## Contents of this repository
* Readme File
* Fishers_Iris_data_set.csv
* Mean_Fisher_Iris.py

## Sir Ronald Aylmer Fisher (February 17, 1890 - July 29, 1962)

The author of the Fisher's Iris data set is Ronald Fisher (pictured below). 

![Image of Ronald Fisher](https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Youngronaldfisher2.JPG/220px-Youngronaldfisher2.JPG)

*Image taken from: https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Youngronaldfisher2.JPG/220px-Youngronaldfisher2.JPG*

Ronald Fisher was born in 1890 and died in 1962 and is widely known by the title "father of statistics". He is widely acclaimed as one of the greatest statisticians ever. Despite this, Fisher was primarily a Biologist and according to the author Richard Hawkins, he was the greatest biologist since Charles Darwin. 

**Interesting facts about Ronald Fisher**

* Ronald Fisher was born in London on February 17, 1890 and died in Adelaide, Australia on July 29, 1962. 
* Ronald suffered from shortsightedness and as a result was not allowed to read under an electric light. Despite this disability Ronald was widely acclaimed as a very bright student by his teachers and received scholarships for his education. 
* In 1909, Fisher was awarded a scholarship to study mathematics as the University of Cambridge and he graduated with a first class honours.
* Fisher had a keen interest in Eugenics which is the improvement of the human race by selective breeding. In 1911, he formed Cambridge University's Eugenics Society, which included amongst it's members Charles Darwin's son. The following is a quote from Fisher:

*"We can set no limit to human potentialities; all that is best in man can be bettered; it is not a question of producing a highly efficient machine, … but of quickening all the distinctly human features, all that is best in man, all the different qualities, some obvious, some infinitely subtle, which we recognize as humanly excellent"*

Quote from: https://www.famousscientists.org/ronald-fisher/

* Ronald volunteered for the British Army at the beginning of World War I but was rejected because of his poor sight. 
* He became a school teacher in 1914 teaching mathematics and physics. 
* He married Ruth Guinness in 1917 and they had 7 daughters and 2 sons together. Their eldest son George was killed in action in World War II in 1943. 
* In 1919 he became a statistician at Rothamsted Experimental Station which afforded him the opportunity to analyse data that had been collected as far back as 1842.
* In 1925, Fisher published a book "Statistical Methods for Research Workers" which went on to be widely acclaimed as a revolutionary piece of work on statistics and biology. 
* In 1935, Fisher released his book "The Design of Experiments" in which he introduced the concept of null hypothesis. 
* In 1952 Fisher was knighted by Queen Elizabeth becoming Sir Ronald Aylmer Fisher. 
* In all, Fisher wrote 7 books and approximately 400 academic papers in the field of statistics. 

**Lady Tasting Tea**

Apart from the Fisher Iris data set Ronald Fisher is also famous for another problem set called Lady Tasting Tea. Fisher published the experiment in his book - The Design of Experiments.The experiment originated when a lady claimed to be able to tell simply from tasting a cup of tea whether the tea or the milk had been infused first. Fisher set about disproving this claim by designing the experiment which consisted of 8 cups of tea, 4 made with the tea infused first and 4 made with the milk infused first. 

## Introduction to the Fisher's Iris Data Set

The Fisher's Iris data set is a multivariate data set that was introduced by Ronald Fisher in 1936. 


**Contents of the Fisher's Iris Data Set**

There are 150 rows of data in the data set in total, each representing a species of Iris flower. There are 3 species in total with 50 rows of data on each species. 

* Iris Setosa
* Iris Versicolor
* Iris Virginica 

*"The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other."*

Quote from: http://archive.ics.uci.edu/ml/datasets/iris

**Detailed below are the contents of each column of data in the data set:**

1. Column 1 contains sepal length in cm
2. Column 2 contains sepal width in cm
3. Column 3 contains petal length in cm
4. Column 4 contains petal length in cm
5. Column 5 contains the name of the species of Iris flower

The data set is available to view in my repository - "Fishers_Iris_data_set.csv"

**The Data set in more detail**




## My Analysis of the Fisher's Iris Data Set

In this section I have detailed the analysis that I carried out on the Fisher's Iris data set. I have broken down the contents of each file in my repository that has been use to analyse the data set. 

**Fishers_Iris_data_set.csv**

This file is a csv file containing the Fisher's Iris data set which I downloaded from the internet and saved in my repository. Further details in the references section of this Readme file. 

**Mean_Fisher_Iris.py**

This file contains a program that calculates the mean of the columns of data in the Fisher's Iris data set. I wrote this file using the numpy module and within the numpy module using the numpy.mean function to calculate the mean of the data in each column. I used the genfromtxt function to read the csv file and set the delimiter as comma. When I first wrote this program the output was nan (not a number) and I had to research how to skip the first row of the data set. I did this using skip_header=1. I also asked for the output to be rounded to one decimal place using the round function and I used formatted strings to return the output in a sentence. I asked for the mean of the first 4 columns of the data set to be calculated and printed as output plus a sentence informing the user about the contents of the fifth column of the data set. In writing this script I used the week 9 lectures on numpy and matplotlib as a starting point and developed the code through further research which is detailed in the references section of this Readme file. 

* How to run the program: Mean_Fisher_Iris.py:
    * Download my repository to your local machine.
    * Please note- The csv file - Fishers_Iris_data_set.csv must also be downloaded to the same folder for this program to run correctly.
    * Open cmder or command prompt and cd (change directory) to the folder where the repository has been downloaded.
    * Type python Mean_Fisher_Iris.py and the enter button.
    * The output will appear on the command line.
  


## References

**This section contains details on the references and research that went into compiling this project.**

*Formatting Readme File:*
* https://guides.github.com/features/mastering-markdown/

*Ronald Fisher:*
* https://www.famousscientists.org/ronald-fisher/
* https://www.britannica.com/biography/Ronald-Aylmer-Fisher
* http://www-history.mcs.st-andrews.ac.uk/Biographies/Fisher.html
* http://www.42evolution.org/ronald-a-fisher/
* https://www.umass.edu/wsp/resources/tales/fisher.html

*Lady Tasting Tea:* 
* https://brainder.org/2015/08/23/the-lady-tasting-tea-and-fishers-exact-test/

*Fisher's Iris Data Set:*
* https://archive.ics.uci.edu/ml/datasets/iris
* https://support.sas.com/documentation/cdl/en/statug/63962/HTML/default/viewer.htm#statug_sashelp_sect007.htm
* https://www.youtube.com/watch?v=PlrEJfvZRNo
* https://www.youtube.com/watch?v=hd1W4CyPX58

*Fishers_Iris_data_set.csv:*
* Fisher's Iris data set downloaded from: https://gist.github.com/curran/a08a1080b88344b0c8a7 and saved as csv file in my repository.

*Mean_Fisher_Iris.py - Calculating the mean of a column in the data set*

* Week 9 video on matplotlib pyplot: https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
* Week 9 video on numpy: https://web.microsoftstream.com/video/74b18405-5ee1-47f0-a42d-e8831a453a91
* Numpy tutorial: https://docs.scipy.org/doc/numpy/user/quickstart.html
* pyplot tutorial: https://matplotlib.org/users/pyplot_tutorial.html
* Using genfromtxt: https://www.numpy.org/devdocs/user/basics.io.genfromtxt.html
* numpy.mean to calculate mean: https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.mean.html
* Skip_Header to skip the first row of data when calculating the mean: https://docs.scipy.org/doc/numpy-1.13.0/user/basics.io.genfromtxt.html