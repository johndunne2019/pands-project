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

## Project Plan

**In completing this project I broke the overall task into several small tasks as described in this section. This is reflected in the layout of this Readme file which has been broken into sections as listed in the Table of contents.**
* Background on Ronald Fisher.
* Introduction to the Fisher Iris data set. 
* Contents of the data set.
* More detailed information on the data set.
* The Iris flower in more detail.
* Examples of interesting analysis pursued by others into the Fisher's Iris data set.
* My Analysis of the Fisher's Iris Data Set.
* List of references compiled as I completed the research. 

## Table of Contents

**Listed below are the main headings included in this Readme file, with each section broke out into subheadings**

* Sir Ronald Aylmer Fisher (February 17, 1890 - July 29, 1962)
    * Interesting facts about Ronald Fisher
    * Lady Tasting Tea
* Introduction to the Fisher's Iris Data Set
    * Contents of the Fisher's Iris Data Set
    * What is unique about the Fisher's Iris data set?
    * The Iris Flower
    * Iris Setosa
    * Iris Versicolor
    * Iris Virginica
    * What is the difference between Sepal and Petal?
* Examples of interesting analysis pursued by others into the Fisher's Iris data set
    * Machine learning mystery
* My Analysis of the Fisher's Iris Data Set
    * Intro_Fisher_Iris.py
    * Fishers_Iris_data_set.csv
    * Mean_Fisher_Iris.py
    * Dataset.Describe.py
    * Histogram.py
* References

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

Apart from the Fisher Iris data set Ronald Fisher is also famous for another problem set called Lady Tasting Tea. Fisher published the experiment in his book - The Design of Experiments. The experiment originated when a lady claimed to be able to tell simply from tasting a cup of tea whether the tea or the milk had been infused first. 

*"We will consider the problem of designing an experiment by means of which this assertion can be tested. […] [It] consists in mixing eight cups of tea, four in one way and four in the other, and presenting them to the subject for judgment in a random order. The subject has been told in advance of that the test will consist, namely, that she will be asked to taste eight cups, that these shall be four of each kind […]. — Fisher, 1935."* - https://brainder.org/2015/08/23/the-lady-tasting-tea-and-fishers-exact-test/

