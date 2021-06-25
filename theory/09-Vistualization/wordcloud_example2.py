#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:00:50 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

from wordcloud import WordCloud

# Create list of words
# https://en.wikipedia.org/wiki/Statistical_hypothesis_testing
text = 'A statistical hypothesis is a hypothesis that is testable on the \
    basis of observed data modelled as the realised values taken by a \
    collection of random variables.[1] A set of data is modelled as being \
    realised values of a collection of random variables having a joint \
    probability distribution in some set of possible joint distributions. \
    The hypothesis being tested is exactly that set of possible probability \
    distributions. A statistical hypothesis test is a method of statistical \
    inference. An alternative hypothesis is proposed for the probability \
    distribution of the data, either explicitly or only informally. The \
    comparison of the two models is deemed statistically significant if, \
    according to a threshold probability—the significance level—the data \
    would be unlikely to occur if the null hypothesis were true. A hypothesis \
    test specifies which outcomes of a study may lead to a rejection of the \
    null hypothesis at a pre-specified level of significance, while using a \
    pre-chosen measure of deviation from that hypothesis (the test statistic, \
    or goodness-of-fit measure). The pre-chosen level of significance is the \
    maximal allowed "false positive rate". One wants to control the risk of \
    incorrectly rejecting a true null hypothesis.'


wordcloud = WordCloud().generate(text)
wordcloud.to_file("wikipedia_wordcloud2.jpg")
