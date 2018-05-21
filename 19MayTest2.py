# -*- coding: utf-8 -*-
"""
Created on Sat May 19 21:34:05 2018

@author: john3
"""

#Overall Goal: Use 18MayTest.pickle to generate dictionary disease:treatment summary from pandas DF
##NOTE this only extracts explicitly mentioned treatment sections, does not yet have functionality to extract
###if the treatment section is in the summary for instance

#The program is also buggy. will crash out because of a bytecode error that have not yet addressed, so
##can only run in roughly 250 disease partitions till all diseases from pickle exhausted instead of all running straight
###thru cuz will crash out



import pickle
import pandas as pd
import numpy as np
import csv
import glob
import requests
import bs4 as bs



with open("18MayTest.pickle", "rb") as f:
    pickle.load(f)
    f.close()
numberslicebegin=0
numbersliceend=50
bob=df["URLS"][numberslicebegin:numbersliceend]


#searches all drug names in FDA Offpatent Offlabel list

counter=0+numberslicebegin
listofdics=[]
for url in bob:
    rarediseaseurl=requests.get("https://rarediseases.info.nih.gov"+url)
    soup=bs.BeautifulSoup(rarediseaseurl.text, "lxml")
    diseasename=soup.find("h1").get_text(strip=True)
    butt=soup.find("div", {"id":"readSpeaker_diseaseTreatmentSection"})
    nameNtreatmentdic={}
    if butt is None:
        print ("No treatment found for "+diseasename)
        counter=counter+1
        print(counter)
        exit
    else:
        try:
            
            poop=[e.get_text(strip=True).replace("\xa0", " ") for e in butt.select(".disease_answer")] #looks in butt in selects .disease_answer tag, after which it strips tag, replaces \xa0 with a space
            poop=poop[0] #allows for string as opposed to a list
            print("Treatment exists for " +diseasename)
            nameNtreatmentdic[diseasename]=poop #jams into dictionary
            listofdics.append(nameNtreatmentdic) 
            counter=counter+1
            print(counter)
        except IndexError:
            pass

#allnames2alllinksdic={k:v for k, v in zip(bignamelist, biglinklist)} #combines name and url list into key value pairs dictionary
print(listofdics)

numberslicebegin=str(numberslicebegin)
numbersliceend=str(numbersliceend)
with open("New19MayTest"+numberslicebegin+"_"+numbersliceend+".csv", 'w', newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(('Disease Name', 'Current Standard of Treatment if Listed on NIH Rare Diseases Website'))
    for i in listofdics:
        for key, value in i.items():
            writer.writerow([key, value])