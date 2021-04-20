#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:30:44 2020

@author: swa
"""

import nltk
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('maxent_treebank_pos_tagger')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

my_testlst = []
testlst = ["12", "2345", "654576", "76", "875", "34"]
for numtest in testlst:
    numtest = int(numtest)
    print(numtest)
    my_testlst.append(numtest*2)
print(my_testlst)