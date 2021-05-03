#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 1 10:35:13 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
Experiment Design 
"""
print('==Experimental Design==\n\n')
"""
A study carried by R. Brown and J.L. Kuk under the title “Secular differences in the association 
between caloric intake, macronutrient intake, and physical activity with obesity” published in 
Obesity Research and Clinical Practice, vol. 10, issue 3, May-June 2016 (243-255) used data 
from 36,377 adults from the National Health and Nutrition Survey, while Physical Activity data 
was available only for 14,419 adults. The main result from this study is that the BMI was 2.3 
greater in 2006 than in 1971 for the same levels of intake and activity so, in plain words, any 
adult today would have to eat less and exercise more to weight the same as one in the 70s; in 
fact we are a 10% heavier today. Then from this study
"""

#i. What are the statistical units? And the sampling method?

print('i - Statistical units are the surveyed adults both in 1971 and in 2006.\n\
    Sampling method unknown, hopefully random, but answering a health survey\n\
    usually implies being concerned about your health, so some bias is to be\n\
    expected. Also, the non-response rate regarding phisical activity is\n\
    noticeable, making it unclear whether the results are representative.\n')


#ii. Identify the response and explanatory variables

print('ii - Response variables: BMI\n\
     Explanatory variables: intake level, activity level, survey year\n')


#iii. Is it observational or experimental? Explain your reasoning

print('iii - It is observational, since no intervention by the scientists was made.\n')


#iv. Can you establish a causal link between the explanatory and response variables?

print('iv - No.\n')


#v. Can you think of any reason that may explain the results of this study?

print('v - I guess there are more explanatory variables than those taken into account.\
      \n    Or maybe the definition of the same variables has changed.\n\n')


"""
Single Variable 
"""
print('==Single Variable==\n\n')
"""
Consider the following set of values
6 20 28 16 16 17 1 17 11 13
7 13 16 8 10 9 4 9 6 13
11 12 10 3 12 19 10 15 11 11
17 20 8 6 3 20 19 3 19 20

Descriptive Values 

Let’s find the values that summarize and characterize the distribution of values
"""

#i. Find the mean, median and mode

setOfValues = np.array([6,20,28,16,16,17,1,17,11,13,7,13,16,8,10,9,4,9,6,13,\
    11,12,10,3,12,19,10,15,11,11,17,20,8,6,3,20,19,3,19,20])
setOfValuesMean = np.mean(setOfValues)
setOfValuesMedian = np.median(setOfValues)
setOfValuesMode = stats.mode(setOfValues)
print('i - Mean: '+ "{:.2f}".format(setOfValuesMean) + \
      '\n    Median: '+ "{:.2f}".format(setOfValuesMedian) + \
      '\n    Mode: '+ str(setOfValuesMode[0][0]) + ' (' + \
      str(setOfValuesMode[1][0]) + ' times)\n' )

    
#ii. Find the standard deviation and the IQR

setOfValuesStd = np.std(setOfValues)
setOfValuesIQR = stats.iqr(setOfValues)
print('ii - Standard deviation: '+ "{:.2f}".format(setOfValuesStd) + \
      '\n     IQR: '+ "{:.2f}".format(setOfValuesIQR) +'\n')


# iii. Find the skewness and kurtosis

setOfValuesSkewness = stats.skew(setOfValues)
setOfValuesKurtosis = stats.kurtosis(setOfValues)
print('iii - Skewness: '+ "{:.2f}".format(setOfValuesSkewness) + \
      '\n      Kurtosis: '+ "{:.2f}".format(setOfValuesKurtosis)  +'\n')


"""
Frequency Distribution 

