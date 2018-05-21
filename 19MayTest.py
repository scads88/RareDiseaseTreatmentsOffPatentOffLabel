# -*- coding: utf-8 -*-
"""
Created on Sat May 19 21:01:57 2018

@author: john3
"""

import requests
import csv
import bs4 as bs
import pandas as pd
import pickle
import string
import numpy as np


#letters = list(string.ascii_uppercase)
letters=["A", "B", "C"]
letters.append("0-9")
print(letters)

bignamelist=[]
biglinklist=[]


for symbol in letters:
    rarediseaseurl=requests.get("https://rarediseases.info.nih.gov/diseases/browse-by-first-letter/"+symbol) #runs through all the different urls
    soup=bs.BeautifulSoup(rarediseaseurl.text, "lxml")

#gives all url pieces as a list
    

    namelist=[]
    for link in soup.select("a"): #helps select the text from the "a" tags in soup
        namelist.append(link.text) #helps select the text from the "a" tags in soup
    endnamelistcut=len(namelist)-17  #mod for what names need removal in the front of the list
    namelist=namelist[171:endnamelistcut] #mod for what names need removal in the front of the list
    for name in namelist:
        bignamelist.append(name)
    
    
    linklist=[]
    for link in soup.find_all("a", href=True): #helps select the hyperlinks from "a href" tags in soup
        linklist.append(link.get("href")) #helps select the hyperlinks from "a href" tags in soup
    endlinklistcut=len(linklist)-16 #mod for what links need removal at end of the list
    linklist=linklist[171:endlinklistcut] #mod for what links need removal in the front of the list
    for link in linklist:
        biglinklist.append(link)
    
    
    print(symbol +" has completed")

#how to pull the actual disease names + plus some trash from a hrefs

#print(newnames)
#print (names)

#this currently overwrites the previous letter and 

#print(diseaselinks)
#print(totallinks)
#print(butthole)
    
    
    
#print(bignamelist)
#print(biglinklist)


allnames2alllinksdic={k:v for k, v in zip(bignamelist, biglinklist)} #combines name and url list into key value pairs dictionary
df=pd.DataFrame.from_dict(allnames2alllinksdic, orient="index") #generates a pandas datafrome from the dictionary created above

#Boring but essential reformating of the dataframe to make it clean and easy to use
df = df.reset_index() 
df.reset_index(drop=True)
df["Name"]=df["index"]
df["URLS"]=df[0]
del df["index"]
del df[0]
df.index = np.arange(1, len(df) + 1)

with open("19MayTest.pickle", "wb") as f:
    pickle.dump(df, f)
    f.close()
#INSERT A PICKLE TEST AND GENERATION FEATURE HERE

df.to_csv("19MayTest.csv") #generates a csv for name, url dataframe


with open("19MayTest.pickle", "rb") as f:
    pickle.load(f)
    f.close()

#print(df["URLS"].head())

import time

page = ''
while page == '':
    try:
        page = requests.get(url)
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        continue



list4treatments=[]

for url in df["URLS"][2]:
    diseaseurlping=requests.get("https://rarediseases.info.nih.gov"+url)
    soup=bs.BeautifulSoup(diseaseurlping.text, "lxml")
    butt=soup.find("div", {"id":"readSpeaker_diseaseTreatmentSection"})
    print(butt)
    
    try: 
        poop=[e.get_text(strip=True) for e in butt.select(".disease_answer")]
    except AttributeError:
        pass
    print(poop)