![Lady tasting tea](https://s3.us-east-2.amazonaws.com/brainder/2015/tastingtea/tea_cups.png)

Image from: https://brainder.org/2015/08/23/the-lady-tasting-tea-and-fishers-exact-test/

The lady in question answered correctly 6 of the 8 trials, however Fisher concluded that it was not possible to prove that she would never be wrong - *"because if a sufficiently large number of cups of tea were offered, a single failure would disprove such hypothesis"* - https://brainder.org/2015/08/23/the-lady-tasting-tea-and-fishers-exact-test/

Fisher's exact solution to the problem is shown here:

![Solution](https://s0.wp.com/latex.php?latex=P_%7B%5Ctext%7BFisher%7D%7D+%3D+%5Cdfrac%7B%28a%2Bb%29%21%28c%2Bd%29%21%28a%2Bc%29%21%28b%2Bd%29%21%7D%7Bn%21a%21b%21c%21d%21%7D&bg=ffffff&fg=333333&s=0)

Image from: https://brainder.org/2015/08/23/the-lady-tasting-tea-and-fishers-exact-test/


## Introduction to the Fisher's Iris Data Set

The Fisher's Iris data set is a multivariate data set that was introduced by Ronald Fisher in 1936 in his paper - "The use of multiple measurements in taxonomic problems". The data set is also referred to as the Edgar Anderson data set as it was Edgar Anderson who collected the data. 

*"It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify themorphologic variation of Iris ﬂowers of three related species."* - https://www.academia.edu/13069408/Report_on_Edgar_Anderson_s_Iris_Data_Analysis


**Contents of the Fisher's Iris Data Set**

There are 150 rows of data in the data set in total, each representing a species of Iris flower. There are 3 species in total with 50 rows of data on each species. 

* Iris Setosa
* Iris Versicolor
* Iris Virginica 

*"The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other."* -  http://archive.ics.uci.edu/ml/datasets/iris

**Detailed below are the contents of each column of data in the data set:**

1. Column 1 contains sepal length in cm
2. Column 2 contains sepal width in cm
3. Column 3 contains petal length in cm
4. Column 4 contains petal width in cm
5. Column 5 contains the name of the species of Iris flower

The data set is available to view in my repository - "Fishers_Iris_data_set.csv" at this link: https://github.com/johndunne2019/pands-project/blob/master/Fishers_Iris_data_set.csv

**What is unique about the Fisher's Iris data set?**

The Fisher's Iris data set is a data set that is commonly used in machine learning. One very significant feature of the data set is that the data concerning two of the species of Iris flowers are easy to separate from one another whilst it is difficult to separate the data concerning the other two species of Iris flowers.

*"One flower species is linearly separable from the other two, but the other two are not linearly separable from each other."* - https://www.kaggle.com/meetsourav/clustering-with-iris-dataset

**Listed below are some of the noteworthy features of the Iris data set taken from: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/**

* Attributes are numeric so you have to figure out how to load and handle data.
* It is a classification problem, allowing you to practice with perhaps an easier type of supervised learning algorithm.
* It is a multi-class classification problem (multi-nominal) that may require some specialized handling.
* It only has 4 attributes and 150 rows, meaning it is small and easily fits into memory (and a screen or A4 page).
* All of the numeric attributes are in the same units and the same scale, not requiring any special scaling or transforms to get started.

**The Iris Flower**
 
The Iris flower is a perennial flower meaning it lives longer than two years and the flower is notably easy to grow. 

**Iris Setosa**

The Iris setosa is a short, grass leaved species native to Siberia and Alaska. It is tolerant to cold temperatures and the petals are lavender blue with silvery-white veining. 


![Image of iris setosa](http://www.twofrog.com/images/iris38a.jpg)

Image from: http://www.twofrog.com/images/iris38a.jpg


**Iris Versicolor**

The Iris Versicolor is a wild flower of Eastern North America. It performs well in shallow water or by waterside but can also perform well under average border conditions. 

![Image of iris versicolor](https://mk0gardengoodsd3tst9.kinstacdn.com/wp-content/uploads/2017/03/Iris_versicolor_3.jpg)

Image from: https://mk0gardengoodsd3tst9.kinstacdn.com/wp-content/uploads/2017/03/Iris_versicolor_3.jpg

**Iris Virginica**

The Iris Virginica also known as the Southern Blueflag is best grown in wet, boggy, acidic soils and is native to America.  It can be poisonous if ingested. 

![image of iris virginica](http://images.mobot.org/TropicosImages2/PlantRecordImages/prod/small240/00004000/4366_Y390-0901020.jpg)

Image from: http://images.mobot.org/TropicosImages2/PlantRecordImages/prod/small240/00004000/4366_Y390-0901020.jpg


**What is the difference between Sepal and Petal?**

Sepals are recurved in such a manner to allow bees to land on them whilst petals are upright. You can see the difference in the image below. 

*"The distinctive flowers have three large outer petals called “falls” and three inner upright petals called “standards.” The falls may have beards or crests. Bearded iris are so-called because they have soft hairs along the center of the falls. In crested iris, the hairs form a comb or ridge."* - https://www.almanac.com/plant/irises



![Image of Iris Flower](https://www.fs.fed.us/wildflowers/beauty/iris/images/blueflagiris_flower.gif)

Image of an Iris Flower showing Sepal and Petal. Taken from: https://www.fs.fed.us/wildflowers/beauty/iris/images/blueflagiris_flower.gif


## Examples of interesting analysis pursued by others into the Fisher's Iris data set

**In this section I am looking at some interesting analysis pursued by others based on the data set. I am doing this with a view to gathering information and ideas that could be useful to me in completing my analysis of the data set.**

**1. Machine learning mystery - https://machinelearningmastery.com/machine-learning-in-python-step-by-step/**

*dataframe.describe() and histogram*

I came across this example in my online research and found it to be interesting and informative and I will draw on some of the topics and examples covered when completing my own analysis of the data set later. In this analysis they have used the pandas module to do some analysis on the data set. Python Data Analysis Library or pandas is an open source library that provides data analysis tools for the python programming language. To further my knowledge of pandas I also read the ten minutes to pandas documentation here: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html.
I liked the dataframe.describe() function which printed a summary of the data set to the screen which included count of rows, mean, standard deviation, min and max. I liked this function as it gives the user a lot of insight into the data set and it is a simple operation. I decided to use this feature in my analysis of the Fisher's Iris data set after reading this example analysis. 
Also in this analysis the author has created a histogram of the data to give a clearer view of distribution of the data. I will also try to do something similar in my analysis of the data set. 

The histogram created by the author in this analysis is shown below:

![histogram](https://3qeqpr26caki16dnhd19sv6by6v-wpengine.netdna-ssl.com/wp-content/uploads/2016/06/Histogram-Plots-for-Each-Input-Variable-for-the-Iris-Flowers-Dataset-1024x768.png)

Image from: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

The author also went on to conduct some more complicated analysis including scatterplots and evaluation of algorithms. Overall, I think this tutorial is a good starting point for someone looking to learn some basic data analysis using the Fisher's Iris data set. 

**2. Machine Learning on Iris - https://diwashrestha.com/2017/09/18/machine-learning-on-iris/**

This is the second example that I came across in the course of my research into the Fisher's Iris data set. In this analysis the author has used the built in dataset function in the seaborne module to read in the data set. They have also used the dataframe.describe() function within pandas in the same way as the author of the first analysis I looked at. An interesting thing the author has done is to split the data in two allocating 30% of the data as a test for evaluating the model. They have done this using the scikit learn train_test_split function. The author has used seaborne and matplotlib to plot a scatterplot of the data set and also a bar chart of the data set. 

The bar chart plotted by the author is shown below:

![bar chart](https://diwashrestha.com/wp-content/uploads/2017/09/plot.png)

Image from: https://diwashrestha.com/wp-content/uploads/2017/09/plot.png

Although this analysis offers some interesting insight in to what data analysis can be conducted using the Fisher Iris data set I found it to be a bit too complicated for a relatively inexperienced user. 

## My Analysis of the Fisher's Iris Data Set

**In this section I have detailed the analysis that I carried out on the Fisher's Iris data set. I have broken down the contents of each file in my repository that has been use to analyse the data set.**

**Libraries Used in my analysis**

*Python Data Analysis Library - https://pandas.pydata.org/*

I used the pandas library in my analysis of the Fisher's Iris data set. Some of the functions I used within the pandas library in my analysis of the data set included:

* pandas.read to read in the csv file from my repository
* Dataframe.describe() to output a summary of the data set to the user
* Dataframe.head() and dataframe.tail() to output the first ten rows and last ten rows of the data set. 


**Fishers_Iris_data_set.csv**

This file is a csv file containing the Fisher's Iris data set which I downloaded from the internet and saved in my repository. Further details in the references section of this Readme file. I have then used the data set as saved in this csv file to write some short scripts used to analyse the data set. These scripts are explained in further detail in this section and you can download and run these scripts on your local machine following the instructions below. 

**How to download each script and run on your machine**

* Download my repository to your local machine (further details at the beginning of this Readme file).
* Please note- The csv file - Fishers_Iris_data_set.csv must also be downloaded to the same folder for this program to run correctly.
* Open cmder or command prompt and cd (change directory) to the folder where the repository has been saved to on your local machine.
* Type python followed by the file name and press the enter key.
* The output will appear on the command line.
* An example would be to run the script "Mean_Fisher_Iris.py" you should type python Mean_Fisher_Iris.py in cmder or command prompt and press the enter key. 

**Intro_Fisher_Iris.py**

Please note- this script must be run while command prompt/cmder is in full screen mode to view all data.
This script is intended to give a short introduction to the data set to the user. I have started this script drawing on the reading of an example of an analysis into the data set that I found online at this link: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/. The pandas module is imported and pandas.read is used to read the csv file directly from my repository. I have used header=0 to set the first row of data as the header for the output. I have used dataframe.head() function within pandas to return the first 10 rows of data as output when the script is run. I have entered the parameter 10 as the default parameter for dataframe.head()is 5. I have also printed a sentence to the screen to inform the user that the first 10 rows of the data set have been displayed. I have used the dataframe.tail() function to show the last ten rows of the data set and in a similar way I have printed a sentence to inform the user they are the last ten rows of the data set. 

**Mean_Fisher_Iris.py**

This file contains a program that calculates the mean of the columns of data in the Fisher's Iris data set. I wrote this file using the numpy module and within the numpy module using the numpy.mean function to calculate the mean of the data in each column. I used the genfromtxt function to read the csv file and set the delimiter as comma. When I first wrote this program the output was nan (not a number) and I had to research how to skip the first row of the data set. I did this using skip_header=1. I also asked for the output to be rounded to one decimal place using the round function and I used formatted strings to return the output in a sentence. I asked for the mean of the first 4 columns of the data set to be calculated and printed as output plus a sentence informing the user about the contents of the fifth column of the data set. In writing this script I used the week 9 lectures on numpy and matplotlib as a starting point and developed the code through further research which is detailed in the references section of this Readme file. 
  
**Dataset.Describe.py**

Please note- this script must be run while command prompt/cmder is in full screen mode to view all data.
This script provides a description of the data set to the user using the dataframe.describe() function within pandas. I first came across the dataframe.describe() function when reading an example analysis of the Fisher's Iris data set here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/. I thought it would be a nice addition to my analysis as there is a good concise summary of the data set returned to the user from a relatively short and simple script. In writing the script I imported the pandas module and gave it a shortened name. I then loaded the csv directly from my repository using the url, important to note the url was taken after I clicked the raw button on the csv file in repository as it does not work correctly otherwise. I also used header=0 to set the first row of the data set as the header for the output. Finally the dataframe.describe() function is printed to the screen which provides a summary of the data set to the user. The summary includes the count of the total number of rows of data in the data set, the mean of each column of data, the standard deviation, the min and the max value in each column. Also included in the summary is the upper, lower and 50 percentiles which by default in dataframe.describe() are set to 25%, 50% and 75%. Further information on the output included in dataframe.describe can be read here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html and I have also provided further details below. I have included the list of references I used in writing this script in the references section of this Readme file. 

*What does each row in the output represent*
* count = total number of rows of data in the data set. 
* mean = the sum of each column of data divided by the count which gives the average measurement in cm also known as the central tendency of the data. 
* std = standard deviation which is a measurement of the variance of each data point relative to the mean. 
* min = the smallest measurement collected in cm in each column of the data set. 
* 25% = the 25th percentile - meaning 25% of the total count of measurements collected fall below this measurement. 
* 50% = the 50th or median percentile meaning this is the central measurement in cm collected in each column, half of the data collected falls below this measurement and half is above this measurement. Further details on how percentile is calculated can be read here: https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/percentiles-rank-range/.
* 75% = the 75th percentile - meaning 75% of the total count of measurements collected fall below this measurement and 25% are above this measurement. 
* max = the largest measurement collected in cm in each column of the data set. 

**Histogram.py**

This program plots a histogram of the first 4 columns of data in the Fisher's Iris data set. I have adapted the script from the example analysis that I read from machine mystery learning at this link: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/. I commented on this analysis in the previous section of this Readme file. This program uses pandas to read the csv file and matplotlib.pyplot to plot the histogram. Within matplotlib.pyplot, the pyplot.hist() command is used to plot the histogram and the pyplot.show() command is used to display the histogram. Within pandas, the csv file is read using pandas.read and the file is read directly from my repository using the url link. This is a short script that I adapted from the example analysis mentioned above and also drawing on additional reading that I completed that has been listed in the references section of this Readme file.

## References

**This section contains details on the references and research that went into compiling this project.**

*Formatting Readme File:*
* https://guides.github.com/features/mastering-markdown/

*Sir Ronald Aylmer Fisher (February 17, 1890 - July 29, 1962):*
* https://www.famousscientists.org/ronald-fisher/
* https://www.britannica.com/biography/Ronald-Aylmer-Fisher
* http://www-history.mcs.st-andrews.ac.uk/Biographies/Fisher.html
* http://www.42evolution.org/ronald-a-fisher/
* https://www.umass.edu/wsp/resources/tales/fisher.html

*Lady Tasting Tea:* 
* https://brainder.org/2015/08/23/the-lady-tasting-tea-and-fishers-exact-test/

*Introduction to the Fisher's Iris Data Set*
* https://archive.ics.uci.edu/ml/datasets/iris
* https://support.sas.com/documentation/cdl/en/statug/63962/HTML/default/viewer.htm#statug_sashelp_sect007.htm
* https://www.youtube.com/watch?v=PlrEJfvZRNo
* Scikit learn - to revisit later -https://www.youtube.com/watch?v=hd1W4CyPX58
* https://diwashrestha.com/2017/09/18/machine-learning-on-iris/
* https://www.academia.edu/13069408/Report_on_Edgar_Anderson_s_Iris_Data_Analysis

*Contents of the Fisher's Iris data set*
*  http://archive.ics.uci.edu/ml/datasets/iris

*What is unique about the Fisher's Iris data set?*
* https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
* https://www.kaggle.com/meetsourav/clustering-with-iris-dataset

*The Iris Flower*
* https://www.gardendesign.com/flowers/iris.html

*Iris Setosa:*
* http://www.perennials.com/plants/iris-setosa-var-arctica.html

*Iris Versicolor*
* http://www.perennials.com/plants/iris-versicolor.html
* https://mk0gardengoodsd3tst9.kinstacdn.com/wp-content/uploads/2017/03/Iris_versicolor_3.jpg

*Iris Virginica*
* https://plants.ces.ncsu.edu/plants/all/iris-virginica/
* http://www.missouribotanicalgarden.org/PlantFinder/PlantFinderDetails.aspx?kempercode=y390

*What is the difference between sepal and petal?:*
* https://www.fs.fed.us/wildflowers/beauty/iris/flowers.shtml
* https://www.theflowerexpert.com/content/mostpopularflowers/morepopularflowers/iris
* https://www.almanac.com/plant/irises

*Fishers_Iris_data_set.csv:*
* Fisher's Iris data set downloaded from: https://gist.github.com/curran/a08a1080b88344b0c8a7 and saved as csv file in my repository.

*Intro_Fisher_Iris.py*
* Adapted from the tutorial here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
* I read how to have the csv file read directly from my repository using the url link here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
* How to read csv file using pandas.read: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
* Header=0: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
* dataframe.head(): https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html
* Read about dataframe.tail() here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html and http://www.datasciencemadesimple.com/head-and-tail-in-python-pandas/

*Mean_Fisher_Iris.py - Calculating the mean of a column in the data set*

* Week 9 video on matplotlib pyplot: https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
* Week 9 video on numpy: https://web.microsoftstream.com/video/74b18405-5ee1-47f0-a42d-e8831a453a91
* Numpy tutorial: https://docs.scipy.org/doc/numpy/user/quickstart.html
* pyplot tutorial: https://matplotlib.org/users/pyplot_tutorial.html
* Using genfromtxt: https://www.numpy.org/devdocs/user/basics.io.genfromtxt.html
* numpy.mean to calculate mean: https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.mean.html
* Skip_Header to skip the first row of data when calculating the mean: https://docs.scipy.org/doc/numpy-1.13.0/user/basics.io.genfromtxt.html

*Dataset_Describe.py*

* Ten minutes to pandas as recommended reading: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
* I first saw an example of the dataset.describe() being user to analyse the Fisher's Iris data set here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
* I then researched further: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html and https://stackoverflow.com/questions/38545828/pandas-describe-by-additional-parameters
* I read how to have the csv file read directly from my repository using the url link here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
* How to read csv file using pandas.read: https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
* Header=0: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
* How to use dataset.describe() and what the output is: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
* 25th, 50th and 75th percentiles and how they are calculated: https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/percentiles-rank-range/

*Histogram.py*

* Adapted from the analysis of the Fisher's Iris data set here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
* Further reading on matplotlib.pyplot: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html and https://matplotlib.org/gallery/statistics/hist.html
* pandas documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.hist.html
* pyplot.hist(): https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html and https://matplotlib.org/gallery/statistics/histogram_features.html
* pyplot.show(): https://matplotlib.org/api/_as_gen/matplotlib.pyplot.show.html