Let’s now find its frequency distribution and plot the corresponding histogram
"""

#iv. Find the distribution of both total and cumulative frequencies
binsDef = 9
freqDistFreq, freqDistBins = np.histogram(setOfValues,bins=binsDef,range=[0,28])
setOfValuesCumFreq = stats.cumfreq(setOfValues, numbins=binsDef)
print('iv - Distribution of frequencies using ' + str(binsDef) + ' bins:')
print(freqDistFreq)
print('     Cummulative frequencies using ' + str(binsDef) + ' bins:')
print(setOfValuesCumFreq[0],end='\n\n')


#v. Since the number of bins (classes) of the distribution is arbitrary, explain 
#how you decide it in your case (If you use a software that decides 
#automatically, explain which rule is used)
print('v - I could have let the software decide, but since we had all integers\n\
    and the max value was 28, I decided to use 27 bins of size 1 for a first\n\
    run, but the results were too noisy. Then, I decided to divide the number\n\
    of bins by three (i.e. bins=9), in the aim of obtaining bins stretching\n\
    from integer to integer, so that the obtained classes were simpler to read\n\
    and also the result had a much better look, so I kept that value at 9.\n\n')


"""
Once we have grouped our date in a frequency distribution, the descriptive values 
we have found before are no longer valid. Then
"""

#vi. Find the approximated mean, median and mode
freqDistValues = np.repeat((freqDistBins[1:] + freqDistBins[:-1]) / 2, \
     freqDistFreq.astype(int))
freqDistValuesMean = np.mean(freqDistValues)
freqDistValuesMedian = np.median(freqDistValues)
freqDistValuesMode = stats.mode(freqDistValues)
print('vi - Aproximated Mean: '+ "{:.2f}".format(freqDistValuesMean) + \
      '\n     Aproximated Median: '+ "{:.2f}".format(freqDistValuesMedian) + \
      '\n     Aproximated Mode: '+ "{:.2f}".format(freqDistValuesMode[0][0]) + \
      ' (' +  str(freqDistValuesMode[1][0]) + ' times)\n' )


#vii. Find the approximated standard deviation and IQR
freqDistValuesStd = np.std(freqDistValues)
freqDistValuesIQR = stats.iqr(freqDistValues)
print('Vii - Aproximated Standard Deviation: '+ "{:.2f}".format(freqDistValuesStd) + \
      '\n      Aproximated IQR: '+ "{:.2f}".format(freqDistValuesIQR) +'\n')



#viii. Find the approximated skewness and kurtosis
freqDistValuesSkewness = stats.skew(freqDistValues)
freqDistValuesKurtosis = stats.kurtosis(freqDistValues)
print('viii - Aproximated Skewness: '+ "{:.2f}".format(freqDistValuesSkewness) + \
    '\n       Aproximated Kurtosis: '+ "{:.2f}".format(freqDistValuesKurtosis)  +'\n\n')



"""
Plots 

Make the following graphical representations:
"""


#ix. Total and cumulative frequencies (in the same graph)
f, (pl1, pl2) = plt.subplots(1, 2)
freqDistFreq, freqDistValues, _ = pl1.hist(setOfValues,bins=binsDef,range=[0,28])
pl1.set_title("histogram")
setOfValuesCumFreq = stats.cumfreq(setOfValues, numbins=binsDef)
x = setOfValuesCumFreq.lowerlimit + np.linspace(0, \
    setOfValuesCumFreq.binsize*setOfValuesCumFreq.cumcount.size, \
    setOfValuesCumFreq.cumcount.size)
pl2.bar(x,setOfValuesCumFreq[0], width=setOfValuesCumFreq.binsize)
pl2.set_title("cummulative frequency")
f.show()
print('ix - See plot\n')


#x. Boxplot, making explicit any possible outlier of the distribution
f2 = plt.figure()
plt.boxplot([setOfValues,freqDistValues], vert=0)
plt.title("box plot of descriptive values and frequency distribution")
f2.show()
print('x - See plot\n\n')


"""
Interpretation 

Let’s give an interpretation of our previous results

"""

#xi. Are these approximated values always the same? Why?
print('xi - No, they depend on the bin size.\n\n')

#xii. Explain the difference between the approximated and the exact values. 
#Which ones would you use in general? Why?
print('xii - They are pretty similar, but of course not the same since we\n\
      rely on an approximation.\n\
      I would use the aproximated values since they give me a little bit of\n\
      independence from the observations and because they use less computing\n\
      power (in the end, they are less numbers).\n\n')

#xiii. Describe the distribution from the shape measures
print('xiii - The distribution is bimodal, right-skewed and platykurtic.\n\n')

#xiv. Describe the distribution from the central tendency and variability 
#measures. Which ones would you use to better describe it?
print('xiv - As corresponds to a right-skewed distribution, the mean (12.21)\n\
      is higher than the median (10.89). Most observations most fall within\n\
      IQR (9.33), with some outliers falling in the higher bin\n\
      Using median and std deviation allows for more robust results than\n\
      mean and std deviation.\n\n')


"""
Bidimensional Distribution 
"""
print('==Bidimensional Distribution==\n\n')
"""
Consider the following scatter plot

Where each point corresponds to the value of two different variables of each 
observational unit (they could correspond, for example, to the height and 
weight of different people in one study). Then
"""

#i. Describe it from the point of view of association, correlation and relationship. 
print('i - The variables have a relationship, their association is linear, strong\n\
    and positive.\n\
    As per correlation, apparently there is, but we are lacking\n\
    information to affirm anything beyond a spurious one.\n\n')

#ii. Give a qualitative estimation of the linear correlation coefficient.
print('ii - The linear correlation coefficient is positive.\n\n')

#iii. Taking a small step into probability, can you give an interpretation of the association 
#in terms of dependency of events (conditional probability)?
print('iii - Given that we have identified a relationship between the variables\n\
      with a positive correlation, we could calculate the probability of the\n\
      dependent variable falling within a certain range given a certain value\n\
      of the independen variable.\n\
      I have no idea how to do that so far, but I hope to be able by the end\n\
      of the Bootcamp :-\)\n\n')
