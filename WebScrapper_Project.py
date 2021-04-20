#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:02:21 2020

@author: swa
"""

from lxml import html
import requests
from pprint import pprint
#
#htmlsource = requests.get("").text #Input url here
#tree = html.fromstring(htmlsource)
#
#reviewslink = tree.xpath('/html/body/div[6]/div[1]/div/div[2]/div/div/div[1]/div[3]/ul/li[4]/a/@href')
##/html/body/div[6]/div[3]/div/div/div/div/div/div[1]/div[2]/div[1]/div[1]
##/html/body/div[6]/div[3]/div/div/div/div/div/div[1]/div[1]/div[1]/a
##/html/body/div[6]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]
##/html/body/div[6]/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[1]
##/html/body/div[6]/div[4]/div/div/div[1]/div/div[5]/div[1]/div/h3/a
##/html/body/div[6]/div[4]/div/div/div[1]/div/div[5]/div[2]/div/h3/a
###remove empty reviews
###reviews = [r.strip() for r in reviews if r.strip() != ""]
#
#pprint(len(reviewslink), "reviews link scrapped. Showing first 60 characters: ")
#
#i=0
#for review in reviewslink:
#    pprint("Review", i, ":", review[:60])
#    i+=1


l = [{'text': '',
  'url': 'https://dutchreview.com/featured-events/things-to-do-during-christmas-in-amsterdam/'},
 {'text': '',
  'url': 'https://dutchreview.com/featured-events/things-to-do-during-christmas-in-amsterdam/'},
 {'text': 'But, I do also think that Dutch people are generally just big fans of cats (this is especially apparent in my boyfriend’s family). This may be why there are some great cat-themed attractions in Amsterdam.',
  'url': 'https://dutchreview.com/featured/cat-lovers-guide-amsterdam/'}]

pprint(l)