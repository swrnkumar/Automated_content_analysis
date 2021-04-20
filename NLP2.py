#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:45:54 2020

@author: swa
"""

import csv
import re
from nltk.sentiment import vader
from nltk.corpus import stopwords
import nltk

with open("Cleaned_Speeches/Speeches_NL_Cleaned.csv") as fi:
    reader=csv.reader(fi)
    firstrow=next(reader)
    print("It looks like we have",len(firstrow),"columns.")
    print("\nThis is the content:\n")
    print(firstrow)
