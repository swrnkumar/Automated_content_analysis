#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:13:09 2020

@author: swa
"""


from lxml import html
import requests
from lxml.html import fromstring
from pprint import pprint
import time
import pandas as pd
import csv

#start_url = "" Input here url
mydataframe = "test.csv"

def create_csv(name_csv="test.csv"):
    """
    Example :
        import csv
        with open('eggs.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile)
            header_list = ["egg_type", "price"]
            spamwriter.writerow(header_list)
    """
    pass

def update_csv(name_csv="test.csv", new_line: list):
    """
    Example :
        import csv
        with open('eggs.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile)
            csv_row_list = ["boiled", 9.99]
            spamwriter.writerow(csv_row_list)
    """
    pass


def get_content(maxpages, startpage):
    #making an empty list to be filled with scrapped content
    releases = []
    page = startpage
    current_url = start_url
    #setting up base url for the links later
    #base_url = "" Input url here
    #retriving the content of the first page
    overview_page = requests.get(current_url)
    first_page_text = ""
    while overview_page.text != first_page_text:
        if page > maxpages: #scrapping only till max pages mentioned
            break
        elif page == 1:
            first_page_text = overview_page.text
        #putting raw content in a tree format
        tree = fromstring(overview_page.text)
        #get all links from a certain section of website
        links = tree.xpath('//*[@class="td-module-thumb"]/a/@href')
        pprint(links)
        for link in links:
            current_page = requests.get(link, timeout=10)
            tree = fromstring(current_page.text)
            try:
                text = "".join(tree.xpath('/html/body/div[6]/article/div[2]/div/div[1]/div/div[2]/p[2]/text()')).strip()
                # text = text.replace("\r|\xa0", "")
                pprint(text)
                # mydataframe = open('test.csv', 'w')
                # with mydataframe:
                #     writer = csv.writer(mydataframe)
                #     writer.writerows(releases)
            except:
                text = ""
        releases.append({"text": text, "url": link})
        pprint(releases)
        #setting a new current url
        page += 1
        current_url = start_url + "/page/" + str(page)
        overview_page = requests.get(current_url)
        
        time.sleep(0.2)
    mydataframe = open('test.csv', 'w')
    with mydataframe:
        writer = csv.writer(mydataframe)
        writer.writerows(releases)
    return releases
       

get_content(2,0)

                