#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:36:49 2020

@author: swa
"""

import pandas as pd
#loading sample data
df = pd.read_csv ("twitter_dataset.csv")
from langdetect import detect
def apply_langdetect(text):
    text = str(text)
    try:
        lang = detect(text)
    except:
        lang = "error"
    return lang    
df['langdetect2'] = df['text'].apply(apply_langdetect)
df['langdetect2'].value_counts()
#print(df)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
testtext = "I love this"
sid.polarity_scores(testtext)

def vader_text(row):
    text = str(row['text']) # IMPORTANT: you need to change 'text' to the name of the column you need to analyse
    try:
        results = sid.polarity_scores(text)
        row['vader_compound'] = results['compound']
        row['vader_negative'] = results['neg']
        row['vader_neutral'] = results['neu']
        row['vader_positive'] = results['pos']
    except:
        pass
    
    return row
df = df.apply(vader_text, axis=1)
df[['vader_compound', 'vader_negative', 'vader_neutral', 'vader_positive']].describe()

from pattern3.nl import sentiment

testtext = "Ik vind dit erg"
sentiment(testtext)

def pattern_text(row):
    text = str(row['text']) # IMPORTANT: you need to change 'text' to the name of the column you need to analyse
    try:
        row['pattern_polarity'], row['pattern_subjectivity'] = sentiment(text)
    except:
        pass
    
    return row

df = df.apply(pattern_text, axis=1)
df[['pattern_polarity', 'pattern_subjectivity']].describe()
